--------------------------------------------------------
--  File created - Monday-December-15-2025   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Procedure SP_CREAR_PRESUPUESTO_COMPLETO
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_CREAR_PRESUPUESTO_COMPLETO" (
    p_id_usuario            IN PRESUPUESTOS.ID_USUARIO%TYPE,
    p_nombre                IN PRESUPUESTOS.NOMBRE_DESCRIPTIVO%TYPE,
    p_fecha_inicio          IN PRESUPUESTOS.FECHA_INICIO%TYPE,
    p_fecha_fin             IN PRESUPUESTOS.FECHA_FIN%TYPE,
    p_ingresos_planificados IN PRESUPUESTOS.INGRESOS_PLANIFICADOS%TYPE,
    p_gastos_planificados   IN PRESUPUESTOS.GASTOS_PLANIFICADOS%TYPE,
    p_ahorros_planificados  IN PRESUPUESTOS.AHORROS_PLANIFICADOS%TYPE,
    p_usuario_creacion      IN VARCHAR2
) IS
BEGIN
    sp_insertar_presupuesto(
        p_id_usuario,
        p_nombre,
        p_fecha_inicio,
        p_fecha_fin,
        p_ingresos_planificados,
        p_gastos_planificados,
        p_ahorros_planificados,
        p_usuario_creacion
    );
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_LISTAR_CATEGORIAS
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_LISTAR_CATEGORIAS" (
    p_tipo_categoria IN CATEGORIAS.TIPO_CATEGORIA%TYPE DEFAULT NULL,
    p_resultado      OUT SYS_REFCURSOR
) IS
BEGIN
    OPEN p_resultado FOR
        SELECT
            ID_CATEGORIA,
            NOMBRE,
            DESCRIPCION,
            TIPO_CATEGORIA,
            ICONO,
            COLOR
        FROM CATEGORIAS
        WHERE p_tipo_categoria IS NULL
           OR TIPO_CATEGORIA = UPPER(p_tipo_categoria)
        ORDER BY NOMBRE;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_ELIMINAR_TRANSACCION
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_ELIMINAR_TRANSACCION" (
    p_id_transaccion IN TRANSACCIONES.ID_TRANSACCION%TYPE
) IS
BEGIN
    DELETE FROM TRANSACCIONES
    WHERE ID_TRANSACCION = p_id_transaccion;

    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(
            -20074,
            'Transacción no encontrada'
        );
    END IF;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_INSERTAR_PRESUPUESTO_DETALLE
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_INSERTAR_PRESUPUESTO_DETALLE" (
    p_id_presupuesto  IN PRESUPUESTO_DETALLES.ID_PRESUPUESTO%TYPE,
    p_id_subcategoria IN PRESUPUESTO_DETALLES.ID_SUBCATEGORIA%TYPE,
    p_monto_mensual   IN PRESUPUESTO_DETALLES.MONTO_MENSUAL%TYPE,
    p_observaciones   IN PRESUPUESTO_DETALLES.OBSERVACIONES%TYPE DEFAULT NULL
) IS
    v_count NUMBER;
BEGIN
    -- Validar presupuesto activo
    SELECT COUNT(*)
    INTO v_count
    FROM PRESUPUESTOS
    WHERE ID_PRESUPUESTO = p_id_presupuesto
      AND ESTADO = 'ACTIVO';

    IF v_count = 0 THEN
        RAISE_APPLICATION_ERROR(
            -20040,
            'El presupuesto no existe o no está activo'
        );
    END IF;

    -- Validar subcategoría activa
    SELECT COUNT(*)
    INTO v_count
    FROM SUBCATEGORIAS
    WHERE ID_SUBCATEGORIA = p_id_subcategoria
      AND ACTIVA = 'Y';

    IF v_count = 0 THEN
        RAISE_APPLICATION_ERROR(
            -20041,
            'La subcategoría no existe o está inactiva'
        );
    END IF;

    -- Evitar duplicados por subcategoría en el mismo presupuesto
    SELECT COUNT(*)
    INTO v_count
    FROM PRESUPUESTO_DETALLES
    WHERE ID_PRESUPUESTO = p_id_presupuesto
      AND ID_SUBCATEGORIA = p_id_subcategoria;

    IF v_count > 0 THEN
        RAISE_APPLICATION_ERROR(
            -20042,
            'Ya existe un detalle para esta subcategoría en el presupuesto'
        );
    END IF;

    INSERT INTO PRESUPUESTO_DETALLES (
        ID_PRESUPUESTO,
        ID_SUBCATEGORIA,
        MONTO_MENSUAL,
        OBSERVACIONES
    ) VALUES (
        p_id_presupuesto,
        p_id_subcategoria,
        p_monto_mensual,
        p_observaciones
    );
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_INSERTAR_OBLIGACION_FIJA
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_INSERTAR_OBLIGACION_FIJA" (
    p_id_usuario        IN OBLIGACIONES_FIJAS.ID_USUARIO%TYPE,
    p_id_subcategoria   IN OBLIGACIONES_FIJAS.ID_SUBCATEGORIA%TYPE,
    p_nombre            IN OBLIGACIONES_FIJAS.NOMBRE%TYPE,
    p_descripcion       IN OBLIGACIONES_FIJAS.DESCRIPCION%TYPE,
    p_monto_mensual     IN OBLIGACIONES_FIJAS.MONTO_MENSUAL%TYPE,
    p_fecha_inicio      IN OBLIGACIONES_FIJAS.FECHA_INICIO%TYPE,
    p_fecha_vencimiento IN OBLIGACIONES_FIJAS.FECHA_VENCIMIENTO%TYPE,
    p_usuario_creacion  IN VARCHAR2
) IS
    v_tipo_categoria CATEGORIAS.TIPO_CATEGORIA%TYPE;
