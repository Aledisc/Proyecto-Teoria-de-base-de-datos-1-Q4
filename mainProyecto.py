import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import cx_Oracle
from tkinter import messagebox

def conectar_oracle():
    try:
        # Ajusta estos parámetros con tu configuración de base de datos
        conn = cx_Oracle.connect('usuario/password@localhost:1521/SID')
        return conn
    except cx_Oracle.DatabaseError as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None


# ---------------------- USUARIOS ---------------------- #
def registrar_usuario(nombre, correo, edad, apellido, salario, password):
    conn = conectar_oracle()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        
        # Validación de los campos
        if not nombre or not correo or not password:
            messagebox.showerror("Error", "Nombre, correo y contraseña son obligatorios.")
            return False
        
        # Verificar si el correo ya está registrado
        cursor.execute("SELECT correo FROM usuarios WHERE correo = :correo", {"correo": correo})
        if cursor.fetchone():
            messagebox.showerror("Error", "Este correo ya está registrado.")
            return False
        
        fecha_registro = datetime.now()
        estado = "Activo"
        
        # Insertar el nuevo usuario en la base de datos
        cursor.execute("""
            INSERT INTO usuarios (nombre, apellido, correo, edad, salario, password, estado, fecha_registro)
            VALUES (:nombre, :apellido, :correo, :edad, :salario, :password, :estado, :fecha_registro)
        """, {
            "nombre": nombre,
            "apellido": apellido,
            "correo": correo,
            "edad": edad,
            "salario": salario,
            "password": password,
            "estado": estado,
            "fecha_registro": fecha_registro
        })
        
        conn.commit()
        messagebox.showinfo("Registro exitoso", f"Usuario '{nombre}' registrado correctamente")
        return True

    except cx_Oracle.DatabaseError as e:
        messagebox.showerror("Error", f"Error al registrar el usuario: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def ingreso_usuario(correo, password):
    conn = conectar_oracle()
    if conn is None:
        return None
    try:
        cursor = conn.cursor()
        # Verificar si el usuario existe
        cursor.execute("SELECT nombre, password, estado FROM usuarios WHERE correo = :correo", {"correo": correo})
        user = cursor.fetchone()

        if user is None:
            messagebox.showerror("Error", "El usuario no existe.")
            return None
        if user[1] != password:
            messagebox.showerror("Error", "Contraseña incorrecta.")
            return None
        if user[2] != "Activo":
            messagebox.showerror("Error", "El usuario está inactivo.")
            return None
        return user[0]  # Devuelve el nombre del usuario si la autenticación es correcta

    except cx_Oracle.DatabaseError as e:
        messagebox.showerror("Error", f"Error al verificar el usuario: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def presupuesto_usuario():
    
    print ("el presupuesto del usuario es: ")
    
#funcion para Presupuesto 
presupuestos = [ ]  # solo es un uso temporal hasta que implemente la base de datos  
def registrarPresupuesto(nombre_presupuesto, año_inicio, mes_inicio, año_fin, mes_fin, total_ingresos, total_gastos, total_ahorro):
    conn = conectar_oracle()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()

        # Validación de los campos
        if not nombre_presupuesto or not año_inicio or not mes_inicio or not año_fin or not mes_fin or not total_ingresos or not total_gastos or not total_ahorro:
            messagebox.showerror("Error", "Todos los campos del presupuesto son obligatorios")
            return False

        if not año_inicio.isdigit() or not año_fin.isdigit():
            messagebox.showerror("Error", "Año de inicio y fin deben ser numéricos.")
            return False

        año_inicio2 = int(año_inicio)
        año_fin2 = int(año_fin)

        try:
            mes_inicio2 = int(mes_inicio)
            mes_fin2 = int(mes_fin)
        except ValueError:
            messagebox.showerror("Error", "Mes de inicio y fin deben ser numéricos.")
            return False

        # Validaciones de mes y año
        if mes_inicio2 < 1 or mes_inicio2 > 12 or mes_fin2 < 1 or mes_fin2 > 12:
            messagebox.showerror("Error", "Los meses deben estar entre 1 y 12.")
            return False

        if año_fin2 < año_inicio2:
            messagebox.showerror("Error", "El año de fin no puede ser menor al año de inicio.")
            return False

        if año_fin2 == año_inicio2 and mes_fin2 < mes_inicio2:
            messagebox.showerror("Error", "Si el año de inicio y fin son iguales, el mes debe ser mayor o igual al mes de inicio.")
            return False

        # Convertir los valores a enteros
        try:
            total_ingresosf = float(total_ingresos)
            total_gastosf = float(total_gastos)
            total_ahorrof = float(total_ahorro)
        except ValueError:
            messagebox.showerror("Error", "Los ingresos, gastos y el ahorro deben ser valores numéricos.")
            return False

        if total_ingresosf <= 0:
            messagebox.showerror("Error", "El total de ingresos debe ser mayor a 0.")
            return False

        if total_gastosf < 0 or total_ahorrof < 0:
            messagebox.showerror("Error", "Los gastos y el ahorro deben ser mayores a 0.")
            return False

        if total_ingresosf < total_gastosf + total_ahorrof:
            messagebox.showerror("Error", "El total de ingresos debe ser mayor o igual a la suma de los gastos y el ahorro.")
            return False

        # Verificar si ya existe un presupuesto activo para el mismo periodo
        cursor.execute("""
            SELECT nombre FROM presupuestos 
            WHERE anio_inicio = :anio_inicio AND mes_inicio = :mes_inicio 
            AND anio_fin = :anio_fin AND mes_fin = :mes_fin AND estado = 'ACTIVO'
        """, {
            "anio_inicio": año_inicio2,
            "mes_inicio": mes_inicio2,
            "anio_fin": año_fin2,
            "mes_fin": mes_fin2
        })

        if cursor.fetchone():
            messagebox.showerror("Error", "Ya existe un presupuesto activo para este período.")
            return False

        # Insertar presupuesto en la base de datos
        cursor.execute("""
            INSERT INTO presupuestos (nombre, anio_inicio, mes_inicio, anio_fin, mes_fin, total_ingresos, total_gastos, total_ahorro, estado, fecha_creacion)
            VALUES (:nombre, :anio_inicio, :mes_inicio, :anio_fin, :mes_fin, :total_ingresos, :total_gastos, :total_ahorro, 'ACTIVO', SYSDATE)
        """, {
            "nombre": nombre_presupuesto,
            "anio_inicio": año_inicio2,
            "mes_inicio": mes_inicio2,
            "anio_fin": año_fin2,
            "mes_fin": mes_fin2,
            "total_ingresos": total_ingresosf,
            "total_gastos": total_gastosf,
            "total_ahorro": total_ahorrof
        })

        conn.commit()
        messagebox.showinfo("Presupuesto registrado", f"Presupuesto '{nombre_presupuesto}' creado exitosamente")
        return True

    except cx_Oracle.DatabaseError as e:
        messagebox.showerror("Error", f"Error al guardar el presupuesto: {e}")
        return False
    finally:
        cursor.close()
        conn.close()
        
#editar el presupuestp
def registrar_presupuesto_detalle(id_detalle, subcategoria, monto_mensual, observaciones):
    conn = conectar_oracle()  # Conexión a la base de datos
    if conn is None:
        return False

    try:
        cursor = conn.cursor()

        # Validación de campos
        if not id_detalle or not subcategoria or not monto_mensual:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return False

        # Insertar en la base de datos
        cursor.execute("""
            INSERT INTO presupuesto_detalle (id_detalle, subcategoria, monto_mensual, observaciones)
            VALUES (:id_detalle, :subcategoria, :monto_mensual, :observaciones)
        """, {
            "id_detalle": id_detalle,
            "subcategoria": subcategoria,
            "monto_mensual": monto_mensual,
            "observaciones": observaciones
        })

        conn.commit()
        messagebox.showinfo("Detalle registrado", "Detalle del presupuesto registrado correctamente.")
        return True
    except cx_Oracle.DatabaseError as e:
        messagebox.showerror("Error", f"Error al registrar el detalle: {e}")
        return False
    finally:
        cursor.close()
        conn.close()
        

# ---------------------- VENTANAS ---------------------- #
def ventana_presupuesto():
    # Configuración de la ventana
    win = tk.Toplevel()
    win.title("Presupuesto")
    win.geometry("650x500")
    win.configure(bg="#020617")

    # Formulario de entrada de presupuesto
    form = tk.Frame(win, bg="#020617")
    form.pack(pady=5)

    # Campos de entrada
    labels = ["Nombre del presupuesto", "Año de inicio", "Mes de inicio (1-12)", "Año de fin", "Mes de fin (1-12)", "Total de ingresos", "Total de gastos", "Total de ahorro"]
    entries = []
    for idx, text in enumerate(labels):
        tk.Label(form, text=text, fg="white", bg="#020617").grid(row=idx*2, column=0, sticky="w")
        entry = tk.Entry(form)
        entry.grid(row=idx*2 + 1, column=0, pady=(0, 8), ipadx=60)
        entries.append(entry)

    def enviar_presupuesto():
        nombre_presupuesto, anio_ini, mes_ini, anio_fin, mes_fin, ingresos, gastos, ahorro = [entry.get() for entry in entries]
        if registrarPresupuesto(nombre_presupuesto, anio_ini, mes_ini, anio_fin, mes_fin, ingresos, gastos, ahorro):
            actualizar_tabla()  # Actualiza la tabla
            for entry in entries:
                entry.delete(0, tk.END)

    tk.Button(
        win,
        text="Guardar presupuesto",
        bg="#22c55e",
        fg="white",
        bd=0,
        font=("Segoe UI", 10, "bold"),
        activebackground="#16a34a",
        activeforeground="white",
        width=22,
        command=enviar_presupuesto
    ).pack(pady=5)

    # Función de regresar al menú principal
    def regresar_menu():
        win.destroy()
        ventana_menu_principal("Usuario")  # Regresar al menú principal

    tk.Button(
        win,
        text="Regresar al Menú Principal",
        bg="#2563eb",
        fg="white",
        bd=0,
        font=("Segoe UI", 10, "bold"),
        activebackground="#1e40af",
        activeforeground="white",
        width=22,
        command=regresar_menu
    ).pack(pady=10)

    # Agregar un botón para editar los detalles del presupuesto
    def editar_detalles():
        ventana_editar_detalles()  # Abrir la ventana para editar los detalles

    tk.Button(
        win,
        text="Editar Detalles",
        bg="#f59e0b",
        fg="white",
        bd=0,
        font=("Segoe UI", 10, "bold"),
        activebackground="#eab308",
        activeforeground="white",
        width=22,
        command=editar_detalles
    ).pack(pady=10)

    # ---------- TABLA DE PRESUPUESTOS ----------
    tabla_frame = tk.Frame(win, bg="#020617")
    tabla_frame.pack(pady=10, fill="both", expand=True)

    columnas = ("nombre", "periodo", "ingresos", "gastos", "ahorro", "estado")

    tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings", height=8)
    tabla.heading("nombre", text="Nombre")
    tabla.heading("periodo", text="Periodo")
    tabla.heading("ingresos", text="Ingresos")
    tabla.heading("gastos", text="Gastos")
    tabla.heading("ahorro", text="Ahorro")
    tabla.heading("estado", text="Estado")

    tabla.column("nombre", width=160)
    tabla.column("periodo", width=130)
    tabla.column("ingresos", width=80, anchor="e")
    tabla.column("gastos", width=80, anchor="e")
    tabla.column("ahorro", width=80, anchor="e")
    tabla.column("estado", width=80, anchor="center")

    tabla.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla.yview)
    scrollbar.pack(side="right", fill="y")
    tabla.configure(yscrollcommand=scrollbar.set)

    # Función para actualizar la tabla con los datos de la lista `presupuestos`
    def actualizar_tabla():
        # Limpiar filas
        for fila in tabla.get_children():
            tabla.delete(fila)

        # Cargar desde la lista `presupuestos`
        for p in presupuestos:
            periodo = f"{p['mes_inicio']:02d}/{p['anio_inicio']} - {p['mes_fin']:02d}/{p['anio_fin']}"
            tabla.insert(
                "",
                "end",
                values=(
                    p["nombre"],
                    periodo,
                    f"{p['total_ingresos']:.2f}",
                    f"{p['total_gastos']:.2f}",
                    f"{p['total_ahorro']:.2f}",
                    p["estado"]
                )
            )
    # Cargar tabla con lo que ya haya
    actualizar_tabla()

def actualizar_tabla_detalles():
    conn = conectar_oracle()  # Conexión a la base de datos
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        # Obtener todos los detalles de presupuesto
        cursor.execute("""
            SELECT id_detalle, subcategoria, monto_mensual, observaciones 
            FROM presupuesto_detalle
        """)

        # Limpiar filas anteriores en la tabla
        for fila in tabla.get_children():
            tabla.delete(fila)

        # Insertar los nuevos detalles en la tabla
        for detalle in cursor.fetchall():
            tabla.insert("", "end", values=(
                detalle[0],  # id_detalle
                detalle[1],  # subcategoria
                f"{detalle[2]:.2f}",  # monto mensual
                detalle[3]  # observaciones
            ))

    except cx_Oracle.DatabaseError as e:
        messagebox.showerror("Error", f"Error al cargar los detalles: {e}")
    finally:
        cursor.close()
        conn.close()

# Ventana para editar los detalles del presupuesto
def ventana_editar_detalles():
    win = tk.Toplevel()
    win.title("Editar Detalles del Presupuesto")
    win.geometry("650x500")
    win.configure(bg="#020617")

    # Encabezado
    tk.Label(
        win,
        text="Editar Detalles del Presupuesto",
        font=("Segoe UI", 14, "bold"),
        fg="#22c55e",
        bg="#020617"
    ).pack(pady=10)

    # Formulario
    form = tk.Frame(win, bg="#020617")
    form.pack(pady=5)

    # Campos de entrada para edición de los detalles
    labels = ["ID del detalle", "Subcategoría", "Monto Mensual", "Observaciones"]
    entries = []
    for idx, text in enumerate(labels):
        tk.Label(form, text=text, fg="white", bg="#020617").grid(row=idx*2, column=0, sticky="w")
        entry = tk.Entry(form)
        entry.grid(row=idx*2 + 1, column=0, pady=(0, 8), ipadx=60)
        entries.append(entry)

    def guardar_detalle():
        id_detalle, subcategoria, monto_mensual, observaciones = [entry.get() for entry in entries]
        if registrar_presupuesto_detalle(id_detalle, subcategoria, monto_mensual, observaciones):
            actualizar_tabla()
            for entry in entries:
                entry.delete(0, tk.END)
    tk.Button(
        win,
        text="Guardar Detalle",
        bg="#22c55e",
        fg="white",
        bd=0,
        font=("Segoe UI", 10, "bold"),
        activebackground="#16a34a",
        activeforeground="white",
        width=22,
        command=guardar_detalle
    ).pack(pady=5)

    # Función de regresar al menú principal
    def regresar_menu():
        win.destroy()
        ventana_menu_principal("Usuario")  # Regresar al menú principal

    tk.Button(
        win,
        text="Regresar al Menú Principal",
        bg="#2563eb",
        fg="white",
        bd=0,
        font=("Segoe UI", 10, "bold"),
        activebackground="#1e40af",
        activeforeground="white",
        width=22,
        command=regresar_menu
    ).pack(pady=10)

def registrar_presupuesto_detalle(id_detalle, subcategoria, monto_mensual, observaciones):
    conn = conectar_oracle()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()

        # Validación de campos
        if not id_detalle or not subcategoria or not monto_mensual:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return False

        # Insertar en la base de datos
        cursor.execute("""
            UPDATE presupuesto_detalle
            SET monto_mensual = :monto_mensual, observaciones = :observaciones
            WHERE id_detalle = :id_detalle AND subcategoria = :subcategoria
        """, {
            "id_detalle": id_detalle,
            "subcategoria": subcategoria,
            "monto_mensual": monto_mensual,
            "observaciones": observaciones
        })

        conn.commit()
        messagebox.showinfo("Detalle actualizado", "Detalle del presupuesto actualizado correctamente.")
        return True
    except cx_Oracle.DatabaseError as e:
        messagebox.showerror("Error", f"Error al actualizar el detalle: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

   
# Transacciones
def registrar_transaccion(correo_usuario, presupuesto_id, año_transaccion, mes_transaccion, subcategoria_id, obligacion_id, tipo_transaccion, descripcion, monto, fecha_transaccion, metodo_pago, numero_factura, observaciones):
    conn = conectar_oracle()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()

        # Verificación de los datos
        if not correo_usuario or not presupuesto_id or not tipo_transaccion or not monto or not fecha_transaccion:
            messagebox.showerror("Error", "Los campos obligatorios deben estar completos.")
            return False

        # Validación del tipo de transacción
        if tipo_transaccion not in ['ingreso', 'gasto', 'ahorro']:
            messagebox.showerror("Error", "El tipo de transacción debe ser 'ingreso', 'gasto' o 'ahorro'.")
            return False

        # Validación de los valores del año y mes de la transacción
        if not (1 <= mes_transaccion <= 12):
            messagebox.showerror("Error", "El mes debe estar entre 1 y 12.")
            return False

        # Insertar la transacción en la base de datos
        cursor.execute("""
            INSERT INTO transacciones (
                correo_usuario, presupuesto_id, año_transaccion, mes_transaccion, subcategoria_id,
                obligacion_id, tipo_transaccion, descripcion, monto, fecha_transaccion, metodo_pago, 
                numero_factura, observaciones
            ) VALUES (
                :correo_usuario, :presupuesto_id, :año_transaccion, :mes_transaccion, :subcategoria_id,
                :obligacion_id, :tipo_transaccion, :descripcion, :monto, :fecha_transaccion, :metodo_pago,
                :numero_factura, :observaciones
            )
        """, {
            "correo_usuario": correo_usuario,
            "presupuesto_id": presupuesto_id,
            "año_transaccion": año_transaccion,
            "mes_transaccion": mes_transaccion,
            "subcategoria_id": subcategoria_id,
            "obligacion_id": obligacion_id,
            "tipo_transaccion": tipo_transaccion,
            "descripcion": descripcion,
            "monto": monto,
            "fecha_transaccion": fecha_transaccion,
            "metodo_pago": metodo_pago,
            "numero_factura": numero_factura,
            "observaciones": observaciones
        })
        conn.commit()
        messagebox.showinfo("Transacción registrada", "Transacción registrada exitosamente.")
        return True
    except cx_Oracle.DatabaseError as e:
        messagebox.showerror("Error", f"Error al guardar la transacción: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def actualizar_tabla_transacciones():
    conn = conectar_oracle()
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        # Obtener todas las transacciones
        cursor.execute("""
            SELECT t.nombre, t.año_transaccion, t.mes_transaccion, t.tipo_transaccion, t.descripcion, t.monto, t.fecha_transaccion
            FROM transacciones t
            JOIN presupuestos p ON t.presupuesto_id = p.id_presupuesto
            WHERE p.estado = 'ACTIVO'
        """)

        # Limpiar filas anteriores
        for fila in tabla.get_children():
            tabla.delete(fila)

        # Insertar los nuevos datos en la tabla
        for t in cursor.fetchall():
            tabla.insert("", "end", values=(
                t[0],  # nombre
                f"{t[1]}/{t[2]:02d}",  # año/mes
                t[3],  # tipo_transaccion
                t[4],  # descripción
                f"{t[5]:.2f}",  # monto
                t[6]  # fecha_transaccion
            ))
    except cx_Oracle.DatabaseError as e:
        messagebox.showerror("Error", f"Error al cargar las transacciones: {e}")
    finally:
        cursor.close()
        conn.close()
        
def ventana_transacciones():
    win = tk.Toplevel()
    win.title("Registrar Transacción")
    win.geometry("650x500")
    win.configure(bg="#020617")
    # Formulario para la transacción
    form = tk.Frame(win, bg="#020617")
    form.pack(pady=5)
    # Campos de entrada
    labels = ["Año de transacción", "Mes de transacción (1-12)", "Subcategoría", "Obligación", "Tipo de transacción", "Descripción", "Monto", "Fecha de la transacción", "Método de pago", "Número de factura", "Observaciones"]
    entries = []
    for idx, text in enumerate(labels):
        tk.Label(form, text=text, fg="white", bg="#020617").grid(row=idx*2, column=0, sticky="w")
        entry = tk.Entry(form)
        entry.grid(row=idx*2 + 1, column=0, pady=(0, 8), ipadx=60)
        entries.append(entry)
    def enviar_transaccion():
        # Obtener todos los datos de los campos
        año_transaccion, mes_transaccion, subcategoria_id, obligacion_id, tipo_transaccion, descripcion, monto, fecha_transaccion, metodo_pago, numero_factura, observaciones = [entry.get() for entry in entries]
        ok = registrar_transaccion(
            "usuario_email",  # Este dato debería venir del usuario que está logueado
            1,  # ID del presupuesto (esto depende de la lógica del presupuesto)
            año_transaccion,
            mes_transaccion,
            subcategoria_id,
            obligacion_id,
            tipo_transaccion,
            descripcion,
            monto,
            fecha_transaccion,
            metodo_pago,
            numero_factura,
            observaciones
        )
        if ok:
            actualizar_tabla_transacciones()
    tk.Button(
        win,
        text="Guardar transacción",
        bg="#22c55e",
        fg="white",
        bd=0,
        font=("Segoe UI", 10, "bold"),
        activebackground="#16a34a",
        activeforeground="white",
        width=22,
        command=enviar_transaccion
    ).pack(pady=5)
    def regresar_menu():
        win.destroy()
        ventana_menu_principal("Usuario")  # Cambiar 'Usuario' por el nombre real del usuario

    # Botón para regresar al Menú Principal
    tk.Button(
        win,
        text="Regresar al Menú Principal",
        bg="#2563eb",
        fg="white",
        bd=0,
        font=("Segoe UI", 10, "bold"),
        activebackground="#1e40af",
        activeforeground="white",
        width=22,
        command=regresar_menu
    ).pack(pady=10)
    # Tabla de transacciones
    tabla_frame = tk.Frame(win, bg="#020617")
    tabla_frame.pack(pady=10, fill="both", expand=True)
    columnas = ("nombre", "año/mes", "tipo", "descripcion", "monto", "fecha")
    tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings", height=8)
    tabla.heading("nombre", text="Nombre")
    tabla.heading("año/mes", text="Año/Mes")
    tabla.heading("tipo", text="Tipo")
    tabla.heading("descripcion", text="Descripción")
    tabla.heading("monto", text="Monto")
    tabla.heading("fecha", text="Fecha")
    tabla.pack(side="left", fill="both", expand=True)
    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla.yview)
    scrollbar.pack(side="right", fill="y")
    tabla.configure(yscrollcommand=scrollbar.set)
    # Actualizar la tabla
    actualizar_tabla_transacciones()
#metodo de obligacion fija 
def registrar_obligacion_fija(descripcion, subcategoria, monto_fijo, dia_vencimiento, fecha_inicio, fecha_fin):
    conn = conectar_oracle()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()

        # Validación de los campos
        if not descripcion or not subcategoria or not monto_fijo or not dia_vencimiento:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return False

        if not monto_fijo.isdigit() or not dia_vencimiento.isdigit():
            messagebox.showerror("Error", "Monto y día de vencimiento deben ser numéricos")
            return False

        # Comprobaciones sobre las fechas
        if fecha_inicio >= fecha_fin:
            messagebox.showerror("Error", "La fecha de inicio debe ser anterior a la fecha de finalización")
            return False

        # Insertar la obligación fija en la base de datos
        cursor.execute("""
            INSERT INTO obligaciones_fijas (descripcion, subcategoria, monto_fijo, dia_vencimiento, fecha_inicio, fecha_fin, estado)
            VALUES (:descripcion, :subcategoria, :monto_fijo, :dia_vencimiento, :fecha_inicio, :fecha_fin, 'ACTIVO')
        """, {
            "descripcion": descripcion,
            "subcategoria": subcategoria,
            "monto_fijo": monto_fijo,
            "dia_vencimiento": dia_vencimiento,
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin
        })

        conn.commit()
        messagebox.showinfo("Obligación registrada", "Obligación fija registrada correctamente")
        return True
    except cx_Oracle.DatabaseError as e:
        messagebox.showerror("Error", f"Error al registrar la obligación fija: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

# Ventana para registrar obligación fija
def ventana_obligacion_fija():
    win = tk.Toplevel()
    win.title("Registrar Obligación Fija")
    win.geometry("650x500")
    win.configure(bg="#020617")

    # Encabezado
    tk.Label(
        win,
        text="Gestión de Obligaciones Fijas",
        font=("Segoe UI", 14, "bold"),
        fg="#22c55e",
        bg="#020617"
    ).pack(pady=10)

    # Formulario
    form = tk.Frame(win, bg="#020617")
    form.pack(pady=5)

    # Campos de entrada
    labels = ["Descripción", "Subcategoría", "Monto fijo mensual", "Día de vencimiento", "Fecha de inicio", "Fecha de fin"]
    entries = []
    for idx, text in enumerate(labels):
        tk.Label(form, text=text, fg="white", bg="#020617").grid(row=idx*2, column=0, sticky="w")
        entry = tk.Entry(form)
        entry.grid(row=idx*2 + 1, column=0, pady=(0, 8), ipadx=60)
        entries.append(entry)

    def enviar_obligacion():
        descripcion, subcategoria, monto_fijo, dia_vencimiento, fecha_inicio, fecha_fin = [entry.get() for entry in entries]
        if registrar_obligacion_fija(descripcion, subcategoria, monto_fijo, dia_vencimiento, fecha_inicio, fecha_fin):
            actualizar_tabla_obligaciones()
            for entry in entries:
                entry.delete(0, tk.END)

    tk.Button(
        win,
        text="Guardar obligación",
        bg="#22c55e",
        fg="white",
        bd=0,
        font=("Segoe UI", 10, "bold"),
        activebackground="#16a34a",
        activeforeground="white",
        width=22,
        command=enviar_obligacion
    ).pack(pady=5)

    # Función de regresar al menú principal
    def regresar_menu():
        win.destroy()
        ventana_menu_principal("Usuario")  # Regresar al menú principal

    tk.Button(
        win,
        text="Regresar al Menú Principal",
        bg="#2563eb",
        fg="white",
        bd=0,
        font=("Segoe UI", 10, "bold"),
        activebackground="#1e40af",
        activeforeground="white",
        width=22,
        command=regresar_menu
    ).pack(pady=10)
       
#meta ahorro 
# Función para registrar una meta de ahorro
def registrar_meta_ahorro(descripcion, monto_objetivo, monto_ahorrado, fecha_inicio, fecha_fin):
    conn = conectar_oracle()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()

        # Validación de los campos
        if not descripcion or not monto_objetivo or not monto_ahorrado or not fecha_inicio or not fecha_fin:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return False

        if not monto_objetivo.isdigit() or not monto_ahorrado.isdigit():
            messagebox.showerror("Error", "Monto objetivo y monto ahorrado deben ser numéricos")
            return False

        # Comprobaciones sobre las fechas
        if fecha_inicio >= fecha_fin:
            messagebox.showerror("Error", "La fecha de inicio debe ser anterior a la fecha de finalización")
            return False

        # Insertar la meta de ahorro en la base de datos
        cursor.execute("""
            INSERT INTO metas_ahorro (descripcion, monto_objetivo, monto_ahorrado, fecha_inicio, fecha_fin, estado)
            VALUES (:descripcion, :monto_objetivo, :monto_ahorrado, :fecha_inicio, :fecha_fin, 'ACTIVO')
        """, {
            "descripcion": descripcion,
            "monto_objetivo": monto_objetivo,
            "monto_ahorrado": monto_ahorrado,
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin
        })

        conn.commit()
        messagebox.showinfo("Meta de ahorro registrada", "Meta de ahorro registrada correctamente")
        return True
    except cx_Oracle.DatabaseError as e:
        messagebox.showerror("Error", f"Error al registrar la meta de ahorro: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

# Ventana para registrar meta de ahorro
def ventana_meta_ahorro():
    win = tk.Toplevel()
    win.title("Registrar Meta de Ahorro")
    win.geometry("650x500")
    win.configure(bg="#020617")

    # Encabezado
    tk.Label(
        win,
        text="Gestión de Metas de Ahorro",
        font=("Segoe UI", 14, "bold"),
        fg="#22c55e",
        bg="#020617"
    ).pack(pady=10)

    # Formulario
    form = tk.Frame(win, bg="#020617")
    form.pack(pady=5)

    # Campos de entrada
    labels = ["Descripción", "Monto objetivo", "Monto ahorrado", "Fecha de inicio", "Fecha de fin"]
    entries = []
    for idx, text in enumerate(labels):
        tk.Label(form, text=text, fg="white", bg="#020617").grid(row=idx*2, column=0, sticky="w")
        entry = tk.Entry(form)
        entry.grid(row=idx*2 + 1, column=0, pady=(0, 8), ipadx=60)
        entries.append(entry)

    def enviar_meta():
        descripcion, monto_objetivo, monto_ahorrado, fecha_inicio, fecha_fin = [entry.get() for entry in entries]
        if registrar_meta_ahorro(descripcion, monto_objetivo, monto_ahorrado, fecha_inicio, fecha_fin):
            actualizar_tabla_metas()
            for entry in entries:
                entry.delete(0, tk.END)

    tk.Button(
        win,
        text="Guardar meta",
        bg="#22c55e",
        fg="white",
        bd=0,
        font=("Segoe UI", 10, "bold"),
        activebackground="#16a34a",
        activeforeground="white",
        width=22,
        command=enviar_meta
    ).pack(pady=5)

    # Función de regresar al menú principal
    def regresar_menu():
        win.destroy()
        ventana_menu_principal("Usuario")  # Regresar al menú principal

    tk.Button(
        win,
        text="Regresar al Menú Principal",
        bg="#2563eb",
        fg="white",
        bd=0,
        font=("Segoe UI", 10, "bold"),
        activebackground="#1e40af",
        activeforeground="white",
        width=22,
        command=regresar_menu
    ).pack(pady=10)
   
# Ventana para crear categoría
def ventana_categoria():
    win = tk.Toplevel()
    win.title("Registrar Categoría")
    win.geometry("650x400")
    win.configure(bg="#020617")

    # Encabezado
    tk.Label(
        win,
        text="Crear Categoría",
        font=("Segoe UI", 14, "bold"),
        fg="#22c55e",
        bg="#020617"
    ).pack(pady=10)

    # Formulario de categoría
    form = tk.Frame(win, bg="#020617")
    form.pack(pady=5)

    # Campo de entrada de nombre de la categoría
    tk.Label(form, text="Nombre de la categoría:", fg="white", bg="#020617").grid(row=0, column=0, sticky="w")
    entry_categoria = tk.Entry(form, width=30)
    entry_categoria.grid(row=1, column=0, pady=(0, 8))

    def guardar_categoria():
        categoria = entry_categoria.get()
        if not categoria:
            messagebox.showerror("Error", "El nombre de la categoría es obligatorio")
            return
        if crear_categoria(categoria):
            # Limpiar campo de entrada
            entry_categoria.delete(0, tk.END)
            # Mensaje de éxito
            messagebox.showinfo("Categoría registrada", f"Categoría '{categoria}' registrada correctamente.")
            win.destroy()

    # Botón para guardar la categoría
    tk.Button(
        win,
        text="Guardar categoría",
        bg="#22c55e",
        fg="white",
        bd=0,
        font=("Segoe UI", 10, "bold"),
        activebackground="#16a34a",
        activeforeground="white",
        width=22,
        command=guardar_categoria
    ).pack(pady=5)

    # Función para regresar al menú principal
    def regresar_menu():
        win.destroy()
        ventana_menu_principal("Usuario")  # Regresar al menú principal

    tk.Button(
        win,
        text="Regresar al Menú Principal",
        bg="#2563eb",
        fg="white",
        bd=0,
        font=("Segoe UI", 10, "bold"),
        activebackground="#1e40af",
        activeforeground="white",
        width=22,
        command=regresar_menu
    ).pack(pady=10)

# Función que guarda la categoría (y crea automáticamente la subcategoría)
def crear_categoria(categoria):
    try:
        # Conexión a la base de datos
        conn = conectar_oracle()  # Asumiendo que la conexión ya está configurada
        if conn is None:
            return False

        cursor = conn.cursor()

        # Insertar la categoría en la base de datos
        cursor.execute("""
            INSERT INTO categorias (nombre)
            VALUES (:categoria)
        """, {"categoria": categoria})

        # Crear automáticamente la subcategoría "General" asociada a la categoría
        cursor.execute("""
            INSERT INTO subcategorias (nombre, categoria_id)
            VALUES ('General', (SELECT id FROM categorias WHERE nombre = :categoria))
        """, {"categoria": categoria})

        conn.commit()
        return True

    except cx_Oracle.DatabaseError as e:
        messagebox.showerror("Error", f"Error al guardar la categoría: {e}")
        return False
    finally:
        cursor.close()
        conn.close()   
    
# ---------------------- MENÚ PRINCIPAL ---------------------- #
def ventana_menu_principal(nombre_usuario):
    menu = tk.Toplevel()
    menu.title("Sistema de Presupuesto - Menú Principal")
    menu.geometry("480x520")
    menu.configure(bg="#020617")
    # Encabezado
    topbar = tk.Frame(menu, bg="#020617")
    topbar.pack(fill="x", pady=10, padx=15)
    tk.Label(
        topbar,
        text="Sistema de Presupuesto",
        font=("Segoe UI", 16, "bold"),
        fg="#22c55e",
        bg="#020617"
    ).pack(side="left")
    tk.Label(
        topbar,
        text=f"Sesión de {nombre_usuario}",
        font=("Segoe UI", 9),
        fg="#9ca3af",
        bg="#020617"
    ).pack(side="right")
    main = tk.Frame(menu, bg="#020617")
    main.pack(pady=15)
    tk.Label(
        main,
        text="Menú principal",
        font=("Segoe UI", 12, "bold"),
        fg="#e5e7eb",
        bg="#020617"
    ).grid(row=0, column=0, columnspan=2, pady=(0, 15))
    def mk_btn(texto, row, col,command=None):
        tk.Button(
            main,
            text=texto,
            width=22,
            height=2,
            bg="#111827",
            fg="#e5e7eb",
            bd=0,
            activebackground="#1f2937",
            activeforeground="white",
            font=("Segoe UI", 9, "bold"),
            command=command
        ).grid(row=row, column=col, padx=10, pady=6)
    mk_btn("Presupuesto",        1, 0, ventana_presupuesto)
    mk_btn("Transacciones",      1, 1, ventana_transacciones)
    mk_btn("Categorías",         2, 0, ventana_categoria)
    mk_btn("Obligaciones Fijas", 2, 1, ventana_obligacion_fija)
    mk_btn("Metas de Ahorro",    3, 0, ventana_meta_ahorro)
    mk_btn("Reportes",           3, 1)
    tk.Button(
        main,
        text="Cerrar sesión",
        width=22,
        height=2,
        bg="#b91c1c",
        fg="white",
        bd=0,
        activebackground="#7f1d1d",
        activeforeground="white",
        font=("Segoe UI", 9, "bold"),
        command=menu.destroy
    ).grid(row=4, column=1, padx=10, pady=15)
# ---------------------- VENTANA REGISTRO ---------------------- #
def ventana_registro():
    reg = tk.Toplevel()
    reg.title("Registrar Usuario")
    reg.geometry("350x430")
    reg.configure(bg="#020617")
    tk.Label(
        reg, text="Registro de Usuario",
        font=("Segoe UI", 14, "bold"),
        fg="#e5e7eb",
        bg="#020617"
    ).pack(pady=10)
    form = tk.Frame(reg, bg="#020617")
    form.pack(pady=5)
    # Campos
    labels = ["Nombre", "Apellido", "Correo", "Edad", "Salario", "Contraseña"]
    entries = []
    for idx, texto in enumerate(labels):
        tk.Label(form, text=texto, font=("Segoe UI", 9), fg="#e5e7eb", bg="#020617").grid(row=idx*2, column=0, sticky="w")
        entry = tk.Entry(form, show="*" if texto == "Contraseña" else "")
        entry.grid(row=idx*2 + 1, column=0, pady=(0, 8), ipadx=60)
        entries.append(entry)
    def enviar_registro():
        nombre, apellido, correo, edad, salario, password = [e.get() for e in entries]
        ok = registrar_usuario(nombre, correo, edad, apellido, salario, password)
        if ok:
            ventana_menu_principal(nombre)
            reg.destroy()
    tk.Button(
        reg,
        text="Registrar",
        bg="#22c55e",
        fg="white",
        bd=0,
        font=("Segoe UI", 10, "bold"),
        activebackground="#16a34a",
        activeforeground="white",
        command=enviar_registro
    ).pack(pady=15)
    
    
# ---------------------- VENTANA LOGIN ---------------------- #
def ventana_login():
    login = tk.Toplevel()
    login.title("Iniciar Sesión")
    login.geometry("350x260")
    login.configure(bg="#020617")
    tk.Label(
        login,
        text="Iniciar Sesión",
        font=("Segoe UI", 14, "bold"),
        fg="#e5e7eb",
        bg="#020617"
    ).pack(pady=10)
    form = tk.Frame(login, bg="#020617")
    form.pack(pady=5)
    tk.Label(form, text="Correo", font=("Segoe UI", 9), fg="#e5e7eb", bg="#020617").grid(row=0, column=0, sticky="w")
    entry_correo = tk.Entry(form)
    entry_correo.grid(row=1, column=0, pady=(0, 10), ipadx=60)
    tk.Label(form, text="Contraseña", font=("Segoe UI", 9), fg="#e5e7eb", bg="#020617").grid(row=2, column=0, sticky="w")
    entry_password = tk.Entry(form, show="*")
    entry_password.grid(row=3, column=0, pady=(0, 10), ipadx=60)
    def enviar_login():
        nombre = ingreso_usuario(entry_correo.get(), entry_password.get())
        if nombre:
            ventana_menu_principal(nombre)
            login.destroy()
    tk.Button(
        login,
        text="Entrar",
        bg="#1d4ed8",
        fg="white",
        bd=0,
        font=("Segoe UI", 10, "bold"),
        activebackground="#1e40af",
        activeforeground="white",
        command=enviar_login
    ).pack(pady=15)
# ---------------------- VENTANA INICIO ---------------------- #
def ventana_inicio():
    root = tk.Tk()
    root.title("Sistema de Presupuesto")
    root.geometry("420x320")
    root.configure(bg="#020617")
    header = tk.Frame(root, bg="#020617")
    header.pack(fill="x", pady=10)
    tk.Label(
        header,
        text="Sistema de Presupuesto",
        font=("Segoe UI", 18, "bold"),
        fg="#22c55e",
        bg="#020617"
    ).pack()
    card = tk.Frame(root, bg="#020617", bd=0)
    card.pack(pady=20)
    tk.Label(
        card,
        text="Acceso al sistema",
        font=("Segoe UI", 11, "bold"),
        fg="#e5e7eb",
        bg="#020617"
    ).grid(row=0, column=0, pady=(0, 15))
    tk.Button(
        card,
        text="Crear cuenta",
        width=20,
        height=2,
        bg="#22c55e",
        fg="white",
        bd=0,
        activebackground="#16a34a",
        activeforeground="white",
        font=("Segoe UI", 10, "bold"),
        command=ventana_registro
    ).grid(row=1, column=0, pady=5)
    tk.Button(
        card,
        text="Iniciar sesión",
        width=20,
        height=2,
        bg="#1d4ed8",
        fg="white",
        bd=0,
        activebackground="#1e40af",
        activeforeground="white",
        font=("Segoe UI", 10, "bold"),
        command=ventana_login
    ).grid(row=2, column=0, pady=5)
    tk.Button(
        card,
        text="Salir",
        width=20,
        height=2,
        bg="#b91c1c",
        fg="white",
        bd=0,
        activebackground="#7f1d1d",
        activeforeground="white",
        font=("Segoe UI", 10, "bold"),
        command=root.destroy
    ).grid(row=3, column=0, pady=(15, 0))

    root.mainloop()
#main ejecucion
if __name__ == "__main__":
    ventana_inicio()
