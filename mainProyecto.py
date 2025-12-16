import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import oracledb
from datetime import date

import oracledb

# ---------------- SESIÓN ACTIVA ----------------
SESSION_USUARIO_ID = None
SESSION_USUARIO_NOMBRE = None
SESSION_PRESUPUESTO_ID = None


def conectar_oracle():
    try:
        connection = oracledb.connect(
            user="SisGestPresupuestos",
            password="1234",
            dsn="localhost/XEPDB1"
        )
        return connection
    except oracledb.DatabaseError as e:
        messagebox.showerror("Error", str(e))
        return None


def registrar_usuario(nombre, apellido, correo, salario):
    conn = conectar_oracle()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()

        if not nombre or not apellido or not correo or not salario:
            messagebox.showerror(
                "Error",
                "Nombre, apellido, correo y salario son obligatorios."
            )
            return False

        cursor.callproc(
            "sp_insertar_usuario",
            [
                nombre,
                apellido,
                correo,
                float(salario),
                "admin"
            ]
        )

        conn.commit()
        messagebox.showinfo(
            "Registro exitoso",
            f"Usuario '{nombre}' registrado correctamente"
        )
        return True

    except oracledb.DatabaseError as e:
        messagebox.showerror(
            "Error",
            f"Error al registrar el usuario:\n{e}"
        )
        return False

    finally:
        cursor.close()
        conn.close()


# Ventana para registrar el usuario
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
    labels = ["Nombre", "Apellido", "Correo", "Salario", "Contraseña"]
    entries = []
    for idx, texto in enumerate(labels):
        tk.Label(form, text=texto, font=("Segoe UI", 9), fg="#e5e7eb", bg="#020617").grid(row=idx * 2, column=0,
                                                                                          sticky="w")
        entry = tk.Entry(form, show="*" if texto == "Contraseña" else "")
        entry.grid(row=idx * 2 + 1, column=0, pady=(0, 8), ipadx=60)
        entries.append(entry)

    def enviar_registro():
        nombre, apellido, correo, edad, salario, password = [e.get() for e in entries]
        ok = registrar_usuario(nombre, apellido, correo, edad, salario, password)
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


def ingreso_usuario(correo, password):
    global SESSION_USUARIO_ID, SESSION_USUARIO_NOMBRE

    conn = conectar_oracle()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()

        nombre_out = cursor.var(str)
        activo_out = cursor.var(str)

        cursor.callproc(
            "sp_validar_usuario",
            [
                correo.strip().lower(),
                nombre_out,
                activo_out
            ]
        )

        nombre = nombre_out.getvalue()
        activo = activo_out.getvalue()

        if nombre is None:
            messagebox.showerror("Error", "El usuario no existe.")
            return None

        if activo is None or activo.strip().upper() != 'Y':
            messagebox.showerror("Error", "El usuario está inactivo.")
            return None

        return nombre

    except oracledb.DatabaseError as e:
        messagebox.showerror(
            "Error",
            f"Error al iniciar sesión:\n{e}"
        )
        return None

    finally:
        cursor.close()
        conn.close()


# Ventana de login para ingresar al sistema
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
    tk.Label(form, text="Contraseña", font=("Segoe UI", 9), fg="#e5e7eb", bg="#020617").grid(row=2, column=0,
                                                                                             sticky="w")
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


# Función para registrar un presupuesto
def registrarPresupuesto(
        nombre_presupuesto,
        anio_inicio,
        mes_inicio,
        anio_fin,
        mes_fin,
        ingresos,
        gastos,
        ahorro
):
    conn = conectar_oracle()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()

        # Validaciones básicas
        if not nombre_presupuesto:
            messagebox.showerror("Error", "El nombre del presupuesto es obligatorio")
            return False

        # Conversión segura
        anio_inicio = int(anio_inicio)
        mes_inicio = int(mes_inicio)
        anio_fin = int(anio_fin)
        mes_fin = int(mes_fin)

        ingresos = float(ingresos)
        gastos = float(gastos)
        ahorro = float(ahorro)

        fecha_inicio = date(anio_inicio, mes_inicio, 1)
        fecha_fin = date(anio_fin, mes_fin, 1)

        # ⚠️ ID DE USUARIO (TEMPORAL PARA DEFENSA)
        id_usuario = 1  # luego puedes hacerlo dinámico
        SESSION_PRESUPUESTO_ID = cursor.lastrowid

        cursor.callproc(
            "sp_insertar_presupuesto",
            [
                id_usuario,
                nombre_presupuesto,
                fecha_inicio,
                fecha_fin,
                ingresos,
                gastos,
                ahorro,
                "admin"
            ]
        )

        conn.commit()
        return True

    except (ValueError, TypeError):
        messagebox.showerror("Error", "Datos numéricos inválidos")
        return False

    except oracledb.DatabaseError as e:
        messagebox.showerror(
            "Error",
            f"Error al registrar el presupuesto:\n{e}"
        )
        return False

    finally:
        cursor.close()
        conn.close()