BEGIN
    -- Validar que la subcategoría sea de tipo GASTO
    SELECT c.TIPO_CATEGORIA
    INTO v_tipo_categoria
    FROM SUBCATEGORIAS sc
    JOIN CATEGORIAS c ON c.ID_CATEGORIA = sc.ID_CATEGORIA
    WHERE sc.ID_SUBCATEGORIA = p_id_subcategoria;

    IF v_tipo_categoria <> 'GASTO' THEN
        RAISE_APPLICATION_ERROR(
            -20050,
            'La obligación fija debe pertenecer a una subcategoría de tipo GASTO'
        );
    END IF;

    -- Validar fechas
    IF p_fecha_vencimiento IS NOT NULL
       AND p_fecha_vencimiento < p_fecha_inicio THEN
        RAISE_APPLICATION_ERROR(
            -20051,
            'La fecha de vencimiento no puede ser menor a la fecha de inicio'
        );
    END IF;

    INSERT INTO OBLIGACIONES_FIJAS (
        ID_USUARIO,
        ID_SUBCATEGORIA,
        NOMBRE,
        DESCRIPCION,
        MONTO_MENSUAL,
        FECHA_INICIO,
        FECHA_VENCIMIENTO,
        ACTIVA,
        FECHA_CREACION,
        USUARIO_CREACION
    ) VALUES (
        p_id_usuario,
        p_id_subcategoria,
        p_nombre,
        p_descripcion,
        p_monto_mensual,
        p_fecha_inicio,
        p_fecha_vencimiento,
        'Y',
        CURRENT_TIMESTAMP,
        p_usuario_creacion
    );
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_INSERTAR_USUARIO
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_INSERTAR_USUARIO" (
    p_nombres          IN Usuarios.nombres%TYPE,
    p_apellidos        IN Usuarios.apellidos%TYPE,
    p_correo           IN Usuarios.correo%TYPE,
    p_salario          IN Usuarios.salario%TYPE,
    p_usuario_creacion IN VARCHAR2
) IS
    v_count NUMBER;
BEGIN
    -- validamos que el correo sea unico
    SELECT COUNT(*)
    INTO v_count
    FROM Usuarios
    WHERE LOWER(correo) = LOWER(p_correo);

    IF v_count > 0 THEN
        RAISE_APPLICATION_ERROR(
            -20001,
            'No se pudo, ya existe un usuario registrado con ese correo'
        );
    END IF;

    INSERT INTO Usuarios (
        nombres,
        apellidos,
        correo,
        fecha_registro,
        salario,
        activo,
        fecha_creacion,
        usuario_creacion
    ) VALUES (
        p_nombres,
        p_apellidos,
        p_correo,
        CURRENT_TIMESTAMP,
        p_salario,
        'Y',
        CURRENT_TIMESTAMP,
        p_usuario_creacion
    );
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_CANCELAR_META_AHORRO
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_CANCELAR_META_AHORRO" (
    p_id_meta_ahorro        IN METAS_AHORROS.ID_META_AHORRO%TYPE,
    p_usuario_modificacion  IN VARCHAR2
) IS
BEGIN
    UPDATE METAS_AHORROS
    SET ESTADO = 'CANCELADA',
        FECHA_MODIFICACION = CURRENT_TIMESTAMP,
        USUARIO_MODIFICACION = p_usuario_modificacion
    WHERE ID_META_AHORRO = p_id_meta_ahorro
      AND ESTADO = 'ACTIVA';

    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(
            -20063,
            'Solo se pueden cancelar metas activas'
        );
    END IF;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_INSERTAR_SUBCATEGORIA
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_INSERTAR_SUBCATEGORIA" (
    p_id_categoria            IN SUBCATEGORIAS.ID_CATEGORIA%TYPE,
    p_nombre                  IN SUBCATEGORIAS.NOMBRE%TYPE,
    p_activa                  IN SUBCATEGORIAS.ACTIVA%TYPE DEFAULT 'Y',
    p_subcategoria_defecto    IN SUBCATEGORIAS.SUBCATEGORIA_POR_DEFECTO%TYPE DEFAULT 'N'
) IS
    v_count NUMBER;
BEGIN
    -- Validar categoría existente
    SELECT COUNT(*)
    INTO v_count
    FROM CATEGORIAS
    WHERE ID_CATEGORIA = p_id_categoria;

    IF v_count = 0 THEN
        RAISE_APPLICATION_ERROR(
            -20020,
            'La categoría no existe'
        );
    END IF;

    -- Si se quiere marcar como subcategoría por defecto,
    -- desmarcar cualquier otra existente
    IF p_subcategoria_defecto = 'Y' THEN
        UPDATE SUBCATEGORIAS
        SET SUBCATEGORIA_POR_DEFECTO = 'N'
        WHERE ID_CATEGORIA = p_id_categoria;
    END IF;

    INSERT INTO SUBCATEGORIAS (
        ID_CATEGORIA,
        NOMBRE,
        ACTIVA,
        SUBCATEGORIA_POR_DEFECTO
    ) VALUES (
        p_id_categoria,
        p_nombre,
        NVL(p_activa, 'Y'),
        NVL(p_subcategoria_defecto, 'N')
    );
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_CONSULTAR_PRESUPUESTO_DETALLE
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_CONSULTAR_PRESUPUESTO_DETALLE" (
    p_id_presupuesto_detalle IN PRESUPUESTO_DETALLES.ID_PRESUPUESTO_DETALLE%TYPE,
    p_resultado              OUT SYS_REFCURSOR
) IS
BEGIN
    OPEN p_resultado FOR
        SELECT
            d.ID_PRESUPUESTO_DETALLE,
            d.MONTO_MENSUAL,
            d.OBSERVACIONES,
            sc.ID_SUBCATEGORIA,
            sc.NOMBRE AS SUBCATEGORIA,
            c.ID_CATEGORIA,
            c.NOMBRE AS CATEGORIA,
            c.TIPO_CATEGORIA
        FROM PRESUPUESTO_DETALLES d
        JOIN SUBCATEGORIAS sc ON sc.ID_SUBCATEGORIA = d.ID_SUBCATEGORIA
        JOIN CATEGORIAS c ON c.ID_CATEGORIA = sc.ID_CATEGORIA
        WHERE d.ID_PRESUPUESTO_DETALLE = p_id_presupuesto_detalle;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_INSERTAR_META_AHORRO
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_INSERTAR_META_AHORRO" (
    p_id_usuario        IN METAS_AHORROS.ID_USUARIO%TYPE,
    p_id_subcategoria   IN METAS_AHORROS.ID_SUBCATEGORIA%TYPE,
    p_nombre            IN METAS_AHORROS.NOMBRE%TYPE,
    p_descripcion       IN METAS_AHORROS.DESCRIPCION%TYPE,
    p_monto_meta        IN METAS_AHORROS.MONTO_META%TYPE,
    p_fecha_inicio      IN METAS_AHORROS.FECHA_INICIO%TYPE,
    p_fecha_objetivo    IN METAS_AHORROS.FECHA_OBJETIVO%TYPE,
    p_prioridad         IN METAS_AHORROS.PRIORIDAD%TYPE,
    p_usuario_creacion  IN VARCHAR2
) IS
    v_tipo_categoria CATEGORIAS.TIPO_CATEGORIA%TYPE;
