--------------------------------------------------------
--  File created - Monday-December-15-2025   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Function FN_AVANCE_META_AHORRO
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE FUNCTION "SISGESTPRESUPUESTOS"."FN_AVANCE_META_AHORRO" (
    p_id_meta_ahorro IN METAS_AHORROS.ID_META_AHORRO%TYPE
) RETURN NUMBER IS
    v_porcentaje NUMBER;
BEGIN
    SELECT
        ROUND((MONTO_AHORRADO / MONTO_META) * 100, 2)
    INTO v_porcentaje
    FROM METAS_AHORROS
    WHERE ID_META_AHORRO = p_id_meta_ahorro;

    RETURN NVL(v_porcentaje, 0);
END;

/
--------------------------------------------------------
--  DDL for Function FN_BALANCE_PRESUPUESTO
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE FUNCTION "SISGESTPRESUPUESTOS"."FN_BALANCE_PRESUPUESTO" (
    p_id_presupuesto IN PRESUPUESTOS.ID_PRESUPUESTO%TYPE
) RETURN NUMBER IS
BEGIN
    RETURN
        fn_total_ingresos_presupuesto(p_id_presupuesto)
      - fn_total_gastos_presupuesto(p_id_presupuesto)
      - fn_total_ahorros_presupuesto(p_id_presupuesto);
END;

/
--------------------------------------------------------
--  DDL for Function FN_MONTO_EJECUTADO_SUBCATEGORIA
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE FUNCTION "SISGESTPRESUPUESTOS"."FN_MONTO_EJECUTADO_SUBCATEGORIA" (
    p_id_presupuesto  IN TRANSACCIONES.ID_PRESUPUESTO%TYPE,
    p_id_subcategoria IN TRANSACCIONES.ID_SUBCATEGORIA%TYPE
) RETURN NUMBER IS
    v_total NUMBER;
BEGIN
    SELECT NVL(SUM(MONTO), 0)
    INTO v_total
    FROM TRANSACCIONES
    WHERE ID_PRESUPUESTO = p_id_presupuesto
      AND ID_SUBCATEGORIA = p_id_subcategoria;

    RETURN v_total;
END;

/
--------------------------------------------------------
--  DDL for Function FN_MONTO_PLANIFICADO_SUBCATEGORIA
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE FUNCTION "SISGESTPRESUPUESTOS"."FN_MONTO_PLANIFICADO_SUBCATEGORIA" (
    p_id_presupuesto  IN PRESUPUESTO_DETALLES.ID_PRESUPUESTO%TYPE,
    p_id_subcategoria IN PRESUPUESTO_DETALLES.ID_SUBCATEGORIA%TYPE
) RETURN NUMBER IS
    v_monto NUMBER;
BEGIN
    SELECT NVL(MONTO_MENSUAL, 0)
    INTO v_monto
    FROM PRESUPUESTO_DETALLES
    WHERE ID_PRESUPUESTO = p_id_presupuesto
      AND ID_SUBCATEGORIA = p_id_subcategoria;

    RETURN v_monto;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RETURN 0;
END;

/
--------------------------------------------------------
--  DDL for Function FN_PORCENTAJE_EJECUCION_SUBCATEGORIA
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE FUNCTION "SISGESTPRESUPUESTOS"."FN_PORCENTAJE_EJECUCION_SUBCATEGORIA" (
    p_id_presupuesto  IN PRESUPUESTO_DETALLES.ID_PRESUPUESTO%TYPE,
    p_id_subcategoria IN PRESUPUESTO_DETALLES.ID_SUBCATEGORIA%TYPE
) RETURN NUMBER IS
    v_planificado NUMBER;
    v_ejecutado   NUMBER;
BEGIN
    v_planificado := fn_monto_planificado_subcategoria(
                        p_id_presupuesto,
                        p_id_subcategoria
                     );

    IF v_planificado = 0 THEN
        RETURN 0;
    END IF;

    v_ejecutado := fn_monto_ejecutado_subcategoria(
                       p_id_presupuesto,
                       p_id_subcategoria
                   );

    RETURN ROUND((v_ejecutado / v_planificado) * 100, 2);
