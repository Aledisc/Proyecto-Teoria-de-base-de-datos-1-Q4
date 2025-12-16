# Avance del Proyecto – Sistema de Presupuesto Personal

## Estado general del proyecto

El proyecto presenta un avance sólido en la capa de base de datos y lógica de negocio, donde se implementaron la mayoría de las funcionalidades planificadas.  
La capa de presentación (frontend) se encuentra implementada de forma parcial, enfocada principalmente en el registro de información.

---

## Funcionalidades completamente implementadas

### Base de datos (Oracle)

- Gestión completa de usuarios mediante procedimientos almacenados.
- Gestión de categorías y subcategorías, incluyendo creación automática de subcategoría por defecto mediante triggers.
- Gestión de presupuestos y detalles de presupuesto, asegurando un único presupuesto activo por período.
- Registro de transacciones de ingresos, gastos y ahorros con validaciones de reglas de negocio.
- Gestión de metas de ahorro con actualización automática mediante triggers.
- Gestión de obligaciones fijas.
- Implementación de reglas de negocio críticas directamente en la base de datos.
- Manejo de errores Oracle (ORA-02291, ORA-01400, ORA-20200).
- Implementación de campos de auditoría.

---

## Funcionalidades parcialmente implementadas

### Interfaz de usuario (Frontend – Tkinter)

- Formularios para inserción de datos en las principales entidades del sistema.
- Validaciones básicas de campos obligatorios.
- Conexión funcional con el backend en Python.

**Limitaciones actuales del frontend:**
- La interfaz está orientada principalmente a operaciones de inserción.
- No se implementaron funcionalidades completas de edición, eliminación ni consultas avanzadas.
- La experiencia visual es básica y prioriza la funcionalidad académica.

---

## Funcionalidades no implementadas

- Módulo de alertas automáticas (excluido por indicaciones del docente).
- Reportes integrados directamente con la base de datos.
- Integración en tiempo real con herramientas de visualización.
- Control avanzado de roles y permisos.

---

## Reportes

Se realizaron reportes mediante Power BI utilizando datos estructurados y simulados, con el objetivo de analizar ingresos, gastos y distribución por categorías.  
Estos reportes cumplen un propósito analítico y demostrativo, pero no se encuentran integrados directamente con la base de datos del sistema.

---

## Observaciones finales

El proyecto cumple con los objetivos académicos principales, destacando especialmente el diseño y la implementación de la base de datos y las reglas de negocio.  
Las funcionalidades no implementadas o parcialmente desarrolladas se deben a limitaciones de tiempo y a decisiones de alcance definidas durante el desarrollo del proyecto.
