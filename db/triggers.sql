--------------------------------------------------------
--  File created - Monday-December-15-2025   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Trigger TRG_CATEGORIA_SUBCAT_DEF
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "SISGESTPRESUPUESTOS"."TRG_CATEGORIA_SUBCAT_DEF" 
AFTER INSERT ON CATEGORIAS
FOR EACH ROW
BEGIN
    INSERT INTO SUBCATEGORIAS (
        ID_CATEGORIA,
        NOMBRE,
        ACTIVA,
        SUBCATEGORIA_POR_DEFECTO
    ) VALUES (
        :NEW.ID_CATEGORIA,
        'General',
        'Y',
        'Y'
    );
END;

/
ALTER TRIGGER "SISGESTPRESUPUESTOS"."TRG_CATEGORIA_SUBCAT_DEF" ENABLE;
--------------------------------------------------------
--  DDL for Trigger TRG_NO_TRANSACCION_PRESUPUESTO_CERRADO
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "SISGESTPRESUPUESTOS"."TRG_NO_TRANSACCION_PRESUPUESTO_CERRADO" 
BEFORE INSERT ON TRANSACCIONES
FOR EACH ROW
DECLARE
    v_estado PRESUPUESTOS.ESTADO%TYPE;
BEGIN
    SELECT ESTADO
    INTO v_estado
    FROM PRESUPUESTOS
    WHERE ID_PRESUPUESTO = :NEW.ID_PRESUPUESTO;

    IF v_estado <> 'ACTIVO' THEN
        RAISE_APPLICATION_ERROR(
            -20200,
            'No se pueden registrar transacciones en presupuestos cerrados'
        );
    END IF;
END;

/
ALTER TRIGGER "SISGESTPRESUPUESTOS"."TRG_NO_TRANSACCION_PRESUPUESTO_CERRADO" ENABLE;
--------------------------------------------------------
--  DDL for Trigger TRG_TRANSACCION_AHORRO_META
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "SISGESTPRESUPUESTOS"."TRG_TRANSACCION_AHORRO_META" 
AFTER INSERT ON TRANSACCIONES
FOR EACH ROW
BEGIN
    IF :NEW.TIPO_TRANSACCION = 'AHORRO' THEN
        sp_actualizar_metas_por_ahorro(
            :NEW.ID_USUARIO,
            :NEW.ID_SUBCATEGORIA,
            :NEW.MONTO
        );
    END IF;
END;

/
ALTER TRIGGER "SISGESTPRESUPUESTOS"."TRG_TRANSACCION_AHORRO_META" ENABLE;
--------------------------------------------------------
--  DDL for Trigger TRG_TRANSACCIONES_AUDIT_UPD
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "SISGESTPRESUPUESTOS"."TRG_TRANSACCIONES_AUDIT_UPD" 
BEFORE UPDATE ON TRANSACCIONES
FOR EACH ROW
BEGIN
    :NEW.FECHA_MODIFICACION := CURRENT_TIMESTAMP;
END;

/
ALTER TRIGGER "SISGESTPRESUPUESTOS"."TRG_TRANSACCIONES_AUDIT_UPD" ENABLE;