END;

/
--------------------------------------------------------
--  DDL for Function FN_TOTAL_AHORROS_PRESUPUESTO
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE FUNCTION "SISGESTPRESUPUESTOS"."FN_TOTAL_AHORROS_PRESUPUESTO" (
    p_id_presupuesto IN TRANSACCIONES.ID_PRESUPUESTO%TYPE
) RETURN NUMBER IS
    v_total NUMBER;
BEGIN
    SELECT NVL(SUM(MONTO), 0)
    INTO v_total
    FROM TRANSACCIONES
    WHERE ID_PRESUPUESTO = p_id_presupuesto
      AND TIPO_TRANSACCION = 'AHORRO';

    RETURN v_total;
END;

/
--------------------------------------------------------
--  DDL for Function FN_TOTAL_EJECUTADO_CATEGORIA
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE FUNCTION "SISGESTPRESUPUESTOS"."FN_TOTAL_EJECUTADO_CATEGORIA" (
    p_id_presupuesto IN TRANSACCIONES.ID_PRESUPUESTO%TYPE,
    p_id_categoria   IN CATEGORIAS.ID_CATEGORIA%TYPE
) RETURN NUMBER IS
    v_total NUMBER;
BEGIN
    SELECT NVL(SUM(t.MONTO), 0)
    INTO v_total
    FROM TRANSACCIONES t
    JOIN SUBCATEGORIAS sc ON sc.ID_SUBCATEGORIA = t.ID_SUBCATEGORIA
    WHERE t.ID_PRESUPUESTO = p_id_presupuesto
      AND sc.ID_CATEGORIA = p_id_categoria;

    RETURN v_total;
END;

/
--------------------------------------------------------
--  DDL for Function FN_TOTAL_GASTOS_PRESUPUESTO
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE FUNCTION "SISGESTPRESUPUESTOS"."FN_TOTAL_GASTOS_PRESUPUESTO" (
    p_id_presupuesto IN TRANSACCIONES.ID_PRESUPUESTO%TYPE
) RETURN NUMBER IS
    v_total NUMBER;
BEGIN
    SELECT NVL(SUM(MONTO), 0)
    INTO v_total
    FROM TRANSACCIONES
    WHERE ID_PRESUPUESTO = p_id_presupuesto
      AND TIPO_TRANSACCION = 'GASTO';

    RETURN v_total;
END;

/
--------------------------------------------------------
--  DDL for Function FN_TOTAL_INGRESOS_PRESUPUESTO
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE FUNCTION "SISGESTPRESUPUESTOS"."FN_TOTAL_INGRESOS_PRESUPUESTO" (
    p_id_presupuesto IN TRANSACCIONES.ID_PRESUPUESTO%TYPE
) RETURN NUMBER IS
    v_total NUMBER;
BEGIN
    SELECT NVL(SUM(MONTO), 0)
    INTO v_total
    FROM TRANSACCIONES
    WHERE ID_PRESUPUESTO = p_id_presupuesto
      AND TIPO_TRANSACCION = 'INGRESO';

    RETURN v_total;
END;

/
--------------------------------------------------------
--  DDL for Function FN_VALIDAR_PRESUPUESTO_ACTIVO
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE FUNCTION "SISGESTPRESUPUESTOS"."FN_VALIDAR_PRESUPUESTO_ACTIVO" (
    p_id_presupuesto IN PRESUPUESTOS.ID_PRESUPUESTO%TYPE
) RETURN BOOLEAN IS
    v_estado PRESUPUESTOS.ESTADO%TYPE;
BEGIN
    SELECT ESTADO
    INTO v_estado
    FROM PRESUPUESTOS
    WHERE ID_PRESUPUESTO = p_id_presupuesto;

    RETURN v_estado = 'ACTIVO';
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RETURN FALSE;
END;

/