# Ventana Presupuesto
def ventana_presupuesto():
    win = tk.Toplevel()
    win.title("Registrar Presupuesto")
    win.geometry("650x500")
    win.configure(bg="#020617")

    form = tk.Frame(win, bg="#020617")
    form.pack(pady=5)

    # Campos de entrada
    labels = ["Nombre del presupuesto", "Año de inicio", "Mes de inicio (1-12)", "Año de fin", "Mes de fin (1-12)",
              "Total de ingresos", "Total de gastos", "Total de ahorro"]
    entries = []
    for idx, text in enumerate(labels):
        tk.Label(form, text=text, fg="white", bg="#020617").grid(row=idx * 2, column=0, sticky="w")
        entry = tk.Entry(form)
        entry.grid(row=idx * 2 + 1, column=0, pady=(0, 8), ipadx=60)
        entries.append(entry)

    def enviar_presupuesto():
        nombre_presupuesto, anio_ini, mes_ini, anio_fin, mes_fin, ingresos, gastos, ahorro = [entry.get() for entry in
                                                                                              entries]
        if registrarPresupuesto(nombre_presupuesto, anio_ini, mes_ini, anio_fin, mes_fin, ingresos, gastos, ahorro):
            messagebox.showinfo("Presupuesto registrado", "Presupuesto registrado correctamente")
            for entry in entries:
                entry.delete(0, tk.END)

    # BOTÓN GUARDAR TRANSACCIÓN (ASEGÚRATE QUE ESTÉ AQUÍ)
    btn_guardar = tk.Button(
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
    )
    btn_guardar.pack(pady=10)

    # Función de regresar al menú principal
    def regresar_menu():
        win.destroy()
        ventana_menu_principal("Usuario")  # Cambia "Usuario" por el nombre real del usuario

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


# Función para registrar una transacción
from datetime import date

from datetime import date

from datetime import date