BEGIN
    -- Validar subcategoría de tipo AHORRO
    SELECT c.TIPO_CATEGORIA
    INTO v_tipo_categoria
    FROM SUBCATEGORIAS sc
    JOIN CATEGORIAS c ON c.ID_CATEGORIA = sc.ID_CATEGORIA
    WHERE sc.ID_SUBCATEGORIA = p_id_subcategoria;

    IF v_tipo_categoria <> 'AHORRO' THEN
        RAISE_APPLICATION_ERROR(
            -20060,
            'La meta debe pertenecer a una subcategoría de tipo AHORRO'
        );
    END IF;

    -- Validar fechas
    IF p_fecha_objetivo < p_fecha_inicio THEN
        RAISE_APPLICATION_ERROR(
            -20061,
            'La fecha objetivo no puede ser menor a la fecha de inicio'
        );
    END IF;

    INSERT INTO METAS_AHORROS (
        ID_USUARIO,
        ID_SUBCATEGORIA,
        NOMBRE,
        DESCRIPCION,
        MONTO_META,
        MONTO_AHORRADO,
        FECHA_INICIO,
        FECHA_OBJETIVO,
        PRIORIDAD,
        ESTADO,
        FECHA_CREACION,
        USUARIO_CREACION
    ) VALUES (
        p_id_usuario,
        p_id_subcategoria,
        p_nombre,
        p_descripcion,
        p_monto_meta,
        0,
        p_fecha_inicio,
        p_fecha_objetivo,
        UPPER(p_prioridad),
        'ACTIVA',
        CURRENT_TIMESTAMP,
        p_usuario_creacion
    );
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_CONSULTAR_PRESUPUESTO
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_CONSULTAR_PRESUPUESTO" (
    p_id_presupuesto IN PRESUPUESTOS.ID_PRESUPUESTO%TYPE,
    p_resultado      OUT SYS_REFCURSOR
) IS
BEGIN
    OPEN p_resultado FOR
        SELECT
            p.ID_PRESUPUESTO,
            p.NOMBRE_DESCRIPTIVO,
            p.FECHA_INICIO,
            p.FECHA_FIN,
            p.INGRESOS_PLANIFICADOS,
            p.GASTOS_PLANIFICADOS,
            p.AHORROS_PLANIFICADOS,
            p.ESTADO,
            p.FECHA_CREACION,
            p.USUARIO_CREACION,
            p.FECHA_MODIFICACION,
            p.USUARIO_MODIFICACION,
            u.NOMBRES || ' ' || u.APELLIDOS AS USUARIO
        FROM PRESUPUESTOS p
        JOIN USUARIOS u ON u.ID_USUARIO = p.ID_USUARIO
        WHERE p.ID_PRESUPUESTO = p_id_presupuesto;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_ACTUALIZAR_PRESUPUESTO_DETALLE
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_ACTUALIZAR_PRESUPUESTO_DETALLE" (
    p_id_presupuesto_detalle IN PRESUPUESTO_DETALLES.ID_PRESUPUESTO_DETALLE%TYPE,
    p_monto_mensual          IN PRESUPUESTO_DETALLES.MONTO_MENSUAL%TYPE,
    p_observaciones          IN PRESUPUESTO_DETALLES.OBSERVACIONES%TYPE DEFAULT NULL
) IS
    v_estado PRESUPUESTOS.ESTADO%TYPE;
BEGIN
    -- Obtener estado del presupuesto
    SELECT p.ESTADO
    INTO v_estado
    FROM PRESUPUESTO_DETALLES d
    JOIN PRESUPUESTOS p
      ON p.ID_PRESUPUESTO = d.ID_PRESUPUESTO
    WHERE d.ID_PRESUPUESTO_DETALLE = p_id_presupuesto_detalle;

    IF v_estado <> 'ACTIVO' THEN
        RAISE_APPLICATION_ERROR(
            -20043,
            'No se pueden modificar detalles de un presupuesto cerrado'
        );
    END IF;

    UPDATE PRESUPUESTO_DETALLES
    SET MONTO_MENSUAL = p_monto_mensual,
        OBSERVACIONES = p_observaciones
    WHERE ID_PRESUPUESTO_DETALLE = p_id_presupuesto_detalle;

    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(
            -20044,
            'Detalle de presupuesto no encontrado'
        );
    END IF;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_ACTUALIZAR_USUARIO
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_ACTUALIZAR_USUARIO" (
    p_id_usuario           IN Usuarios.id_usuario%TYPE,
    p_nombres              IN Usuarios.nombres%TYPE,
    p_apellidos            IN Usuarios.apellidos%TYPE,
    p_salario              IN Usuarios.salario%TYPE,
    p_usuario_modificacion IN VARCHAR2
) IS
BEGIN
    UPDATE Usuarios
    SET nombres = p_nombres,
        apellidos = p_apellidos,
        salario = p_salario,
        fecha_modificacion = CURRENT_TIMESTAMP,
        usuario_modificacion = p_usuario_modificacion
    WHERE id_usuario = p_id_usuario;

    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(
            -20002,
            'Usuario no encontrado'
        );
    END IF;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_ACTUALIZAR_CATEGORIA
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_ACTUALIZAR_CATEGORIA" (
    p_id_categoria          IN CATEGORIAS.ID_CATEGORIA%TYPE,
    p_nombre                IN CATEGORIAS.NOMBRE%TYPE,
    p_descripcion           IN CATEGORIAS.DESCRIPCION%TYPE,
    p_icono                 IN CATEGORIAS.ICONO%TYPE,
    p_color                 IN CATEGORIAS.COLOR%TYPE,
    p_usuario_modificacion  IN VARCHAR2
) IS
BEGIN
    UPDATE CATEGORIAS
    SET NOMBRE = p_nombre,
        DESCRIPCION = p_descripcion,
        ICONO = p_icono,
        COLOR = p_color,
        FECHA_MODIFICACION = CURRENT_TIMESTAMP,
        USUARIO_MODIFICACION = p_usuario_modificacion
    WHERE ID_CATEGORIA = p_id_categoria;

    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(
            -20011,
            'Categoría no encontrada'
        );
    END IF;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_ELIMINAR_SUBCATEGORIA
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_ELIMINAR_SUBCATEGORIA" (
    ---NO ELIIMINADO FISICO, SOLO DESACTIVACION
    p_id_subcategoria IN SUBCATEGORIAS.ID_SUBCATEGORIA%TYPE
) IS
    v_defecto SUBCATEGORIAS.SUBCATEGORIA_POR_DEFECTO%TYPE;