def verificar_estado_presupuesto(presupuesto_id):
    conn = conectar_oracle()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT estado
            FROM presupuestos
            WHERE id_presupuesto = :presupuesto_id
        """, {"presupuesto_id": presupuesto_id})

        resultado = cursor.fetchone()

        if resultado is None:
            messagebox.showerror("Error", "El presupuesto no existe.")
            return False

        if resultado[0] != 'ACTIVO':
            messagebox.showerror("Error", "No se pueden registrar transacciones en presupuestos cerrados.")
            return False

        return True

    except oracledb.DatabaseError as e:
        messagebox.showerror("Error", f"Error al verificar el estado del presupuesto:\n{e}")
        return False

    finally:
        cursor.close()
        conn.close()


from datetime import datetime


def registrar_transaccion(
        id_usuario,
        presupuesto_id,
        fecha_str,
        id_subcategoria,
        tipo,
        descripcion,
        monto,
        metodo_pago
):
    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror(
            "Error",
            "La fecha debe tener el formato YYYY-MM-DD"
        )
        return False

    conn = conectar_oracle()
    cursor = conn.cursor()

    cursor.callproc(
        "sp_insertar_transaccion",
        [
            SESSION_USUARIO_ID,
            presupuesto_id,
            fecha,
            id_subcategoria,
            tipo,
            descripcion,
            monto,
            metodo_pago,
            "admin"  # usuario_creacion
        ]
    )

    conn.commit()
    cursor.close()
    conn.close()
    return True


def ventana_transacciones():
    print(">>> ventana_transacciones ejecutada")

    win = tk.Toplevel()
    win.title("Registrar Transacción")
    win.geometry("650x550")
    win.configure(bg="#020617")

    form = tk.Frame(win, bg="#020617")
    form.pack(pady=10)

    labels = [
        "Fecha (YYYY-MM-DD)",
        "ID Subcategoría",
        "Tipo (INGRESO/GASTO/AHORRO)",
        "Descripción",
        "Monto",
        "Método de pago"
    ]

    entries = []

    for i, text in enumerate(labels):
        tk.Label(form, text=text, fg="white", bg="#020617") \
            .grid(row=i * 2, column=0, sticky="w")
        e = tk.Entry(form, width=40)
        e.grid(row=i * 2 + 1, column=0, pady=5)
        entries.append(e)

    def enviar_transaccion():
        print(">>> click guardar")

        fecha, id_subcat, tipo, desc, monto, metodo = \
            [e.get() for e in entries]

        registrar_transaccion(
            SESSION_USUARIO_ID,
            1,  # presupuesto activo
            fecha,
            int(id_subcat),
            tipo.upper(),
            desc,
            float(monto),
            metodo
        )

    # 👇 BOTÓN GUARDA SIEMPRE
    tk.Button(
        win,
        text="Guardar Transacción",
        bg="#22c55e",
        fg="white",
        font=("Segoe UI", 10, "bold"),
        width=25,
        command=enviar_transaccion
    ).pack(pady=15)

    tk.Button(
        win,
        text="Regresar",
        bg="#2563eb",
        fg="white",
        width=25,
        command=win.destroy
    ).pack(pady=5)


# insertar categoria
def insertar_categoria(nombre, descripcion, tipo_categoria, icono, color):
    """Insertar una nueva categoría en la base de datos."""
    conn = conectar_oracle()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()

        # Verificación de los campos
        if not nombre or not tipo_categoria:
            messagebox.showerror("Error", "Nombre y tipo de categoría son obligatorios.")
            return False

        # Llamar al procedimiento de base de datos para insertar la categoría
        cursor.callproc("sp_insertar_categoria", [nombre, descripcion, tipo_categoria, icono, color, "admin"])

        conn.commit()
        messagebox.showinfo("Categoría registrada", f"Categoría '{nombre}' registrada correctamente")
        return True

    except cx_Oracle.DatabaseError as e:
        messagebox.showerror("Error", f"Error al registrar la categoría: {e}")
        return False
    finally:
        cursor.close()
        conn.close()


def ventana_categoria():
    win = tk.Toplevel()
    win.title("Registrar Categoría")
    win.geometry("650x500")
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

    # Campos de entrada
    tk.Label(form, text="Nombre de la categoría:", fg="white", bg="#020617").grid(row=0, column=0, sticky="w")
    entry_categoria = tk.Entry(form, width=30)
    entry_categoria.grid(row=1, column=0, pady=(0, 8))

    tk.Label(form, text="Tipo de categoría (ingreso/gasto):", fg="white", bg="#020617").grid(row=2, column=0,
                                                                                             sticky="w")
    entry_tipo_categoria = tk.Entry(form, width=30)
    entry_tipo_categoria.grid(row=3, column=0, pady=(0, 8))

    tk.Label(form, text="Descripción de la categoría:", fg="white", bg="#020617").grid(row=4, column=0, sticky="w")
    entry_descripcion = tk.Entry(form, width=30)
    entry_descripcion.grid(row=5, column=0, pady=(0, 8))

    tk.Label(form, text="Color de la categoría:", fg="white", bg="#020617").grid(row=6, column=0, sticky="w")
    entry_color = tk.Entry(form, width=30)
    entry_color.grid(row=7, column=0, pady=(0, 8))

    def guardar_categoria():
        categoria = entry_categoria.get()
        tipo_categoria = entry_tipo_categoria.get()
        descripcion = entry_descripcion.get()
        color = entry_color.get()

        if categoria and tipo_categoria:
            if insertar_categoria(categoria, descripcion, tipo_categoria, None, color):
                messagebox.showinfo("Categoría registrada", f"Categoría '{categoria}' registrada correctamente.")
                entry_categoria.delete(0, tk.END)
                entry_tipo_categoria.delete(0, tk.END)
                entry_descripcion.delete(0, tk.END)
                entry_color.delete(0, tk.END)
                cargar_categorias()  # Recargar las categorías después de guardar
        else:
            messagebox.showerror("Error", "El nombre y el tipo de la categoría son obligatorios")

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

    # Tabla de Categorías
    tabla_frame = tk.Frame(win, bg="#020617")
    tabla_frame.pack(pady=10, fill="both", expand=True)

    columnas = ("ID", "Nombre", "Tipo", "Descripción", "Color")

    tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings", height=8)
    tabla.heading("ID", text="ID")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Tipo", text="Tipo")
    tabla.heading("Descripción", text="Descripción")
    tabla.heading("Color", text="Color")

    tabla.column("ID", width=80)
    tabla.column("Nombre", width=150)
    tabla.column("Tipo", width=100)
    tabla.column("Descripción", width=150)
    tabla.column("Icono", width=100)

    tabla.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla.yview)
    scrollbar.pack(side="right", fill="y")
    tabla.configure(yscrollcommand=scrollbar.set)

    # Función para cargar las categorías
    def cargar_categorias():
        conn = conectar_oracle()
        if conn is None:
            return

        try:
            cursor = conn.cursor()

            # Cursor de salida correcto con oracledb
            out_cursor = cursor.var(oracledb.CURSOR)

            cursor.callproc(
                "sp_listar_categorias",
                [
                    None,  # o 'INGRESO' / 'GASTO'
                    out_cursor
                ]
            )

            # Limpiar tabla
            for fila in tabla.get_children():
                tabla.delete(fila)

            # Insertar filas
            for categoria in out_cursor.getvalue():
                tabla.insert(
                    "",
                    "end",
                    values=(
                        categoria[0],  # id_categoria
                        categoria[1],  # nombre
                        categoria[2],  # tipo_categoria
                        categoria[3],  # descripcion
                        categoria[4]  # color
                    )
                )

        except oracledb.DatabaseError as e:
            messagebox.showerror(
                "Error",
                f"Error al cargar las categorías:\n{e}"
            )

        finally:
            cursor.close()
            conn.close()

    win.after(100, cargar_categorias)

    # Función de regresar al menú principal
    def regresar_menu():
        win.destroy()
        ventana_menu_principal("Usuario")

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


from datetime import datetime
import oracledb


def insertar_obligacion_fija(
        id_subcategoria,
        nombre,
        descripcion,
        monto_mensual,
        fecha_inicio_str,
        fecha_vencimiento_str
):
    conn = conectar_oracle()
    if conn is None:
        return False

    try:
        # Parsear fechas
        try:
            fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d")
            fecha_vencimiento = datetime.strptime(fecha_vencimiento_str, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror(
                "Error",
                "Las fechas deben tener el formato YYYY-MM-DD"
            )
            return False

        cursor = conn.cursor()

        cursor.callproc(
            "sp_insertar_obligacion_fija",
            [
                SESSION_USUARIO_ID,  # id_usuario
                id_subcategoria,
                nombre,
                descripcion,
                float(monto_mensual),
                fecha_inicio,
                fecha_vencimiento,
                "admin"  # usuario_creacion
            ]
        )

        conn.commit()
        messagebox.showinfo(
            "Obligación registrada",
            f"Obligación '{nombre}' registrada correctamente"
        )
        return True

    except oracledb.DatabaseError as e:
        messagebox.showerror(
            "Error",
            f"Error al registrar la obligación fija:\n{e}"
        )
        return False

    finally:
        cursor.close()
        conn.close()


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
    labels = ["Nombre", "Descripción", "Monto Mensual", "Fecha de inicio", "Fecha de vencimiento"]
    entries = []
    for idx, text in enumerate(labels):
        tk.Label(form, text=text, fg="white", bg="#020617").grid(row=idx * 2, column=0, sticky="w")
        entry = tk.Entry(form)
        entry.grid(row=idx * 2 + 1, column=0, pady=(0, 8), ipadx=60)
        entries.append(entry)

    def enviar_obligacion():
        nombre, descripcion, monto_mensual, fecha_inicio, fecha_vencimiento = [entry.get() for entry in entries]
        if insertar_obligacion_fija(1, nombre, descripcion, monto_mensual, fecha_inicio,
                                    fecha_vencimiento):  # Subcategoria ID de ejemplo: 1
            messagebox.showinfo("Obligación registrada", "Obligación fija registrada correctamente")
            for entry in entries:
                entry.delete(0, tk.END)

    tk.Button(
        win,
        text="Guardar obligación fija",
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
        ventana_menu_principal("Usuario")

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


from datetime import datetime
import oracledb


def insertar_meta_ahorro(
        id_subcategoria,
        nombre,
        descripcion,
        monto_meta,
        fecha_inicio_str,
        fecha_objetivo_str,
        prioridad
):
    conn = conectar_oracle()
    if conn is None:
        return False

    try:
        # Validaciones mínimas
        if not nombre or not monto_meta or not fecha_inicio_str or not fecha_objetivo_str or not prioridad:
            messagebox.showerror(
                "Error",
                "Todos los campos son obligatorios."
            )
            return False

        # Parseo de fechas
        try:
            fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d")
            fecha_objetivo = datetime.strptime(fecha_objetivo_str, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror(
                "Error",
                "Las fechas deben tener el formato YYYY-MM-DD"
            )
            return False

        cursor = conn.cursor()

        cursor.callproc(
            "sp_insertar_meta_ahorro",
            [
                SESSION_USUARIO_ID,  # id_usuario
                id_subcategoria,
                nombre,
                descripcion,
                float(monto_meta),
                fecha_inicio,
                fecha_objetivo,
                prioridad.upper(),
                "admin"  # usuario_creacion
            ]
        )

        conn.commit()

        messagebox.showinfo(
            "Meta de ahorro registrada",
            f"Meta de ahorro '{nombre}' registrada correctamente"
        )
        return True

    except oracledb.DatabaseError as e:
        messagebox.showerror(
            "Error",
            f"Error al registrar la meta de ahorro:\n{e}"
        )
        return False

    finally:
        cursor.close()
        conn.close()


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
    labels = ["Nombre", "Descripción", "Monto Meta", "Fecha de inicio", "Fecha de objetivo", "Prioridad"]
    entries = []
    for idx, text in enumerate(labels):
        tk.Label(form, text=text, fg="white", bg="#020617").grid(row=idx * 2, column=0, sticky="w")
        entry = tk.Entry(form)
        entry.grid(row=idx * 2 + 1, column=0, pady=(0, 8), ipadx=60)
        entries.append(entry)

    def enviar_meta():
        nombre, descripcion, monto_meta, fecha_inicio, fecha_objetivo, prioridad = \
            [entry.get() for entry in entries]

        insertar_meta_ahorro(
            21,  # id_subcategoria (AHORRO)
            nombre,
            descripcion,
            monto_meta,
            fecha_inicio,
            fecha_objetivo,
            prioridad
        )

    tk.Button(
        win,
        text="Guardar meta de ahorro",
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
        ventana_menu_principal("Usuario")

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

    def mk_btn(texto, row, col, command=None):
        btn = tk.Button(
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
        )
        btn.grid(row=row, column=col, padx=10, pady=6)
        return btn

    mk_btn("Presupuesto", 1, 0, lambda: ventana_presupuesto())
    mk_btn("Transacciones", 1, 1, lambda: ventana_transacciones())
    mk_btn("Categorías", 2, 0, lambda: ventana_categoria())
    mk_btn("Obligaciones Fijas", 2, 1, lambda: ventana_obligacion_fija())
    mk_btn("Metas de Ahorro", 3, 0, lambda: ventana_meta_ahorro())
    mk_btn("Reportes", 3, 1, lambda: ventana_reportes())

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
    reg.geometry("350x500")
    reg.configure(bg="#020617")

    tk.Label(
        reg, text="Registro de Usuario",
        font=("Segoe UI", 14, "bold"),
        fg="#e5e7eb",
        bg="#020617"
    ).pack(pady=10)

    form = tk.Frame(reg, bg="#020617")
    form.pack(pady=5)

    labels = ["Nombre", "Apellido", "Correo", "Edad", "Salario", "Contraseña"]
    entries = []

    for idx, texto in enumerate(labels):
        tk.Label(
            form,
            text=texto,
            font=("Segoe UI", 9),
            fg="#e5e7eb",
            bg="#020617"
        ).grid(row=idx * 2, column=0, sticky="w")

        entry = tk.Entry(form, show="*" if texto == "Contraseña" else "")
        entry.grid(row=idx * 2 + 1, column=0, pady=(0, 8), ipadx=60)
        entries.append(entry)

    def enviar_registro():
        nombre = entries[0].get()
        apellido = entries[1].get()
        correo = entries[2].get()
        # entries[3] = edad → se ignora
        salario = entries[4].get()
        # entries[5] = contraseña → se ignora

        ok = registrar_usuario(nombre, apellido, correo, salario)
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


# ------------------ventana reportes son las 4:37 am dios mio-------------------
def ventana_reportes():
    win = tk.Toplevel()
    win.title("Reportes del Sistema")
    win.geometry("750x500")
    win.configure(bg="#020617")

    tk.Label(
        win,
        text="Reportes",
        font=("Segoe UI", 16, "bold"),
        fg="#22c55e",
        bg="#020617"
    ).pack(pady=10)

    tabla_frame = tk.Frame(win, bg="#020617")
    tabla_frame.pack(fill="both", expand=True, padx=10, pady=10)

    columnas = ("col1", "col2")
    tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings")
    tabla.heading("col1", text="Descripción")
    tabla.heading("col2", text="Monto / Valor")

    tabla.column("col1", width=400)
    tabla.column("col2", width=200)

    tabla.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla.yview)
    scrollbar.pack(side="right", fill="y")
    tabla.configure(yscrollcommand=scrollbar.set)

    def limpiar_tabla():
        for fila in tabla.get_children():
            tabla.delete(fila)

    # ==============================
    # REPORTE 1: GASTOS POR CATEGORÍA
    # ==============================
    def reporte_gastos_categoria():
        limpiar_tabla()
        conn = conectar_oracle()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT c.nombre, SUM(t.monto)
            FROM transacciones t
            JOIN subcategorias s ON s.id_subcategoria = t.id_subcategoria
            JOIN categorias c ON c.id_categoria = s.id_categoria
            WHERE t.tipo_transaccion = 'GASTO'
            GROUP BY c.nombre
        """)

        for nombre, total in cursor.fetchall():
            tabla.insert("", "end", values=(nombre, total))

        cursor.close()
        conn.close()

    # ==============================
    # REPORTE 2: RESUMEN PRESUPUESTO
    # ==============================
    def reporte_resumen_presupuesto():
        limpiar_tabla()
        conn = conectar_oracle()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                SUM(CASE WHEN tipo_transaccion = 'INGRESO' THEN monto ELSE 0 END) AS ingresos,
                SUM(CASE WHEN tipo_transaccion = 'GASTO' THEN monto ELSE 0 END) AS gastos,
                SUM(CASE WHEN tipo_transaccion = 'AHORRO' THEN monto ELSE 0 END) AS ahorros
            FROM transacciones
        """)

        ingresos, gastos, ahorros = cursor.fetchone()

        tabla.insert("", "end", values=("Total Ingresos", ingresos or 0))
        tabla.insert("", "end", values=("Total Gastos", gastos or 0))
        tabla.insert("", "end", values=("Total Ahorros", ahorros or 0))

        cursor.close()
        conn.close()

    # ==============================
    # REPORTE 3: METAS DE AHORRO
    # ==============================
    def reporte_metas_ahorro():
        limpiar_tabla()
        conn = conectar_oracle()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT nombre, monto_meta
            FROM metas_ahorros
            WHERE estado = 'ACTIVA'
        """)

        for nombre, monto in cursor.fetchall():
            tabla.insert("", "end", values=(nombre, monto))

        cursor.close()
        conn.close()

    botones = tk.Frame(win, bg="#020617")
    botones.pack(pady=10)

    tk.Button(
        botones,
        text="Gastos por Categoría",
        width=22,
        command=reporte_gastos_categoria
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        botones,
        text="Resumen General",
        width=22,
        command=reporte_resumen_presupuesto
    ).grid(row=0, column=1, padx=5)

    tk.Button(
        botones,
        text="Metas de Ahorro",
        width=22,
        command=reporte_metas_ahorro
    ).grid(row=0, column=2, padx=5)

    tk.Button(
        win,
        text="Cerrar",
        bg="#b91c1c",
        fg="white",
        width=20,
        command=win.destroy
    ).pack(pady=10)


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
    tk.Label(form, text="Contraseña", font=("Segoe UI", 9), fg="#e5e7eb", bg="#020617").grid(row=2, column=0,
                                                                                             sticky="w")
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


# main ejecucion
if __name__ == "__main__":
    ventana_inicio()