BEGIN
    SELECT SUBCATEGORIA_POR_DEFECTO
    INTO v_defecto
    FROM SUBCATEGORIAS
    WHERE ID_SUBCATEGORIA = p_id_subcategoria;

    IF v_defecto = 'Y' THEN
        RAISE_APPLICATION_ERROR(
            -20022,
            'No se puede eliminar la subcategoría por defecto'
        );
    END IF;

    UPDATE SUBCATEGORIAS
    SET ACTIVA = 'N'
    WHERE ID_SUBCATEGORIA = p_id_subcategoria;

    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(
            -20023,
            'Subcategoría no encontrada'
        );
    END IF;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_INSERTAR_PRESUPUESTO
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_INSERTAR_PRESUPUESTO" (
    p_id_usuario            IN PRESUPUESTOS.ID_USUARIO%TYPE,
    p_nombre                IN PRESUPUESTOS.NOMBRE_DESCRIPTIVO%TYPE,
    p_fecha_inicio          IN PRESUPUESTOS.FECHA_INICIO%TYPE,
    p_fecha_fin             IN PRESUPUESTOS.FECHA_FIN%TYPE,
    p_ingresos_planificados IN PRESUPUESTOS.INGRESOS_PLANIFICADOS%TYPE,
    p_gastos_planificados   IN PRESUPUESTOS.GASTOS_PLANIFICADOS%TYPE,
    p_ahorros_planificados  IN PRESUPUESTOS.AHORROS_PLANIFICADOS%TYPE,
    p_usuario_creacion      IN VARCHAR2
) IS
    v_count NUMBER;
BEGIN
    -- Validación de fechas
    IF p_fecha_fin < p_fecha_inicio THEN
        RAISE_APPLICATION_ERROR(
            -20030,
            'La fecha de fin no puede ser menor a la fecha de inicio'
        );
    END IF;

    -- Validar presupuesto activo único por usuario
    SELECT COUNT(*)
    INTO v_count
    FROM PRESUPUESTOS
    WHERE ID_USUARIO = p_id_usuario
      AND ESTADO = 'ACTIVO';

    IF v_count > 0 THEN
        RAISE_APPLICATION_ERROR(
            -20031,
            'El usuario ya tiene un presupuesto activo'
        );
    END IF;

    INSERT INTO PRESUPUESTOS (
        ID_USUARIO,
        NOMBRE_DESCRIPTIVO,
        FECHA_INICIO,
        FECHA_FIN,
        INGRESOS_PLANIFICADOS,
        GASTOS_PLANIFICADOS,
        AHORROS_PLANIFICADOS,
        ESTADO,
        FECHA_CREACION,
        USUARIO_CREACION
    ) VALUES (
        p_id_usuario,
        p_nombre,
        p_fecha_inicio,
        p_fecha_fin,
        p_ingresos_planificados,
        p_gastos_planificados,
        p_ahorros_planificados,
        'ACTIVO',
        CURRENT_TIMESTAMP,
        p_usuario_creacion
    );
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_LISTAR_DETALLES_PRESUPUESTO
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_LISTAR_DETALLES_PRESUPUESTO" (
    p_id_presupuesto IN PRESUPUESTO_DETALLES.ID_PRESUPUESTO%TYPE,
    p_resultado      OUT SYS_REFCURSOR
) IS
BEGIN
    OPEN p_resultado FOR
        SELECT
            d.ID_PRESUPUESTO_DETALLE,
            sc.NOMBRE AS SUBCATEGORIA,
            c.NOMBRE AS CATEGORIA,
            c.TIPO_CATEGORIA,
            d.MONTO_MENSUAL,
            d.OBSERVACIONES
        FROM PRESUPUESTO_DETALLES d
        JOIN SUBCATEGORIAS sc ON sc.ID_SUBCATEGORIA = d.ID_SUBCATEGORIA
        JOIN CATEGORIAS c ON c.ID_CATEGORIA = sc.ID_CATEGORIA
        WHERE d.ID_PRESUPUESTO = p_id_presupuesto
        ORDER BY c.NOMBRE, sc.NOMBRE;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_CONSULTAR_TRANSACCION
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_CONSULTAR_TRANSACCION" (
    p_id_transaccion IN TRANSACCIONES.ID_TRANSACCION%TYPE,
    p_resultado      OUT SYS_REFCURSOR
) IS
BEGIN
    OPEN p_resultado FOR
        SELECT
            t.ID_TRANSACCION,
            t.FECHA,
            t.TIPO_TRANSACCION,
            t.DESCRIPCION,
            t.MONTO,
            t.METODO_PAGO,
            sc.NOMBRE AS SUBCATEGORIA,
            c.NOMBRE AS CATEGORIA,
            t.FECHA_REGISTRO,
            t.USUARIO_CREACION,
            t.FECHA_MODIFICACION,
            t.USUARIO_MODIFICACION
        FROM TRANSACCIONES t
        JOIN SUBCATEGORIAS sc ON sc.ID_SUBCATEGORIA = t.ID_SUBCATEGORIA
        JOIN CATEGORIAS c ON c.ID_CATEGORIA = sc.ID_CATEGORIA
        WHERE t.ID_TRANSACCION = p_id_transaccion;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_DESACTIVAR_OBLIGACION_FIJA
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_DESACTIVAR_OBLIGACION_FIJA" (
    p_id_obligacion_fija IN OBLIGACIONES_FIJAS.ID_OBLIGACION_FIJA%TYPE,
    p_usuario_modificacion IN VARCHAR2
) IS
BEGIN
    UPDATE OBLIGACIONES_FIJAS
    SET ACTIVA = 'N',
        FECHA_MODIFICACION = CURRENT_TIMESTAMP,
        USUARIO_MODIFICACION = p_usuario_modificacion
    WHERE ID_OBLIGACION_FIJA = p_id_obligacion_fija;

    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(
            -20053,
            'Obligación fija no encontrada'
        );
    END IF;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_CONSULTAR_OBLIGACION_FIJA
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_CONSULTAR_OBLIGACION_FIJA" (
    p_id_obligacion_fija IN OBLIGACIONES_FIJAS.ID_OBLIGACION_FIJA%TYPE,
    p_resultado          OUT SYS_REFCURSOR
) IS
BEGIN
    OPEN p_resultado FOR
        SELECT
            o.ID_OBLIGACION_FIJA,
            o.NOMBRE,
            o.DESCRIPCION,
            o.MONTO_MENSUAL,
            o.FECHA_INICIO,
            o.FECHA_VENCIMIENTO,
            o.ACTIVA,
            sc.NOMBRE AS SUBCATEGORIA,
            c.NOMBRE AS CATEGORIA,
            o.FECHA_CREACION,
            o.USUARIO_CREACION,
            o.FECHA_MODIFICACION,
            o.USUARIO_MODIFICACION
        FROM OBLIGACIONES_FIJAS o
        JOIN SUBCATEGORIAS sc ON sc.ID_SUBCATEGORIA = o.ID_SUBCATEGORIA
        JOIN CATEGORIAS c ON c.ID_CATEGORIA = sc.ID_CATEGORIA
        WHERE o.ID_OBLIGACION_FIJA = p_id_obligacion_fija;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_ELIMINAR_CATEGORIA
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_ELIMINAR_CATEGORIA" (
    ---NO ELIMINA LA CATEGORIA, SOLAMENTE DESACTIVA
    p_id_categoria          IN CATEGORIAS.ID_CATEGORIA%TYPE,
    p_usuario_modificacion  IN VARCHAR2
) IS
BEGIN
    UPDATE CATEGORIAS
    SET FECHA_MODIFICACION = CURRENT_TIMESTAMP,
        USUARIO_MODIFICACION = p_usuario_modificacion
    WHERE ID_CATEGORIA = p_id_categoria;

    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(
            -20012,
            'Categoría no encontrada'
        );
    END IF;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_INSERTAR_TRANSACCION
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_INSERTAR_TRANSACCION" (
    p_id_usuario       IN NUMBER,
    p_id_presupuesto   IN NUMBER,
    p_fecha            IN DATE,
    p_id_subcategoria  IN NUMBER,
    p_tipo             IN VARCHAR2,
    p_descripcion      IN VARCHAR2,
    p_monto            IN NUMBER,
    p_metodo_pago      IN VARCHAR2,
    p_usuario_creacion IN VARCHAR2
) AS
BEGIN
    INSERT INTO transacciones (
        id_usuario,
        id_presupuesto,
        fecha,
        id_subcategoria,
        tipo_transaccion,
        descripcion,
        monto,
        metodo_pago,
        fecha_registro,
        usuario_creacion
    ) VALUES (
        p_id_usuario,
        p_id_presupuesto,
        p_fecha,
        p_id_subcategoria,
        p_tipo,
        p_descripcion,
        p_monto,
        p_metodo_pago,
        SYSDATE,
        p_usuario_creacion
    );
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_INSERTAR_CATEGORIA
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_INSERTAR_CATEGORIA" (
    p_nombre             IN CATEGORIAS.NOMBRE%TYPE,
    p_descripcion        IN CATEGORIAS.DESCRIPCION%TYPE,
    p_tipo_categoria     IN CATEGORIAS.TIPO_CATEGORIA%TYPE,
    p_icono              IN CATEGORIAS.ICONO%TYPE,
    p_color              IN CATEGORIAS.COLOR%TYPE,
    p_usuario_creacion   IN VARCHAR2
) IS
BEGIN
    -- Validar tipo de categoría
    IF UPPER(p_tipo_categoria) NOT IN ('INGRESO', 'GASTO', 'AHORRO') THEN
        RAISE_APPLICATION_ERROR(
            -20010,
            'Tipo de categoría inválido. Use INGRESO, GASTO o AHORRO'
        );
    END IF;

    INSERT INTO CATEGORIAS (
        NOMBRE,
        DESCRIPCION,
        TIPO_CATEGORIA,
        ICONO,
        COLOR,
        FECHA_CREACION,
        USUARIO_CREACION
    ) VALUES (
        p_nombre,
        p_descripcion,
        UPPER(p_tipo_categoria),
        p_icono,
        p_color,
        CURRENT_TIMESTAMP,
        p_usuario_creacion
    );
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_CERRAR_PRESUPUESTO
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_CERRAR_PRESUPUESTO" (
    p_id_presupuesto       IN PRESUPUESTOS.ID_PRESUPUESTO%TYPE,
    p_usuario_modificacion IN VARCHAR2
) IS
BEGIN
    UPDATE PRESUPUESTOS
    SET ESTADO = 'CERRADO',
        FECHA_MODIFICACION = CURRENT_TIMESTAMP,
        USUARIO_MODIFICACION = p_usuario_modificacion
    WHERE ID_PRESUPUESTO = p_id_presupuesto
      AND ESTADO = 'ACTIVO';

    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(
            -20034,
            'Solo se pueden cerrar presupuestos activos'
        );
    END IF;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_LISTAR_OBLIGACIONES_USUARIO
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_LISTAR_OBLIGACIONES_USUARIO" (
    p_id_usuario IN OBLIGACIONES_FIJAS.ID_USUARIO%TYPE,
    p_activa     IN OBLIGACIONES_FIJAS.ACTIVA%TYPE DEFAULT NULL,
    p_resultado  OUT SYS_REFCURSOR
) IS
BEGIN
    OPEN p_resultado FOR
        SELECT
            ID_OBLIGACION_FIJA,
            NOMBRE,
            MONTO_MENSUAL,
            FECHA_INICIO,
            FECHA_VENCIMIENTO,
            ACTIVA
        FROM OBLIGACIONES_FIJAS
        WHERE ID_USUARIO = p_id_usuario
          AND (p_activa IS NULL OR ACTIVA = p_activa)
        ORDER BY FECHA_INICIO;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_CONSULTAR_SUBCATEGORIA
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_CONSULTAR_SUBCATEGORIA" (
    p_id_subcategoria IN SUBCATEGORIAS.ID_SUBCATEGORIA%TYPE,
    p_resultado       OUT SYS_REFCURSOR
) IS
BEGIN
    OPEN p_resultado FOR
        SELECT
            sc.ID_SUBCATEGORIA,
            sc.NOMBRE,
            sc.ACTIVA,
            sc.SUBCATEGORIA_POR_DEFECTO,
            c.ID_CATEGORIA,
            c.NOMBRE AS NOMBRE_CATEGORIA,
            c.TIPO_CATEGORIA
        FROM SUBCATEGORIAS sc
        JOIN CATEGORIAS c ON c.ID_CATEGORIA = sc.ID_CATEGORIA
        WHERE sc.ID_SUBCATEGORIA = p_id_subcategoria;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_ACTUALIZAR_OBLIGACION_FIJA
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_ACTUALIZAR_OBLIGACION_FIJA" (
    p_id_obligacion_fija IN OBLIGACIONES_FIJAS.ID_OBLIGACION_FIJA%TYPE,
    p_nombre             IN OBLIGACIONES_FIJAS.NOMBRE%TYPE,
    p_descripcion        IN OBLIGACIONES_FIJAS.DESCRIPCION%TYPE,
    p_monto_mensual      IN OBLIGACIONES_FIJAS.MONTO_MENSUAL%TYPE,
    p_fecha_vencimiento  IN OBLIGACIONES_FIJAS.FECHA_VENCIMIENTO%TYPE,
    p_activa             IN OBLIGACIONES_FIJAS.ACTIVA%TYPE,
    p_usuario_modificacion IN VARCHAR2
) IS
BEGIN
    UPDATE OBLIGACIONES_FIJAS
    SET NOMBRE = p_nombre,
        DESCRIPCION = p_descripcion,
        MONTO_MENSUAL = p_monto_mensual,
        FECHA_VENCIMIENTO = p_fecha_vencimiento,
        ACTIVA = p_activa,
        FECHA_MODIFICACION = CURRENT_TIMESTAMP,
        USUARIO_MODIFICACION = p_usuario_modificacion
    WHERE ID_OBLIGACION_FIJA = p_id_obligacion_fija;

    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(
            -20052,
            'Obligación fija no encontrada'
        );
    END IF;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_ELIMINAR_PRESUPUESTO_DETALLE
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_ELIMINAR_PRESUPUESTO_DETALLE" (
    p_id_presupuesto_detalle IN PRESUPUESTO_DETALLES.ID_PRESUPUESTO_DETALLE%TYPE
) IS
BEGIN
    DELETE FROM PRESUPUESTO_DETALLES
    WHERE ID_PRESUPUESTO_DETALLE = p_id_presupuesto_detalle;

    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(
            -20045,
            'Detalle de presupuesto no encontrado'
        );
    END IF;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_ACTUALIZAR_METAS_POR_AHORRO
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_ACTUALIZAR_METAS_POR_AHORRO" (
    p_id_usuario      IN METAS_AHORROS.ID_USUARIO%TYPE,
    p_id_subcategoria IN METAS_AHORROS.ID_SUBCATEGORIA%TYPE,
    p_monto           IN NUMBER
) IS
BEGIN
    UPDATE METAS_AHORROS
    SET MONTO_AHORRADO = MONTO_AHORRADO + p_monto,
        FECHA_MODIFICACION = CURRENT_TIMESTAMP
    WHERE ID_USUARIO = p_id_usuario
      AND ID_SUBCATEGORIA = p_id_subcategoria
      AND ESTADO = 'ACTIVA';

    -- Marcar como completada si alcanza la meta
    UPDATE METAS_AHORROS
    SET ESTADO = 'COMPLETADA',
        FECHA_MODIFICACION = CURRENT_TIMESTAMP
    WHERE ID_USUARIO = p_id_usuario
      AND ID_SUBCATEGORIA = p_id_subcategoria
      AND MONTO_AHORRADO >= MONTO_META
      AND ESTADO = 'ACTIVA';
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_CONSULTAR_CATEGORIA
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_CONSULTAR_CATEGORIA" (
    p_id_categoria IN CATEGORIAS.ID_CATEGORIA%TYPE,
    p_resultado    OUT SYS_REFCURSOR
) IS
BEGIN
    OPEN p_resultado FOR
        SELECT
            ID_CATEGORIA,
            NOMBRE,
            DESCRIPCION,
            TIPO_CATEGORIA,
            ICONO,
            COLOR,
            FECHA_CREACION,
            USUARIO_CREACION,
            FECHA_MODIFICACION,
            USUARIO_MODIFICACION
        FROM CATEGORIAS
        WHERE ID_CATEGORIA = p_id_categoria;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_LISTAR_PRESUPUESTOS_USUARIO
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_LISTAR_PRESUPUESTOS_USUARIO" (
    p_id_usuario IN PRESUPUESTOS.ID_USUARIO%TYPE,
    p_estado     IN PRESUPUESTOS.ESTADO%TYPE DEFAULT NULL,
    p_resultado  OUT SYS_REFCURSOR
) IS
BEGIN
    OPEN p_resultado FOR
        SELECT
            ID_PRESUPUESTO,
            NOMBRE_DESCRIPTIVO,
            FECHA_INICIO,
            FECHA_FIN,
            INGRESOS_PLANIFICADOS,
            GASTOS_PLANIFICADOS,
            AHORROS_PLANIFICADOS,
            ESTADO,
            FECHA_CREACION
        FROM PRESUPUESTOS
        WHERE ID_USUARIO = p_id_usuario
          AND (p_estado IS NULL OR ESTADO = p_estado)
        ORDER BY FECHA_INICIO DESC;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_CONSULTAR_USUARIO
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_CONSULTAR_USUARIO" (
    p_id_usuario IN Usuarios.id_usuario%TYPE,
    p_resultado  OUT SYS_REFCURSOR
) IS
BEGIN
    OPEN p_resultado FOR
        SELECT
            id_usuario,
            nombres,
            apellidos,
            correo,
            fecha_registro,
            salario,
            activo,
            fecha_creacion,
            usuario_creacion,
            fecha_modificacion,
            usuario_modificacion
        FROM Usuarios
        WHERE id_usuario = p_id_usuario;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_ACTUALIZAR_META_AHORRO
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_ACTUALIZAR_META_AHORRO" (
    p_id_meta_ahorro        IN METAS_AHORROS.ID_META_AHORRO%TYPE,
    p_nombre                IN METAS_AHORROS.NOMBRE%TYPE,
    p_descripcion           IN METAS_AHORROS.DESCRIPCION%TYPE,
    p_monto_meta            IN METAS_AHORROS.MONTO_META%TYPE,
    p_fecha_objetivo        IN METAS_AHORROS.FECHA_OBJETIVO%TYPE,
    p_prioridad             IN METAS_AHORROS.PRIORIDAD%TYPE,
    p_usuario_modificacion  IN VARCHAR2
) IS
BEGIN
    UPDATE METAS_AHORROS
    SET NOMBRE = p_nombre,
        DESCRIPCION = p_descripcion,
        MONTO_META = p_monto_meta,
        FECHA_OBJETIVO = p_fecha_objetivo,
        PRIORIDAD = UPPER(p_prioridad),
        FECHA_MODIFICACION = CURRENT_TIMESTAMP,
        USUARIO_MODIFICACION = p_usuario_modificacion
    WHERE ID_META_AHORRO = p_id_meta_ahorro
      AND ESTADO = 'ACTIVA';

    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(
            -20062,
            'La meta no existe o no está activa'
        );
    END IF;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_ACTUALIZAR_PRESUPUESTO
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_ACTUALIZAR_PRESUPUESTO" (
    p_id_presupuesto        IN PRESUPUESTOS.ID_PRESUPUESTO%TYPE,
    p_nombre                IN PRESUPUESTOS.NOMBRE_DESCRIPTIVO%TYPE,
    p_fecha_inicio          IN PRESUPUESTOS.FECHA_INICIO%TYPE,
    p_fecha_fin             IN PRESUPUESTOS.FECHA_FIN%TYPE,
    p_ingresos_planificados IN PRESUPUESTOS.INGRESOS_PLANIFICADOS%TYPE,
    p_gastos_planificados   IN PRESUPUESTOS.GASTOS_PLANIFICADOS%TYPE,
    p_ahorros_planificados  IN PRESUPUESTOS.AHORROS_PLANIFICADOS%TYPE,
    p_usuario_modificacion  IN VARCHAR2
) IS
BEGIN
    IF p_fecha_fin < p_fecha_inicio THEN
        RAISE_APPLICATION_ERROR(
            -20032,
            'Fechas inválidas para el presupuesto'
        );
    END IF;

    UPDATE PRESUPUESTOS
    SET NOMBRE_DESCRIPTIVO = p_nombre,
        FECHA_INICIO = p_fecha_inicio,
        FECHA_FIN = p_fecha_fin,
        INGRESOS_PLANIFICADOS = p_ingresos_planificados,
        GASTOS_PLANIFICADOS = p_gastos_planificados,
        AHORROS_PLANIFICADOS = p_ahorros_planificados,
        FECHA_MODIFICACION = CURRENT_TIMESTAMP,
        USUARIO_MODIFICACION = p_usuario_modificacion
    WHERE ID_PRESUPUESTO = p_id_presupuesto
      AND ESTADO <> 'CERRADO';

    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(
            -20033,
            'Presupuesto no encontrado o ya cerrado'
        );
    END IF;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_ACTUALIZAR_TRANSACCION
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_ACTUALIZAR_TRANSACCION" (
    p_id_transaccion       IN TRANSACCIONES.ID_TRANSACCION%TYPE,
    p_fecha                IN TRANSACCIONES.FECHA%TYPE,
    p_descripcion          IN TRANSACCIONES.DESCRIPCION%TYPE,
    p_monto                IN TRANSACCIONES.MONTO%TYPE,
    p_metodo_pago          IN TRANSACCIONES.METODO_PAGO%TYPE,
    p_usuario_modificacion IN VARCHAR2
) IS
BEGIN
    UPDATE TRANSACCIONES
    SET FECHA = p_fecha,
        DESCRIPCION = p_descripcion,
        MONTO = p_monto,
        METODO_PAGO = p_metodo_pago,
        FECHA_MODIFICACION = CURRENT_TIMESTAMP,
        USUARIO_MODIFICACION = p_usuario_modificacion
    WHERE ID_TRANSACCION = p_id_transaccion;

    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(
            -20073,
            'Transacción no encontrada'
        );
    END IF;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_LISTAR_METAS_USUARIO
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_LISTAR_METAS_USUARIO" (
    p_id_usuario IN METAS_AHORROS.ID_USUARIO%TYPE,
    p_estado     IN METAS_AHORROS.ESTADO%TYPE DEFAULT NULL,
    p_resultado  OUT SYS_REFCURSOR
) IS
BEGIN
    OPEN p_resultado FOR
        SELECT
            ID_META_AHORRO,
            NOMBRE,
            MONTO_META,
            MONTO_AHORRADO,
            FECHA_OBJETIVO,
            PRIORIDAD,
            ESTADO
        FROM METAS_AHORROS
        WHERE ID_USUARIO = p_id_usuario
          AND (p_estado IS NULL OR ESTADO = p_estado)
        ORDER BY PRIORIDAD, FECHA_OBJETIVO;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_ACTUALIZAR_SUBCATEGORIA
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_ACTUALIZAR_SUBCATEGORIA" (
    p_id_subcategoria         IN SUBCATEGORIAS.ID_SUBCATEGORIA%TYPE,
    p_nombre                  IN SUBCATEGORIAS.NOMBRE%TYPE,
    p_activa                  IN SUBCATEGORIAS.ACTIVA%TYPE,
    p_subcategoria_defecto    IN SUBCATEGORIAS.SUBCATEGORIA_POR_DEFECTO%TYPE
) IS
    v_id_categoria SUBCATEGORIAS.ID_CATEGORIA%TYPE;
BEGIN
    -- Obtener categoría padre
    SELECT ID_CATEGORIA
    INTO v_id_categoria
    FROM SUBCATEGORIAS
    WHERE ID_SUBCATEGORIA = p_id_subcategoria;

    -- Si se marca como por defecto, desmarcar las demás
    IF p_subcategoria_defecto = 'Y' THEN
        UPDATE SUBCATEGORIAS
        SET SUBCATEGORIA_POR_DEFECTO = 'N'
        WHERE ID_CATEGORIA = v_id_categoria;
    END IF;

    UPDATE SUBCATEGORIAS
    SET NOMBRE = p_nombre,
        ACTIVA = p_activa,
        SUBCATEGORIA_POR_DEFECTO = p_subcategoria_defecto
    WHERE ID_SUBCATEGORIA = p_id_subcategoria;

    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(
            -20021,
            'Subcategoría no encontrada'
        );
    END IF;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_DESACTIVAR_USUARIO
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_DESACTIVAR_USUARIO" (
    --AQUI SOLAMENTE DESACTIVAMOS PORQUE NO SE PUEDE ELIMINAR COMO TAL EL USUARIO SEGUN LA LOGICA DE NEGOCIO
    --
    p_id_usuario           IN Usuarios.id_usuario%TYPE,
    p_usuario_modificacion IN VARCHAR2
) IS
BEGIN
    UPDATE Usuarios
    SET activo = 'N',
        fecha_modificacion = CURRENT_TIMESTAMP,
        usuario_modificacion = p_usuario_modificacion
    WHERE id_usuario = p_id_usuario;

    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(
            -20003,
            'Usuario no encontrado'
        );
    END IF;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_CONSULTAR_META_AHORRO
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_CONSULTAR_META_AHORRO" (
    p_id_meta_ahorro IN METAS_AHORROS.ID_META_AHORRO%TYPE,
    p_resultado      OUT SYS_REFCURSOR
) IS
BEGIN
    OPEN p_resultado FOR
        SELECT
            m.ID_META_AHORRO,
            m.NOMBRE,
            m.DESCRIPCION,
            m.MONTO_META,
            m.MONTO_AHORRADO,
            m.FECHA_INICIO,
            m.FECHA_OBJETIVO,
            m.PRIORIDAD,
            m.ESTADO,
            sc.NOMBRE AS SUBCATEGORIA,
            c.NOMBRE AS CATEGORIA,
            m.FECHA_CREACION,
            m.USUARIO_CREACION,
            m.FECHA_MODIFICACION,
            m.USUARIO_MODIFICACION
        FROM METAS_AHORROS m
        JOIN SUBCATEGORIAS sc ON sc.ID_SUBCATEGORIA = m.ID_SUBCATEGORIA
        JOIN CATEGORIAS c ON c.ID_CATEGORIA = sc.ID_CATEGORIA
        WHERE m.ID_META_AHORRO = p_id_meta_ahorro;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_LISTAR_TRANSACCIONES_PRESUPUESTO
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_LISTAR_TRANSACCIONES_PRESUPUESTO" (
    p_id_presupuesto IN TRANSACCIONES.ID_PRESUPUESTO%TYPE,
    p_resultado      OUT SYS_REFCURSOR
) IS
BEGIN
    OPEN p_resultado FOR
        SELECT
            ID_TRANSACCION,
            FECHA,
            TIPO_TRANSACCION,
            DESCRIPCION,
            MONTO,
            METODO_PAGO
        FROM TRANSACCIONES
        WHERE ID_PRESUPUESTO = p_id_presupuesto
        ORDER BY FECHA DESC;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_LISTAR_USUARIOS
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_LISTAR_USUARIOS" (
    p_resultado OUT SYS_REFCURSOR
) IS
BEGIN
    OPEN p_resultado FOR
        SELECT
            id_usuario,
            nombres,
            apellidos,
            correo,
            salario,
            activo
        FROM Usuarios
        ORDER BY id_usuario;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_LISTAR_SUBCATEGORIAS_POR_CATEGORIA
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_LISTAR_SUBCATEGORIAS_POR_CATEGORIA" (
    p_id_categoria IN SUBCATEGORIAS.ID_CATEGORIA%TYPE,
    p_resultado    OUT SYS_REFCURSOR
) IS
BEGIN
    OPEN p_resultado FOR
        SELECT
            ID_SUBCATEGORIA,
            NOMBRE,
            ACTIVA,
            SUBCATEGORIA_POR_DEFECTO
        FROM SUBCATEGORIAS
        WHERE ID_CATEGORIA = p_id_categoria
        ORDER BY SUBCATEGORIA_POR_DEFECTO DESC, NOMBRE;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_RESUMEN_CATEGORIA_PRESUPUESTO
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_RESUMEN_CATEGORIA_PRESUPUESTO" (
    p_id_presupuesto IN PRESUPUESTOS.ID_PRESUPUESTO%TYPE,
    p_resultado      OUT SYS_REFCURSOR
) IS
BEGIN
    OPEN p_resultado FOR
        SELECT
            c.NOMBRE AS CATEGORIA,
            c.TIPO_CATEGORIA,
            fn_total_ejecutado_categoria(p_id_presupuesto, c.ID_CATEGORIA)
                AS TOTAL_EJECUTADO
        FROM CATEGORIAS c;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_RESUMEN_PRESUPUESTO
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_RESUMEN_PRESUPUESTO" (
    p_id_presupuesto IN PRESUPUESTOS.ID_PRESUPUESTO%TYPE,
    p_resultado      OUT SYS_REFCURSOR
) IS
BEGIN
    OPEN p_resultado FOR
        SELECT
            fn_total_ingresos_presupuesto(p_id_presupuesto) AS INGRESOS,
            fn_total_gastos_presupuesto(p_id_presupuesto)   AS GASTOS,
            fn_total_ahorros_presupuesto(p_id_presupuesto)  AS AHORROS,
            fn_balance_presupuesto(p_id_presupuesto)        AS BALANCE
        FROM DUAL;
END;

/
--------------------------------------------------------
--  DDL for Procedure SP_VALIDAR_USUARIO
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "SISGESTPRESUPUESTOS"."SP_VALIDAR_USUARIO" (
    p_correo   IN  VARCHAR2,
    p_nombre   OUT VARCHAR2,
    p_activo   OUT CHAR
) IS
BEGIN
    SELECT nombres, activo
    INTO p_nombre, p_activo
    FROM usuarios
    WHERE correo = p_correo;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        p_nombre := NULL;
        p_activo := 'N';
END;

/
