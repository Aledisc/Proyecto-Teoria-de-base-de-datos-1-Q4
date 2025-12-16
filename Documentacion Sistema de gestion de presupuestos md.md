![][image1]

**Teoría de base de datos 1**

**Nombre del Trabajo**

Documentación del proyecto 

**Proyecto**

Sistema de gestión de presupuestos personal

**Tecnologías principales**

Oracle, Python, TKinter, Power BI

**Nombres de los integrantes y números de cuenta**

Jorge Discua \- 22311096

 Edgar Vásquez \- 22211135 

 **Docente** 

Ing. Elvin Deras

**Fecha de entrega**

 15/12/25

## **1\. Introducción**

### **1.1 Contexto del problema**

Hoy en día, gestionar las finanzas personales se ha convertido en un desafío constante para la mayoría de la población. Si bien la mayoría de las personas generan ingresos periódicos, existe una dificultad constante para mantener registros claros y estructurados de dónde se gasta el dinero, cuánto se ahorra y si las decisiones financieras que se toman son o serán sostenibles a mediano y largo plazo.

Gran parte de este problema se debe a la falta de herramientas adecuadas para registrar y analizar la información financiera personal. Muchas personas recurren a métodos informales, como anotaciones en papel, aplicaciones generales o incluso la memoria, lo que genera errores, omisiones y una visión incompleta de su situación económica real. Esta falta de control detallado generalmente resulta en gastos innecesarios, desequilibrio entre ingresos y gastos, incapacidad para cumplir con los objetivos financieros e incluso, en casos extremos, en endeudamiento continuo.

Por otro lado, aunque existen aplicaciones comerciales para la gestión de finanzas personales, estas suelen presentar varias limitaciones, como que algunas son demasiado complejas para el usuario promedio; otras requieren suscripciones pagadas, y la gran mayoría no permite personalización ad hoc según las necesidades específicas de cada usuario. Además, en contextos académicos o de aprendizaje, estas herramientas no permiten analizar ni comprender la lógica interna de cómo se gestionan los datos, lo que limita su utilidad como medio formativo.

En este contexto, surge la necesidad de desarrollar un Sistema de Gestión de Presupuestos Personales cuyo objetivo principal sea facilitar, de forma clara, estructurada y accesible, el registro, la organización y el análisis de los ingresos y gastos del usuario. Este proyecto busca simular un escenario real de gestión de finanzas personales donde el usuario pueda crear categorías de gastos, registrar movimientos financieros, establecer presupuestos y estudiar su comportamiento económico a lo largo del tiempo.

Desde una perspectiva académica, el presente proyecto responde a la necesidad de aplicar los conocimientos teóricos adquiridos en temas como bases de datos, modelado de información, programación y análisis de datos, integrándolos en una solución práctica que represente un problema real. La gestión financiera personal es aún más relevante de desarrollar, ya que puede implicar datos sensibles, las relaciones entre entidades, la validación de la información y la creación de informes, lo que la convierte en un caso práctico ideal para el desarrollo de sistemas de información.

Al mismo tiempo, se apoya en la visualización de datos como herramienta clave en la toma de decisiones. No basta con almacenar información financiera; es necesario transformarlo en informes y gráficos a través de los cuales se puedan observar patrones, tendencias y áreas de mejora. En relación a esto, se incorpora el uso de herramientas de análisis y visualización como Power BI, que permite al usuario tener una interpretación más intuitiva de su comportamiento financiero. En pocas palabras, el proyecto nace como respuesta a una problemática real y cotidiana: la dificultad de llevar un control financiero personal eficiente. Al mismo tiempo, sirve como un ejercicio integral de desarrollo de software y análisis de datos, permitiendo aplicar conocimientos técnicos en un contexto práctico, comprensible y de alto valor tanto académico como personal.

### **1.2 Justificación del proyecto**

La elaboración del Sistema de Gestión de Presupuesto Personal se justifica por la necesidad de contar con una herramienta que permita organizar y analizar la información financiera de forma clara y estructurada. Una gestión adecuada de los ingresos y gastos garantiza la estabilidad económica, pero no todas las familias cuentan con métodos adecuados para supervisar de cerca sus finanzas, lo que dificulta la toma de decisiones.

Este proyecto permite aplicar los conocimientos adquiridos en los campos de bases de datos, programación y análisis de información. El problema en cuestión representa un enfoque muy realista, que implica la gestión de datos, la elaboración de estructuras relacionales y la generación de informes, todo lo cual contribuye al desarrollo de habilidades técnicas esenciales en la formación profesional.

Además, el sistema mejora la comprensión del comportamiento financiero mediante la aplicación de informes y visualizaciones. Permite identificar patrones de gasto, comparar ingresos y gastos, y analizar el cumplimiento presupuestario. Esta capacidad analítica aporta un valor significativo a este proyecto, ya que datos sencillos se convierten en información útil para la toma de decisiones.

Finalmente, el sistema se justifica como una solución didáctica y funcional que muestra cómo el manejo y visualización adecuada de los datos puede apoyar la gestión financiera personal, sirviendo al mismo tiempo como un ejercicio integral de desarrollo y análisis de sistemas de información en un entorno académico.

### **1.3 Objetivos del proyecto**

#### **1.3.1 Objetivo general**

Desarrollar un sistema de gestión de presupuestos personales que permita registrar, organizar y analizar la información financiera de un usuario, facilitando el control de ingresos y gastos mediante el uso de estructuras de datos y herramientas de visualización que apoyen la toma de decisiones financieras.

#### **1.3.2 Objetivos específicos**

* Diseñar una estructura de datos adecuada para el almacenamiento de información financiera, incluyendo usuarios, categorías, presupuestos y movimientos financieros.

* Implementar mecanismos para el registro de ingresos y gastos, permitiendo su clasificación por categoría y periodo de tiempo.

* Establecer presupuestos planificados y comparar dichos valores con los gastos reales registrados, con el fin de evaluar el comportamiento financiero del usuario.

* Generar reportes y visualizaciones que representen de forma clara el estado financiero, incluyendo ingresos, gastos, balance y distribución por categorías.

* Facilitar el análisis del comportamiento financiero a lo largo del tiempo mediante la representación gráfica de los datos históricos.

* Aplicar conceptos teóricos de bases de datos y análisis de información en un proyecto práctico que simule un escenario real de gestión financiera personal.

## **2\. Alcance del Proyecto**

El objetivo del presente proyecto es profundizar en el diseño y desarrollo de un Sistema de Gestión de Presupuesto Personal, dirigido al registro, organización y análisis de los datos financieros de un usuario a nivel individual. El sistema está conceptualizado como uno que apoyaría la toma de decisiones en finanzas, permitiendo al usuario percibir claramente los ingresos, los gastos y el comportamiento económico a lo largo del tiempo.

Dentro del alcance funcional del sistema se cuenta con la administración de usuarios, permitiendo identificar a cada usuario como entidad independiente dentro del sistema. Para cada uno de ellos, el sistema contempla la posibilidad de registrar diferentes movimientos financieros, que pueden clasificarse como ingresos o gastos y asociarse a categorías previamente definidas. Estas categorías permiten agrupar los movimientos según su naturaleza, tales como alimentación, transporte, servicios, entretenimiento, entre otros, facilitando así el análisis posterior.

El proyecto abarcará también la fijación y gestión presupuestaria, entendida como las cantidades previstas para un período de tiempo determinado. Estos presupuestos permiten establecer el límite financiero y comparar el gasto real con lo planificado, proporcionando un punto de referencia claro del nivel de control financiero por parte del usuario. Si bien el sistema permite su almacenamiento y análisis, su propósito es principalmente analítico y de soporte, no la ejecución automática de restricciones de gasto.

En cuanto a la gestión de la información, el alcance de este proyecto incluye el diseño de un modelo de datos, la definición de las tablas, relaciones y estructuras necesarias para el almacenamiento coherente de la información financiera. Se consideran aspectos básicos de la integridad de los datos, como la correcta asociación de usuarios con categorías y movimientos, para que la simulación del entorno de la base de datos sea lo más realista posible.

Además, el sistema también permitirá la generación de informes y la visualización de datos mediante sus herramientas de análisis. Mediante el uso de conjuntos de datos estructurados o incluso visualizaciones gráficas, el sistema permitirá el mapeo adecuado del comportamiento financiero del usuario, mostrando la evolución del gasto por categoría, ingresos versus gastos, la evolución temporal de los movimientos y la distribución porcentual del gasto. Estas visualizaciones tendrán como objetivo facilitar la comprensión de la información y apoyar la toma de decisiones.

Este proyecto se centrará en un entorno académico y demostrativo. Por lo tanto, no se considerarán mecanismos avanzados de seguridad, como autenticación compleja o cifrado de datos, integración con servicios financieros reales, etc. El sistema no prevé la conexión directa con cuentas bancarias, medios de pago ni la automatización de ninguna forma de transacción financiera.

Asimismo, el desarrollo de una aplicación móvil o web para un entorno productivo, ni la implementación de funcionalidades avanzadas relacionadas con IA, previsiones financieras automáticas o sugerencias, no forman parte del alcance de este proyecto. El sistema se basa principalmente en la gestión, el análisis y la visualización adecuados de la información financiera, priorizando la claridad, la estructura y la comprensión de los datos. El alcance del proyecto se resume en el desarrollo de un sistema funcional para gestionar presupuestos y permitir el análisis estructurado de datos financieros personales; también debe centrarse en una herramienta de aprendizaje académico, modelar correctamente la información y permitir la creación de informes claros y comprensibles; esto implica excluir temas típicos de sistemas comerciales o de producción a gran escala.

## **3\. Arquitectura del sistema**

#### **3.1 Arquitectura general**

El Sistema de Gestión de Presupuestos Personales se diseñó siguiendo el modelo de arquitectura en tres capas, una estructura ampliamente utilizada en el desarrollo de sistemas de información por su claridad, escalabilidad y separación de responsabilidades. Esta arquitectura permite dividir el sistema en componentes bien definidos, facilitando el mantenimiento, la comprensión del flujo de datos y la evolución futura del sistema.

Las capas que conforman esta arquitectura son: capa de presentación, capa de lógica de negocio y capa de datos, cada una con funciones específicas y responsabilidades claramente delimitadas.

#### **3.2 Capa de presentación (Tkinter)**

La capa de presentación es la encargada de la interacción directa con el usuario. En este proyecto, dicha capa se implementa utilizando Tkinter, una biblioteca gráfica incluida en Python que permite desarrollar interfaces de usuario de escritorio de manera sencilla y funcional.

Esta capa tiene como objetivo principal capturar las acciones del usuario y mostrar la información de forma clara y comprensible. Entre sus responsabilidades se incluyen:

* Mostrar formularios para el registro de usuarios, categorías, presupuestos e ingresos/gastos.

* Permitir la navegación entre las diferentes funcionalidades del sistema.  
    
* Presentar mensajes informativos, de confirmación y de error al usuario.

* Mostrar resultados obtenidos del sistema, como listados de movimientos o resúmenes básicos.

La capa de presentación no contiene lógica de negocio ni acceso directo a la base de datos. Su función se limita exclusivamente a la visualización de la información y a la captura de eventos, los cuales son enviados a la capa de lógica para su procesamiento. Esta separación evita dependencias innecesarias y mejora la organización del código.

#### **3.3 Capa de lógica de negocio (Python)**

La capa de lógica de negocio constituye el núcleo funcional del sistema y se encuentra implementada en Python. Esta capa es responsable de procesar la información recibida desde la interfaz gráfica, aplicar las reglas del negocio y coordinar la comunicación entre la capa de presentación y la capa de datos.

Dentro de esta capa se realizan tareas como:

* Validación de datos ingresados por el usuario (formatos, valores permitidos, campos obligatorios).

* Clasificación de movimientos financieros como ingresos o gastos.

* Gestión de categorías y asociación de estas con los movimientos.

* Cálculo de totales, balances y comparaciones entre valores planificados y reales.

* Preparación de la información que será enviada a la capa de datos para su almacenamiento o consulta.

Además, esta capa actúa como intermediaria entre la interfaz y la base de datos, evitando que la capa de presentación tenga conocimiento directo de las estructuras de almacenamiento. De esta manera, cualquier cambio en la base de datos o en las reglas del negocio puede ser gestionado desde la lógica sin afectar directamente a la interfaz gráfica.

#### **3.4 Capa de datos (Oracle)**

La capa de datos es la encargada del almacenamiento persistente de la información del sistema y se implementa utilizando una base de datos Oracle. Esta capa se responsabiliza de mantener la integridad, consistencia y disponibilidad de los datos financieros registrados.

Entre sus funciones principales se incluyen:

* Almacenamiento de información relacionada con usuarios, categorías, presupuestos y movimientos financieros.

* Gestión de relaciones entre las entidades del sistema.

* Ejecución de consultas, procedimientos almacenados y funciones para la obtención y manipulación de datos.

* Garantizar la integridad referencial y la coherencia de la información almacenada.

El acceso a la base de datos se realiza exclusivamente a través de la capa de lógica de negocio, lo que permite controlar las operaciones de inserción, actualización y consulta de datos. Esta separación reduce riesgos, mejora la seguridad y facilita la administración del sistema.

#### **3.5 Flujo general de funcionamiento**

El flujo de funcionamiento del sistema sigue una secuencia clara entre las capas:

1. El usuario interactúa con la interfaz gráfica en la capa de presentación.

2. Las acciones del usuario son enviadas a la capa de lógica de negocio.

3. La lógica valida y procesa la información, aplicando las reglas correspondientes.

4. En caso necesario, la lógica se comunica con la capa de datos para almacenar o recuperar información.

5. Los resultados obtenidos regresan a la capa de lógica y posteriormente a la capa de presentación para ser mostrados al usuario.

Este enfoque garantiza un sistema modular, organizado y fácil de mantener.

#### **3.6 Ventajas de la arquitectura utilizada**

La arquitectura en tres capas aporta múltiples beneficios al proyecto, entre los cuales destacan:

* Separación clara de responsabilidades entre interfaz, lógica y datos.

* Mayor facilidad de mantenimiento y escalabilidad.

* Posibilidad de reemplazar o mejorar una capa sin afectar significativamente a las demás.

* Mejora en la organización del código y comprensión del sistema.

## **4\. Modelo de datos**

#### **4.1 Diagrama entidad-relación (ER)**

#### 

### **4.2 Modelo relacional (RM)**

### 

# 

# 

# 

# 

### 

### **4.3 Diccionario de datos**

El presente diccionario de datos describe las entidades principales del Sistema de Gestión de Presupuestos Personales, detallando la estructura de cada tabla, sus atributos, tipos de datos y una breve descripción funcional. Este diccionario permite comprender de manera precisa cómo se almacena y organiza la información dentro del sistema, sirviendo como referencia técnica para el desarrollo, mantenimiento y análisis del mismo.

#### **4.3.1 Tabla: USUARIOS**

**Descripción:**  
Almacena la información básica de los usuarios que utilizan el sistema. Cada usuario representa una entidad independiente con sus propios presupuestos y movimientos financieros.

| Campo | Tipo de dato | Descripción |
| ----- | ----- | ----- |
| id\_usuario | NUMBER | Identificador único del usuario. |
| nombres | VARCHAR2 | Nombre(s) del usuario. |
| apellidos | VARCHAR2 | Apellido(s) del usuario. |
| correo | VARCHAR2 | Correo electrónico del usuario. |
| fecha\_registro | DATE | Fecha en la que el usuario fue registrado en el sistema. |
| activo | NUMBER(1) | Indica si el usuario se encuentra activo (1) o inactivo (0). |

#### **4.3.2 Tabla: CATEGORIAS**

**Descripción:**  
Contiene categorías utilizadas para clasificar los movimientos financieros, permitiendo agrupar ingresos y gastos según su naturaleza.

| Campo | Tipo de dato | Descripción |
| ----- | ----- | ----- |
| id\_categoria | NUMBER | Identificador único de la categoría. |
| nombre | VARCHAR2 | Nombre de la categoría (ej. Alimentación, Transporte). |
| descripcion | VARCHAR2 | Descripción general de la categoría. |
| tipo\_categoria | VARCHAR2 | Indica si la categoría corresponde a un Ingreso o un Gasto. |
| icono | VARCHAR2 | Identificador visual o icono asociado a la categoría. |

#### **4.3.3 Tabla: PRESUPUESTOS**

**Descripción:**  
Almacena los presupuestos planificados por cada usuario para un periodo determinado. Permite comparar los valores planificados con los gastos reales registrados.

| Campo | Tipo de dato | Descripción |
| ----- | ----- | ----- |
| id\_presupuesto | NUMBER | Identificador único del presupuesto. |
| id\_usuario | NUMBER | Identificador del usuario asociado al presupuesto. |
| nombre\_descriptivo | VARCHAR2 | Nombre o descripción del presupuesto. |
| fecha\_inicio | DATE | Fecha de inicio del periodo del presupuesto. |
| fecha\_fin | DATE | Fecha de finalización del periodo del presupuesto. |
| ingresos\_planificados | NUMBER | Monto total de ingresos esperados. |
| gastos\_planificados | NUMBER | Monto total de gastos planificados. |
| ahorros\_planificados | NUMBER | Monto destinado al ahorro. |
| fecha\_creacion | DATE | Fecha de creación del presupuesto. |
| estado | VARCHAR2 | Estado del presupuesto (Activo, Cerrado, etc.). |

#### **4.3.4 Tabla: SUBCATEGORIAS**

**Descripción:**  
 Permite un mayor nivel de detalle en la clasificación de las transacciones, asociando subcategorías a una categoría principal.

| Campo | Tipo de dato | Descripción |
| ----- | ----- | ----- |
| id\_subcategoria | NUMBER | Identificador único de la subcategoría. |
| id\_categoria | NUMBER | Categoría a la que pertenece la subcategoría. |
| nombre | VARCHAR2 | Nombre de la subcategoría. |
| descripcion | VARCHAR2 | Descripción de la subcategoría. |

#### **4.3.5 Tabla: PRESUPUESTO\_DETALLES**

**Descripción:**  
 Desglosa el presupuesto total en montos asignados por categoría o subcategoría, permitiendo un control más específico del gasto planificado.

| Campo | Tipo de dato | Descripción |
| ----- | ----- | ----- |
| id\_detalle | NUMBER | Identificador único del detalle del presupuesto. |
| id\_presupuesto | NUMBER | Presupuesto al que pertenece el detalle. |
| id\_categoria | NUMBER | Categoría asociada al monto planificado. |
| id\_subcategoria | NUMBER | Subcategoría asociada (opcional). |
| monto\_asignado | NUMBER | Monto planificado para la categoría o subcategoría. |

#### **4.3.6 Tabla: TRANSACCIONES**

**Descripción:**  
 Registra todos los movimientos financieros realizados por los usuarios, incluyendo ingresos, gastos, pagos de obligaciones y aportes a metas de ahorro.

| Campo | Tipo de dato | Descripción |
| ----- | ----- | ----- |
| id\_transaccion | NUMBER | Identificador único de la transacción. |
| id\_usuario | NUMBER | Usuario que realizó la transacción. |
| id\_categoria | NUMBER | Categoría asociada a la transacción. |
| id\_subcategoria | NUMBER | Subcategoría asociada (opcional). |
| fecha | DATE | Fecha de la transacción. |
| monto | NUMBER | Monto del ingreso o gasto. |
| tipo | VARCHAR2 | Tipo de transacción (Ingreso o Gasto). |
| descripcion | VARCHAR2 | Descripción opcional de la transacción. |

#### **4.3.7 Tabla: METAS\_AHORROS**

**Descripción:**  
 Permite definir metas de ahorro con un monto objetivo y dar seguimiento al progreso de ahorro del usuario.

| Campo | Tipo de dato | Descripción |
| ----- | ----- | ----- |
| id\_meta | NUMBER | Identificador único de la meta de ahorro. |
| id\_usuario | NUMBER | Usuario propietario de la meta. |
| nombre | VARCHAR2 | Nombre descriptivo de la meta. |
| monto\_objetivo | NUMBER | Monto total que se desea ahorrar. |
| monto\_actual | NUMBER | Monto acumulado hasta el momento. |
| fecha\_inicio | DATE | Fecha de inicio de la meta. |
| fecha\_fin | DATE | Fecha estimada de cumplimiento. |
| estado | VARCHAR2 | Estado de la meta (Activa, Cumplida). |

#### **4.3.8 Tabla: OBLIGACIONES\_FIJAS**

**Descripción:**  
 Registra los gastos recurrentes u obligaciones financieras periódicas del usuario, como servicios, alquileres o pagos fijos.

| Campo | Tipo de dato | Descripción |
| ----- | ----- | ----- |
| id\_obligacion | NUMBER | Identificador único de la obligación. |
| id\_usuario | NUMBER | Usuario al que pertenece la obligación. |
| nombre | VARCHAR2 | Nombre de la obligación. |
| monto | NUMBER | Monto fijo de la obligación. |
| periodicidad | VARCHAR2 | Frecuencia de pago (Mensual, Quincenal). |
| fecha\_inicio | DATE | Fecha de inicio de la obligación. |
| estado | VARCHAR2 | Estado de la obligación (Activa, Cancelada). |

#### **4.3.9 Observaciones finales**

El diccionario de datos fue diseñado para reflejar un sistema financiero personal realista, permitiendo un alto nivel de detalle en la planificación, ejecución y análisis de las finanzas del usuario. La estructura facilita la generación de reportes y visualizaciones, así como la extensión futura del sistema sin comprometer su integridad.

## **5\. Reglas de negocio implementadas**

Las reglas de negocio del Sistema de Gestión de Presupuestos Personales definen el comportamiento, las restricciones y las validaciones que rigen el funcionamiento del sistema. Estas reglas garantizan la coherencia de la información financiera, el correcto control presupuestal y la correcta relación entre las distintas entidades del modelo de datos.  
Las reglas descritas a continuación corresponden únicamente a las funcionalidades implementadas, excluyendo de manera explícita el módulo de alertas automáticas, el cual fue descartado según indicaciones del docente

### **5.1 Reglas de negocio relacionadas con usuarios**

* Todo usuario debe contar con un identificador único dentro del sistema.

* El correo electrónico del usuario debe ser único y no puede repetirse entre distintos registros.

* Un usuario puede tener múltiples presupuestos a lo largo del tiempo, pero estos deben estar claramente delimitados por su periodo de vigencia.

* Un usuario puede registrar múltiples transacciones, metas de ahorro y obligaciones fijas asociadas a su perfil.

* Los usuarios inactivos no pueden registrar nuevas transacciones ni crear nuevos presupuestos.

### **5.2 Reglas de negocio relacionadas con categorías y subcategorías**

* Toda categoría debe pertenecer a un único tipo: ingreso, gasto o ahorro.

* Toda categoría debe contar obligatoriamente con al menos una subcategoría asociada.

* Al momento de crear una categoría, el sistema crea automáticamente una subcategoría por defecto (por ejemplo, “General”), garantizando que la categoría siempre sea utilizable

* Las subcategorías heredan el tipo de su categoría padre y no pueden cambiarlo de manera independiente.

* No se permite registrar transacciones ni asignaciones presupuestarias directamente a una categoría; estas deben realizarse exclusivamente a nivel de subcategoría.

* Una subcategoría solo puede pertenecer a una única categoría.

* Toda subcategoría utilizada en transacciones o presupuestos debe encontrarse activa.

### **5.3 Reglas de negocio relacionadas con presupuestos**

* Todo presupuesto debe estar asociado a un usuario específico.

* Cada presupuesto debe contar con un periodo de vigencia definido por año y mes de inicio y fin.

* El periodo de fin del presupuesto debe ser igual o posterior al periodo de inicio.

* Un usuario no puede tener más de un presupuesto activo que cubra el mismo periodo de tiempo.

* El presupuesto define los montos globales planificados para ingresos, gastos y ahorro, los cuales sirven como referencia para el análisis financiero.

* Un presupuesto puede encontrarse en diferentes estados, tales como activo o cerrado.

* No se permite registrar transacciones fuera del periodo de vigencia del presupuesto asociado.

### **5.4 Reglas de negocio relacionadas con los detalles del presupuesto**

* Todo detalle de presupuesto debe estar asociado a una subcategoría específica.

* El monto asignado en el detalle de presupuesto corresponde a un monto mensual fijo, el cual se aplica a todos los meses dentro de la vigencia del presupuesto.

* No se permite que un detalle de presupuesto tenga valores nulos en la subcategoría o en el monto asignado.

* Si se desea asignar montos distintos para meses diferentes, se debe crear un nuevo presupuesto para ese periodo.

* El monto ejecutado de una subcategoría se calcula dinámicamente sumando las transacciones registradas para el mes correspondiente.

* El porcentaje de ejecución presupuestal se obtiene comparando el monto ejecutado frente al monto mensual asignado.

### **5.5 Reglas de negocio relacionadas con transacciones**

* Toda transacción debe estar asociada a un usuario, un presupuesto y una subcategoría.

* El tipo de la transacción (ingreso, gasto o ahorro) debe coincidir con el tipo de la categoría padre de la subcategoría asociada.

* Toda transacción debe contar con un monto mayor a cero.

* Las transacciones incluyen campos de año y mes presupuestal, los cuales determinan a qué periodo se imputa el movimiento financiero.

* El año y mes presupuestal pueden ser distintos a la fecha real de la transacción, permitiendo flexibilidad contable, siempre que se encuentren dentro de la vigencia del presupuesto

* Toda transacción asociada a una obligación fija debe utilizar la misma subcategoría definida en dicha obligación.

* Las transacciones constituyen la fuente principal para el cálculo de gastos ejecutados, ingresos reales y avances en metas de ahorro.

### **5.6 Reglas de negocio relacionadas con obligaciones fijas**

* Toda obligación fija debe estar asociada a una subcategoría de tipo gasto.

* Las obligaciones fijas representan compromisos financieros recurrentes con monto y periodicidad definidos.

* Una obligación puede tener una fecha de finalización o ser indefinida.

* La fecha de finalización, si existe, debe ser posterior a la fecha de inicio.

* Las obligaciones fijas pueden utilizarse como referencia para el registro de transacciones periódicas.

* Una obligación inactiva no puede ser utilizada para asociar nuevas transacciones.

### **5.7 Reglas de negocio relacionadas con metas de ahorro**

* Toda meta de ahorro debe estar asociada a una subcategoría de tipo ahorro.

* Una subcategoría de ahorro solo puede estar asociada a una meta activa a la vez.

* El monto acumulado de una meta no puede superar el monto objetivo definido.

* El progreso de la meta se calcula como el porcentaje entre el monto acumulado y el monto objetivo.

* El monto acumulado se actualiza automáticamente al registrarse transacciones de ahorro asociadas a la subcategoría de la meta, garantizando consistencia en tiempo real  
  .

* Una meta cambia automáticamente su estado a completado cuando alcanza o supera el 100% del monto objetivo.

* La fecha objetivo de una meta debe ser posterior a la fecha de inicio.

### **5.8 Exclusión del módulo de alertas**

Aunque el diseño original del sistema contempla la generación de alertas automáticas relacionadas con ejecución presupuestal, vencimiento de obligaciones y avance de metas de ahorro, dicho módulo fue excluido de la implementación final siguiendo instrucciones directas del docente.  
No obstante, el diseño del modelo de datos y de las reglas de negocio deja abierta la posibilidad de incorporar este módulo en futuras extensiones del sistema, sin necesidad de modificar la estructura base de la base de datos.

### **5.9 Consideraciones finales sobre las reglas de negocio**

Las reglas de negocio implementadas permiten representar de manera fiel el comportamiento financiero personal, asegurando coherencia entre presupuestos, transacciones, obligaciones y metas de ahorro. Estas reglas constituyen el núcleo lógico del sistema y garantizan que la información almacenada pueda ser analizada de forma confiable mediante reportes y visualizaciones, cumpliendo los objetivos académicos del proyecto

## **6\. Auditoría y seguridad de datos**

La auditoría y la seguridad de los datos son aspectos fundamentales en cualquier sistema de información que gestione datos sensibles. En el Sistema de Gestión de Presupuestos Personales, estos aspectos se abordan mediante la implementación de campos de auditoría obligatorios en todas las tablas y mediante un control estructurado del acceso y la modificación de la información, garantizando la trazabilidad, integridad y confiabilidad de los datos almacenados.

### **6.1 Campos de auditoría**

Con el objetivo de mantener un registro detallado de las operaciones realizadas sobre la base de datos, todas las tablas del sistema incluyen campos de auditoría obligatorios, los cuales permiten identificar quién creó o modificó un registro, así como el momento exacto en que dichas acciones ocurrieron.

Los campos de auditoría implementados son los siguientes:

| Campo | Descripción |
| ----- | ----- |
| creado\_por | Identifica el usuario o proceso que creó el registro. |
| creado\_en | Fecha y hora exacta en la que se realizó la inserción del registro. |
| modificado\_por | Identifica el usuario o proceso que realizó la última modificación del registro. |
| modificado\_en | Fecha y hora exacta de la última modificación del registro. |

Estos campos se encuentran presentes en todas las entidades principales del sistema, incluyendo usuarios, categorías, subcategorías, presupuestos, detalles de presupuesto, transacciones, metas de ahorro y obligaciones fijas.

La actualización de estos campos se realiza de manera automática mediante valores por defecto y lógica implementada en la base de datos, evitando que dependan de la intervención manual del usuario. Esto asegura que la información de auditoría sea consistente y confiable.

### 

### 

### **6.2 Justificación de los campos de auditoría**

La inclusión de campos de auditoría se justifica principalmente por la necesidad de trazabilidad y control de cambios dentro del sistema. Dado que el sistema gestiona información financiera personal, resulta fundamental poder identificar el origen de cada registro y las modificaciones que ha sufrido a lo largo del tiempo.

Desde el punto de vista técnico, los campos de auditoría permiten:

* Rastrear errores o inconsistencias en los datos, identificando cuándo y por quién se realizó una modificación.

* Facilitar el mantenimiento y la depuración del sistema, especialmente durante pruebas y validaciones.

* Proporcionar soporte para análisis históricos y revisión de cambios en la información financiera.

* Simular buenas prácticas utilizadas en sistemas reales de gestión financiera y contable.

Desde el punto de vista académico, la implementación de auditoría demuestra la aplicación de buenas prácticas de diseño de bases de datos, alineadas con sistemas empresariales reales, donde la trazabilidad de la información es un requisito indispensable.

## **6.3 Seguridad de los datos**

La seguridad de los datos en el sistema se gestiona principalmente a través de la **separación de responsabilidades** y el control del acceso a la base de datos. El diseño del sistema sigue el principio de que la mayor parte de la lógica de negocio reside en la base de datos, lo que reduce el riesgo de manipulaciones incorrectas desde la capa de presentación.

Las principales medidas de seguridad implementadas incluyen:

* Acceso controlado a la base de datos mediante credenciales específicas.

* Uso de procedimientos almacenados para realizar operaciones CRUD, evitando el acceso directo a las tablas.

* Validación de reglas de negocio en la base de datos, garantizando la integridad de la información.

* Restricciones de claves primarias y foráneas para mantener la coherencia entre las entidades.

* Control del estado de los registros (activos/inactivos) en lugar de eliminaciones físicas cuando corresponde.

Estas medidas permiten minimizar errores, prevenir inconsistencias y asegurar que los datos financieros sean manipulados únicamente bajo las reglas definidas por el sistema.

### **6.4 Consideraciones finales**

La implementación de auditoría y seguridad de datos en el Sistema de Gestión de Presupuestos Personales refuerza la confiabilidad del sistema y su alineación con prácticas profesionales de desarrollo de sistemas de información. Aunque el proyecto se desarrolla en un entorno académico, las decisiones adoptadas reflejan escenarios reales de sistemas financieros, sentando una base sólida para futuras extensiones o adaptaciones a entornos productivos 

## **7\. Procesos almacenados**

### **7.1 Tabla resumen de procedimientos almacenados**

La siguiente tabla presenta un resumen de los procedimientos almacenados implementados en la base de datos del sistema, indicando la tabla principal que afectan y el tipo de operación que realizan. Esta clasificación permite identificar de forma clara la cobertura funcional del sistema a nivel de base de datos.

| Procedimiento almacenado | Tabla(s) asociada(s) | Tipo |
| ----- | ----- | ----- |
| SP\_INSERTAR\_USUARIO | USUARIOS | Inserción |
| SP\_ACTUALIZAR\_USUARIO | USUARIOS | Actualización |
| SP\_DESACTIVAR\_USUARIO | USUARIOS | Lógica (desactivación) |
| SP\_CONSULTAR\_USUARIO | USUARIOS | Consulta |
| SP\_LISTAR\_USUARIOS | USUARIOS | Consulta |
| SP\_VALIDAR\_USUARIO | USUARIOS | Validación |
| SP\_INSERTAR\_CATEGORIA | CATEGORIAS | Inserción |
| SP\_ACTUALIZAR\_CATEGORIA | CATEGORIAS | Actualización |
| SP\_ELIMINAR\_CATEGORIA | CATEGORIAS | Lógica (desactivación) |
| SP\_CONSULTAR\_CATEGORIA | CATEGORIAS | Consulta |
| SP\_LISTAR\_CATEGORIAS | CATEGORIAS | Consulta |
| SP\_INSERTAR\_SUBCATEGORIA | SUBCATEGORIAS | Inserción |
| SP\_ACTUALIZAR\_SUBCATEGORIA | SUBCATEGORIAS | Actualización |
| SP\_ELIMINAR\_SUBCATEGORIA | SUBCATEGORIAS | Lógica (desactivación) |
| SP\_CONSULTAR\_SUBCATEGORIA | SUBCATEGORIAS | Consulta |
| SP\_LISTAR\_SUBCATEGORIAS\_POR\_CATEGORIA | SUBCATEGORIAS | Consulta |
| SP\_INSERTAR\_PRESUPUESTO | PRESUPUESTOS | Inserción |
| SP\_CREAR\_PRESUPUESTO\_COMPLETO | PRESUPUESTOS | Orquestación |
| SP\_ACTUALIZAR\_PRESUPUESTO | PRESUPUESTOS | Actualización |
| SP\_CERRAR\_PRESUPUESTO | PRESUPUESTOS | Lógica (cierre) |
| SP\_CONSULTAR\_PRESUPUESTO | PRESUPUESTOS | Consulta |
| SP\_LISTAR\_PRESUPUESTOS\_USUARIO | PRESUPUESTOS | Consulta |
| SP\_RESUMEN\_PRESUPUESTO | PRESUPUESTOS | Resumen |
| SP\_INSERTAR\_PRESUPUESTO\_DETALLE | PRESUPUESTO\_DETALLES | Inserción |
| SP\_ACTUALIZAR\_PRESUPUESTO\_DETALLE | PRESUPUESTO\_DETALLES | Actualización |
| SP\_ELIMINAR\_PRESUPUESTO\_DETALLE | PRESUPUESTO\_DETALLES | Eliminación |
| SP\_CONSULTAR\_PRESUPUESTO\_DETALLE | PRESUPUESTO\_DETALLES | Consulta |
| SP\_LISTAR\_DETALLES\_PRESUPUESTO | PRESUPUESTO\_DETALLES | Consulta |
| SP\_INSERTAR\_TRANSACCION | TRANSACCIONES | Inserción |
| SP\_ACTUALIZAR\_TRANSACCION | TRANSACCIONES | Actualización |
| SP\_ELIMINAR\_TRANSACCION | TRANSACCIONES | Eliminación |
| SP\_CONSULTAR\_TRANSACCION | TRANSACCIONES | Consulta |
| SP\_LISTAR\_TRANSACCIONES\_PRESUPUESTO | TRANSACCIONES | Consulta |
| SP\_INSERTAR\_META\_AHORRO | METAS\_AHORROS | Inserción |
| SP\_ACTUALIZAR\_META\_AHORRO | METAS\_AHORROS | Actualización |
| SP\_CANCELAR\_META\_AHORRO | METAS\_AHORROS | Lógica (cancelación) |
| SP\_CONSULTAR\_META\_AHORRO | METAS\_AHORROS | Consulta |
| SP\_LISTAR\_METAS\_USUARIO | METAS\_AHORROS | Consulta |
| SP\_ACTUALIZAR\_METAS\_POR\_AHORRO | METAS\_AHORROS | Lógica (cálculo) |
| SP\_INSERTAR\_OBLIGACION\_FIJA | OBLIGACIONES\_FIJAS | Inserción |
| SP\_ACTUALIZAR\_OBLIGACION\_FIJA | OBLIGACIONES\_FIJAS | Actualización |
| SP\_DESACTIVAR\_OBLIGACION\_FIJA | OBLIGACIONES\_FIJAS | Lógica (desactivación) |
| SP\_CONSULTAR\_OBLIGACION\_FIJA | OBLIGACIONES\_FIJAS | Consulta |
| SP\_LISTAR\_OBLIGACIONES\_USUARIO | OBLIGACIONES\_FIJAS | Consulta |
| SP\_RESUMEN\_CATEGORIA\_PRESUPUESTO | CATEGORIAS / TRANSACCIONES | Resumen |

### **7.2 Observaciones generales**

* El sistema implementa procedimientos para todas las operaciones críticas, evitando el acceso directo a las tablas.

* No se realizan eliminaciones físicas en la mayoría de entidades; se privilegia la desactivación lógica, alineada con las reglas de negocio.

* Existen procedimientos de orquestación (como SP\_CREAR\_PRESUPUESTO\_COMPLETO) que encapsulan múltiples operaciones, reduciendo errores desde la capa de aplicación.

* Los procedimientos de resumen concentran la lógica de cálculo financiero directamente en la base de datos, garantizando consistencia en los reportes.

### **7.3 Descripción detallada de los procedimientos**

### **USUARIOS**

1. #### **Insertar usuario**

#### 

#### **Nombre: sp\_insertar\_usuario**

**Tipo:** Procedimiento (CRUD)

**Descripción:** Registra un nuevo usuario al sistema

**Parámetros de entrada:**

| Parámetro | Tipo | Descripción |
| ----- | ----- | ----- |
| **p\_nombres** | **VARCHAR2** | **Nombres del usuario** |
| **p\_apellidos** | **VARCHAR2** | **Apellidos del usuario** |
| **p\_correo** | **VARCHAR2** | **Correo electrónico** |
| **p\_salario** | **NUMBER** | **Salario mensual** |
| **p\_usuario\_creacion** | **VARCHAR2** | **Usuario que crea el registro** |

**Uso en SQL:**  
**![][image2]**

**Uso en Python (front):**

**![][image3]**

2. #### **Actualizar usuario**

#### **Nombre: sp\_actualizar\_usuario**

**Tipo:** Procedimiento (CRUD)

**Descripción:** un nuevo usuario al sistema

**Parámetros de entrada:**

| Parámetro | Tipo | Descripción |
| ----- | ----- | ----- |
| **p\_id\_usuario** | **NUMBER** | **ID del usuario** |
| **p\_nombres** | **VARCHAR2** | **Nombres** |
| **p\_apellidos** | **VARCHAR2** | **Apellidos** |
| **p\_correo** | **VARCHAR2** | **Correo** |
| **p\_salario** | **NUMBER** | **Salario** |
| **p\_activo** | **CHAR** | **'Y' / 'N'** |
| **p\_usuario\_modificacion** | **VARCHAR2** | **Auditoría** |

**Uso en SQL:**  
**![][image4]**

**Uso en Python (front):**

**![][image5]**

## 

3. #### **Listar usuarios**

#### **Nombre: sp\_listar\_usuarios**

**Tipo:** Procedimiento (Consulta)

**Descripción:** Devuelve una lista de usuarios registrados

**Parámetros de salida:**

| Parámetro | Tipo |
| ----- | ----- |
| **p\_resultado** | **SYS\_REFCURSOR** |

**Uso en Python (front):**

**![][image6]**

### **CATEGORIAS Y SUBCATEGORIAS**

#### 

4. #### **Insertar categoría**

#### **Nombre: sp\_insertar\_categoria**

**Tipo:** Procedimiento (CRUD)

**Descripción:** Crea una categoría financiera. El sistema genera automática una subcategoria “general”

**Parámetros de entrada:**

| Parámetro | Tipo |
| ----- | ----- |
| **p\_nombre** | **VARCHAR2** |
| **p\_descripcion** | **VARCHAR2** |
| **p\_tipo\_categoria** | **VARCHAR2 (INGRESO / GASTO / AHORRO)** |
| **p\_icono** | **VARCHAR2** |
| **p\_color** | **VARCHAR2** |
| **p\_usuario\_creacion** | **VARCHAR2** |

**Uso en SQL:**  
**![][image7]**

**Uso en Python (front):**

**![][image8]**

5. ### **Listar categorias**

#### **Nombre: sp\_listar\_categorias**

**Tipo:** Procedimiento (Consulta)

**Descripción:** Devuelve todas las categorías del sistema.

**Uso en Python (front):**

**![][image9]**

6. #### **Listar categorias de una categoría**

#### **Nombre: sp\_listar\_subcategorias\_categoria**

**Tipo:** Procedimiento (Consulta)

**Descripción:** Devuelve las subcategorías de una categoría.

**Parámetros de entrada:**

| Parámetro | Tipo |
| ----- | ----- |
| **p\_id\_categoria** | **NUMBER** |
| **p\_resultado** | **SYS\_REFCURSOR (OUT)** |

**Uso en Python (front):**

**![][image10]**

### **PRESUPUESTOS**

7. #### **Insertar presupuesto**

#### **Nombre: sp\_insertar\_presupuesto**

**Tipo:** Procedimiento (Negocio)

**Descripción:** Crea un presupuesto activo. Solo se permite uno activo por usuario.

**Parámetros de entrada:**

| Parámetro | Tipo |
| ----- | ----- |
| **p\_id\_usuario** | **NUMBER** |
| **p\_nombre** | **VARCHAR2** |
| **p\_fecha\_inicio** | **DATE** |
| **p\_fecha\_fin** | **DATE** |
| **p\_ingresos\_planificados** | **NUMBER** |
| **p\_gastos\_planificados** | **NUMBER** |
| **p\_ahorros\_planificados** | **NUMBER** |
| **p\_usuario\_creacion** | **VARCHAR2** |

**Uso en Python (front):**

**![][image11]**

#### 

8. #### **Listar presupuestos**

#### **Nombre: sp\_listar\_presupuestos\_usuario**

**Tipo:** Procedimiento (Consulta)

**Descripción:** Lista los presupuestos de un usuario, opcionalmente filtrados por el estado.

**Parámetros de entrada:**

| Parámetro | Tipo |
| ----- | ----- |
| **p\_id\_usuario** | **NUMBER** |
| **p\_estado** | **VARCHAR2 (opcional)** |
| **p\_resultado** | **SYS\_REFCURSOR** |

**Uso en Python (front):**

**![][image12]**

#### 

9. #### **Consultar presupuesto**

#### **Nombre: sp\_consultar\_presupuesto**

**Tipo:** Procedimiento (Consulta)

**Descripción:** Obtiene el detalle completo de un presupuesto.

**Uso en Python (front):**  
**![][image13]**

10. #### **Cerrar presupuesto**

#### **Nombre: sp\_cerrar\_presupuesto**

**Tipo:** Procedimiento (CRUD)

**Descripción:** Cierra un presupuesto activo.

**Parámetros de entrada:**

| Parámetro | Tipo |
| ----- | ----- |
| **p\_id\_presupuesto** | **NUMBER** |
| **p\_usuario\_modificacion** | **VARCHAR2** |

# 

### 

### **DETALLES DE PRESUPUESTO**

11. #### **Insertar presupuesto detalle**

#### **Nombre: sp\_insertar\_presupuesto\_detalle**

**Tipo:** Procedimiento (CRUD)

**Descripción:** Asigna un monto mensual a una subcategoría dentro del presupuesto.

**Parámetros de entrada:**

| Parámetro | Tipo |
| ----- | ----- |
| **p\_id\_presupuesto** | **NUMBER** |
| **p\_id\_subcategoria** | **NUMBER** |
| **p\_monto\_mensual** | **NUMBER** |
| **p\_observaciones** | **VARCHAR2** |

#### 

12. #### **Actualizar presupuesto detalle**

#### **Nombre: sp\_actualizar\_presupuesto\_detalle**

**Tipo:** Procedimiento (CRUD)

**Descripción:** Actualiza el monto asignado a una subcategoria del presupuesto.

**Parámetros de entrada:**

| Parámetro | Tipo |
| ----- | ----- |
| **p\_id\_presupuesto\_detalle** | **NUMBER** |
| **p\_monto\_mensual** | **NUMBER** |
| **p\_observaciones** | **VARCHAR2** |

#### 

13. #### **Listar detalles de presupuesto**

#### **Nombre: sp\_listar\_detalles\_presupuesto**

**Tipo:** Procedimiento (Consulta)

**Descripción:** Lista los detalles de un presupuesto

**Uso en Python:**

**![][image14]**

#### 

14. #### **Consultar presupuesto detalle**

#### **Nombre: sp\_consultar\_presupuesto\_detalle**

**Tipo:** Procedimiento (Consulta)

**Descripción:** Consulta un detalle específico del presupuesto.

### **OBLIGACIONES FIJAS**

15. #### **Insertar obligación fija**

#### **Nombre: sp\_insertar\_ogligacion\_fija**

**Tipo:** Procedimiento (Negocio)

**Descripción:** Registra una obligación mensual fija (ej. alquiler)

**Parámetros de entrada:**

| Parámetro | Tipo |
| ----- | ----- |
| p\_id\_usuario | NUMBER |
| p\_id\_subcategoria | NUMBER (GASTO) |
| p\_nombre | VARCHAR2 |
| p\_descripcion | VARCHAR2 |
| p\_monto\_mensual | NUMBER |
| p\_fecha\_inicio | DATE |
| p\_fecha\_vencimiento | DATE |
| p\_usuario\_creacion | VARCHAR2 |

16. #### **Actualizar obligación fija**

#### **Nombre: sp\_actualizar\_obligacion\_fija**

**Tipo:** Procedimiento (CRUD)

**Descripción:** Actualiza los datos de una obligación fija existente.

**Uso en Python:**

**![][image15]**

# 

17. #### **Desactivar obligación fija**

#### **Nombre: sp\_desactivar\_obligacion\_fija**

**Tipo:** Procedimiento (Negocio)

**Descripción:** Desactiva (borrado lógico) una obligación fija.

**Uso en Python:**

**![][image16]**

18. #### **Listar obligaciones de usuario**

#### **Nombre: sp\_listar\_obligaciones\_usuario**

**Tipo:** Procedimiento (Consulta)

**Descripción:** Lista las obligaciones fijas de un usuario.

**Uso en Python:**

**![][image17]**

19. #### **Consultar obligación fija**

#### **Nombre: sp\_consultar\_obligacion\_fija**

**Tipo:** Procedimiento (Consulta)

**Descripción:** Consulta el detalle de una obligación fija específica.

**Uso en Python:**

**![][image18]**

### **METAS DE AHORRO**

20. #### **Insertar meta ahorro**

#### **Nombre: sp\_insertar\_meta\_ahorro**

**Tipo:** Procedimiento (Negocio)

**Descripción:** Crea una meta de ahorro asociada a una subcategoría AHORRO

**Parámetros de entrada:**

| Parámetro | Tipo |
| ----- | ----- |
| **p\_id\_usuario** | **NUMBER** |
| **p\_id\_subcategoria** | **NUMBER** |
| **p\_nombre** | **VARCHAR2** |
| **p\_descripcion** | **VARCHAR2** |
| **p\_monto\_meta** | **NUMBER** |
| **p\_fecha\_inicio** | **DATE** |
| **p\_fecha\_objetivo** | **DATE** |
| **p\_prioridad** | **VARCHAR2** |
| **p\_usuario\_creacion** | **VARCHAR2** |

**Uso en Python:**  
**![][image19]**

21. #### **Cancelar meta ahorro**

#### **Nombre: sp\_cancelar\_meta\_ahorro**

**Tipo:** Procedimiento (Negocio)

**Descripción:** Cancela una meta de ahorro activa.

**Uso en Python:**  
**![][image20]**

22. #### **Listar metas ahorro**

#### **Nombre: sp\_listar\_metas\_usuario**

**Tipo:** Procedimiento (Negocio)

**Descripción:** Muestra las metas de ahorro del usuario.

**Uso en Python:**  
**![][image21]**

23. #### **Consultar meta ahorro**

#### **Nombre: sp\_consultar\_meta\_ahorro**

**Tipo:** Procedimiento (Negocio)

**Descripción:** Consulta los datos de una meta de ahorro.

**Uso en Python:**  
**![][image22]**

### **TRANSACCIONES**

24. #### **Registrar transacción completa**

#### **Nombre: sp\_registrar\_transaccion\_completa**

**Tipo:** Procedimiento (Negocio \- principal)

**Descripción:** Registra una transacción aplicando todas las reglas del sistema.

**Parámetros de entrada:**

| Parámetro | Tipo |
| ----- | ----- |
| **p\_id\_usuario** | **NUMBER** |
| **p\_id\_presupuesto** | **NUMBER** |
| **p\_fecha** | **DATE** |
| **p\_id\_subcategoria** | **NUMBER** |
| **p\_tipo\_transaccion** | **VARCHAR2** |
| **p\_monto** | **NUMBER** |
| **p\_descripcion** | **VARCHAR2** |
| **p\_metodo\_pago** | **VARCHAR2** |
| **p\_usuario\_creacion** | **VARCHAR2** |

**Uso en Python (front):**

**![][image23]**

25. #### **Listar transacciones de un presupuesto**

#### **Nombre: sp\_listar\_transacciones\_presupuesto**

**Tipo:** Procedimiento (Consulta)

**Descripción:** Lista las transacciones de un presupuesto.

**Uso en Python (front):**

**![][image24]**

26. #### **Consultar transacción**

#### **Nombre: sp\_consultar\_transaccion**

**Tipo:** Procedimiento (Consulta)

**Descripción:** Muestra los detalles de una transacción.

**Uso en Python (front):**

**![][image25]**

27. #### **Eliminar transacción**

#### **Nombre: sp\_eliminar\_transaccion**

**Uso en Python (front):**

**cursor.callproc(**  
    **"sp\_eliminar\_transaccion",**  
    **\[1\]**  
**)**  
**connection.commit()**

### **FUNCIONES DE CONSULTA (REPORTES)**

28. #### **Obtener balance del presupuesto**

#### **Nombre: fn\_balance\_presupuesto**

**Descripción:** Devuelve el balance del presupuesto

**Uso en Python (front):**

**![][image26]**

29. #### **Obtener avance de meta ahorro**

#### **Nombre: fn\_avance\_meta\_ahorro**

**Tipo:** Función	

**Descripción:** Devuelve el porcentaje de avance de una meta de ahorro.

**Uso en Python (front):**

**![][image27]**

30. ### **Total ingresos de un presupuesto**

#### **Nombre: fn\_total\_ingresos\_presupuesto**

**Uso en Python (front):**

**total\_ingresos \= cursor.callfunc(**  
    **"fn\_total\_ingresos\_presupuesto",**  
    **float,**  
    **\[1\]**  
**)**

31. #### **Obtener total de gastos de presupuesto**

#### **Nombre: fn\_totalgastos\_presupuesto**

**Uso en Python (front):**

**total\_gastos \= cursor.callfunc(**  
    **"fn\_total\_gastos\_presupuesto",**  
    **float,**  
    **\[1\]**  
**)**

32. #### **Obtener total ahorros presupuesto**

#### **Nombre: fn\_avance\_meta\_ahorro**

**Uso en Python (front):**

**total\_ahorros \= cursor.callfunc(**  
    **"fn\_total\_ahorros\_presupuesto",**  
    **float,**  
    **\[1\]**  
**)**

33. #### **Porcentaje de ejecución de subcategoria**

#### **Nombre: fn\_porcentaje\_ejecucion\_subcategoria**

**Uso en Python (front):**

**porcentaje \= cursor.callfunc(**  
    **"fn\_porcentaje\_ejecucion\_subcategoria",**  
    **float,**  
    **\[1, 5\]**  
**)**

34. #### **Total ejecutado categoría**

#### **Nombre: fn\_total\_ejecutado\_categoria**

**Uso en Python (front):**  
**total\_categoria \= cursor.callfunc(**  
    **"fn\_total\_ejecutado\_categoria",**  
    **float,**  
    **\[1, 2\]**  
**)**

## **8\. Triggers**

### **8.1 Tabla resumen de triggers**

| Trigger | Tabla asociada | Momento | Tipo | Descripción |
| ----- | ----- | ----- | ----- | ----- |
| TRG\_CATEGORIA\_SUBCAT\_DEF | CATEGORIAS / SUBCATEGORIAS | AFTER INSERT | Regla de negocio | Crea automáticamente una subcategoría por defecto al insertar una nueva categoría. |
| TRG\_NO\_TRANSACCION\_PRESUPUESTO\_CERRADO | TRANSACCIONES / PRESUPUESTOS | BEFORE INSERT | Validación | Evita registrar transacciones en presupuestos que no se encuentren en estado activo. |
| TRG\_TRANSACCION\_AHORRO\_META | TRANSACCIONES / METAS\_AHORROS | AFTER INSERT | Lógica de negocio | Actualiza automáticamente el avance de las metas de ahorro al registrar transacciones de tipo ahorro. |
| TRG\_TRANSACCIONES\_AUDIT\_UPD | TRANSACCIONES | BEFORE UPDATE | Auditoría | Actualiza automáticamente la fecha de modificación de una transacción. |

### **8.2 Justificación del uso de triggers**

El uso de triggers en el Sistema de Gestión de Presupuestos Personales se justifica por la necesidad de garantizar la integridad de los datos, la correcta aplicación de reglas de negocio críticas y la automatización de procesos directamente en la base de datos, independientemente de la capa de presentación o de la lógica de aplicación.

Dado que el sistema maneja información financiera sensible, resulta fundamental que ciertas validaciones y acciones no dependan exclusivamente de la aplicación cliente, sino que estén protegidas y controladas a nivel de base de datos. Los triggers permiten asegurar que estas reglas se ejecuten siempre que ocurran eventos específicos sobre las tablas, evitando inconsistencias y errores que podrían comprometer la confiabilidad de la información.

En primer lugar, los triggers se utilizan para reforzar reglas de negocio que no pueden ser violadas bajo ninguna circunstancia, como la restricción de registrar transacciones en presupuestos cerrados. Este tipo de validación es crítica, ya que garantiza que los datos financieros respeten el estado lógico del presupuesto, incluso si una inserción se realiza por medios distintos a la interfaz principal del sistema.

Asimismo, los triggers permiten la automatización de comportamientos derivados, como la creación automática de una subcategoría por defecto al insertar una nueva categoría. Esta lógica evita estados inconsistentes en el modelo de datos y asegura que toda categoría sea inmediatamente utilizable sin requerir acciones adicionales por parte del usuario o del desarrollador.

Otro uso importante de los triggers en el sistema es la actualización automática de información relacionada, como el avance de las metas de ahorro al registrar transacciones de tipo ahorro. Este enfoque centraliza el cálculo y la actualización del progreso directamente en la base de datos, garantizando coherencia entre las transacciones registradas y el estado actual de las metas, sin necesidad de cálculos redundantes en la aplicación.

Desde el punto de vista de la auditoría, los triggers permiten mantener actualizados los campos de control, como la fecha de modificación de los registros, de manera transparente y confiable. Esto asegura que toda modificación quede registrada correctamente, fortaleciendo la trazabilidad de los datos y facilitando futuras tareas de mantenimiento, validación o análisis histórico.

Finalmente, el uso de triggers contribuye a una arquitectura más robusta y profesional, donde la base de datos no se limita únicamente al almacenamiento de información, sino que actúa como un componente activo en la aplicación de reglas y validaciones. Este enfoque es coherente con prácticas utilizadas en sistemas reales de gestión financiera y contable, y refuerza el carácter académico y técnico del proyecto.

En conclusión, los triggers implementados permiten garantizar la consistencia, integridad y confiabilidad de la información financiera del sistema, automatizando procesos críticos y asegurando el cumplimiento de las reglas de negocio definidas, independientemente del origen de las operaciones realizadas sobre la base de datos.

## **9\. Backend en Python**

### **9.1 Descripción general del backend**

El backend del Sistema de Gestión de Presupuestos Personales fue desarrollado en Python y constituye la capa de lógica de negocio dentro de la arquitectura en tres capas del sistema. Su función principal es actuar como intermediario entre la interfaz gráfica desarrollada en Tkinter y la base de datos Oracle, coordinando el flujo de información, aplicando validaciones básicas y ejecutando las operaciones correspondientes mediante procedimientos almacenados.

El backend no accede directamente a las tablas de la base de datos para operaciones críticas, sino que delega estas acciones a procedimientos almacenados, garantizando que las reglas de negocio y la integridad de los datos se mantengan centralizadas en la base de datos.

### **9.2 Conexión con la base de datos**

La comunicación con la base de datos Oracle se realiza mediante la librería oracledb, utilizando una función centralizada de conexión:

![][image28]

Esta función encapsula la lógica de conexión, permitiendo reutilizarla en todas las operaciones del sistema. En caso de error, el backend captura la excepción y notifica al usuario mediante mensajes visuales, evitando que el sistema falle de forma abrupta.

Este enfoque permite:

* Centralizar la configuración de la conexión.

* Facilitar el mantenimiento y posibles cambios futuros.

* Garantizar un manejo controlado de errores de base de datos.

### **9.3 Gestión de sesión**

El backend implementa un manejo básico de sesión mediante variables globales:

* SESSION\_USUARIO\_ID

* SESSION\_USUARIO\_NOMBRE

* SESSION\_PRESUPUESTO\_ID

Estas variables permiten mantener el contexto del usuario autenticado durante la ejecución del sistema, facilitando la asociación correcta de presupuestos, transacciones, metas de ahorro y obligaciones fijas con el usuario activo.

Este mecanismo, aunque simple, resulta adecuado para el alcance académico del proyecto y permite simular el comportamiento de un sistema con sesiones persistentes.

### **9.4 Gestión de usuarios**

El backend incluye funciones para el registro y validación de usuarios, las cuales interactúan directamente con procedimientos almacenados en la base de datos:

* Registro de nuevos usuarios mediante sp\_insertar\_usuario

* Validación de usuarios activos mediante sp\_validar\_usuario

Antes de realizar cualquier operación, el backend ejecuta validaciones básicas sobre los datos ingresados, como campos obligatorios y formatos correctos. La lógica de validación crítica (existencia, estado activo) se delega a la base de datos.

Este enfoque garantiza:

* Separación clara entre validación básica y reglas de negocio.

* Mayor seguridad y consistencia de los datos.

* Simulación de un sistema real de autenticación.

### **9.5 Gestión de presupuestos**

El backend permite la creación y gestión de presupuestos mediante funciones que:

* Reciben los datos ingresados por el usuario.

* Realizan conversiones seguras de tipos numéricos y fechas.

* Validan la coherencia de los periodos de inicio y fin.

* Ejecutan el procedimiento almacenado sp\_insertar\_presupuesto.

Además, el backend controla el estado del presupuesto antes de permitir el registro de transacciones, reforzando a nivel de aplicación las reglas que posteriormente son validadas también en la base de datos.

### **9.6 Gestión de transacciones**

El registro de transacciones es una de las funcionalidades centrales del backend. Para ello, el sistema:

* Valida el formato de fechas.

* Verifica que el presupuesto asociado se encuentre activo.

* Envía la información al procedimiento almacenado sp\_insertar\_transaccion.

El backend no calcula saldos ni actualiza metas directamente, ya que estas responsabilidades se encuentran delegadas a triggers y procedimientos en la base de datos, garantizando consistencia global independientemente del origen de la transacción.

### **9.7 Gestión de categorías y subcategorías**

El backend permite la creación y consulta de categorías mediante funciones que llaman a procedimientos almacenados como sp\_insertar\_categoria y sp\_listar\_categorias.  
 La creación automática de subcategorías por defecto no se gestiona en Python, sino que se realiza mediante triggers en la base de datos, reduciendo la complejidad de la capa de aplicación y reforzando la integridad del modelo.

### 

### **9.8 Gestión de obligaciones fijas y metas de ahorro**

El backend implementa funciones específicas para:

* Registrar obligaciones fijas, validando fechas y montos.

* Registrar metas de ahorro, verificando campos obligatorios y formatos.

* Delegar el cálculo del progreso de las metas a la base de datos.

Este diseño permite que la aplicación se limite a capturar y enviar información, mientras que la lógica financiera compleja se mantiene centralizada en la base de datos.

### **9.9 Generación de reportes**

El backend incluye funcionalidades para la generación de reportes básicos mediante consultas SQL, tales como:

* Gastos por categoría.

* Resumen general de ingresos, gastos y ahorros.

* Listado de metas de ahorro activas.

Estos reportes se presentan en la interfaz gráfica y sirven como complemento visual al análisis financiero realizado posteriormente mediante herramientas externas como Power BI.

### **9.10 Consideraciones finales del backend**

El backend desarrollado en Python cumple el rol de orquestador del sistema, coordinando la interacción entre la interfaz gráfica y la base de datos sin duplicar reglas de negocio ni comprometer la integridad de la información. Su diseño modular, basado en funciones claramente definidas, facilita la comprensión del sistema y su mantenimiento, al mismo tiempo que se alinea con prácticas utilizadas en sistemas reales de gestión financiera

## **10\. Interfaz gráfica del sistema (Tkinter)**

### **10..1 Descripción general de la interfaz gráfica**

La interfaz gráfica del Sistema de Gestión de Presupuestos Personales fue desarrollada utilizando Tkinter, la biblioteca estándar de Python para la creación de interfaces gráficas de escritorio. Esta interfaz constituye la capa de presentación del sistema y es el medio principal mediante el cual el usuario interactúa con las funcionalidades del sistema.

El diseño de la interfaz se orienta a ofrecer una experiencia clara y estructurada, permitiendo al usuario navegar entre las distintas funcionalidades sin necesidad de conocimientos técnicos. La interfaz se comunica exclusivamente con la capa lógica del sistema (backend en Python), evitando el acceso directo a la base de datos y manteniendo una separación adecuada de responsabilidades.

### **10.2 Estructura general de ventanas**

La interfaz gráfica se organiza en ventanas independientes, cada una asociada a un módulo funcional específico del sistema. Este enfoque facilita la navegación, mejora la legibilidad del código y permite aislar cada funcionalidad de forma clara.

Las principales ventanas implementadas son:

* Ventana de inicio

* Ventana de registro de usuarios

* Ventana de inicio de sesión

* Menú principal

* Ventana de gestión de presupuestos

* Ventana de transacciones

* Ventana de categorías

* Ventana de obligaciones fijas

* Ventana de metas de ahorro

* Ventana de reportes

Cada ventana se implementa como un objeto Toplevel, lo que permite mantener múltiples vistas abiertas sin cerrar la aplicación principal.

 

### **10..3 Ventana de inicio y autenticación**

La ventana de inicio actúa como punto de entrada al sistema, ofreciendo al usuario las opciones de crear una cuenta, iniciar sesión o salir de la aplicación. Esta ventana tiene un diseño simple y directo, reduciendo la fricción inicial del usuario.

Las ventanas de registro e inicio de sesión permiten capturar los datos necesarios para autenticar al usuario. En estas ventanas se realizan validaciones básicas de campos obligatorios antes de enviar la información al backend, el cual se encarga de ejecutar los procedimientos almacenados correspondientes para el registro y validación del usuario.

 

### **10.4 Menú principal**

El menú principal funciona como el núcleo de navegación del sistema. Desde esta ventana, el usuario puede acceder a todas las funcionalidades principales mediante botones claramente identificados.

Entre las opciones disponibles se encuentran:

* Gestión de presupuestos

* Registro de transacciones

* Administración de categorías

* Gestión de obligaciones fijas

* Gestión de metas de ahorro

* Visualización de reportes

* Cierre de sesión

El menú principal también muestra información contextual, como el nombre del usuario que ha iniciado sesión, reforzando la noción de sesión activa dentro del sistema.

 

### **10.5 Formularios de captura de información**

La mayoría de las ventanas del sistema utilizan formularios para la captura de información financiera. Estos formularios están compuestos por:

* Etiquetas descriptivas (Label)

* Campos de entrada (Entry)

* Botones de acción (Button)

Antes de enviar los datos al backend, la interfaz realiza validaciones mínimas, como la verificación de campos obligatorios y formatos básicos de fecha o valores numéricos. Este enfoque mejora la experiencia del usuario y reduce errores comunes de entrada de datos. Jojojo creo que nadie se dará cuenta si pongo un pequeño easter egg en medio de todo el documento, o si? Bromas inge. En el grupo de la clase mencionaron que mientras más llena estaba la documentación más probabilidades de recibir un buen puntaje teniamos, asi que aqui esta esta documentación de más de 100 páginas y personalmente creo que demasiado completa, tanto como para que alguien normal la lea completa siendo sincero. 

### **11.6 Gestión visual de datos**

Para la visualización de información estructurada, como listas de categorías o reportes, la interfaz utiliza el componente Treeview de la librería ttk. Este componente permite mostrar información en formato tabular, facilitando la lectura y comprensión de los datos.

Además, se implementan barras de desplazamiento (Scrollbar) para manejar volúmenes de información mayores, asegurando que la interfaz se mantenga usable incluso con un número elevado de registros.

### **11.7 Mensajes y retroalimentación al usuario**

La interfaz gráfica proporciona retroalimentación constante al usuario mediante cuadros de diálogo (messagebox), los cuales informan sobre:

* Operaciones exitosas

* Errores de validación

* Errores de conexión o base de datos

* Restricciones de negocio (por ejemplo, presupuestos cerrados)

Esta comunicación directa mejora la usabilidad del sistema y permite al usuario comprender el resultado de sus acciones sin ambigüedades.

### **10.8 Diseño visual y experiencia de usuario**

El diseño visual de la interfaz utiliza una paleta de colores oscuros y contrastantes, lo que mejora la legibilidad y reduce la fatiga visual. Se emplean estilos consistentes para botones, etiquetas y formularios, reforzando una identidad visual uniforme en todo el sistema.

Aunque el diseño no pretende competir con interfaces comerciales, cumple adecuadamente su función académica y funcional, priorizando la claridad, la organización y la facilidad de uso.

### **10.9 Relación con la arquitectura del sistema**

La interfaz gráfica se comunica exclusivamente con el backend en Python, el cual a su vez interactúa con la base de datos mediante procedimientos almacenados. Esta separación garantiza que la interfaz no contenga lógica de negocio ni validaciones críticas, alineándose con la arquitectura en tres capas definida para el sistema.

Cualquier cambio en la lógica del sistema o en la base de datos puede realizarse sin afectar directamente la interfaz, siempre que se mantengan los contratos de comunicación definidos.

###  

### **10.10 Consideraciones finales de la interfaz gráfica**

La interfaz gráfica desarrollada con Tkinter cumple de manera efectiva su rol como capa de presentación del Sistema de Gestión de Presupuestos Personales. Su diseño modular, su integración con el backend y su enfoque en la experiencia del usuario permiten una interacción clara y ordenada con el sistema, facilitando el registro, análisis y visualización de la información financiera.

## **11\. Reportes y visualización de datos**

### **11.1 Introducción a los reportes**

El sistema de gestión de presupuestos personales no se limita únicamente al registro y almacenamiento de información financiera, sino que también contempla la visualización y análisis de los datos como un componente clave para la toma de decisiones.  
 Para este propósito, se utilizaron reportes generados con Power BI, los cuales permiten transformar grandes volúmenes de datos financieros en información clara, resumida y visualmente comprensible.

Los reportes fueron construidos a partir de datasets estructurados que representan transacciones, categorías y periodos de tiempo, permitiendo analizar el comportamiento financiero del usuario desde distintas perspectivas.

## **11.2 Herramienta utilizada: Power BI**

Power BI fue seleccionado como herramienta de visualización por las siguientes razones:

* Permite una integración sencilla con datasets en formato estructurado (CSV).

* Facilita la creación de gráficos interactivos sin necesidad de programación avanzada.

* Es ampliamente utilizada en entornos profesionales para análisis de datos.

* Permite representar grandes volúmenes de información de manera resumida y clara.

El uso de Power BI complementa el sistema, ya que permite analizar la información financiera sin afectar el rendimiento ni la lógica interna del sistema principal.

## **11..3 Reporte 1: Gastos por categoría**

### **Descripción del reporte**

El primer reporte presenta la **distribución de los gastos del usuario por categoría**, permitiendo identificar en qué áreas se concentra el mayor consumo de recursos financieros.

Este reporte se construyó utilizando una gráfica de barras/dona, donde cada categoría representa una porción del gasto total. El reporte permite visualizar rápidamente cuáles categorías tienen mayor impacto en el presupuesto del usuario.

### **Objetivo del reporte**

* Identificar las categorías con mayor gasto acumulado.

* Facilitar la detección de patrones de consumo.

* Apoyar la toma de decisiones relacionadas con la reducción o redistribución del gasto.

### **Información visualizada**

* Categoría

* Monto total gastado

* Porcentaje del gasto total

📎 **Evidencia:**

**![][image29]**  
 *Fuente: Elaboración propia mediante Power BI.*

## **11.4 Reporte 2: Resumen financiero general**

### **Descripción del reporte**

El segundo reporte presenta un resumen financiero general, comparando los ingresos, gastos y ahorros del usuario en un periodo determinado. Este reporte ofrece una visión global del estado financiero y permite evaluar si el usuario mantiene un balance positivo.

El reporte se apoya en gráficos combinados y tarjetas de indicadores, mostrando totales acumulados y comparaciones claras entre los distintos tipos de movimientos financieros.

### **Objetivo del reporte**

* Analizar la relación entre ingresos y gastos.

* Identificar si el usuario mantiene un balance financiero saludable.

* Evaluar el nivel de ahorro alcanzado en el periodo analizado.

### **Información visualizada**

* Total de ingresos

* Total de gastos

* Total de ahorros

* Balance financiero general

📎 **Evidencia:**

**![][image30]**  
 *Fuente: Elaboración propia mediante Power BI*

## **11.5 Importancia de los reportes en el sistema**

Los reportes generados permiten convertir datos financieros en **información útil**, facilitando la interpretación del comportamiento económico del usuario. A diferencia de los listados tradicionales, las visualizaciones gráficas permiten identificar tendencias, patrones y posibles áreas de mejora de forma rápida e intuitiva.

Además, el uso de Power BI demuestra la capacidad del sistema para integrarse con herramientas de análisis externas, reforzando su valor académico y su aplicabilidad en escenarios reales de análisis financiero.

 

## **11.6 Consideraciones finales sobre los reportes**

Los reportes desarrollados cumplen una función complementaria al sistema principal, proporcionando una visión analítica de la información financiera almacenada. Aunque los datos utilizados pueden ser simulados con fines académicos, la estructura y el análisis realizados reflejan escenarios reales de gestión financiera personal.

La incorporación de Power BI como herramienta de visualización fortalece el proyecto, demostrando la importancia del análisis de datos como parte integral de un sistema de información moderno.

## **12\. Manejo de errores**

## **12.1 Introducción al manejo de errores**

El manejo de errores es un componente esencial en el desarrollo de sistemas de información, especialmente cuando se trabaja con bases de datos relacionales que aplican restricciones de integridad y reglas de negocio. En el Sistema de Gestión de Presupuestos Personales, se implementó un manejo de errores orientado a detectar, controlar y comunicar adecuadamente los fallos que pueden ocurrir durante la ejecución de operaciones sobre la base de datos Oracle.

El sistema contempla tanto errores estándar de Oracle como errores personalizados, los cuales son capturados en la capa de backend y comunicados al usuario de manera comprensible a través de la interfaz gráfica.

## **12.2 Error ORA-02291 – Violación de clave foránea**

### **Descripción del error**

El error ORA-02291: integrity constraint violated \- parent key not found ocurre cuando se intenta insertar o actualizar un registro que hace referencia a una clave foránea inexistente en la tabla padre.

En el contexto del sistema, este error puede presentarse, por ejemplo, al intentar registrar una transacción asociada a un usuario, presupuesto, categoría o subcategoría que no existe o que ha sido desactivada.

### **Manejo en el sistema**

Este error es gestionado principalmente a nivel de base de datos mediante restricciones de integridad referencial. Cuando ocurre, el backend captura la excepción y muestra un mensaje claro al usuario, indicando que la información relacionada no existe o no es válida.

Este manejo evita:

* Registros huérfanos en la base de datos.

* Inconsistencias entre entidades relacionadas.

* Fallos silenciosos que comprometan la integridad del sistema.

## **12.3 Error ORA-01400 – Inserción de valores nulos**

### **Descripción del error**

El error ORA-01400: cannot insert NULL into se produce cuando se intenta insertar un valor nulo en una columna definida como obligatoria (NOT NULL).

En el sistema, este error puede presentarse si el usuario no completa campos obligatorios en formularios como:

* Registro de usuarios

* Creación de presupuestos

* Registro de transacciones

* Definición de metas de ahorro u obligaciones fijas

### **Manejo en el sistema**

El sistema aplica un manejo preventivo y reactivo:

* **Preventivo:**  
   La interfaz gráfica valida que los campos obligatorios estén completos antes de enviar la información al backend.

* **Reactivo:**  
   En caso de que el error ocurra en la base de datos, el backend captura la excepción y muestra un mensaje informativo al usuario, indicando que existen campos obligatorios sin completar.

Este enfoque doble mejora la experiencia del usuario y refuerza la integridad de los datos.

## **12.4 Error ORA-20200 – Error personalizado de negocio**

### **Descripción del error**

El error ORA-20200 corresponde a un error personalizado, definido explícitamente en procedimientos almacenados o triggers mediante la instrucción RAISE\_APPLICATION\_ERROR. Este tipo de error se utiliza para comunicar violaciones a reglas de negocio que no pueden ser expresadas únicamente mediante restricciones estructurales.

En el sistema, este error se utiliza para situaciones como:

* Intentar registrar transacciones en presupuestos cerrados.

* Violaciones a reglas de vigencia de presupuestos.

* Inconsistencias en la relación entre transacciones, metas de ahorro u obligaciones fijas.

### **Manejo en el sistema**

Cuando se produce un error ORA-20200, el backend captura el mensaje definido en la base de datos y lo presenta al usuario de forma clara, permitiendo comprender la razón exacta por la cual la operación fue rechazada.

Este enfoque permite:

* Centralizar las reglas de negocio en la base de datos.

* Proporcionar mensajes específicos y contextualizados.

* Evitar la duplicación de lógica en la capa de aplicación.

## **12.5 Comunicación de errores al usuario**

Todos los errores capturados por el backend son comunicados al usuario mediante cuadros de diálogo en la interfaz gráfica. Los mensajes están diseñados para ser claros y comprensibles, evitando exponer detalles técnicos innecesarios, pero proporcionando suficiente información para corregir la acción realizada.

Este enfoque mejora la usabilidad del sistema y reduce la frustración del usuario ante errores comunes.

## **12.6 Importancia del manejo de errores en el sistema**

El manejo adecuado de errores permite que el sistema sea más robusto, confiable y fácil de mantener. Al anticipar y controlar errores tanto estructurales como lógicos, el sistema garantiza que la información financiera almacenada sea consistente y que las reglas de negocio se respeten en todo momento.

Además, la inclusión de errores personalizados demuestra una comprensión avanzada del uso de Oracle como motor de base de datos y refuerza el carácter profesional y académico del proyecto.

## **13\. Limitaciones del sistema**

A pesar de que el Sistema de Gestión de Presupuestos Personales cumple con los objetivos planteados y ofrece una solución funcional para la administración y análisis de información financiera, es importante reconocer una serie de limitaciones propias de su alcance académico, las tecnologías utilizadas y las decisiones de diseño adoptadas durante su desarrollo.

### **13.1 Limitaciones tecnológicas**

El sistema fue desarrollado como una aplicación de escritorio utilizando Tkinter, lo que implica que su ejecución está limitada a entornos locales. No se cuenta con acceso remoto ni con una arquitectura web o cliente-servidor distribuida, lo que restringe su uso a un único equipo por sesión.

Asimismo, el uso de Oracle como motor de base de datos, aunque robusto y profesional, requiere una configuración previa y conocimientos técnicos para su instalación y administración, lo cual puede limitar su adopción en entornos no académicos o por usuarios sin experiencia técnica.

## **13.2 Limitaciones funcionales**

El sistema está orientado a la gestión financiera de un usuario a la vez por sesión, por lo que no contempla escenarios de uso simultáneo por múltiples usuarios concurrentes.

Adicionalmente, el sistema no incluye funcionalidades avanzadas como:

* Predicción de gastos o ingresos futuros.

* Recomendaciones financieras automáticas.

* Análisis avanzado basado en inteligencia artificial.

* Integración con instituciones bancarias o plataformas de pago.

Estas funcionalidades fueron consideradas fuera del alcance del proyecto.

## **13.3 Limitaciones de seguridad**

Aunque el sistema implementa controles básicos de seguridad y auditoría, no se incluyen mecanismos avanzados como:

* Encriptación de contraseñas.

* Autenticación multifactor.

* Gestión de roles y permisos detallados.

* Protección avanzada contra accesos no autorizados.

Estas medidas no fueron implementadas debido al enfoque académico del proyecto y a las restricciones de tiempo y alcance establecidas.

## **13.4 Limitaciones en la visualización de datos**

Los reportes generados mediante **Power BI** se realizan utilizando datasets exportados y no están integrados de forma dinámica con la base de datos del sistema. Esto implica que los reportes no se actualizan en tiempo real y requieren la generación manual de los datos para su análisis.

Además, los reportes tienen un enfoque descriptivo y no predictivo, limitándose a representar información histórica.

## **13.5 Limitaciones de usabilidad**

La interfaz gráfica, aunque funcional y clara, presenta limitaciones en cuanto a personalización y diseño visual avanzado. No se incluyen opciones como:

* Temas personalizables.

* Adaptación a distintos tamaños de pantalla.

* Accesibilidad avanzada para usuarios con discapacidades.

Estas características podrían mejorar la experiencia del usuario, pero no fueron prioritarias dentro del alcance del proyecto.

## **13.6 Consideraciones finales sobre las limitaciones**

Las limitaciones identificadas no afectan el cumplimiento de los objetivos académicos del proyecto, sino que delimitan de manera clara el contexto en el que el sistema fue desarrollado. Reconocer estas limitaciones permite identificar oportunidades de mejora y posibles extensiones futuras, así como demostrar una comprensión realista del alcance y las capacidades del sistema.

## **14\. Posibles mejoras futuras**

El Sistema de Gestión de Presupuestos Personales establece una base funcional sólida para la administración y análisis de información financiera. No obstante, existen múltiples oportunidades de mejora que podrían implementarse en futuras versiones del sistema para ampliar sus capacidades, mejorar la experiencia del usuario y acercarlo a un entorno de producción real.

## **14.1 Evolución hacia una arquitectura web**

Una de las principales mejoras futuras sería la migración del sistema hacia una arquitectura web, utilizando un backend basado en servicios y una interfaz accesible desde el navegador. Esto permitiría el acceso remoto al sistema, la gestión de múltiples usuarios concurrentes y una mayor escalabilidad.

La lógica de negocio actualmente centralizada en la base de datos y el backend facilita esta transición, ya que la separación de capas ya se encuentra definida.

## **14.2 Integración en tiempo real con herramientas de análisis**

Actualmente, los reportes se generan a partir de datasets exportados. Una mejora futura sería la integración directa con herramientas de análisis, permitiendo la actualización automática de los reportes a partir de la base de datos, ya sea mediante conexiones en vivo o procesos de sincronización periódicos.

Esto permitiría análisis en tiempo real y una toma de decisiones más inmediata.

## **14.3 Implementación de alertas financieras**

Aunque el módulo de alertas fue excluido de la implementación actual por indicaciones académicas, su incorporación futura permitiría notificar al usuario sobre:

* Excesos de gasto respecto al presupuesto.

* Vencimientos de obligaciones fijas.

* Avance o incumplimiento de metas de ahorro.

El diseño actual del sistema facilita esta mejora, ya que las reglas de negocio y la estructura de datos necesarias ya se encuentran definidas.

## **14.4 Mejora de la seguridad del sistema**

En futuras versiones, se podrían implementar mecanismos de seguridad más avanzados, tales como:

* Encriptación de contraseñas.

* Autenticación basada en roles.

* Control de permisos por usuario.

* Registro detallado de accesos al sistema.

Estas mejoras permitirían elevar el sistema a un nivel más cercano a entornos productivos reales.

## **14.5 Automatización de transacciones recurrentes**

Otra mejora relevante sería la automatización del registro de transacciones asociadas a obligaciones fijas, generando automáticamente los movimientos correspondientes según su periodicidad. Esto reduciría la intervención manual del usuario y aumentaría la precisión del registro financiero.

## **14.6 Análisis avanzado y predicción financiera**

A largo plazo, el sistema podría incorporar funcionalidades de análisis avanzado, tales como:

* Proyección de gastos e ingresos futuros.

* Identificación de patrones de consumo.

* Recomendaciones financieras personalizadas.

Estas mejoras podrían apoyarse en técnicas de análisis estadístico o aprendizaje automático, utilizando los datos históricos almacenados en el sistema.

## **14.7 Mejoras en la experiencia de usuario**

Finalmente, se podrían realizar mejoras orientadas a la experiencia del usuario, como:

* Diseño visual más moderno.

* Personalización de temas.

* Mejora en la navegación.

* Accesibilidad avanzada.

Estas mejoras permitirían una interacción más cómoda e intuitiva con el sistema.

## **14.8 Consideraciones finales**

Las mejoras propuestas no afectan la funcionalidad actual del sistema, sino que representan posibles evoluciones que podrían desarrollarse en futuras iteraciones. La estructura del sistema y las decisiones de diseño adoptadas permiten que estas mejoras sean viables sin necesidad de reconstruir la solución desde cero.

## **15\. Conclusiones**

El desarrollo del Sistema de Gestión de Presupuesto Personal permitió la integración funcional y coherente de los conocimientos adquiridos en diferentes asignaturas de la carrera, especialmente los relacionados con bases de datos, programación y análisis de información. Durante la ejecución del proyecto, se logró construir una solución funcional a un problema real, como la gestión de las finanzas personales, aplicando los principios de diseño y las buenas prácticas propias de los sistemas de información.

Algunas de las conclusiones clave derivadas del proyecto se relacionan con la centralización de las reglas de negocio en la base de datos. El uso de procedimientos almacenados y disparadores permitió garantizar la precisión, consistencia y fiabilidad de los datos financieros, independientemente de la capa desde la que se realizaran las operaciones. Esto contribuyó a reducir las duplicaciones en la lógica de la aplicación y mejoró la robustez general del sistema.

Mediante la adopción de una arquitectura de tres niveles, se estableció una clara separación de responsabilidades entre la interfaz gráfica, la lógica de negocio y los niveles de datos. Esta estructura no solo mejoró la organización del código, sino que también facilitó la comprensión del flujo de información dentro del sistema y sentó las bases para futuras mejoras o ampliaciones.

Python como lenguaje backend, junto con Tkinter para la interfaz gráfica de usuario (GUI), resultó ser adecuado para un proyecto académico. Este desarrollo permitió crear una aplicación funcional y fácil de entender que podía interactuar con una base de datos robusta como Oracle sin comprometer la claridad del diseño ni la experiencia del usuario.

Por otro lado, la integración de informes y visualizaciones mediante Power BI demostró cómo el análisis de datos aportaba valor al registro de información. La capacidad de convertir datos financieros en representaciones visuales claras mejoró la visión del comportamiento financiero para el usuario y reforzó la utilidad del sistema para la toma de decisiones. Finalmente, el proyecto permitió comprender que el desarrollo de un sistema de información va más allá del desarrollo de funcionalidades visibles: comprender cómo tratar errores, auditar la información, definir reglas de negocio e identificar limitaciones son aspectos importantes para construir soluciones sólidas y sostenibles que se adapten a escenarios reales. El sistema desarrollado, en su conjunto, cumple con los objetivos propuestos y representa una experiencia integral de aprendizaje en el desarrollo de sistemas de información enfocados en la gestión financiera.

## **16\. Anexos**

### **16.1 Código main en Python:**

import tkinter as tk

from tkinter import ttk, messagebox

from datetime import datetime

import oracledb

from datetime import date

import oracledb

\# \---------------- SESIÓN ACTIVA \----------------

SESSION\_USUARIO\_ID \= None

SESSION\_USUARIO\_NOMBRE \= None

SESSION\_PRESUPUESTO\_ID \= None

def conectar\_oracle():

   try:

       connection \= oracledb.connect(

           user="SisGestPresupuestos",

           password="1234",

           dsn="localhost/XEPDB1"

       )

       return connection

   except oracledb.DatabaseError as e:

       messagebox.showerror("Error", str(e))

       return None

def registrar\_usuario(nombre, apellido, correo, salario):

   conn \= conectar\_oracle()

   if conn is None:

       return False

   try:

       cursor \= conn.cursor()

       if not nombre or not apellido or not correo or not salario:

           messagebox.showerror(

               "Error",

               "Nombre, apellido, correo y salario son obligatorios."

           )

           return False

       cursor.callproc(

           "sp\_insertar\_usuario",

           \[

               nombre,

               apellido,

               correo,

               float(salario),

               "admin"

           \]

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

           f"Error al registrar el usuario:\\n{e}"

       )

       return False

   finally:

       cursor.close()

       conn.close()

      

\# Ventana para registrar el usuario

def ventana\_registro():

   reg \= tk.Toplevel()

   reg.title("Registrar Usuario")

   reg.geometry("350x430")

   reg.configure(bg="\#020617")

   tk.Label(

       reg, text="Registro de Usuario",

       font=("Segoe UI", 14, "bold"),

       fg="\#e5e7eb",

       bg="\#020617"

   ).pack(pady=10)

   form \= tk.Frame(reg, bg="\#020617")

   form.pack(pady=5)

   \# Campos

   labels \= \["Nombre", "Apellido", "Correo", "Salario", "Contraseña"\]

   entries \= \[\]

   for idx, texto in enumerate(labels):

       tk.Label(form, text=texto, font=("Segoe UI", 9), fg="\#e5e7eb", bg="\#020617").grid(row=idx\*2, column=0, sticky="w")

       entry \= tk.Entry(form, show="\*" if texto \== "Contraseña" else "")

       entry.grid(row=idx\*2 \+ 1, column=0, pady=(0, 8), ipadx=60)

       entries.append(entry)

   def enviar\_registro():

       nombre, apellido, correo, edad, salario, password \= \[e.get() for e in entries\]

       ok \= registrar\_usuario(nombre, apellido, correo, edad, salario, password)

       if ok:

           ventana\_menu\_principal(nombre)

           reg.destroy()

   tk.Button(

       reg,

       text="Registrar",

       bg="\#22c55e",

       fg="white",

       bd=0,

       font=("Segoe UI", 10, "bold"),

       activebackground="\#16a34a",

       activeforeground="white",

       command=enviar\_registro

   ).pack(pady=15)

def ingreso\_usuario(correo, password):

   global SESSION\_USUARIO\_ID, SESSION\_USUARIO\_NOMBRE

   conn \= conectar\_oracle()

   if conn is None:

       return None

   try:

       cursor \= conn.cursor()

       nombre\_out \= cursor.var(str)

       activo\_out \= cursor.var(str)

       cursor.callproc(

           "sp\_validar\_usuario",

           \[

               correo.strip().lower(),

               nombre\_out,

               activo\_out

           \]

       )

       nombre \= nombre\_out.getvalue()

       activo \= activo\_out.getvalue()

       if nombre is None:

           messagebox.showerror("Error", "El usuario no existe.")

           return None

       if activo is None or activo.strip().upper() \!= 'Y':

           messagebox.showerror("Error", "El usuario está inactivo.")

           return None

       return nombre

   except oracledb.DatabaseError as e:

       messagebox.showerror(

           "Error",

           f"Error al iniciar sesión:\\n{e}"

       )

       return None

   finally:

       cursor.close()

       conn.close()

      

\# Ventana de login para ingresar al sistema

def ventana\_login():

   login \= tk.Toplevel()

   login.title("Iniciar Sesión")

   login.geometry("350x260")

   login.configure(bg="\#020617")

   tk.Label(

       login,

       text="Iniciar Sesión",

       font=("Segoe UI", 14, "bold"),

       fg="\#e5e7eb",

       bg="\#020617"

   ).pack(pady=10)

   form \= tk.Frame(login, bg="\#020617")

   form.pack(pady=5)

   tk.Label(form, text="Correo", font=("Segoe UI", 9), fg="\#e5e7eb", bg="\#020617").grid(row=0, column=0, sticky="w")

   entry\_correo \= tk.Entry(form)

   entry\_correo.grid(row=1, column=0, pady=(0, 10), ipadx=60)

   tk.Label(form, text="Contraseña", font=("Segoe UI", 9), fg="\#e5e7eb", bg="\#020617").grid(row=2, column=0, sticky="w")

   entry\_password \= tk.Entry(form, show="\*")

   entry\_password.grid(row=3, column=0, pady=(0, 10), ipadx=60)


   def enviar\_login():

       nombre \= ingreso\_usuario(entry\_correo.get(), entry\_password.get())

       if nombre:

           ventana\_menu\_principal(nombre)

           login.destroy()

   tk.Button(

       login,

       text="Entrar",

       bg="\#1d4ed8",

       fg="white",

       bd=0,

       font=("Segoe UI", 10, "bold"),

       activebackground="\#1e40af",

       activeforeground="white",

       command=enviar\_login

   ).pack(pady=15)

      

\# Función para registrar un presupuesto

def registrarPresupuesto(

   nombre\_presupuesto,

   anio\_inicio,

   mes\_inicio,

   anio\_fin,

   mes\_fin,

   ingresos,

   gastos,

   ahorro

):

   conn \= conectar\_oracle()

   if conn is None:

       return False

   try:

       cursor \= conn.cursor()

       \# Validaciones básicas

       if not nombre\_presupuesto:

           messagebox.showerror("Error", "El nombre del presupuesto es obligatorio")

           return False

       \# Conversión segura

       anio\_inicio \= int(anio\_inicio)

       mes\_inicio \= int(mes\_inicio)

       anio\_fin \= int(anio\_fin)

       mes\_fin \= int(mes\_fin)

       ingresos \= float(ingresos)

       gastos \= float(gastos)

       ahorro \= float(ahorro)

       fecha\_inicio \= date(anio\_inicio, mes\_inicio, 1)

       fecha\_fin \= date(anio\_fin, mes\_fin, 1)

       \# ⚠️ ID DE USUARIO (TEMPORAL PARA DEFENSA)

       id\_usuario \= 1  \# luego puedes hacerlo dinámico

       SESSION\_PRESUPUESTO\_ID \= cursor.lastrowid

       cursor.callproc(

           "sp\_insertar\_presupuesto",

           \[

               id\_usuario,

               nombre\_presupuesto,

               fecha\_inicio,

               fecha\_fin,

               ingresos,

               gastos,

               ahorro,

               "admin"

           \]

       )

       conn.commit()

       return True

   except (ValueError, TypeError):

       messagebox.showerror("Error", "Datos numéricos inválidos")

       return False

   except oracledb.DatabaseError as e:

       messagebox.showerror(

           "Error",

           f"Error al registrar el presupuesto:\\n{e}"

       )

       return False

   finally:

       cursor.close()

       conn.close()


\#Ventana Presupuesto

def ventana\_presupuesto():

   win \= tk.Toplevel()

   win.title("Registrar Presupuesto")

   win.geometry("650x500")

   win.configure(bg="\#020617")


   form \= tk.Frame(win, bg="\#020617")

   form.pack(pady=5)

   \# Campos de entrada

   labels \= \["Nombre del presupuesto", "Año de inicio", "Mes de inicio (1-12)", "Año de fin", "Mes de fin (1-12)", "Total de ingresos", "Total de gastos", "Total de ahorro"\]

   entries \= \[\]

   for idx, text in enumerate(labels):

       tk.Label(form, text=text, fg="white", bg="\#020617").grid(row=idx\*2, column=0, sticky="w")

       entry \= tk.Entry(form)

       entry.grid(row=idx\*2 \+ 1, column=0, pady=(0, 8), ipadx=60)

       entries.append(entry)

   def enviar\_presupuesto():

       nombre\_presupuesto, anio\_ini, mes\_ini, anio\_fin, mes\_fin, ingresos, gastos, ahorro \= \[entry.get() for entry in entries\]

       if registrarPresupuesto(nombre\_presupuesto, anio\_ini, mes\_ini, anio\_fin, mes\_fin, ingresos, gastos, ahorro):

           messagebox.showinfo("Presupuesto registrado", "Presupuesto registrado correctamente")

           for entry in entries:

               entry.delete(0, tk.END)

   \# BOTÓN GUARDAR TRANSACCIÓN (ASEGÚRATE QUE ESTÉ AQUÍ)

   btn\_guardar \= tk.Button(

       win,

       text="Guardar transacción",

       bg="\#22c55e",

       fg="white",

       bd=0,

       font=("Segoe UI", 10, "bold"),

       activebackground="\#16a34a",

       activeforeground="white",

       width=22,

       command=enviar\_transaccion

   )

   btn\_guardar.pack(pady=10)

   \# Función de regresar al menú principal

   def regresar\_menu():

       win.destroy()

       ventana\_menu\_principal("Usuario")  \# Cambia "Usuario" por el nombre real del usuario

   tk.Button(

       win,

       text="Regresar al Menú Principal",

       bg="\#2563eb",

       fg="white",

       bd=0,

       font=("Segoe UI", 10, "bold"),

       activebackground="\#1e40af",

       activeforeground="white",

       width=22,

       command=regresar\_menu

   ).pack(pady=10)

\# Función para registrar una transacción

from datetime import date

from datetime import date

from datetime import date

def verificar\_estado\_presupuesto(presupuesto\_id):

   conn \= conectar\_oracle()

   if conn is None:

       return False

   try:

       cursor \= conn.cursor()

       cursor.execute("""

           SELECT estado

           FROM presupuestos

           WHERE id\_presupuesto \= :presupuesto\_id

       """, {"presupuesto\_id": presupuesto\_id})

       resultado \= cursor.fetchone()

       if resultado is None:

           messagebox.showerror("Error", "El presupuesto no existe.")

           return False

       if resultado\[0\] \!= 'ACTIVO':

           messagebox.showerror("Error", "No se pueden registrar transacciones en presupuestos cerrados.")

           return False

       return True

   except oracledb.DatabaseError as e:

       messagebox.showerror("Error", f"Error al verificar el estado del presupuesto:\\n{e}")

       return False

   finally:

       cursor.close()

       conn.close()

from datetime import datetime

def registrar\_transaccion(

   id\_usuario,

   presupuesto\_id,

   fecha\_str,

   id\_subcategoria,

   tipo,

   descripcion,

   monto,

   metodo\_pago

):

   try:

       fecha \= datetime.strptime(fecha\_str, "%Y-%m-%d")

   except ValueError:

       messagebox.showerror(

           "Error",

           "La fecha debe tener el formato YYYY-MM-DD"

       )

       return False

   conn \= conectar\_oracle()

   cursor \= conn.cursor()

   cursor.callproc(

       "sp\_insertar\_transaccion",

       \[

           SESSION\_USUARIO\_ID,

           presupuesto\_id,

           fecha,

           id\_subcategoria,

           tipo,

           descripcion,

           monto,

           metodo\_pago,

           "admin"  \# usuario\_creacion

       \]

   )

   conn.commit()

   cursor.close()

   conn.close()

   return True

def ventana\_transacciones():

   print("\>\>\> ventana\_transacciones ejecutada")

   win \= tk.Toplevel()

   win.title("Registrar Transacción")

   win.geometry("650x550")

   win.configure(bg="\#020617")

   form \= tk.Frame(win, bg="\#020617")

   form.pack(pady=10)

   labels \= \[

       "Fecha (YYYY-MM-DD)",

       "ID Subcategoría",

       "Tipo (INGRESO/GASTO/AHORRO)",

       "Descripción",

       "Monto",

       "Método de pago"

   \]

   entries \= \[\]

   for i, text in enumerate(labels):

       tk.Label(form, text=text, fg="white", bg="\#020617")\\

           .grid(row=i\*2, column=0, sticky="w")

       e \= tk.Entry(form, width=40)

       e.grid(row=i\*2 \+ 1, column=0, pady=5)

       entries.append(e)

   def enviar\_transaccion():

       print("\>\>\> click guardar")

       fecha, id\_subcat, tipo, desc, monto, metodo \= \\

           \[e.get() for e in entries\]

       registrar\_transaccion(

           SESSION\_USUARIO\_ID,

           1,  \# presupuesto activo

           fecha,

           int(id\_subcat),

           tipo.upper(),

           desc,

           float(monto),

           metodo

       )

   \# 👇 BOTÓN GUARDA SIEMPRE

   tk.Button(

       win,

       text="Guardar Transacción",

       bg="\#22c55e",

       fg="white",

       font=("Segoe UI", 10, "bold"),

       width=25,

       command=enviar\_transaccion

   ).pack(pady=15)

   tk.Button(

       win,

       text="Regresar",

       bg="\#2563eb",

       fg="white",

       width=25,

       command=win.destroy

   ).pack(pady=5)


\#insertar categoria

def insertar\_categoria(nombre, descripcion, tipo\_categoria, icono, color):

   *"""Insertar una nueva categoría en la base de datos."""*

   conn \= conectar\_oracle()

   if conn is None:

       return False

   try:

       cursor \= conn.cursor()

       \# Verificación de los campos

       if not nombre or not tipo\_categoria:

           messagebox.showerror("Error", "Nombre y tipo de categoría son obligatorios.")

           return False

       \# Llamar al procedimiento de base de datos para insertar la categoría

       cursor.callproc("sp\_insertar\_categoria", \[nombre, descripcion, tipo\_categoria, icono, color, "admin"\])

      

       conn.commit()

       messagebox.showinfo("Categoría registrada", f"Categoría '{nombre}' registrada correctamente")

       return True

   except cx\_Oracle.DatabaseError as e:

       messagebox.showerror("Error", f"Error al registrar la categoría: {e}")

       return False

   finally:

       cursor.close()

       conn.close()

      

def ventana\_categoria():

   win \= tk.Toplevel()

   win.title("Registrar Categoría")

   win.geometry("650x500")

   win.configure(bg="\#020617")

   \# Encabezado

   tk.Label(

       win,

       text="Crear Categoría",

       font=("Segoe UI", 14, "bold"),

       fg="\#22c55e",

       bg="\#020617"

   ).pack(pady=10)

   \# Formulario de categoría

   form \= tk.Frame(win, bg="\#020617")

   form.pack(pady=5)

   \# Campos de entrada

   tk.Label(form, text="Nombre de la categoría:", fg="white", bg="\#020617").grid(row=0, column=0, sticky="w")

   entry\_categoria \= tk.Entry(form, width=30)

   entry\_categoria.grid(row=1, column=0, pady=(0, 8))

   tk.Label(form, text="Tipo de categoría (ingreso/gasto):", fg="white", bg="\#020617").grid(row=2, column=0, sticky="w")

   entry\_tipo\_categoria \= tk.Entry(form, width=30)

   entry\_tipo\_categoria.grid(row=3, column=0, pady=(0, 8))

   tk.Label(form, text="Descripción de la categoría:", fg="white", bg="\#020617").grid(row=4, column=0, sticky="w")

   entry\_descripcion \= tk.Entry(form, width=30)

   entry\_descripcion.grid(row=5, column=0, pady=(0, 8))

   tk.Label(form, text="Color de la categoría:", fg="white", bg="\#020617").grid(row=6, column=0, sticky="w")

   entry\_color \= tk.Entry(form, width=30)

   entry\_color.grid(row=7, column=0, pady=(0, 8))

   def guardar\_categoria():

       categoria \= entry\_categoria.get()

       tipo\_categoria \= entry\_tipo\_categoria.get()

       descripcion \= entry\_descripcion.get()

       color \= entry\_color.get()

       if categoria and tipo\_categoria:

           if insertar\_categoria(categoria, descripcion, tipo\_categoria, None, color):

               messagebox.showinfo("Categoría registrada", f"Categoría '{categoria}' registrada correctamente.")

               entry\_categoria.delete(0, tk.END)

               entry\_tipo\_categoria.delete(0, tk.END)

               entry\_descripcion.delete(0, tk.END)

               entry\_color.delete(0, tk.END)

               cargar\_categorias()  \# Recargar las categorías después de guardar

       else:

           messagebox.showerror("Error", "El nombre y el tipo de la categoría son obligatorios")

   tk.Button(

       win,

       text="Guardar categoría",

       bg="\#22c55e",

       fg="white",

       bd=0,

       font=("Segoe UI", 10, "bold"),

       activebackground="\#16a34a",

       activeforeground="white",

       width=22,

       command=guardar\_categoria

   ).pack(pady=5)

   \# Tabla de Categorías

   tabla\_frame \= tk.Frame(win, bg="\#020617")

   tabla\_frame.pack(pady=10, fill="both", expand=True)

   columnas \= ("ID", "Nombre", "Tipo", "Descripción", "Color")

   tabla \= ttk.Treeview(tabla\_frame, columns=columnas, show="headings", height=8)

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

   scrollbar \= ttk.Scrollbar(tabla\_frame, orient="vertical", command=tabla.yview)

   scrollbar.pack(side="right", fill="y")

   tabla.configure(yscrollcommand=scrollbar.set)

   \# Función para cargar las categorías

   def cargar\_categorias():

       conn \= conectar\_oracle()

       if conn is None:

           return

       try:

           cursor \= conn.cursor()

           \# Cursor de salida correcto con oracledb

           out\_cursor \= cursor.var(oracledb.CURSOR)

           cursor.callproc(

               "sp\_listar\_categorias",

               \[

                   None,  \# o 'INGRESO' / 'GASTO'

                   out\_cursor

               \]

           )

           \# Limpiar tabla

           for fila in tabla.get\_children():

               tabla.delete(fila)

           \# Insertar filas

           for categoria in out\_cursor.getvalue():

               tabla.insert(

                   "",

                   "end",

                   values=(

                       categoria\[0\],  \# id\_categoria

                       categoria\[1\],  \# nombre

                       categoria\[2\],  \# tipo\_categoria

                       categoria\[3\],  \# descripcion

                       categoria\[4\]  \# color

                   )

               )

       except oracledb.DatabaseError as e:

           messagebox.showerror(

               "Error",

               f"Error al cargar las categorías:\\n{e}"

           )

       finally:

           cursor.close()

           conn.close()

   win.after(100, cargar\_categorias)

   \# Función de regresar al menú principal

   def regresar\_menu():

       win.destroy()

       ventana\_menu\_principal("Usuario")

   tk.Button(

       win,

       text="Regresar al Menú Principal",

       bg="\#2563eb",

       fg="white",

       bd=0,

       font=("Segoe UI", 10, "bold"),

       activebackground="\#1e40af",

       activeforeground="white",

       width=22,

       command=regresar\_menu

   ).pack(pady=10)

from datetime import datetime

import oracledb

def insertar\_obligacion\_fija(

   id\_subcategoria,

   nombre,

   descripcion,

   monto\_mensual,

   fecha\_inicio\_str,

   fecha\_vencimiento\_str

):

   conn \= conectar\_oracle()

   if conn is None:

       return False

   try:

       \# Parsear fechas

       try:

           fecha\_inicio \= datetime.strptime(fecha\_inicio\_str, "%Y-%m-%d")

           fecha\_vencimiento \= datetime.strptime(fecha\_vencimiento\_str, "%Y-%m-%d")

       except ValueError:

           messagebox.showerror(

               "Error",

               "Las fechas deben tener el formato YYYY-MM-DD"

           )

           return False

       cursor \= conn.cursor()

       cursor.callproc(

           "sp\_insertar\_obligacion\_fija",

           \[

               SESSION\_USUARIO\_ID,      \# id\_usuario

               id\_subcategoria,

               nombre,

               descripcion,

               float(monto\_mensual),

               fecha\_inicio,

               fecha\_vencimiento,

               "admin"                  \# usuario\_creacion

           \]

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

           f"Error al registrar la obligación fija:\\n{e}"

       )

       return False

   finally:

       cursor.close()

       conn.close()

def ventana\_obligacion\_fija():

   win \= tk.Toplevel()

   win.title("Registrar Obligación Fija")

   win.geometry("650x500")

   win.configure(bg="\#020617")

   \# Encabezado

   tk.Label(

       win,

       text="Gestión de Obligaciones Fijas",

       font=("Segoe UI", 14, "bold"),

       fg="\#22c55e",

       bg="\#020617"

   ).pack(pady=10)

   \# Formulario

   form \= tk.Frame(win, bg="\#020617")

   form.pack(pady=5)

   \# Campos de entrada

   labels \= \["Nombre", "Descripción", "Monto Mensual", "Fecha de inicio", "Fecha de vencimiento"\]

   entries \= \[\]

   for idx, text in enumerate(labels):

       tk.Label(form, text=text, fg="white", bg="\#020617").grid(row=idx\*2, column=0, sticky="w")

       entry \= tk.Entry(form)

       entry.grid(row=idx\*2 \+ 1, column=0, pady=(0, 8), ipadx=60)

       entries.append(entry)

   def enviar\_obligacion():

       nombre, descripcion, monto\_mensual, fecha\_inicio, fecha\_vencimiento \= \[entry.get() for entry in entries\]

       if insertar\_obligacion\_fija(1, nombre, descripcion, monto\_mensual, fecha\_inicio, fecha\_vencimiento):  \# Subcategoria ID de ejemplo: 1

           messagebox.showinfo("Obligación registrada", "Obligación fija registrada correctamente")

           for entry in entries:

               entry.delete(0, tk.END)

   tk.Button(

       win,

       text="Guardar obligación fija",

       bg="\#22c55e",

       fg="white",

       bd=0,

       font=("Segoe UI", 10, "bold"),

       activebackground="\#16a34a",

       activeforeground="white",

       width=22,

       command=enviar\_obligacion

   ).pack(pady=5)

   \# Función de regresar al menú principal

   def regresar\_menu():

       win.destroy()

       ventana\_menu\_principal("Usuario")

   tk.Button(

       win,

       text="Regresar al Menú Principal",

       bg="\#2563eb",

       fg="white",

       bd=0,

       font=("Segoe UI", 10, "bold"),

       activebackground="\#1e40af",

       activeforeground="white",

       width=22,

       command=regresar\_menu

   ).pack(pady=10)

from datetime import datetime

import oracledb

def insertar\_meta\_ahorro(

   id\_subcategoria,

   nombre,

   descripcion,

   monto\_meta,

   fecha\_inicio\_str,

   fecha\_objetivo\_str,

   prioridad

):

   conn \= conectar\_oracle()

   if conn is None:

       return False

   try:

       \# Validaciones mínimas

       if not nombre or not monto\_meta or not fecha\_inicio\_str or not fecha\_objetivo\_str or not prioridad:

           messagebox.showerror(

               "Error",

               "Todos los campos son obligatorios."

           )

           return False

       \# Parseo de fechas

       try:

           fecha\_inicio \= datetime.strptime(fecha\_inicio\_str, "%Y-%m-%d")

           fecha\_objetivo \= datetime.strptime(fecha\_objetivo\_str, "%Y-%m-%d")

       except ValueError:

           messagebox.showerror(

               "Error",

               "Las fechas deben tener el formato YYYY-MM-DD"

           )

           return False

       cursor \= conn.cursor()

       cursor.callproc(

           "sp\_insertar\_meta\_ahorro",

           \[

               SESSION\_USUARIO\_ID,      \# id\_usuario

               id\_subcategoria,

               nombre,

               descripcion,

               float(monto\_meta),

               fecha\_inicio,

               fecha\_objetivo,

               prioridad.upper(),

               "admin"                  \# usuario\_creacion

           \]

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

           f"Error al registrar la meta de ahorro:\\n{e}"

       )

       return False

   finally:

       cursor.close()

       conn.close()

def ventana\_meta\_ahorro():

   win \= tk.Toplevel()

   win.title("Registrar Meta de Ahorro")

   win.geometry("650x500")

   win.configure(bg="\#020617")

   \# Encabezado

   tk.Label(

       win,

       text="Gestión de Metas de Ahorro",

       font=("Segoe UI", 14, "bold"),

       fg="\#22c55e",

       bg="\#020617"

   ).pack(pady=10)

   \# Formulario

   form \= tk.Frame(win, bg="\#020617")

   form.pack(pady=5)

   \# Campos de entrada

   labels \= \["Nombre", "Descripción", "Monto Meta", "Fecha de inicio", "Fecha de objetivo", "Prioridad"\]

   entries \= \[\]

   for idx, text in enumerate(labels):

       tk.Label(form, text=text, fg="white", bg="\#020617").grid(row=idx\*2, column=0, sticky="w")

       entry \= tk.Entry(form)

       entry.grid(row=idx\*2 \+ 1, column=0, pady=(0, 8), ipadx=60)

       entries.append(entry)

   def enviar\_meta():

       nombre, descripcion, monto\_meta, fecha\_inicio, fecha\_objetivo, prioridad \= \\

           \[entry.get() for entry in entries\]

       insertar\_meta\_ahorro(

           21,  \# id\_subcategoria (AHORRO)

           nombre,

           descripcion,

           monto\_meta,

           fecha\_inicio,

           fecha\_objetivo,

           prioridad

       )

   tk.Button(

       win,

       text="Guardar meta de ahorro",

       bg="\#22c55e",

       fg="white",

       bd=0,

       font=("Segoe UI", 10, "bold"),

       activebackground="\#16a34a",

       activeforeground="white",

       width=22,

       command=enviar\_meta

   ).pack(pady=5)

   \# Función de regresar al menú principal

   def regresar\_menu():

       win.destroy()

       ventana\_menu\_principal("Usuario")

   tk.Button(

       win,

       text="Regresar al Menú Principal",

       bg="\#2563eb",

       fg="white",

       bd=0,

       font=("Segoe UI", 10, "bold"),

       activebackground="\#1e40af",

       activeforeground="white",

       width=22,

       command=regresar\_menu

   ).pack(pady=10)

    


\# \---------------------- MENÚ PRINCIPAL \---------------------- \#

def ventana\_menu\_principal(nombre\_usuario):

   menu \= tk.Toplevel()

   menu.title("Sistema de Presupuesto \- Menú Principal")

   menu.geometry("480x520")

   menu.configure(bg="\#020617")

   \# Encabezado

   topbar \= tk.Frame(menu, bg="\#020617")

   topbar.pack(fill="x", pady=10, padx=15)

   tk.Label(

       topbar,

       text="Sistema de Presupuesto",

       font=("Segoe UI", 16, "bold"),

       fg="\#22c55e",

       bg="\#020617"

   ).pack(side="left")

   tk.Label(

       topbar,

       text=f"Sesión de {nombre\_usuario}",

       font=("Segoe UI", 9),

       fg="\#9ca3af",

       bg="\#020617"

   ).pack(side="right")

   main \= tk.Frame(menu, bg="\#020617")

   main.pack(pady=15)

   tk.Label(

       main,

       text="Menú principal",

       font=("Segoe UI", 12, "bold"),

       fg="\#e5e7eb",

       bg="\#020617"

   ).grid(row=0, column=0, columnspan=2, pady=(0, 15))

   def mk\_btn(texto, row, col, command=None):

       btn \= tk.Button(

           main,

           text=texto,

           width=22,

           height=2,

           bg="\#111827",

           fg="\#e5e7eb",

           bd=0,

           activebackground="\#1f2937",

           activeforeground="white",

           font=("Segoe UI", 9, "bold"),

           command=command

       )

       btn.grid(row=row, column=col, padx=10, pady=6)

       return btn

   mk\_btn("Presupuesto", 1, 0, lambda: ventana\_presupuesto())

   mk\_btn("Transacciones", 1, 1, lambda: ventana\_transacciones())

   mk\_btn("Categorías", 2, 0, lambda: ventana\_categoria())

   mk\_btn("Obligaciones Fijas", 2, 1, lambda: ventana\_obligacion\_fija())

   mk\_btn("Metas de Ahorro", 3, 0, lambda: ventana\_meta\_ahorro())

   mk\_btn("Reportes", 3, 1, lambda: ventana\_reportes())

   tk.Button(

       main,

       text="Cerrar sesión",

       width=22,

       height=2,

       bg="\#b91c1c",

       fg="white",

       bd=0,

       activebackground="\#7f1d1d",

       activeforeground="white",

       font=("Segoe UI", 9, "bold"),

       command=menu.destroy

   ).grid(row=4, column=1, padx=10, pady=15)

\# \---------------------- VENTANA REGISTRO \---------------------- \#

def ventana\_registro():

   reg \= tk.Toplevel()

   reg.title("Registrar Usuario")

   reg.geometry("350x500")

   reg.configure(bg="\#020617")

   tk.Label(

       reg, text="Registro de Usuario",

       font=("Segoe UI", 14, "bold"),

       fg="\#e5e7eb",

       bg="\#020617"

   ).pack(pady=10)

   form \= tk.Frame(reg, bg="\#020617")

   form.pack(pady=5)

   labels \= \["Nombre", "Apellido", "Correo", "Edad", "Salario", "Contraseña"\]

   entries \= \[\]

   for idx, texto in enumerate(labels):

       tk.Label(

           form,

           text=texto,

           font=("Segoe UI", 9),

           fg="\#e5e7eb",

           bg="\#020617"

       ).grid(row=idx\*2, column=0, sticky="w")

       entry \= tk.Entry(form, show="\*" if texto \== "Contraseña" else "")

       entry.grid(row=idx\*2 \+ 1, column=0, pady=(0, 8), ipadx=60)

       entries.append(entry)

   def enviar\_registro():

       nombre \= entries\[0\].get()

       apellido \= entries\[1\].get()

       correo \= entries\[2\].get()

       \# entries\[3\] \= edad → se ignora

       salario \= entries\[4\].get()

       \# entries\[5\] \= contraseña → se ignora

       ok \= registrar\_usuario(nombre, apellido, correo, salario)

       if ok:

           ventana\_menu\_principal(nombre)

           reg.destroy()

   tk.Button(

       reg,

       text="Registrar",

       bg="\#22c55e",

       fg="white",

       bd=0,

       font=("Segoe UI", 10, "bold"),

       activebackground="\#16a34a",

       activeforeground="white",

       command=enviar\_registro

   ).pack(pady=15)

\#------------------ventana reportes son las 4:37 am dios mio-------------------

def ventana\_reportes():

   win \= tk.Toplevel()

   win.title("Reportes del Sistema")

   win.geometry("750x500")

   win.configure(bg="\#020617")

   tk.Label(

       win,

       text="Reportes",

       font=("Segoe UI", 16, "bold"),

       fg="\#22c55e",

       bg="\#020617"

   ).pack(pady=10)

   tabla\_frame \= tk.Frame(win, bg="\#020617")

   tabla\_frame.pack(fill="both", expand=True, padx=10, pady=10)

   columnas \= ("col1", "col2")

   tabla \= ttk.Treeview(tabla\_frame, columns=columnas, show="headings")

   tabla.heading("col1", text="Descripción")

   tabla.heading("col2", text="Monto / Valor")

   tabla.column("col1", width=400)

   tabla.column("col2", width=200)

   tabla.pack(side="left", fill="both", expand=True)

   scrollbar \= ttk.Scrollbar(tabla\_frame, orient="vertical", command=tabla.yview)

   scrollbar.pack(side="right", fill="y")

   tabla.configure(yscrollcommand=scrollbar.set)

   def limpiar\_tabla():

       for fila in tabla.get\_children():

           tabla.delete(fila)

   \# \==============================

   \# REPORTE 1: GASTOS POR CATEGORÍA

   \# \==============================

   def reporte\_gastos\_categoria():

       limpiar\_tabla()

       conn \= conectar\_oracle()

       cursor \= conn.cursor()

       cursor.execute("""

           SELECT c.nombre, SUM(t.monto)

           FROM transacciones t

           JOIN subcategorias s ON s.id\_subcategoria \= t.id\_subcategoria

           JOIN categorias c ON c.id\_categoria \= s.id\_categoria

           WHERE t.tipo\_transaccion \= 'GASTO'

           GROUP BY c.nombre

       """)

       for nombre, total in cursor.fetchall():

           tabla.insert("", "end", values=(nombre, total))

       cursor.close()

       conn.close()

   \# \==============================

   \# REPORTE 2: RESUMEN PRESUPUESTO

   \# \==============================

   def reporte\_resumen\_presupuesto():

       limpiar\_tabla()

       conn \= conectar\_oracle()

       cursor \= conn.cursor()

       cursor.execute("""

           SELECT

               SUM(CASE WHEN tipo\_transaccion \= 'INGRESO' THEN monto ELSE 0 END) AS ingresos,

               SUM(CASE WHEN tipo\_transaccion \= 'GASTO' THEN monto ELSE 0 END) AS gastos,

               SUM(CASE WHEN tipo\_transaccion \= 'AHORRO' THEN monto ELSE 0 END) AS ahorros

           FROM transacciones

       """)

       ingresos, gastos, ahorros \= cursor.fetchone()

       tabla.insert("", "end", values=("Total Ingresos", ingresos or 0))

       tabla.insert("", "end", values=("Total Gastos", gastos or 0))

       tabla.insert("", "end", values=("Total Ahorros", ahorros or 0))

       cursor.close()

       conn.close()

   \# \==============================

   \# REPORTE 3: METAS DE AHORRO

   \# \==============================

   def reporte\_metas\_ahorro():

       limpiar\_tabla()

       conn \= conectar\_oracle()

       cursor \= conn.cursor()

       cursor.execute("""

           SELECT nombre, monto\_meta

           FROM metas\_ahorros

           WHERE estado \= 'ACTIVA'

       """)

       for nombre, monto in cursor.fetchall():

           tabla.insert("", "end", values=(nombre, monto))

       cursor.close()

       conn.close()

   botones \= tk.Frame(win, bg="\#020617")

   botones.pack(pady=10)

   tk.Button(

       botones,

       text="Gastos por Categoría",

       width=22,

       command=reporte\_gastos\_categoria

   ).grid(row=0, column=0, padx=5)

   tk.Button(

       botones,

       text="Resumen General",

       width=22,

       command=reporte\_resumen\_presupuesto

   ).grid(row=0, column=1, padx=5)

   tk.Button(

       botones,

       text="Metas de Ahorro",

       width=22,

       command=reporte\_metas\_ahorro

   ).grid(row=0, column=2, padx=5)

   tk.Button(

       win,

       text="Cerrar",

       bg="\#b91c1c",

       fg="white",

       width=20,

       command=win.destroy

   ).pack(pady=10)

\# \---------------------- VENTANA LOGIN \---------------------- \#

def ventana\_login():

   login \= tk.Toplevel()

   login.title("Iniciar Sesión")

   login.geometry("350x260")

   login.configure(bg="\#020617")

   tk.Label(

       login,

       text="Iniciar Sesión",

       font=("Segoe UI", 14, "bold"),

       fg="\#e5e7eb",

       bg="\#020617"

   ).pack(pady=10)

   form \= tk.Frame(login, bg="\#020617")

   form.pack(pady=5)

   tk.Label(form, text="Correo", font=("Segoe UI", 9), fg="\#e5e7eb", bg="\#020617").grid(row=0, column=0, sticky="w")

   entry\_correo \= tk.Entry(form)

   entry\_correo.grid(row=1, column=0, pady=(0, 10), ipadx=60)

   tk.Label(form, text="Contraseña", font=("Segoe UI", 9), fg="\#e5e7eb", bg="\#020617").grid(row=2, column=0, sticky="w")

   entry\_password \= tk.Entry(form, show="\*")

   entry\_password.grid(row=3, column=0, pady=(0, 10), ipadx=60)

   def enviar\_login():

       nombre \= ingreso\_usuario(entry\_correo.get(), entry\_password.get())

       if nombre:

           ventana\_menu\_principal(nombre)

           login.destroy()

   tk.Button(

       login,

       text="Entrar",

       bg="\#1d4ed8",

       fg="white",

       bd=0,

       font=("Segoe UI", 10, "bold"),

       activebackground="\#1e40af",

       activeforeground="white",

       command=enviar\_login

   ).pack(pady=15)

\# \---------------------- VENTANA INICIO \---------------------- \#

def ventana\_inicio():

   root \= tk.Tk()

   root.title("Sistema de Presupuesto")

   root.geometry("420x320")

   root.configure(bg="\#020617")

   header \= tk.Frame(root, bg="\#020617")

   header.pack(fill="x", pady=10)

   tk.Label(

       header,

       text="Sistema de Presupuesto",

       font=("Segoe UI", 18, "bold"),

       fg="\#22c55e",

       bg="\#020617"

   ).pack()

   card \= tk.Frame(root, bg="\#020617", bd=0)

   card.pack(pady=20)

   tk.Label(

       card,

       text="Acceso al sistema",

       font=("Segoe UI", 11, "bold"),

       fg="\#e5e7eb",

       bg="\#020617"

   ).grid(row=0, column=0, pady=(0, 15))

   tk.Button(

       card,

       text="Crear cuenta",

       width=20,

       height=2,

       bg="\#22c55e",

       fg="white",

       bd=0,

       activebackground="\#16a34a",

       activeforeground="white",

       font=("Segoe UI", 10, "bold"),

       command=ventana\_registro

   ).grid(row=1, column=0, pady=5)

   tk.Button(

       card,

       text="Iniciar sesión",

       width=20,

       height=2,

       bg="\#1d4ed8",

       fg="white",

       bd=0,

       activebackground="\#1e40af",

       activeforeground="white",

       font=("Segoe UI", 10, "bold"),

       command=ventana\_login

   ).grid(row=2, column=0, pady=5)

   tk.Button(

       card,

       text="Salir",

       width=20,

       height=2,

       bg="\#b91c1c",

       fg="white",

       bd=0,

       activebackground="\#7f1d1d",

       activeforeground="white",

       font=("Segoe UI", 10, "bold"),

       command=root.destroy

   ).grid(row=3, column=0, pady=(15, 0))

   root.mainloop()

\#main ejecucion

if \_\_name\_\_ \== "\_\_main\_\_":

   ventana\_inicio()

### **16.2 Esquema de las tablas de la base de datos**

 \--------------------------------------------------------

\--  File created \- Saturday-December-13-2025  

\--------------------------------------------------------

\--------------------------------------------------------

\--  DDL for Table USUARIOS

\--------------------------------------------------------

  CREATE TABLE "SISGESTPRESUPUESTOS"."USUARIOS"

   (  "ID\_USUARIO" NUMBER GENERATED ALWAYS AS IDENTITY MINVALUE 1 MAXVALUE 9999999999999999999999999999 INCREMENT BY 1 START WITH 1 CACHE 20 NOORDER  NOCYCLE  NOKEEP  NOSCALE ,

  "NOMBRES" VARCHAR2(100 BYTE),

  "APELLIDOS" VARCHAR2(100 BYTE),

  "CORREO" VARCHAR2(150 BYTE),

  "FECHA\_REGISTRO" TIMESTAMP (6),

  "SALARIO" NUMBER,

  "ACTIVO" CHAR(1 BYTE),

  "FECHA\_CREACION" TIMESTAMP (6) DEFAULT CURRENT\_TIMESTAMP,

  "USUARIO\_CREACION" VARCHAR2(50 BYTE),

  "FECHA\_MODIFICACION" TIMESTAMP (6),

  "USUARIO\_MODIFICACION" VARCHAR2(50 BYTE)

   ) SEGMENT CREATION IMMEDIATE

  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255

 NOCOMPRESS LOGGING

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS" ;

\--------------------------------------------------------

\--  DDL for Table TRANSACCIONES

\--------------------------------------------------------

  CREATE TABLE "SISGESTPRESUPUESTOS"."TRANSACCIONES"

   (  "ID\_TRANSACCION" NUMBER GENERATED ALWAYS AS IDENTITY MINVALUE 1 MAXVALUE 9999999999999999999999999999 INCREMENT BY 1 START WITH 1 CACHE 20 NOORDER  NOCYCLE  NOKEEP  NOSCALE ,

  "ID\_USUARIO" NUMBER,

  "ID\_PRESUPUESTO" NUMBER,

  "FECHA" TIMESTAMP (6),

  "ID\_SUBCATEGORIA" NUMBER,

  "ID\_OBLIGACION\_FIJA" NUMBER,

  "TIPO\_TRANSACCION" VARCHAR2(50 BYTE),

  "DESCRIPCION" VARCHAR2(200 BYTE),

  "MONTO" NUMBER,

  "METODO\_PAGO" VARCHAR2(50 BYTE),

  "FECHA\_REGISTRO" TIMESTAMP (6),

  "FECHA\_CREACION" TIMESTAMP (6) DEFAULT CURRENT\_TIMESTAMP,

  "USUARIO\_CREACION" VARCHAR2(50 BYTE),

  "FECHA\_MODIFICACION" TIMESTAMP (6),

  "USUARIO\_MODIFICACION" VARCHAR2(50 BYTE)

   ) SEGMENT CREATION IMMEDIATE

  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255

 NOCOMPRESS LOGGING

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS" ;

\--------------------------------------------------------

\--  DDL for Table SUBCATEGORIAS

\--------------------------------------------------------

  CREATE TABLE "SISGESTPRESUPUESTOS"."SUBCATEGORIAS"

   (  "ID\_SUBCATEGORIA" NUMBER GENERATED ALWAYS AS IDENTITY MINVALUE 1 MAXVALUE 9999999999999999999999999999 INCREMENT BY 1 START WITH 1 CACHE 20 NOORDER  NOCYCLE  NOKEEP  NOSCALE ,

  "ID\_CATEGORIA" NUMBER,

  "NOMBRE" VARCHAR2(100 BYTE),

  "ACTIVA" CHAR(1 BYTE),

  "SUBCATEGORIA\_POR\_DEFECTO" CHAR(1 BYTE)

   ) SEGMENT CREATION IMMEDIATE

  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255

 NOCOMPRESS LOGGING

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS" ;

\--------------------------------------------------------

\--  DDL for Table PRESUPUESTOS

\--------------------------------------------------------

  CREATE TABLE "SISGESTPRESUPUESTOS"."PRESUPUESTOS"

   (  "ID\_PRESUPUESTO" NUMBER GENERATED ALWAYS AS IDENTITY MINVALUE 1 MAXVALUE 9999999999999999999999999999 INCREMENT BY 1 START WITH 1 CACHE 20 NOORDER  NOCYCLE  NOKEEP  NOSCALE ,

  "ID\_USUARIO" NUMBER,

  "NOMBRE\_DESCRIPTIVO" VARCHAR2(150 BYTE),

  "FECHA\_INICIO" TIMESTAMP (6),

  "FECHA\_FIN" TIMESTAMP (6),

  "INGRESOS\_PLANIFICADOS" NUMBER,

  "GASTOS\_PLANIFICADOS" NUMBER,

  "AHORROS\_PLANIFICADOS" NUMBER,

  "FECHA\_CREACION" TIMESTAMP (6),

  "ESTADO" VARCHAR2(50 BYTE),

  "USUARIO\_CREACION" VARCHAR2(50 BYTE),

  "FECHA\_MODIFICACION" TIMESTAMP (6),

  "USUARIO\_MODIFICACION" VARCHAR2(50 BYTE)

   ) SEGMENT CREATION IMMEDIATE

  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255

 NOCOMPRESS LOGGING

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS" ;

\--------------------------------------------------------

\--  DDL for Table PRESUPUESTO\_DETALLES

\--------------------------------------------------------

  CREATE TABLE "SISGESTPRESUPUESTOS"."PRESUPUESTO\_DETALLES"

   (  "ID\_PRESUPUESTO\_DETALLE" NUMBER GENERATED ALWAYS AS IDENTITY MINVALUE 1 MAXVALUE 9999999999999999999999999999 INCREMENT BY 1 START WITH 1 CACHE 20 NOORDER  NOCYCLE  NOKEEP  NOSCALE ,

  "ID\_PRESUPUESTO" NUMBER,

  "ID\_SUBCATEGORIA" NUMBER,

  "MONTO\_MENSUAL" NUMBER,

  "OBSERVACIONES" VARCHAR2(200 BYTE)

   ) SEGMENT CREATION IMMEDIATE

  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255

 NOCOMPRESS LOGGING

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS" ;

\--------------------------------------------------------

\--  DDL for Table OBLIGACIONES\_FIJAS

\--------------------------------------------------------

  CREATE TABLE "SISGESTPRESUPUESTOS"."OBLIGACIONES\_FIJAS"

   (  "ID\_OBLIGACION\_FIJA" NUMBER GENERATED ALWAYS AS IDENTITY MINVALUE 1 MAXVALUE 9999999999999999999999999999 INCREMENT BY 1 START WITH 1 CACHE 20 NOORDER  NOCYCLE  NOKEEP  NOSCALE ,

  "ID\_USUARIO" NUMBER,

  "ID\_SUBCATEGORIA" NUMBER,

  "NOMBRE" VARCHAR2(100 BYTE),

  "DESCRIPCION" VARCHAR2(200 BYTE),

  "MONTO\_MENSUAL" NUMBER,

  "FECHA\_INICIO" TIMESTAMP (6),

  "FECHA\_VENCIMIENTO" TIMESTAMP (6),

  "ACTIVA" CHAR(1 BYTE),

  "FECHA\_CREACION" TIMESTAMP (6) DEFAULT CURRENT\_TIMESTAMP,

  "USUARIO\_CREACION" VARCHAR2(50 BYTE),

  "FECHA\_MODIFICACION" TIMESTAMP (6),

  "USUARIO\_MODIFICACION" VARCHAR2(50 BYTE)

   ) SEGMENT CREATION IMMEDIATE

  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255

 NOCOMPRESS LOGGING

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS" ;

\--------------------------------------------------------

\--  DDL for Table METAS\_AHORROS

\--------------------------------------------------------

  CREATE TABLE "SISGESTPRESUPUESTOS"."METAS\_AHORROS"

   (  "ID\_META\_AHORRO" NUMBER GENERATED ALWAYS AS IDENTITY MINVALUE 1 MAXVALUE 9999999999999999999999999999 INCREMENT BY 1 START WITH 1 CACHE 20 NOORDER  NOCYCLE  NOKEEP  NOSCALE ,

  "ID\_USUARIO" NUMBER,

  "ID\_SUBCATEGORIA" NUMBER,

  "NOMBRE" VARCHAR2(100 BYTE),

  "DESCRIPCION" VARCHAR2(200 BYTE),

  "MONTO\_META" NUMBER,

  "MONTO\_AHORRADO" NUMBER,

  "FECHA\_INICIO" TIMESTAMP (6),

  "FECHA\_OBJETIVO" TIMESTAMP (6),

  "PRIORIDAD" VARCHAR2(50 BYTE),

  "ESTADO" VARCHAR2(50 BYTE),

  "FECHA\_CREACION" TIMESTAMP (6) DEFAULT CURRENT\_TIMESTAMP,

  "USUARIO\_CREACION" VARCHAR2(50 BYTE),

  "FECHA\_MODIFICACION" TIMESTAMP (6),

  "USUARIO\_MODIFICACION" VARCHAR2(50 BYTE)

   ) SEGMENT CREATION IMMEDIATE

  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255

 NOCOMPRESS LOGGING

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS" ;

\--------------------------------------------------------

\--  DDL for Table CATEGORIAS

\--------------------------------------------------------

  CREATE TABLE "SISGESTPRESUPUESTOS"."CATEGORIAS"

   (  "ID\_CATEGORIA" NUMBER GENERATED ALWAYS AS IDENTITY MINVALUE 1 MAXVALUE 9999999999999999999999999999 INCREMENT BY 1 START WITH 1 CACHE 20 NOORDER  NOCYCLE  NOKEEP  NOSCALE ,

  "NOMBRE" VARCHAR2(100 BYTE),

  "DESCRIPCION" VARCHAR2(150 BYTE),

  "TIPO\_CATEGORIA" VARCHAR2(50 BYTE),

  "ICONO" VARCHAR2(50 BYTE),

  "COLOR" VARCHAR2(20 BYTE),

  "FECHA\_CREACION" TIMESTAMP (6) DEFAULT CURRENT\_TIMESTAMP,

  "USUARIO\_CREACION" VARCHAR2(50 BYTE),

  "FECHA\_MODIFICACION" TIMESTAMP (6),

  "USUARIO\_MODIFICACION" VARCHAR2(50 BYTE)

   ) SEGMENT CREATION IMMEDIATE

  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255

 NOCOMPRESS LOGGING

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS" ;

\--------------------------------------------------------

\--  DDL for Index SYS\_C008242

\--------------------------------------------------------

  CREATE UNIQUE INDEX "SISGESTPRESUPUESTOS"."SYS\_C008242" ON "SISGESTPRESUPUESTOS"."USUARIOS" ("ID\_USUARIO")

  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS" ;

\--------------------------------------------------------

\--  DDL for Index SYS\_C008254

\--------------------------------------------------------

  CREATE UNIQUE INDEX "SISGESTPRESUPUESTOS"."SYS\_C008254" ON "SISGESTPRESUPUESTOS"."TRANSACCIONES" ("ID\_TRANSACCION")

  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS" ;

\--------------------------------------------------------

\--  DDL for Index SYS\_C008246

\--------------------------------------------------------

  CREATE UNIQUE INDEX "SISGESTPRESUPUESTOS"."SYS\_C008246" ON "SISGESTPRESUPUESTOS"."SUBCATEGORIAS" ("ID\_SUBCATEGORIA")

  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS" ;

\--------------------------------------------------------

\--  DDL for Index SYS\_C008248

\--------------------------------------------------------

  CREATE UNIQUE INDEX "SISGESTPRESUPUESTOS"."SYS\_C008248" ON "SISGESTPRESUPUESTOS"."PRESUPUESTOS" ("ID\_PRESUPUESTO")

  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS" ;

\--------------------------------------------------------

\--  DDL for Index SYS\_C008250

\--------------------------------------------------------

  CREATE UNIQUE INDEX "SISGESTPRESUPUESTOS"."SYS\_C008250" ON "SISGESTPRESUPUESTOS"."PRESUPUESTO\_DETALLES" ("ID\_PRESUPUESTO\_DETALLE")

  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS" ;

\--------------------------------------------------------

\--  DDL for Index SYS\_C008252

\--------------------------------------------------------

  CREATE UNIQUE INDEX "SISGESTPRESUPUESTOS"."SYS\_C008252" ON "SISGESTPRESUPUESTOS"."OBLIGACIONES\_FIJAS" ("ID\_OBLIGACION\_FIJA")

  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS" ;

\--------------------------------------------------------

\--  DDL for Index SYS\_C008256

\--------------------------------------------------------

  CREATE UNIQUE INDEX "SISGESTPRESUPUESTOS"."SYS\_C008256" ON "SISGESTPRESUPUESTOS"."METAS\_AHORROS" ("ID\_META\_AHORRO")

  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS" ;

\--------------------------------------------------------

\--  DDL for Index SYS\_C008244

\--------------------------------------------------------

  CREATE UNIQUE INDEX "SISGESTPRESUPUESTOS"."SYS\_C008244" ON "SISGESTPRESUPUESTOS"."CATEGORIAS" ("ID\_CATEGORIA")

  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS" ;

\--------------------------------------------------------

\--  DDL for Trigger TRG\_TRANSACCIONES\_AUDIT\_UPD

\--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "SISGESTPRESUPUESTOS"."TRG\_TRANSACCIONES\_AUDIT\_UPD"

BEFORE UPDATE ON TRANSACCIONES

FOR EACH ROW

BEGIN

    :NEW.FECHA\_MODIFICACION :\= CURRENT\_TIMESTAMP;

END;

/

ALTER TRIGGER "SISGESTPRESUPUESTOS"."TRG\_TRANSACCIONES\_AUDIT\_UPD" ENABLE;

\--------------------------------------------------------

\--  DDL for Trigger TRG\_TRANSACCION\_AHORRO\_META

\--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "SISGESTPRESUPUESTOS"."TRG\_TRANSACCION\_AHORRO\_META"

AFTER INSERT ON TRANSACCIONES

FOR EACH ROW

BEGIN

    IF :NEW.TIPO\_TRANSACCION \= 'AHORRO' THEN

        sp\_actualizar\_metas\_por\_ahorro(

            :NEW.ID\_USUARIO,

            :NEW.ID\_SUBCATEGORIA,

            :NEW.MONTO

        );

    END IF;

END;

/

ALTER TRIGGER "SISGESTPRESUPUESTOS"."TRG\_TRANSACCION\_AHORRO\_META" ENABLE;

\--------------------------------------------------------

\--  DDL for Trigger TRG\_NO\_TRANSACCION\_PRESUPUESTO\_CERRADO

\--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "SISGESTPRESUPUESTOS"."TRG\_NO\_TRANSACCION\_PRESUPUESTO\_CERRADO"

BEFORE INSERT ON TRANSACCIONES

FOR EACH ROW

DECLARE

    v\_estado PRESUPUESTOS.ESTADO%TYPE;

BEGIN

    SELECT ESTADO

    INTO v\_estado

    FROM PRESUPUESTOS

    WHERE ID\_PRESUPUESTO \= :NEW.ID\_PRESUPUESTO;

    IF v\_estado \<\> 'ACTIVO' THEN

        RAISE\_APPLICATION\_ERROR(

            \-20200,

            'No se pueden registrar transacciones en presupuestos cerrados'

        );

    END IF;

END;

/

ALTER TRIGGER "SISGESTPRESUPUESTOS"."TRG\_NO\_TRANSACCION\_PRESUPUESTO\_CERRADO" ENABLE;

\--------------------------------------------------------

\--  DDL for Trigger TRG\_CATEGORIA\_SUBCAT\_DEF

\--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "SISGESTPRESUPUESTOS"."TRG\_CATEGORIA\_SUBCAT\_DEF"

AFTER INSERT ON CATEGORIAS

FOR EACH ROW

BEGIN

    INSERT INTO SUBCATEGORIAS (

        ID\_CATEGORIA,

        NOMBRE,

        ACTIVA,

        SUBCATEGORIA\_POR\_DEFECTO

    ) VALUES (

        :NEW.ID\_CATEGORIA,

        'General',

        'Y',

        'Y'

    );

END;

/

ALTER TRIGGER "SISGESTPRESUPUESTOS"."TRG\_CATEGORIA\_SUBCAT\_DEF" ENABLE;

\--------------------------------------------------------

\--  Constraints for Table USUARIOS

\--------------------------------------------------------

  ALTER TABLE "SISGESTPRESUPUESTOS"."USUARIOS" MODIFY ("ID\_USUARIO" NOT NULL ENABLE);

  ALTER TABLE "SISGESTPRESUPUESTOS"."USUARIOS" ADD PRIMARY KEY ("ID\_USUARIO")

  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS"  ENABLE;

  ALTER TABLE "SISGESTPRESUPUESTOS"."USUARIOS" MODIFY ("FECHA\_CREACION" NOT NULL ENABLE);

  ALTER TABLE "SISGESTPRESUPUESTOS"."USUARIOS" MODIFY ("USUARIO\_CREACION" NOT NULL ENABLE);

\--------------------------------------------------------

\--  Constraints for Table TRANSACCIONES

\--------------------------------------------------------

  ALTER TABLE "SISGESTPRESUPUESTOS"."TRANSACCIONES" MODIFY ("ID\_TRANSACCION" NOT NULL ENABLE);

  ALTER TABLE "SISGESTPRESUPUESTOS"."TRANSACCIONES" ADD PRIMARY KEY ("ID\_TRANSACCION")

  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS"  ENABLE;

  ALTER TABLE "SISGESTPRESUPUESTOS"."TRANSACCIONES" MODIFY ("FECHA\_CREACION" NOT NULL ENABLE);

  ALTER TABLE "SISGESTPRESUPUESTOS"."TRANSACCIONES" MODIFY ("USUARIO\_CREACION" NOT NULL ENABLE);

\--------------------------------------------------------

\--  Constraints for Table SUBCATEGORIAS

\--------------------------------------------------------

  ALTER TABLE "SISGESTPRESUPUESTOS"."SUBCATEGORIAS" MODIFY ("ID\_SUBCATEGORIA" NOT NULL ENABLE);

  ALTER TABLE "SISGESTPRESUPUESTOS"."SUBCATEGORIAS" ADD PRIMARY KEY ("ID\_SUBCATEGORIA")

  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS"  ENABLE;

\--------------------------------------------------------

\--  Constraints for Table PRESUPUESTOS

\--------------------------------------------------------

  ALTER TABLE "SISGESTPRESUPUESTOS"."PRESUPUESTOS" MODIFY ("ID\_PRESUPUESTO" NOT NULL ENABLE);

  ALTER TABLE "SISGESTPRESUPUESTOS"."PRESUPUESTOS" ADD PRIMARY KEY ("ID\_PRESUPUESTO")

  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS"  ENABLE;

  ALTER TABLE "SISGESTPRESUPUESTOS"."PRESUPUESTOS" MODIFY ("USUARIO\_CREACION" NOT NULL ENABLE);

\--------------------------------------------------------

\--  Constraints for Table PRESUPUESTO\_DETALLES

\--------------------------------------------------------

  ALTER TABLE "SISGESTPRESUPUESTOS"."PRESUPUESTO\_DETALLES" MODIFY ("ID\_PRESUPUESTO\_DETALLE" NOT NULL ENABLE);

  ALTER TABLE "SISGESTPRESUPUESTOS"."PRESUPUESTO\_DETALLES" ADD PRIMARY KEY ("ID\_PRESUPUESTO\_DETALLE")

  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS"  ENABLE;

\--------------------------------------------------------

\--  Constraints for Table OBLIGACIONES\_FIJAS

\--------------------------------------------------------

  ALTER TABLE "SISGESTPRESUPUESTOS"."OBLIGACIONES\_FIJAS" MODIFY ("ID\_OBLIGACION\_FIJA" NOT NULL ENABLE);

  ALTER TABLE "SISGESTPRESUPUESTOS"."OBLIGACIONES\_FIJAS" ADD PRIMARY KEY ("ID\_OBLIGACION\_FIJA")

  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS"  ENABLE;

  ALTER TABLE "SISGESTPRESUPUESTOS"."OBLIGACIONES\_FIJAS" MODIFY ("FECHA\_CREACION" NOT NULL ENABLE);

  ALTER TABLE "SISGESTPRESUPUESTOS"."OBLIGACIONES\_FIJAS" MODIFY ("USUARIO\_CREACION" NOT NULL ENABLE);

\--------------------------------------------------------

\--  Constraints for Table METAS\_AHORROS

\--------------------------------------------------------

  ALTER TABLE "SISGESTPRESUPUESTOS"."METAS\_AHORROS" MODIFY ("ID\_META\_AHORRO" NOT NULL ENABLE);

  ALTER TABLE "SISGESTPRESUPUESTOS"."METAS\_AHORROS" ADD PRIMARY KEY ("ID\_META\_AHORRO")

  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS"  ENABLE;

  ALTER TABLE "SISGESTPRESUPUESTOS"."METAS\_AHORROS" MODIFY ("FECHA\_CREACION" NOT NULL ENABLE);

  ALTER TABLE "SISGESTPRESUPUESTOS"."METAS\_AHORROS" MODIFY ("USUARIO\_CREACION" NOT NULL ENABLE);

\--------------------------------------------------------

\--  Constraints for Table CATEGORIAS

\--------------------------------------------------------

  ALTER TABLE "SISGESTPRESUPUESTOS"."CATEGORIAS" MODIFY ("ID\_CATEGORIA" NOT NULL ENABLE);

  ALTER TABLE "SISGESTPRESUPUESTOS"."CATEGORIAS" ADD PRIMARY KEY ("ID\_CATEGORIA")

  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS

  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645

  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1

  BUFFER\_POOL DEFAULT FLASH\_CACHE DEFAULT CELL\_FLASH\_CACHE DEFAULT)

  TABLESPACE "USERS"  ENABLE;

  ALTER TABLE "SISGESTPRESUPUESTOS"."CATEGORIAS" MODIFY ("FECHA\_CREACION" NOT NULL ENABLE);

  ALTER TABLE "SISGESTPRESUPUESTOS"."CATEGORIAS" MODIFY ("USUARIO\_CREACION" NOT NULL ENABLE);

\--------------------------------------------------------

\--  Ref Constraints for Table TRANSACCIONES

\--------------------------------------------------------

  ALTER TABLE "SISGESTPRESUPUESTOS"."TRANSACCIONES" ADD CONSTRAINT "FK\_TRANS\_USUARIO" FOREIGN KEY ("ID\_USUARIO")

    REFERENCES "SISGESTPRESUPUESTOS"."USUARIOS" ("ID\_USUARIO") ENABLE;

  ALTER TABLE "SISGESTPRESUPUESTOS"."TRANSACCIONES" ADD CONSTRAINT "FK\_TRANS\_PRESUPUESTO" FOREIGN KEY ("ID\_PRESUPUESTO")

    REFERENCES "SISGESTPRESUPUESTOS"."PRESUPUESTOS" ("ID\_PRESUPUESTO") ENABLE;

  ALTER TABLE "SISGESTPRESUPUESTOS"."TRANSACCIONES" ADD CONSTRAINT "FK\_TRANS\_SUBCATEGORIA" FOREIGN KEY ("ID\_SUBCATEGORIA")

    REFERENCES "SISGESTPRESUPUESTOS"."SUBCATEGORIAS" ("ID\_SUBCATEGORIA") ENABLE;

  ALTER TABLE "SISGESTPRESUPUESTOS"."TRANSACCIONES" ADD CONSTRAINT "FK\_TRANS\_OBLIGACION" FOREIGN KEY ("ID\_OBLIGACION\_FIJA")

    REFERENCES "SISGESTPRESUPUESTOS"."OBLIGACIONES\_FIJAS" ("ID\_OBLIGACION\_FIJA") ENABLE;

\--------------------------------------------------------

\--  Ref Constraints for Table SUBCATEGORIAS

\--------------------------------------------------------

  ALTER TABLE "SISGESTPRESUPUESTOS"."SUBCATEGORIAS" ADD CONSTRAINT "FK\_SUBCATEGORIA\_CATEGORIA" FOREIGN KEY ("ID\_CATEGORIA")

    REFERENCES "SISGESTPRESUPUESTOS"."CATEGORIAS" ("ID\_CATEGORIA") ENABLE;

\--------------------------------------------------------

\--  Ref Constraints for Table PRESUPUESTOS

\--------------------------------------------------------

  ALTER TABLE "SISGESTPRESUPUESTOS"."PRESUPUESTOS" ADD CONSTRAINT "FK\_PRESUPUESTO\_USUARIO" FOREIGN KEY ("ID\_USUARIO")

    REFERENCES "SISGESTPRESUPUESTOS"."USUARIOS" ("ID\_USUARIO") ENABLE;

\--------------------------------------------------------

\--  Ref Constraints for Table PRESUPUESTO\_DETALLES

\--------------------------------------------------------

  ALTER TABLE "SISGESTPRESUPUESTOS"."PRESUPUESTO\_DETALLES" ADD CONSTRAINT "FK\_DET\_PRESUPUESTO" FOREIGN KEY ("ID\_PRESUPUESTO")

    REFERENCES "SISGESTPRESUPUESTOS"."PRESUPUESTOS" ("ID\_PRESUPUESTO") ENABLE;

  ALTER TABLE "SISGESTPRESUPUESTOS"."PRESUPUESTO\_DETALLES" ADD CONSTRAINT "FK\_DET\_SUBCATEGORIA" FOREIGN KEY ("ID\_SUBCATEGORIA")

    REFERENCES "SISGESTPRESUPUESTOS"."SUBCATEGORIAS" ("ID\_SUBCATEGORIA") ENABLE;

\--------------------------------------------------------

\--  Ref Constraints for Table OBLIGACIONES\_FIJAS

\--------------------------------------------------------

  ALTER TABLE "SISGESTPRESUPUESTOS"."OBLIGACIONES\_FIJAS" ADD CONSTRAINT "FK\_OBLIG\_USUARIO" FOREIGN KEY ("ID\_USUARIO")

    REFERENCES "SISGESTPRESUPUESTOS"."USUARIOS" ("ID\_USUARIO") ENABLE;

  ALTER TABLE "SISGESTPRESUPUESTOS"."OBLIGACIONES\_FIJAS" ADD CONSTRAINT "FK\_OBLIG\_SUBCATEGORIA" FOREIGN KEY ("ID\_SUBCATEGORIA")

    REFERENCES "SISGESTPRESUPUESTOS"."SUBCATEGORIAS" ("ID\_SUBCATEGORIA") ENABLE;

\--------------------------------------------------------

\--  Ref Constraints for Table METAS\_AHORROS

\--------------------------------------------------------

  ALTER TABLE "SISGESTPRESUPUESTOS"."METAS\_AHORROS" ADD CONSTRAINT "FK\_META\_USUARIO" FOREIGN KEY ("ID\_USUARIO")

    REFERENCES "SISGESTPRESUPUESTOS"."USUARIOS" ("ID\_USUARIO") ENABLE;

  ALTER TABLE "SISGESTPRESUPUESTOS"."METAS\_AHORROS" ADD CONSTRAINT "FK\_META\_SUBCATEGORIA" FOREIGN KEY ("ID\_SUBCATEGORIA")

    REFERENCES "SISGESTPRESUPUESTOS"."SUBCATEGORIAS" ("ID\_SUBCATEGORIA") ENABLE;

[image1]: <data:image/png;base64,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>

[image2]: <data:image/png;base64,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>

[image3]: <data:image/png;base64,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>

[image4]: <data:image/png;base64,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>

[image5]: <data:image/png;base64,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>

[image6]: <data:image/png;base64,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>

[image7]: <data:image/png;base64,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>

[image8]: <data:image/png;base64,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>

[image9]: <data:image/png;base64,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>

[image10]: <data:image/png;base64,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>

[image11]: <data:image/png;base64,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>

[image12]: <data:image/png;base64,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>

[image13]: <data:image/png;base64,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>

[image14]: <data:image/png;base64,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>

[image15]: <data:image/png;base64,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>

[image16]: <data:image/png;base64,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>

[image17]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAAEoCAYAAACAWV+9AABLX0lEQVR4Xu3df3AUVb43fq/f/XGfy/Xx8a7L7nVXp7D82RQVQcsVEgRFwl4IaBRJIZEvGVmMYliMrBALR2WANVE3LBtk77DUyPKMpirIDlIOxVOzqTs3hbMpspZWWWvV43/+6X/+53+fp093n+7T55z+MTPpMCTvP16lpLtnTp/pH+855/SZa1KpFAEAAADA9LtG/gMAAAAATA8ELQAAAICEIGgBAAAAJARBCwAAACAhCFoAAAAACUHQAgAAAEgIghYAAABAQhC0AGBWOpj/IX2Tv4naNMtgBrw+RlNTU4qx1zXrwlVj26vX0TcXblT+DsGaLmi17hymsVKFpkYzyjIAgDgO5n9A9OU1RJ/cQAcNdTnMAAStWehmKl641jq3tinLIEjTBa3u4xX7hDyDoAUAtdt2eB59x0LW5/NodI26vOkZHdQ7VKDSeNULKNUKlU5nqXuJZv2rQjflxpswaC3ppszxIpUnhLqerFL5XJ6yPa1k8PW25qjClo3nqFt+DQfbtnK82/sb30ZWNV//7Aj1rzOU13BZ5RrzHwNOuQaf6/DK5Wqh7v05Kpal9YPep5GyGTfRpU+uoW/RWhwbghYAzB5rbqSvWcj68gd06Vea5c1uSS/lLmpugNzEGGVWa7Zres0XtFp25Kg8qaljl1nXfP3pDFquMuV61EBj9AxTqSqvK6pQbquwjRnMs6NCwJJNlmlEfp86y+ZaM988x66lLwY0y0CBoAUAs8QtNPrxP1ndGt/mf6ZZ3uzaKXvWuWFOlCi3t5NarL+3UOfeHJUmnJtgaZg6lW2bXZMFra0jVOahwqrrblrptBYayzoovWeExsqF6Qlavm3Mz3LnCBV5kLo4In2WnTTCg3ZljLLbO6iVd30vWUndOwepcLFEI0LQSp9w7pmTFRo7lHbWN6i1J0tjTp1PVQvUL3ah11U2P6tr/vL19Ad0zUeKHbSMdf00crZMVeEbQO6VLk0TZsQJxfvt3SDlrR8p5CCvmbZ5vkzF4xmleT5zxl6uvIb2YGX4PjnfiJZ0m984hLqrFCn363b19fi6p0tUEb7RFIZ6qSPwYG6h7kPyfrBuhkHq1X7zbaBsTcxY10uDUr1Vy+a+7O92blZc+PFpbSuHfP45O39v2WJewIQm+sq5HPVp61p/3ujLFbG+9lxrrGyxLM9S0XqtKhX2aJZb6wxSyVrH/Oa8UVzGLvYZyo2anwsPCYx5fMrnmKXRfdl5vdNleB3lAs8XQdxrwGq+f1NUPp5WP4fVWffmVD4m3GhrtSPvtDKUaFC3n245zM9ir9DaEFJvgXW2pJP6hvJWV5N8rI28qOua8sQ/10Th551MOQ8mq+a+5GlgU0grS2ytlD3nvO54nnp1x6Is8Frvseo7MmjZjL0Fqlp1V6SseKxu5gGwQrke9T107POzQvmdmrox+ihfsfe1fLTT+3s9ZZOM/xdrOb6Gvn7rFmUZ+MUKWu1mxQc1M1beH6B23/oRJ1QzBK3VA1RwDj4dudz1B62yGVrMi562Gbjs+1ZiWZ0JWFctk8VI03AppMm4WqJhpfm3zrI1sbDj09f8bwk/Pq1tgoJW2bxpHRhzLkKS8ohybBo9Oe9bs0Jq/k9F7YfuXKu/bPEZNPC+fYxV3+/XLE9R629L9vvI34B52XQmpG/Y4vp17kvuL3Zr1jf/+XNlmaLGa0D767w8cpdKOw2et7epmseN8vnUoN+p58rJXmUZ1/ee5rOIqjdNnfFrWpDSO8JNWRB+jMrnmij8vBMZPSMhXXpy/ddhIw8zUmANE3it97DyxQ1a3rlhXqM3CH93g5ZZtl/HK5tVL+ey1KpZxrjnZ2mYOvjf6ymbpO3V6+xWrf/+N3pZsxw8kUGr96TTLHl+ULmI9L3nLPN9yBEnlBK0/JLuOnTTetVM67pvehr1By37hBl73d9CZPA6MC+AXZr3KQ3FaFFyWxoCvsm4337N5TvEZfHLJv69Jj15mvziC/oi0jk6IG9bEyEEnM0qx6de+PGpPfbEwKCMkTHcz618rEv4O3+feBfMsPOMvYf+XEvVWbZa9TrfijWtWm5rlvnecnAKYZVXfrK4kX15+gb6ll30P72e/iAvk9RzDbAIrQOVE2kyNg6751jDN/+U+SXLei3zS85meZlAd80JqbfQOtMx+HVFLkc955oo/LzjWg8V7f3Qngc81GqOwxq49xhzP8Ja7nx09S6xjouooLVkJaUPjbmfl7YFlH3hFluAKyUaO56h9DLdMdZl1+l++e8ifmxFjDmLUzafW+jCX51WrTflZSCKCFpdNFJ2Dmxd8u9xPizW/+v+PeKEusJBK863RlkjQUsbmgK26zzifPMwL9zFowPUpT2xHPudepRbEVwGZc86ZTjSIfw9ftmUZU2nnwpWi5wcJsOEH5/aY8+9kem7dPgx67vImvXPjzXWHVU4lHbHgOiEnmeM9lxL1Vm22vHXkVu1+Lfl6vsD8W9aqemsZ8fhefa36ws/jnwSqp5rAOe1UlaowrtkdN2JNdPcDHV0146QegutMy1eDrnFtZ5zTRR+3nGZUXud4gH9eVD7/qjc1jz5+Aujq3eJUi73c9GrnNa0UHNWt/aY0rJXUZ4I7NZ8VjLNsdVI2QQH//z9q3hM5MyJCFreyaX/IDUfYNQJdUWDFg+OAWUL0EjQquV92De2gfed/XewsQ+dmht0Bw9lIfWkvyjVW7Ym5DazR9ycfML3X1un7kWplvdJabt2K6Uxyu3nA1Y94ecZozvXUvWXrVa8u8UX9DrM/bPLHXTzbdmSoRwba6Prop6ueja1vekErY/nK8v86rsGiLqPlb190La81CMo4Eh015x66k03Ps1HKkdd55oo/LyzeZ9NlEaCFu9+nbEWLUXFrIOAMZcKNkB9kPLnhPuC7ylCFrTC6pTRXDumpWxsvjo7aNG5qPNubosIWlEnv+YDjDqhrmjQiihbgJkLWjbr5sQGELsDQcuUlwaod/GLfUg9XbGgNVNdh/XcYCL2X1undb0PZ1DHc+xC6R/gPjVRpEFhYG/4ecbozrVUg2WrBR9ALHTbbHC6zpTj3+aNawowjfW8+Xf/I2bQCv/8oxneU16M/DRX3Xi5qpTfKS/zGAe8rjW3C7nWejO/AOQiA410LNb6Hoo49e6tE6WRoOVeO83jNq1ZrhV4rfco5ZK3MVopPVR0zgl12EYUY50wrlAoB/t36betyvou3ho+kac+/rdpKhuCVjwRQcs7+bV94roPMOKEci8U8kXWkWzQEsZB+brTwgUGLb7/yskXXgfx2U9tWfUhdxnxwCoOcJS2dbsOfSfhdJUtxEwFLTd8hA/a9Avff+2x1/BNhrO/nY7xi6Xw2YWeZ4z2XEtNY9mi8fEzvJuQt6r6nmZy8XFd5vqlHA1sEiZ/TCVQzzV0HdZzDeDc8Fgdo8IZZ8zSmcYGwdu8MWjBIcIbJ6W9ocesN3ccFGu9ULq0g75c13OuicLPO47XQdg6DdvDn6oLbolV8DqWr8MuQy23HGac9bygXqTscvl1IuzMO2X3Pgd+LgW1QnUe9b6Uh0/AWnvZeNBC12G4iKDljWfQDYB0l/nGZ/DuBPkGLz1NIl9kHe63DfEb2zRyu9wq5g0r5jdRvp++v4sDFhMLWjbt4FTemsAuiLqBuO5AXfmR++kt25XlHWuV9/oCLzR+4cen9tis8UYWiYcm4fXCzjNxvJcyFqrBshWcYyHWmAxjwO7itG42vB4DLsihj6nbN6Vpredf/a/Yg+HruQZY3GkcWCA2fP8uHojXAhDGDUABg/S98WHSOV1jvfFxUNqusyXeQzb+oFXPuSaKd93hn41ynMc0fN45T84PUzroszX4kJgp60nNwPV82wgPH+nC2epBtc60YYa9lnMesbqsdZygG7S8qRfszz7gPuA+yR4wJUiDZStewGD4OCKDlje3i1nxo1lKr2qx/m4sS9sHqmYqAHcQ8HjBGbjHJtzL+wf2yRdZzv22YV68huRvW9PAfVqPlW+MBnd2ueNlWlalKXOyRHnpCQ5+8g9vYfvOWpkGqSg+FSIfrDEvKn7dNHKuRIWj/ZTesNKbj2bJSucbtPxNSpgLpsom3OP74Uw655SvOpqRAms9ZWte3rdzdnwOUp/bctJCK7dnKH8+r9x8Io9P+dis8UZmy1CBzS10qI+613mtOcayLhp4z/kyIbZGhpxnmdN8TJB6rtVXNo97DAfdQCT2+Bbzov2687Sh/BQk596Ypqj8Xr8zDxz/TJz6n5Z65n5KX3zOLvrfp0tpeZmkjmuA2N3GHgjgn2c7f3Re99nUSniq0Z6s0rkOGK3UxSYsdW6A4vtbaqw3t9XCDHSD1jXNPi77hsa84QpyaEjVd655Yl53hDnLrPfY4l0LW1Z1U98h9jMzwkSiEu94nqLioeDutPYDvJtMPQasCUutn7MR30e43rJuf/7ZOL0OBXZsyBPJBoWZlPjgk/RFZX+BymdzlN3ZTR3iw1DWZKXedV087/j0IvJ9YOX2rK/1vOGyKfg598803ikvA1F00GLNieLgT5+Avlxx1l15/RPOPCzyRdbVHTwgUnNQ1CN8LhjNhWA5/1bgVz6ety/YSrliXlQCtlEF1LP8GLDs4ojm21o9ZWtm6gMEfpqbT8jxqT02a7yR2XhXS5Cy9A007Dyzy6Y9Buoqm0d8/bCxQS4nEFYrrM5DnpI0b0yZkJ8FsW5y01LPnlPOPFrfFW5SlslquwYIXSrKmCxvHq3YrSMhwueQYt2wmpaaWust8PifsmYXt5+mVINWreda1FxdFuXaGWNsX8h+iuvJLdZ+Ueeb5n22hv80jvLTSCFhxjdViNhyFPBD3D7y1CdR94FKgQamo2wSzKMVX4ygxRjU8eKI8oOVGefbkE77r81vBMKEgJVSgbJsff4ByxdZkWZ2dIvuoKiTNfMwG3AuvsdEmYpH+bdvaf1NWW89d/Zk52aqlKu+MOMOghdPmoh61tZVpRQym3x9ZWtu9vE5VqrEnuU66PjUHpu13sgswiB48bPhs/Zrf7RVf56xb7iBx0BdZfPU1HVoEX4iRB4vJjM6aOCk8FAH/0z2dk5jPQuEmeFPaY99v7jXAO/G73QZyq/ldtPX263mFzTzev5QwMzrddRby45h/3Hm/Gg1m6vJDki6oMXEP9fqDVqM+7Sq7wESs4yj5rkg/tizJFbXoe59fOeoc85p3kf32fC6k187NMyYWt3jSmg5YoPS9+eoIF83zOuAdQwEXdfdH8cWtmHzbwXcz+oqm8SdQwszw0eKGbQAAJrdze7F/9s/3xQ5KB4A6md9qfnbDXRQswz8ELQAYPbo+hF9w24AbKzWrzTLAaBxa+ab59j36O+7NctAgaAFALPKtsPznC7EeTS6Rl0OAA0wbqJLn7ApHdBqHNdVGbTCBxnrBI03AIDZ6GD+B/ZA3cv/k3JL1eWJcsdMxRV/bBXAlXULjZ671jq3tinLIAiCFgDMQjdTbvSH9M3JK/CtG0ELZjHWYvztxz9W/g7BrsqgBQAAAHA1QNACAAAASAiCFgAAAEBCELQAAAAAEoKgBQAAAJAQBC0AAACAhCBoAQAAACQEQQsAAAAgIQhaAAAAAAlB0AIAAABICIIWAAAAQEIQtAAAAAASgqAFAAAAkBAELQAAAICEIGgBAAAAJARBCwAAACAhCFoAAAAACUHQAgAAAEgIghYAAABAQhC0AAAAABKCoAUAAACQEAQtAAAAgIQgaAEAAAAkBEELAAAAICEIWgAAAAAJQdACAAAASAiCFgAAAEBCELQAAAAAEoKgBQAAAJAQBC0AAACAhCBoAQAAACQEQQsAAAAgIQhaAAAAAAlB0AIAAABICIIWAAAAQEIQtAAAAAASgqAFAAAAkBAELQAAAICEIGgBAAAAJARBCwAAACAhCFoAAAAACUHQAgAAAEgIghYAAABAQhC05pxuyo1P0dSUZDxH3cq6tswZzfpTY5TRrDunrJlPX/1tHo2u0SwDAABIIWjNQQha04KFrM+vIfryWvrq8M3qcgAAgBSCFrw+Fhm0fLbmqDLHg9YfRr9nBqxr6LuP59M2zXIAAAAOQWuuQ9CqTfoG+tYMWfT5PBpdoVkOAAAgqCloGet6afB0iSpVu/uoWi5Sbn83tfjW87qmxl5XX8O9sZ/J+P/Ob+DO31u2ZGmsXHW7qirnctS3WvN6S7opK5TJUilRYaiXOgzN+ozRQf1Hi1SeELaZKFPx+AB16bZxysb+P3a5GhCvnm0tj/XR4Em2L16ZpiarVD47Qv3rDGV9RSJBix8DRcqa9dm+Y9BXZ1Pm/gzvaFG3E46BWurZWNdPI2fLVJ30Pk+rzl7pIkOzvss8DnqHClQa996neDxD3Us061puoeL/Yd2F19A3x3+uWQ4AAOAXO2i17y04N1iZfMNtMGiVzRvqgTGqKu/Dlo34w8DqDI2JAUuiff/VA1SoqOu6KgUakG/oTtlil6sB8euZMfdfWU8wWaLhjfI2kkSDVoUKxwPqbKpMI1sDXts8BrTbaOo5uL5slfcHqF0pXyr0ONAeN0znj+gbqzXrOjqlC+QAAACSeEFr4zCVnJtQtZSnTE+r1VLQsT1D+fP56Q1a3ESJcns7rVaclh05Klt/r1Jhj7dN78mKXaZzg5RexVtIWmjllj4aPF2m/H75/dspe9ZpvaiMUXb7SruVyGilrr05KvEWpPf7/S0hYtlilKtuNdUzYwat8SLlh/qoe529rrX/2wepKOyL8j6iRIOWo+rVGWt9ypedv5/LUqv2tWPW8+qsu5+V0ax7DBjLumjgeMkJa2wbuWWvk4ZLXtny+9PUagUngzIn2b/l/bHtOv7PVmsW/eUn1KZZDgAAIIsRtAwaeN8OJ9WzWX3rgM80BK0J8ybua1Uy3Cffyse63L/zv5WG2v2vFWRH3nmPEg3KrVYmYydfXqTscmEZL1vMctWn1noOZxwo2nVZHqEuzXJX0kGrKteZaeOIE5zMZWLLkHAMxKlnHrSnzg9q6sugvvec5VKgM/YW7BBWNT9nuWwhRs/Z3YZf/+4WZRkAAIBOjKDVTwWr1aBC+R3yMp1Gg5Y+BHUft2+alePd7t86j5Ts1zLLVjw6QF3L5JYLv65jZWv96vsDAWN30k7ZpZYTp2xxy1WfWus5QtwAFXc9rsagpT0GUn2Ut8bHVSgndh8Kx4C8jVrPXTRitYyZn9XegM+9x3m9aoH6hb/3O4G2crJX3SbQz+jS31jQ+j5d+pW8DAAAQC86aG0WWh/kZVoRN9nIoBX3fZh2GnjfabVwsEHQrCutUzOg2b3BhoQi3nLiK7tTtvjlqkPN9WxzB86LA/tFUQHqigQtvlwfaNlrq9vIvGDqC2s+fAybWFYe0ILKFuQmL2il5WUAAAB60UEr1o1VFHGTndagZWvZkqHcqBk2hKfOpibLlP+1v0sxM2ova8qgVcf+Gz187FKIqAB1RYOWGZJ69K+tbiPjIarWoBVVtiD/Tn//FEELAABqEx203JtViYY3yMt0wm9k7tihaQxaHoNaezKULzkD3qUuI979FDxA3Os6zO8U/j4TQavmem6l7Dm7nn0D+7m4ASruelyszyn8GEgZAftaU9AKaBUT8a7DiTz1CX93x/Yd6VC3CYSuQwAAqF2MoNXhPqFVea8vYGyTfv3Sb1t9y4yeESrzVqdEgpbDyFLReq0yjWwW/r4nfBC04S4v0IBmkHZd5WLTCDiho3I6YKoBS6317E3tUDygjlFqOeQE2qgAdQWCVvtvnbF18nvWFLS8rmD9wwOGt1wak9fBx/ZVzABWwzQNxQsYDA8AALWJEbRS1Mpv2iwEjA5S3yZ7KoGVAdMO8Bvc1HjBmTSzhTr35r2QxTQctLpp5FyJCkf7Kb1BaM1ZspLSQ0U3MIktWqlUL+X53EnS9A7p/QW3fOVjUtdiA0GLt6LZwge611bPvPXNnt7CnmTToNZNfTQ4KrynHGZkCQet8rE0dfCHFNhnc2jM2b5qhjB/EK81aHlPkcrTO6Qpc9p+8EE7X9dyHsTZfo/R4M4uZ3qHVLzpHT6ej+kdAAAgllhBSzfo3KO54W7lA7tl5s31hDPB5DQELX4z12M3cnXaB1+rmkZ1NKO2jjQQtNwpCJwy+bokFbXVc7fzFKXWeMWuTzlAufUczmuJipgU1eEf9xb12ZgB7L2+wHqOHbTMYJkOq4OAY4AJm+hU1wpn6fo3e8LSL/+Fiis0ywEAACQxgxZjUMeLIzRWqrg/dcKe8Bt5sUPbzdX+6xwVhZm3K6UCZbe0eDfThoOWMAhefOJukv38TI4y7L002zCBP9kS8DM3jQSt+F2HXC313EK97xSpLMyOXx0vUeEQm4DTCUjNFLTMz4YdB4PP6fZFLFvcoMXY9VUUf+InxjHAWMcBO36E+ise7Q/+6SbxJ3j+Ez/BAwAA0WoIWgBxhY/Rupq17b6evnN+VLq4Rl0OAAAgQtCCBMzeoMXk/nKtPVbrwo9pm2Y5AAAAh6AFCZjdQStl3ESXPrG7EL/N34SB8QAAEAhBCxIwy4MWs2Y+ffU5C1vX0te//5m6HAAAIIWgBYmYA0HL1Lb5Rvr6k3+lUYzVAgCAAAhaAAAAAAlB0AIAAABICIIWAAAAQEJCg9bKlSvpF7/4hfJ3AAAAAIiGoAUAAACQEAQtAAAAgIQgaAEAAAAkBEELAAAAICEIWgAAAAAJQdACAAAASMgcDFqL6ER2H336e9M7m+kl628P0hn2b2bgEWpVtmlSD6ynCV5uwUR6kbqu1iI6MtBvbTM5sIaeVpZD3TZstT+P7PrY9fraHvWz/PT3W+k1zbpaD6yhC0PmNsP9dGFz3GOgSc2mfYEZ89JzL9jnzcEn6aW71OWN8s7RZ+lIC/ubdz/ZpVkfgJmDQUs4WdyboBC+9jyorH+14PvVTEGr9jLNEnUELR83RCNoXfX7AjMm6aD1dNp5feG85Ne4us5zmBPmdtByW6+8oDWx/R5l/atFM4aaZizTjLgSQQsAEuUGrTefcFuw+DXO0KwPwMzJoLXr2d32yeK2Xt1JR169+gNBM4aaZizTjEDQAph1Wp/sUc7rl/p+Y/1NXheAm5NBy/1WInQTxgkEH73RT58O2+uxLo3xPevptV/cqqzHb7JW69iChfTKjh6aeMs+GT8d3k0Xnm2jjgXq6zcqzj74uklFUYHg9kV0aOez3n4wh5+lD7rulfZFGO8WRdNN27L4fhp61rmYMe+wel5LLy3SlCnF9/kFOvGA+e8Fd9JLabOu33G2fet5OvPYwmn6pnkrPd35JF04aHe12q//Al3Y+Qj1GvK6KS9osX1k5ereSuO1HANxg1YD4/Ta2x7xjmeFU6d8/QW30jMd6+nMqy/QJK/f3/+GJg+ax0DnImrRvL637Z3U2+Wvu4/SD9LTt0vrNbAvxqKl9O6e572yDZtle2MrnVgrf/78+LfrtX3VWvu85vvzxhY6pDunHR2rnfV5vZnHwEc72qgr5LNkZfPVGStXR0Sd1SDsvLfqM+DcVuosrGwRxyMvw5kN/r+3PvAgndhtXjeGhOuGdd48rH7+4vs414aWXzxMZ/jnY36mE/vW0y7N+eaNneL05fTh56VYtqHnzWMz5PPUfIHi9xNlXQDHnAxa9Xgm/bx0Ijt0FzF+Mr78mD7UmCZ3t037oPuwC66njqBlmOHpLc02Dv/FtZGgFbLt8HY6slgtm3uBf+xe/X79vp/OrL1N2a4mC+6hI/uFgCV7yyzbMmkb4Rh49w3hQi4IPQYibmzqen7hx4AZMMzyTWq28/iDljc2RW9y51J9oDWW0geH1fUZ+aZc9778x2aaCAyM5vZ9S6ndXZ8f/y/QmZ3b9XUw3ENDmpv5M9sCrgGMef48o7k5G8vW07i2bFKQbUDYeR8UtILLFVC2iONRG7QCPk/X0JP0klxnfBuzzLseCzhGNftTc9AKOS4thzfTK5pjAKAeCFpx3PUwfWRelE6tWUitzoXBuONO6xv+R3vWKie9e5N1TOx+mJ65gy27lZ7u6nEuHrvp1IOa92pA2AU3kOYbmqx3h93VOrnvEXrG4N/2b6WH7rufhnY+S6fWqttwtZXJDFoHe+hU1/3OTdt8j7ZH6CMn5E2aN0x5G/cCa900fuPVtflt9dAeJxy9uoY6lPeK75ntTsgwA9UJ9xhgZTO/bfOLtfkej4vbNXoMRNzYgsSq7wXmTcZpxeiyypSi1nuX0iknqLJ6lkPT09u20/ju9fRa2530kNMSYdyxkF55locP/hSWaKHbJc/q7lTHPe7589qO7aHHjbVOnH0xzHPT2Rerjp3j0ypbmgepfvpgDd9G+qJhluvdFbda+9vyC+9YG9/mf09jxRP25zG8m8508v3wHwMTz94r1dttdGifv55Zy2BH24N0Ys9WelcOM3UKqyd90PLKNf7s0nhlizgeg4LWhde20Anzc+/g1w3zPbrWPOGGvAtb7vS/Fn8fHgKH7HOOtbC1tD3mbPcb4fOURJTTZu7/y86Xn8Nb6FDbbXYLnlU2s8zC9UY+DwDqgaAVh3Py7pK/fQURbrLj6XuUk/WVXfZJrrswNiLsghsoRtDir3uhq/aWobrKJDEe88rYJS3zvsn+xrw5SnXtXrS3hFx0Izgh2wpFKzTLjUfoAl8uhqZGj4FYNwxVrPpes9kOIAcf8/992WP2ewoDfaPdQycO2u95RgpOxn847/POVjpUR+tAnH3hXwLYgy1eq5XHHY+572HlwZdP3zLrViqXbliBGEwuPKk5B9gxYO0nny6G4++1W91mGoXVkz5oeeX6YJX6eloRx6M2aIVwv7zsbvMvE1vBhrYonw9/HzkIq9vry2l5kIdmfculF6p76FACTy7C3IOgFQdrATC/5Uy+8aT37SdMRHhxB1QqXWeNCbvgBoooK/P4lmftdcxv8x91C9+AY6irTLKQMvLXn9zJW8FEvCsy5KIbZe0W+71fW+tvsRIcetkug+/beUiZmchjIM4NQyNWfQcFLfMGY/29pqDlBRf5JssHCU/suFezXbTofVlE71rv/Rv64D/kZQ4eHt0Q5JX3o8c064tj69y/t9EZK0ybgVH7ZcvrjpS73F7qs1tVP+i8x20JnG5h9aQPWl652DjGWGWLOB5rDVr6QCu+z3ZtCOLb6fbVElFOpsvpAp7cFdRixb88hLScAdQAQSsmY9ka+8JgXbR30wXWjfKA3eUgrxt1k3WXN9ilJQu74AaKKqvlNnqlz2kZsLBBs3YX3+MRF+hay2QsutfqjvTeS6ApY62vX6sOHjLlG4JAe/GPqteoYyDGDUMnVn24rXRC1+EDD9IHvOtQewO6lZ5mXeVv7KbJgLE9/pssD0Hy3+OL3hfeBaoGHI8ctoODoUUXtO5bT+Oa/VVpyiGO72ODuV+1u9J4F+p0CKunoKCljDuMKlvE8RgUtFp+wboin6dJ8SEakXxeRbxPpBjbu18ANPXFBe0PQD0QtGrQ2/WE8ISSbfLlR9QnVOLeZF9+WHNDq1/YBTdQVFkF1kWTPUHkPqVkGn6eTq3SdKc4ailT+ABdfRlref168G+/yg1B0FDQCjoGYtwwdOLWx9NBA7s13WksaL/Gx7uFkINWaKCJIXpfeEuTJuC4piFoid1ZoYLLcWrgeX9AHdpKQ/eq69UjrJ4Cg5aj48FH4pUt4njUBZPoBy72qedVxPtEirH9a7vt99bVl7uOZn8A6oWgVY/bF9Kuri3uk04XNgtdRkzETZbfmHWDuxsRdsENFFHWIKwF5BT/RvzWk9LYFE/8MnnjYNgAVV/3bEgZ479+naJanlJC16E4fiekzEzkMRDjhqETqz74uLLsVm/QMWulDXrkno9p+X0/XUjLXcfBwYWXRRnwHFP0vvD3DuniUcadBZfXogtaSlir1630+MOPeA9Q7A8+pmoRVk9RQcsTUbaI45GfA16d3kunnNea3L+eXrnX3/of3XWof59IMbaPPPfcrsOAcZkANULQakDggM6wm+wC7wKkvdA3IOyCGyisrFEWPEwfWRe15+nd+zTLU963x8lno8bp8NYJdexMS6c6SSBX1z7XomWNPdCZtVbIUzgwi9c4g+GfpXfF6SfC6tU9BkLGFsW4YejEqQ9+o5HrOYjbqnfwMXpGXs72hQ+Gl45nt9v18BPxHyQRxNkX3g00+fLD2sHwfCyS1x1aT9DiExqHfF614OGvkYc0BG4dyOeY8WDwMRgkqGzuedBDQ9IAcXHaC7dO3e5W/XnTu+PKBS13jGLAQxqGu3wzvVLHcatlpGnk4hRNTU1R5fSA9liF2QtBK461m63JSTuEb/Li4/DKN3Z+sX7TvFjd5w2eZ9uc4K1AtVz8YopzY1KEBQLLInp337P0QfdSeqZFeBDg9tvoGT5NgfK0lce92bIuRmF6DJX39BqbRoL9rfXe+2lotzB/k6aMde1zTYSWNml6h8cfXksfsd/jY2WW58Ryj4GtNNR2p7vfsY+BODcMjTj14d6YzXruWBQwzlDgPvXJPsPVd9rrs8+/4wn79widz0cJLsJYsE8PbqGhh73Pf9qmd3Bb2/ZJ0zvcQ6/tdAKAWW5vuoJ6glaK2vnDC2x6h6776WlpmpND6a003id94TK/PHyQ3UonOr0HNXxTYoS0ktbCPcfe6aEjzmSrrQ884h6b6nHmletp4fMPL5s3JcjEzqX2ZLu3s8mY/V3Qbp26X8LsKSTsyXnZdBgP0inn91V19Vzvce+Ktb33ZVee3uGZjifd4QuBTzbW4/UxK2TZqlTYa6jrwKyFoBUHv/jqZDUTFYatz7zVo46BqEPUJJI26YITc7yJdxOS5h1S9JvrBo/RSt3VFjzZqXSRDRw3dPCFwC6QWDfjRrEJW4VAoXhjOo6BkMlaBfJ+1nMMWI+vB42FYzNjd/MboyPsMxzup4nDdnDTBZewyUTl9evZFyZ0ItFh+fisL2jFGqembBPymZrhT9fSU5fAz+c3dthRzpuQcoWULfD8HNpCJ/rsz86rU7O+dgfX1+TB3faXNLnOYgUlWcT+/F49b6LGg07ufnB6W522jlDZDVpTVDnera4DsxaCVhzWT4g8IQwYdX56RPn5GQe/WMsnsvXzDpqfHqlTXTemmoOWMAhe/KkK66dxAn6CSKL+1IdDvsia33h7u/hP1fCfd2FPQTkXUuWGMUNBi4n9E0Te+i91s4cndvv3O/AYiL5Z6PazrmNgwUI6st9p1XpT/xTh5B7/jcZY1EanXt0tjOmyfxrplcW3umXQBhdrW/PzZ8ePUHdKmKt3XxzKT+ME/kRWvUGL4U9eiu9jH6dnzM/UnpBWKpcz2NwtP//ZpoCflKqXca/wUzVMdiu9u/rOwPPGHQQvHs+RZbuNdok/ccV+SsoZ16c9Bszr5ivPCg/POD+L9C6bgJRfh+R6nqGgxajXpZCfIGqYQekTFQStOQpBKwmR3XEAV4rX0jC552H/MtZ1spnPWq+b6R0A6vbrAlV51+EezXKYtRC0koCgBU2Lf/vfTafa5GUpbzB0yAMOAFADo5U6tmdprOJ0HZZHqFteB2Y1BK0kIGhB0/Ke7mSP3btdJOx33sTH+3HsAjTONwjeNDFGmdWa9WBWQ9BKQk1BK3p8gV/wpIgQjo/niks3rmM2eCYdMKiZe2s7HdEMhoak1HoNYHAduCo4Qas6XqLCUC91aKaTgNkPQSsJCFpNCUHLwwZDf/CqMPhcGNStDtSHZNV6DWBwHQC4WiBoAQAAACQEQQsAAAAgIQhaAAAAAAlB0AIAAABICIIWAAAAQEIQtAAAAAASgqAFAAAAkBAELQAAAICEIGgBAAAAJARBCwAAACAhczZo9ay9TP939z8kl+l/L1LXBYBZpvW85vz/B326dpu6LgBAAxC0ELQgScv7aHi0RJXJMcrIy+DKQdACgBky54NWqVVdFqR3qEClypT1a+xT4znq1qwzY7bmqMLKwVTy1CsvN2XO2MvHXleXwQxxPycErWbGrwcIWgAw3RC0YgStlsf6aPB0yQ41XDMFrakqFfYayjoIWk0AQeuqgKAFAElB0IoMWh00XLIDS+lkhjInK00WtCpUYa1s5wepXVoHQasJIGhdFRC0ACApCFqRQStFrYfGqDw6aP1/9/FmC1pjNHK0bAWu/A7/OmFBq2VLlgqlClUnnVaxySpVSgUa3NHuX5e/z5mM+e926jtapHLV26Y8mqXuJerr21qo+1CBSuNVp+XNNFGmsaFeJRTOOKOD+tm+TDjlcsrWZajr8nqsHO9Wlrn1IxwP7jESqUK5rer71ces6/05KpaFup6sUOn0IPWuk1o7Xx+zl5tl9r9GN+XG9eWy68D5O6u740Wq8GOnan6mB7rIUMrklEs+BsxyKWUKW7/q7Mdqed1Gy+ZB0AKApCBoxQhaomYMWpkNw1Qy/7/6/oDvhqIPWgalj5Soym9iiiqVjqS913GDxJgZzISbn0jTmsZCWWY0YH1T1Qxu6jYzZPUAFfhYO1mlQAPSDb3pg5aRpuGgz0ZX7rqDlnksHeilXFl9D3bcjO1vlV7PPAbOBJTLCu617cdUtUTDPWpAq69sfghaAJAUBK3ZELRSrZQ9x/6/SNnl3jq6oGX08O3MQHV8gLqW2TeullVpyo7ygGDe0DbK72Orlkao19qmhbqHik5gK9PIZn/52n/rjGkzb465vZ3Uwv5utFLX3hyVnBax0m+l1rMZ0U7Zs87NvDJG2e0rfWWz9vH9fm1gVQILowla2uWJdR0a1P8+DycVGhvqo06nhbFlVTf1DY1R8ej0BS2uMpqlNDsOjA7K8jBVGqYO8fV25O19rxZpkNezU67ye3LQMr8AnHCOP+uY6aJWq3WxhVZuz9IYD8bme3T6tquzbBIELQBICoLWrAhaKfemVjnZ666jBi0eyMz13uvTdKe00+B5Zzl/HSFoqa1Q/MYst5r1Ut66MVYov1NtgTB+XbADWsTNLxH85m+GyUFNV5S9TB9YmzJobRyhsvX6ZjjStPZoNRi0yseEFk8maB/5+2hbPCXLs1R09kN3zKRWD1qttmFd5DWVTYKgBQBJQdCaLUEr1UkjF81/Vws04IwzUoNWhsasbco0wlusJMaBor1/Zgiy/ua+jxk+QsYv+YLWZufmb9ZRWvMeXjnCb35J6DrGxrOp3aycHTSqVNjj/a2Zg1bHEafl8FyWWjXLtRoIWtXTuoAe8HlutLu0rbo7O0IDm1o12zr2O2W6OKK0WNkMyp61X6t0pMO3rK6ySRC0ACApCFqzJmixQft2SCoessejKCHIGcsVetMRgoPv3wHbKO/B8JtmJP1rJol3s2lDU0q/P80ctDKjIWUL0kDQqul9TO17C87+O6plKp60HywRuYFRN3bLwc89uQz1lk2EoAUASUHQmkVBK2X02V12TquAEhp4S1PYTX86gha/kUfSv2aSooKJbn9Cb+RXOmiFlS3IDAYty5Juyhwf8yb7NZVP9vm6E3lLI4IWAMw2CFqzKWiZOoWpHtTQwLtRSjS8QfOaKaHr8LzT6hDwPpz6HsI2V7qONPjnxwa8y8sY3nWY3+n9LfRGzh8uCNrXiPprVNT+aAUGrXQyQUtgLEtT5iRrvapS4UVhGS9T4Lg9oevwt/4nCKejbAhaAJAUBK2kg5aRtsdOsRvB6YHoQcFxBd3AnUHFbAxS1rkBeSHIm3y1ckIaNGzpdJeXj3aGv49DG7RS/VSwniwMHgsWpczmQZqsUGHvND+ZuMcZiF8tUlYzGN5e5o1zY3h3Y/W9Pv/6q83gyufhCjoe3FbEEg0KA+ynDd+fgMH9Wnybibzwd3E6juSCls2wj7FjXd7f3G7tgEH97ngv9ZiajrIhaAFAUhC0kg5avm40/U/l1CUwAPHH/YtUdJ4gFEMQH8elTO/wWB+N8GkPquZr8lAQ+D42fdAyqO8971H9/P40dTjvw6ZR6NjeTyOnS+q0AwK3zqTQ0zj+ROSUMr1Den/B+nv5mL9c7vghNo/TlhZi+9faM0hFcbLTwOOBh04zqJ0bpPQqtr28TiOE/Zmw63qlM72DsaxLP72DG2qq1r6zVqZB/tlbpidodR8tUun0CPVv73DLZE/XMGi9t/jAgfhErDy9Q+fOEbeuq6MZZdB/PWWTIWgBQFIQtGIEregJKNUbk2srb9Fo/GbgExaA3Ef+bf4QFD6R6NRkmUbEFoWw90kFBa2U1ZKnnzzSE1YX3nohdVsno2fEbjHTlIndyJVWx+UZGuOz4UvKx/P2tASBQcs8fvj4I8X07JvRM+zOTaaj1nOr/hi4mKO8FXbUctUTZsLOG3WqkJS/hVDn4gilNaG7nrLJELQAICkIWkkHLXEixgZvBj6hAUhoHZjShCDdz5wE/VxL6PuEBC3G6KDeIfl9qlQtFykvTKypw+fnCq/b+hnr+mnkbNn7CSITKxefVFNmbMrSmPjzNua6Iy92kMHHvYUELW19T/e+Lemm7EnpJ4Wsn64J+Ikko4uyo04ANMN18Wg/dRj881TLVVeY4YPgpf0Oq2drP06XqCIGx0qJCkO9VvmU9VN1lk2CoAUASUHQihG0GsYn6FS6SyBI32nejVmgfs1ygOmEoAUASUHQSjJoWeORhJ8PKY+EtHoAZyzrcFrR1PFSAElA0AKApCBoJRW05LmkJsYoE/epsDmMdwNZXUy68VIACUDQAoCkzPmg5XeZ/vcidd26OEGrOh4+vgT8rKA1WaXB59j4J3X57JTxh/JI6hgqqFHrec35j6AFANMPQSupoAUQG4LWjEPQAoAZMmeDFgAAAEDSELQAAAAAEoKgBQAAAJAQBC0AAACAhIQGLQAAAACoH4IWAAAAQEIQtAAAAAASgqAFAAAAkBAELQAAAICEIGgBAAAAJCR20Nr26nX0zYUb6VX8Zh8AAABALDGD1s1UvHAt0ZfX0Hcfz6dtynIAAAAAkMUMWibjJrr0yTVW2Po2fxO1ycsBAAAAwCd+0GLWzKevPmdh61r6YkCzHAAAAABctQUt0+bD86xWLbp8vbIMAAAAADw1B61U6uc0/l92F6K6DAAAAAC4OoJWitpevc4KWi9rlgEAAACAra6glTJ+Ql98fg1delqzDAAAAAAs9QWt1C104a/X0Ndvyn8HAAAAAK7OoJWig3/+Pn2b/5nydwAAAACw1R+08t8nOjdf+TsAAAAA2BC0AAAAABLSUNBC1yEAAABAsLqDVvECBsMDAAAAhKkzaP3Umt5hvFP+OwAAAABwdQUtTFgKAAAAEK2OoHWzNYcWfoIHAAAAIFzNQatt4Dr6jv2o9N9uUJYBAAAAgKe2oLVmPn31OWvN+h79fbdmOQAAAAC44gct4ya69IndZfht/iZqk5cDAAAAgE/MoHULjZ671gpZ3308n7YpywEAAABAFjNopWjb4Xn07cc/pl2GugwAAAAAVLGDFgAAAADUBkELAAAAICEIWgAAAAAJQdACAAAASAiCFgAAAEBCELQAAAAAEoKgBQAAAJAQBC0AAACAhCBoAQAAACQEQQsAAAAgIQhaAAAAAAlB0AIAAABICIIWAAAAQEIQtAAAAAASgqAFAAAAkBAELQAAAICEIGgBAAAAJARBCwAAACAhCFoAAAAACUHQAgAAAEgIghYAAABAQhC0AAAAABKCoAUAAACQEAQtAAAAgIQgaAEAAAAkBEELAAAAICEIWgAAAAAJQdACAAAASAiCFgAAAEBCELQAAAAAEoKgBQAAAJAQBC0AAACAhCBoAQAAACQEQQsAAAAgIQhaAAAAAAlB0AIAAABICIIWAAAAQEIQtAAAAAASgqAFAAAAkBAELQAAAICEIGgBAAAAJARBCwAAACAhdQQtg257aJhWHL5Mm/70D9eqx+X1YEYtO0a/HDE/i9xn9Mv/f5u6HACa3+tjNDU1pRh7XbNukziY/yF9k7+J2jTLUmt+Ql/897/Qhc2aZQBzRM1B69bHz9MTQsBC0GoOdz0nBN+3T9FdmnVmr07KnCxSuVqm3FZ5GYBe5+t5KparVD7erSy7Yq6yoHUw/wOiL68h+uQGOmioy3e9+S/0HVv++TwaXaMuB5gLagxae2nFH+2b+aP7BjXL4YqZ0y1aGRqzbkgVBC2ILXPGDjGVZgpaPt2UG2/eoLXt8LxYISoqjAHMdrUFrWWnaD1rMTn6Ad0tLwO4YhC0oHYIWg1YcyN9zcLTlz+gS7/SLPe5mUY/vtYKW9/95af6LkaAWay2oLX2Q7vbcM51TUFzQ9CC2iFo1esWMzj9kxWcvs3/TLNcY8V8+upzFsy+R3/frVkOMIvVFrQePx9/DNCCDbQofZHWse4sZ+zQxpFL9MhzGbpjgWZ93lq2P2v9e8HSQXpo6DPayP6W+wc9+sYpWrhQs12tnH1Y/xzrXjPotv84Re1HnDLmPqN1+wb15UvdQ2t/55SH7cu7l2lt/zDdLZVp8X5nzNoGeXu/O3Zcssvx/A5lWWy8ziT2vmnWZ8T9X/AULe4fp0ed7uBNf7xM7c/tpdu0+18Ho4P6jxapPCGMN5koU/H4AHXpuhD4+JTxnLSM33CEIBUwlkVn+m5SLdS9P2eN63Fff7JCpdOD1LvO8K8r7Eu38jqa/RG2sW/8BnW8aL5Xhb9PlcqjWX29WeuOSOUy1z+bo8yWFs36tpYtWapOeutXSgUa3NGurMfYocQpL/tcjxepwretlmnsQBcZmu3q0b5jkAqlivI5ejSBekk3ZU+XqFL11quWx5T9sQN5DGcy7ja9J52ylIapQ1Nepu89u+6r7w/462FJJ/UN5b16tspVpJEXO2LUV7ygFRYYK+w9tcdgiox1/TRytuw/Bs7laWCTdCzLdl7vdBleRznt8aj38vF/trsQ/8+NtFmzXNVNw+dZvVbN/dcflwBXg4iglaVVmhu5Qg5eCzO0gocXnSMf0iI5NPHQYL7Wwif1A+43vX0iOuBF4WHRDFR3P2+HHdkT+7K0QNxmwQ66/9BnynqWd8fp/uXehemu5+1B6e1PtanvLbh7l/16UeuFaiBobTrwYeBn9OiuF9XtarV6gAo8JOhUCjSwWtqmmYOWkabhkhBkJMpNroGgNWUGqt4TZeU9mOpohlp9r2VQ+rh+3eD3N7c5UqKqvK6lSqUjaSUE8Jv52IFeypXlbeztxva3Su9Tu3azDvTlEkn1tjpDY2KYl8sl3KTrCVqpjSNUtv5eomHtF6g+ylvvX6XCXn9I4fWmU3qnU/NaouSCltFj7pMQ/vzKlOsJDlu5v9itWd/858+VZaGMn9AXVqvWD2m8S7NctqfgHQvVAvXLywGuEgkErV/S4owTSo6cpyUrHrZDy4I2umPtKfrlu/Y2T+zZ638vHhpyzmuOjNPStRutbResOEXrrL9/RivWymWsEQ8azvts/J1ZxmUs7Bh0mxvwzPC0mG9juOFp6dqnaIHV2nMP3bpikFbxoHL4GN3mvP6Cp8atv4WGnRRv+ZqG/RHYrxnx3nz/HY/uydJtt6fsFshdTvDMnacWebuatFP2rBNKKmOU3b7Sfj2jlbr25qjktDpU3+/339BrCVo+SXcdGtT/Pg9ZFRob6qPOJfayllXd1Dc0RsWj0xi0uHGz7npazToyqOMADyDSzX55lorOzTG/t4tanRYGY1kHpVnr29kR5f2Nnpx9AzaDQdcy+4basipN2VHeimS+x0b/NnJgqJhhMM22NTooe8apm5AWn1gMM5w7x0b5vQGnbAa1bhqgvBPulGPGPNYGzzvLSjkaeMxuwTOWddHAcR4mSzQoh/pUeEDx6zBDtr1u6UiHunxn3n6fSp565fcw67R4ctD9XFg9D55z6isyPCQUtAwzGDpfgtzPMSUdA+a+9Glbq35aW1iSnHJC2rcnY3Q5ImjBLBERtCRxug4f+oAetW7W43Sf3GrFrOLLL9KSu4W/i60zI+dpsW9bww0R63Y85X+9WglBY+PQCbrL1022jZa+bS9zu/7uHqR2K5RdVl9r4bC7rO0h5298HNs+uwuUsadeEEPVU/SA9T5ioGtcrUFr3XNSt+UCM1g7+7N0mWbbuHbknRu5/gZn7OTLi5RdLixr1qDltmhUQr/p+zQatC6OUNp3oxNuuvuFv291QtNEIeDGKGul7DnnJvten7TMCy2Vk72+ZWLQKh+TWrx4GabGKKO8Xw34jdWss7S8jIfDCTMAiH/nx5o2GBjUd9oONbqAFBZQZK2Hivb+a8Ik7zaM8zoWwwvHI6HzSyUTtNx9OW9e25TX48dAlQp75GWmp2+gb1n336fX0x/kZTFs/t3/sLsPL/w4xqB4dB3C7DDtQYuPPXriZaHp3WcHtf2O3cyl1hw3aOkDGp8nKjRExMH34eiHtFAzFomHFXdesA3O+m+eUNa1AmDGXn9tzwb7b/efoHVs/QPDTvfjBrr/sL2O14rn1EHDLUd+NQWt3+k+Qx40GwtaXcfsrixlvIor7dxApIt5kwatjiMlu1znslK3XYhGglZAaHK778SbrtHvtgJVLxa81sNAvK7Mm7zUasUYB/SBgr939XSf5jPlr5lg0OKtRlLQ4sda5UTavz7H61TsCnSEBRSFwfdR7j7k3Yb6+tSLe7wmE7Qyo/b6xQP6Lw3dx+1WLd3rpQ7PqyEoafzqf9lB7W830EF5GcAsNe1Ba9Eeu9sw7GavhBnGDVrnabFmm2kTYx9Et/XYXYF8kL5MDYBOdyt//buHqd0Mlevf/kyYFkNaZ5rUFLS07z09QYt3s2kv1A5taGjSoMVvTGH7o2gkaGm3CWb0DLvdsRY2QH80Rxmr21Faf4O5rrVeQCjirVPyzdn5vGqqg1q53aBS12FPhgpu16E/vPPPJlKjQcssx4BzXPtax3g4DArhRgf1DhXU8liijtckglYXjWjH2Kl0r9f2phO0Pp6vLIsl7bSIffmvNCovA5ilpj1oteyLvtlfTUGLt9DFD1o8rNj7YY3Zypn//yR7389o+SpzncXHaG3Ia9arWYJWnGByVQUtp6xh+6MIDU0B+xO6TQTrhm7PdC7eLKtnB/1PKm7m3aBNGLRM3U4LlVbVLLPUFS12aYZqOGilvG5KobWPf6kYe13TOmSkAx4c4KKO1ySClveaUXSv53b9IWgBxDbtQYsHD2Wwu8vrOrRCB/97kwYtd/3Dx9RlQteh9/Qg/9s43Xe3M7aMdSM6458e7XvB/OZu72tDUztoNEvQ4l0PbOCyvMzmdR3mdwp/DwxafP2gG1OyQSt6fzRCQ1PA/oRuUwNrSoExZ9wUe7pNHJ8U1AVmc7sOzw/6WmjCbubTZvWg3dpWLtKYOL2DNYVGlrqdBxBEod1cEWrfp15nEDnvJnS6basFGtB09bpjoczPeaWv7HGP1ySCVsCXnLga7TrkQQtdhzCHTHvQcgeD//GiNKBdXv4hLRLHSDVr0OKtT7rB8EvMZdbg8Uv0gHAhtZ9SZGHF/skiO4S10ZI3zHWPfEB3O2V45EnNt+AGNEvQcrtTqkXK6gbDu8ulGxT/+0ReWL+dMqPeE3/6GxO/cUnBbbq4Tz/pB/drCfviG7wdtj/TFbQc6RNOWBkVW3O8J+jUcU2d7rLyUf/UA2E382jCdBITZsALeKCAh6agsUNavJ4vjlCnvCwCb3mtKg8FBOs8are4Wd2HznvLDw5wbrfmWanlegnvIg06nrl4QYu3qin7sTqjPZ74mEO5GzYWPsaqzsHwbtdjrKCGwfAwO0x/0Eq9QG182gNpeoe7Oj90pmlgTw9KYaBZgxYPSH/yT+9w2+oT9IgzGas87xaf4qH9jYskPlm4YDP792e09rD9FKKvRW8aNE3Qcr/5TynTO6T3F9z5e8rHpJu2O36oaq1vLEvTIJ8mIvTG5IWHqTKbcFEzNqkhwv6YQSG/P+22ULBpBLTTOwj7UnqnO97+1BO0WH2ezVF2Zzd1OI/pW+OahCkR5CfuvJYWYXqHx/pohJeNddGJT4OmGgxa7kByxzl9l7kbGM4NUnpDB3Wsi/E5ClMVVEt5ymzv8E9xsWeECqUijWiOG/chB2lqjFDLnVa30jBlrKcNK5TfoVkvJQRd8wsH+zc/VtyJXuXPXxEvaLn7UTVDrDVBLRvXNkhFPreYfDzxlkP2eY4OUt8W7wEKa7qSQ2xS3oK+aznFp3f4Pl1Ky8uiuXNwHf+5skyB6R1glkggaJmWn3ADlU6nGUxulbdp2qBlWpilVcIM9yJ1ioiU12rHvHnCnWPLHhjPt218agfeTRtOqs/Q/Z+uoBU1IaI98ab6aHmr0NojuJijvDUlQfCNqXV/8ESXYTepuJQB5xI1gATsCxO0P/UELb5NkHJOmiaCEVvVJJNlGtG0ODUUtIRB7pbz+h+k96b9CMB+VeBoP3VI+8PmBbPHnQUJOG6WmwEw6DPVjOmy8ekxKlRhAS+sJW0rHw8nmXS21ZQr1pgz+fgI2Q+r3uX1U3Emhg0Yw5fy5sL6rnCTsiwUJiyFOSqZoMW07KUH9l+iTv7zLqYnhi7S0s5t/lnXuWYOWszt22i9M9kqs/HIOK3ofkH/czV8ioc/ya1LbXTfAec1pmFqh2YOWozyEx8m9vMjuf12C4+8vsXoouyoMyB60rux2jcg9cbk0fwMjWM6gpaF/czLSeknharB44f4vng/cRKxP/UELWEQvK+ex0tUGOpVQomnhboPCU/DBf2UkKOhoBWz65DV17Azj9dU1dyfCf8+uft2Rg3pxrpeGpR+goe9RvlcngZ3dgYeb7pj1BIYtMxt9noBoPTbVmW5qGXHsHdMOscKmyBU+/mn6gxarEybsjQmHvvOz/xYLYma9ZmWLRnKyfs+EfLEKif8BM+pwONLtY0PpMdP8MAcU1vQAgBIhNcCWD2TVQMi63Z+x5vpXTeQH2bKzXThr6xl6hr69s83xRhrZTIa63IEuJohaAFAE/CexAsa8+TODh85ozokrutH9I01TYMZnH6lWe5zM41+fK3d3Tj67/GCGcAsgqAFAE3AGzBv/WahMEDb+o3MnYM0xh9ICOgKg5m17fA8pwtxHo2uUZdzB/M/sLsMP7mBDsotlQBzAIIWzBmxxr8I6huPBPUxKH08ZLJSjj1ZFzTGC2acG6Iu/0/KLVWXbz7wr7HCGMBshqAFcwaCVrMzqOO5QSqUKlSVnqJjg/vHjmf0Dx3AFXQz5UZ/SN+cDBirtWY+ffW3eVTEmDqYwxC0AAAAABKCoAUAAACQEAQtAAAAgISEBq3du3fT5s2blb8DAAAAQDQELQAAAICEIGgBAAAAJARBCwAAACAhCFoAAAAACUHQAgAAAEgIghYAAABAQhC0EreN7jvwGW360z+o88AxuktZ3ixuptGPv09fHb5Zs6y5bXv1Ovrmwo30Kn6wFgAAmgyCVtKWnaL1ZshiQWvTny7T0mWadRq0YNUxeujwZdq4L6ssi4eFrGutH4f97uP5tE1Z3sxupuKFq7XsAAAw2yFoJS75Fq27nrtsB7n99QWtg/kfWEGFPrmBDl6NrULGTXTpk2usffg2H/DjtgAAAFcAgtYs0EjQatt9PX3HQtbn82h0jbr8qrFmPn31OQtb19IXA5rlAAAAVwCC1ixQf9D6GV36Gwsn/0RfHb5Fs/zqsvnwPLtl7vL19IersWUOAABmnTkWtLbR0rfZWKmLtHhBim5dMUwPDX1GG3P2GKqNb1+k+1bco27njLNi/79g6aC9DQs25naPvnGKFi4Meh/J26eCuw75WC4rLP2SFqYv0rp37e3W7RukO26P8fo6Ie+5+a1/sYPJf/2IXtYs5xbvZ6/ljC9bsIEWPXeRHv2j/fob371EDz35lLKNha3L9mPEK8/GkUv0yHMZumOBuG6WVrHlufPUIr+G6yl6wNrny9S2XF7G/ZzG/8vuQvz6ras/OAIAwNVvjgaty7TiufP0hBxKrJv9JXpAHrDuhKCFTwZs8/YJKcwEBKGQ0OMGrbfP04pD9pgunwPDdGvU6+sEvicPJf9EX7wqL/NbvN9+rVVPvkBt2vf9jFZtaPNvtzBDK47I6wmOfEiL3IC6g9p+x/4+Tvfdrb6/7UVafjRqnRS1vXqdHR7/+99CwyMAAMBMmKNBy/HuOC1du5EWsGUte2k5X/bGoP03TnxycMTbZsGKU7TOag37jFasld9L8Ph5e9vA0CO9h+mJQyfo7jsNc9k9TrgzA+D9mu1SdXYddv6IvrHGZl1HpyK62Rbvd8rltPyt3zdId7GyLdhgLnNC4eFjdJu7zS9pccb5+5HztGTFw3Z9LmijO9aeol86LXVP7NnrrN9G9x1gfwt7KtNp9fqjGdCUZQLjJ/SFNVbrB3Tpac1yAACAGTR3g9a752mx3OW35ASttQLFeatr0f07D0Ej8jaGG0LW7QjoPmNqDFpPmIHJa71KuWVe9bhmu1SdQevAv9otP3+9kTbLyyRu0LL2c4d/OS+32O330Af0qPW3cbpPrmNmFV9+kZY4rVOL9tjBbNUG+9/WPouh6v4TtI5t4wt0OrfQhb863YdvyssAAABm1pwNWvrQwrunpJYVJ0zoQgMPOeuf26Ysc9UUtOzxY+IyHnT0Za4vaB3Mf9+eDuHPNynLZPz9O/tfVJa5LU1/MkOo87c7dlyyA+PLGc36DO8q9FoC+TbtT9ldkFbgFVsKlzv1E2OusIN/dvYt/zNlGQAAwExC0NIul7oCnRDEg0TNagpaXmDhEglaNYQR/v6hYVLAW6fC1lf2yakjvs2mP16m9Wbo7dzlhDtpeRgeIuncfGUZAADATELQ0i6XnmybhUHrD6P/X2JBq2Vf9PrKPvmeumwz/ztor3P0A7rbXH5bz3hoHYgQtAAAoFkgaIkWZGmVNeB7nO5fLPx9FgateroOw4KTiJfHG+wu87oOl69y/rZgkB5h+3BgmBaYn4PVhWjVmxl6HzJf83n2mmFTO3jcfYsRIgEAAJKEoCW49Sm71UQJRE0etPj4JiukaJbrtL3pTO5Zw2D4uEErtfZD+0nJP15UHzjwLf+QFrnj0ZzwxerIXG5N4XD3ILWzucr6XnDKoI5f0ylewGB4AABoDnM2aK3dsYNutaZPMP9++8N096bz9KgzVcOqx6U5oZo8aLnBxSx7e7e5X77JTQPw6R2+nEejMad3iB20Ui9QG59DS5re4a7OD50pMdgTjOLr8Skexqn9jX84Txa20ZI3WCAbp7Xsc3O6EdX3E/3Umd7hn2m8U14GAAAws+Zs0AqybteLvqkVLLUGLWGqhjC+4NRI0DL3y541XSMw3P2cxv873izq/P3jBy3T8hNuoNLp3OefwoLhg+gZ/rcFvJWRiZzaAROWAgBAc5m7QUsMAbnPaP3hD+m+hzZotkldBUHLdPs2WtI/TuudyUBdgUFL+AmeiFDC37+moMW07KUH9l+izj965Xli6CIt7dym7eJ0u0D/dNn7+93D1M73JXJqh5u9ObQiwiMAAMBMmLNBKzS0zBXGv9PfL9s/w/P1mzery68ybQPX0XcsOP7tBjqoWQ4AADDTELTmODecfD6PimvU5VeNNfPpK2ts1vfo77s1ywEAAK4ABC0g1uU2+vG1Vpfbd3+9kV5VljezW2j0nFP2j+fTNmU5AADAlYOgBTbj53Thwg/oq8NXXxfitsPz6NuPf0y7Ip6eBAAAmGlzLGgBAAAAzBwELQAAAICEIGgBAAAAJCQ0aJ39y4euu+66CwAAAABqgKAFAAAAkBAELQAAAICExA5a8jIAAAAACIegBQAAAJAQBC0AAACAhCBoAQAAACQEQQsAAAAgIQhaAAAAAAlB0AIAAABIyP8DX7YxQXo2cRkAAAAASUVORK5CYII=>

[image18]: <data:image/png;base64,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>

[image19]: <data:image/png;base64,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>

[image20]: <data:image/png;base64,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>

[image21]: <data:image/png;base64,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>

[image22]: <data:image/png;base64,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>

[image23]: <data:image/png;base64,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>

[image24]: <data:image/png;base64,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>

[image25]: <data:image/png;base64,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>

[image26]: <data:image/png;base64,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>

[image27]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAaYAAACfCAYAAACyc33SAAAb/UlEQVR4Xu3dX2wU170H8LS3t7pXUdSbqs29SpusjCCQQdbyJ+KfTSD8MalZUxySWFwbX9u44ACmjkMCjoxJMHZjU2I314Fec5FLqQHJJHVAXSuSu+rGolsLp6ISaqWbtz7mLW99+935c878OXNmdmdm1xmb78PnwXtmdmfPnjnfmTNnxo8kEgkCAACIi0fEFwBgEWocpezcHM0Jspca3MuaGmg0415nLjNKDa5lvSiUem2AxtNZys0632fiHXHZhafyJ4/Tl589TucUdxmEh2ACeBh8TcFU9c4E5cT1F0kwaaH01d8eIfrbt+nuT9zlEB6CCeAh1HOrkGASqCETLJg6aTzHPudmL7VsUiTLLFC7nqAv/qKF0jfpi/6n3OUQCYIJ4CE0L8HEz9JmxqhdLFvQnqKp32uh9Ah9NfYkVbrKISoEE8BDaF6C6cS4MYxX6PILxP7+R/VQoj89Tuck5RBdsGBSKqile5QmhAuZuUyaxvsaKOlYvoJ6P2Hl1zvd78WWGbhjLDP9Qa2jLLm3nQauTNL0TM4al57N0fTHI9S5WzIkwI/ObvWof1dR+wfqumwYQV/vZi81rBE/30ZJUdvgOKUzts/LTdPkpR6P9RRKvT5Ck9P25bM0eaWL6hb4hdBkfQ+Nfjzt+I2z6XEaeC1Fin1Z87rFBPVI3od3fq5rCayDMzpFrR5HaTLr/K3kdSipc71NjFJPfVKyvEHZ3UkjwvfJTU/S6Nt1zu8TefvCK7jONYH2Q7l5CaaCl7euZbnaiv199H3bet34DlkabVR/41d79QkWZrvIqr/v65K6s1F2t9HAtTRleT+h1aHWLrr96vBJ+vyeMYT3oEssg2IJFEwNl2w/vETuWqejISgn2RFTbpw6Je+X2DxAaX3daRp52V7WQxOS9zfNpmnIsXzC6iQzE2oDtXVcdncGqErcBs3OLhrnHY+Ee2dRqOXDaddypulRailyxzU/1O81nPa8WO3qYCIG05zawbddltdj7mYPVYjbdkm+rHTbmCq1Dcou+nPZ613uNhFq+8IKWOeJ4PuhTGmCKc9+a+d4jyjBNEfp616/cZbGjkoOYhP52oW8Peu6HjPOlj77Lr0llkHRBAumD9Pq0aJ6dNqaoq3sLELZVEddv+I7rxoYe+zr8IufORo/4X6/ip+ljfU+6RV2crWBZyZpbLCdGnZXsJ0sSVtbB2iSHd24zsLMTpKVp0eoTb/YmqSGwUm246sBuF/cjloaSrP1cmka626hCj1UFKrY3UI9V7TXnOsoR8fYZ2Vpoo8vr21fL02wgMv+qj1v55DPf12ZpQcPHuR3+6xr3TAUPvSibf/NAWrfy85C1mylhqMDNKGerRY1mDj1YKK3Wfud1bOTs3wWl9CWNvfSJPsNx07WsTrX2l9KP3uYFLdNs7PXbC/6xfftxvfR2+wlHgZa2xQ6rzDbF1LgOk+E2Q/dFlMwGbI0/k6tfqajnSGPTbPXbzrX0b08xA6ItX5ijHr03zahn4mmWnto7M6YtD1rRn/7DT2YvvyfH7rKoHgCBZO3FqthCZ142xXj6M4VJLZhvIl35Ec1MsrZSaPBTY9Qnb3MFkw5tQE7j4K9G751VjdJvTvdn+dmDVGmf1blLt/JzgK9zhIDmN9gqqWRT43vlb3cUlioFiOYPh0Rzi5tv5W9LfHPmhmn9gLPRnnbk58pK9T+K1YuHhiF2b5QQtS5L+/9UFSaYAq7vPf+qcsbTNM02uzsQxTPz1ao67oxopL7uFfSLvz8gO7+URvG+yf6vEMsg2IqUjD5NCzeoYgdNR/GU1/vKrCj0Xk1OLOTVANG8n5enWQna6TZK22udeT4UaH8c6y6MMa+3eUxtYcfRarfa7OkXCZqMHmEjHQ9xZp6nPt0nHpbt/pcB9DU0Yh+1KyeEZ30OPBp9mibYbYvjDB17stnPxQspmDSQt21Dm+brs/m7ShLY4ckn+XrCfpCv2/pUZqUtAsonoDBlKQGbdhkOue6i5tzNyx+VOgczksNG8N4XoFgXpiccX+GtLGH6iR55yW+7mP/CE2L2yK1wIKpu9BOxCZUnScCdFhOSrPakdsuVM/NZimtDWnxoRgHqwPy/h34QYaw/SG3L7Awda4Lsx86Lapgkn0Hr2Ay9195m/WlfJ/+zoLpplgGRRUgmKrUhuAxqcBG1rAq+ozhN2s4L8Wu68g7DUU9ks3b+YsNLlQnmWeHkDE/Jx/5dwtiXofyCu5EbELVeSLcZ3H67Mkx58y8OW1YZkCYKcdDx+93+JqDKdTnhN8P7Xw7dS9Bt7fg5fPsh8UMpjxt1teW7yGY5knhwXSIX/DPUfpSF9U57uLO07D4hWs+bMeHMD4doVpxWds1nLnshHvIxqux52lwXp0kfz09nHKtI+fRmZXAvAYTrz9xWMuPb50r1PuxvM49f8Og1tRS++CEeaCQvmD/DXmblE+80fGhPPEG0GJtXz5h6jzKfmjj26l7CVovBS/vv93mdeViBJO5/+afIOKGobz5UnAw1fHp0eoP3SKWK2005tOwrAuORifBh/Em+yoky1ozeybPuq8NJNnZl6vB+XaS3sHEt2UuOya9nuDGz/Z8rl0sSNY1HOmkDhnzGkmaBhzXSJzT6cU6L7zDKkzLZTaJQZiBxa8fyi9yK1b59S7nUGDE7dOnImtDbLNZtY341WXwOo+2H1p8O3UvQeul4OX5PqXVg7NPUJpHaJoPVxYlmKzPCj5z9km6+ydMfpgPBQeTedSiTdflN66t2Uot3WOUtl0H8twhjo7ps99y13vYbDyvC77WzKLcJwPs5laFKl5tp4Gbtvs3xAYXMpisacjae07QwFFrKnJyu3y6eBWf5q5NF9emtLNpyPqU8fp26r00SdPXJdNUY86cxaYdjV/pMadXa9No66RTl23PQrvWSSmt3tSzmK4rznt/XHVecIdl0z2u30jbe7SBUuZZgtYuusypwa6zXvPsYk6YLq7+rtf4Nk7TiDjUF2b7TNbRv0494GlzLWMJWueR90PGt1P3ErReAizPDxLmMuPsBvok1Z4cs0JJU5Rgsi4t6OtqU/Rftd+SUth08a/GfuAqg+IpOJgSm9UzGfuFZ4ccZbNGw/LeIdSjOe0en5ms3mBcR6k2DX43r2aM9V0NLmwwJfLdbCdbp4BxfmEnWhCUFvVo0ud7iXWe8PmtZiZo9JrR6brqL0CHZeLreJHe1JznRmi13U68IzlTCbN9JtbO+WeIw4SioHUecj/Md1OuQdh3zH3Kn/hZpiD12Og1qUj9jS6z/bNIwaTtv13X/epD3odoKk8/Ztxge+87dF5SDsVReDAltJly6tGp/bEfs8Yjgrr2Js2G79lIVbUf8E4iR2NH3eWWJLVdsD1SSGU8bkW7mZUN9YkNLkIwafTH1tx0Pp5kbmaaJj9gZwKudayZUfZGrW3nxKWeBfwkZfV79QmTC9TfWXs8Tq/0sT9V1K6eIepDV/qyWUpfMx7/5NkmgnRYnG3Sg+sxPINtHr+RJsRjjMJsn03hQ3lcsDoPsx/GPphUVT+1PfpJZX5/vh1FCyaN0S5cj3WanqQR30cZ8UcSfYMenBbLoFgCBRMAwMOu6f1/ZQ9x/Tf8g8ASQTABAATyQ8r8gf3bi1/j316UAoIJACAo/KPAkkIwAQCEYP1r9W/R52897SqH8BBMAAAhNZ34Dn352eO41lRkCCYAAIgVBBMAAMQKggkAAGIFwQQAALFSUDBt3bqV1q9f73odAACg2BBMAAAQKwgmAACIFQQTAADECoIJAABiBcEEAACxgmACAIBYQTAlyuly7yn68y9UF/bTG/prz9Mt7W9N1w6qcK0jWFZOZ1oaKTP4prEO11tDB8RlAUBg7YO39ohlD6E9jWYfMlW/XH/tQMsx9loHXd0iWWeRQTAlltPwaTFIbMF04nnJOjZlq6xgEyGYoGRW0pnDzZQ5f4QubxDLFhoEk8Ou/TTL+hBeH1YwHVsEv3d+CCbVmRNikNjOovIEU6r+sLHc+Va6vGslJSXLABQfP3haDB0VgslhQw3NCMFknUUtht87PwRTwhZM5rCdtaPMtK5yLS9bd+qVpa4ygNJBMC1aZjDZhu3MYGqkvjLJOosMgkl1/HCHcHZkDe/NtJS7lrdYy2GHgvmFYFq0VuygKfG3NYf3GumMuPwihGBK2MZvbcN2/EzIP5gC7FDsiEd/v7KV1Hf0MM1cMNb984UOut2ykVJFPBJKrl5Hg9o1iPc62ZGW9jmdlDlRTW+UC8s/v48doR2m4aT7vXRb9hk7xoX99LZ9O8uW0MFUDd06fYxm+ff5xZs0e+4w3agtlwxt8jozdrCq7dV0+12+jep679ZT3/olwjp2S+iA+nn6OkNW/U0d3UFt4vfilpUb9X2eTU4ZMj5nsLI4Z7m8/Wht4GB9M81o2zXUof69VL8GOdzFvt979XRG8g/llPKNdPHEEav+hjpp5tQ+enutsKztong+svYYqE1EEbpNqB3xJnU712+jW2KbEOvCpLaH2ldo6pztO50/ZrQHSV1rjH2bdfply+mNlmZrXzx/hG7tXUmKuJ59/1X/Tu1U22A/b09qHXZsozrp/ht8+6QHHeZZFILJtNiDKQjrImR+js6Bdypd++lGv3tZzczhte4dIhTb5A2ZoVYaXm1ffiVdPGOU8VlAIn5WOXt8o2Mb89XH7FHn8vZO6NbRVvMir3P7mmlQttNqnXy3bQcXSA8iFLUuBt3LGjqN8BDXCYjXwe3DPOCZ3hoabndu72z7Rse6yqYayvCAFQ0d0Ttqc/lIwRS0TYQXpU3caKmnWVl9XGikPrFN5GkP2nXfYXv9Mfyg89betR4Tl9R2US20C173agC1tR6RrKN+r45K5wzekNsHCKbA8u10dtJgYmban6eXliWMI7bDrKEP1RfpaEjthM4109W6dXSgfAnrBJbQC5U76PZ54/PFDtKcxHF6F6Vc77eWrr6nrddBV593lh1oalWPFmvoTOVyekH7PupryjMr6W3+nVxnYbaJJRp157y4xdjG5Hpr+zJN7pB5g3fy2tmI+t30+tPWU8rpeF093W4Q11lKg13s+3bX0NurjTMxfftaWCh6hWAAZpvQOtSuHZRatpFuaEfgegf7Jt2uXU5J/vvbZ2qWqfXKDlJm1A7v4DPG60llFfV1sOHl/n10XHokLjmq9hW8TYRVjDbBJxIlV6tnT2z7xIOmg62s3tnyFXo9ad9JXYcf/Knt+SVh+8xryuz3Mete3Rf7TrA2Ju4H/PfjoXlOPYvbYNRjam8jO8Byfq+w2wcIpoiCD+VpMi2rnEeMZWqnoTf4QjuZ8JS9VgdZZy9bsY1u69sgdhoJaxgv0PT3VXT5HKubavvrtk7ofKNraEs2rKpbXU0Zvf6M4R5HmRc+ROnRuR8/anT+YocXlHsqr+07nqk2Oh4+FGOrw4p9zcYyaphVud5XDdVu7T3epBu7xDJN0GDy5tkmiq6wNtEnDCtK24TZXj3u61F20BQvFw6mzGBS6zbTJOyL/HcSDxLtB5bv1tBBR3uy9QP8e0XYPkAwRRQimM7tpYNimfk+0TuZvGRH7ow5w1DoqPkwXqZhpeN1f151Y71+e6+4TsLaPiGYzDO6U9vy3/DM1DUZR+ieMys9Pisos+N0zepUQ+VHbDlJMJ3p8KkH2/tKhyiLGEx+baK4itgmquuN13jwS/S9JW/PvJ3PHl3nDCUdr1fhWg7fhvdekR7kmMOD/HtF2D5AMEXktaNJ+O78xQ8mpXwtDWoX/MWnUXCS7VB+xGb+OIYx+LBUM/WtcH+ONRmhQ35twFU3eepM1gklrE5c3knL8XXyKlYwme8j+T1dwVROF1k95CP/zsGDKUybCKf0bcI8UPH57byCvbCJTQLf/dctyvYBgimiPDuUnW/DlnRkEfheUOek28GvediG8/g0VXUHcx9dLlV3cp+Lu0zUTkgTpjOxhmzy8Ok8ChE2mHg95CP/zsGCKXybCGp+2gQ/G/b77bw6/jBtyX//dYuyfYBgiijPDmXn27AlHVloS6nvFOsA+uupr3Kpc3qu73YkqO2Qc9jujXbt6No2JGVnTjPvpKmWjVTHLt4bvOrG63VG0glp+E4c5AL9fO344YJJMvwTSJBgitYmApmvNsFfEycp2JhDZcLN7/MRTFG2DxBMEeXZoex8G7akIwutkk2kkI/XJ2vZBXfpdiSsSQb6DsWG8fr3UZu4XMJ2VCi7bqbNOOMXuqN2Qhp+5hZkFh1fx2ecvxjCBhMf7hGn4BeG/84eF9ely4ZsEwHMW5tI7rJuQpVNhlm9i00uOEwXhWnw8xJMEbYvmirquZmjubk5yt0ZopZC95WYQTBFkmeHsvNt2JKOLDRr5tPsqR10gE3XrVi7jgY7+Owxr+3Q8CnWh2l4jzEbb+bQWslyttlcQ0fo6s7lRue6bCkdTO2jKdu9Q5E7IZ01tfrPg610NbXKMRVZOl3cNh17tnufPn3ZmLKrrbOcDu6qphunm+lixDoPG0zWzCy1jjt20PHnrDMZfQp8bQ3d7t3vcQuB/eHD2s24fAq4TNQ2Ubj5axO2s0BhOvZL26rpNvss171FiXkKpgjbF0njKGXVUNKCSTP9Qa17mQUAwRRJnh3KzrdhSzqyCA7wo1aZc8fcHaSAT2Oe6deG9XyO6FZUmveYuGhPL2B3xkfvhAzKJvUo0+vztO2VdDT5r61Er/PQwaSq2sPvgfHifad/RXW957pi3UZtEwWbzzbhe/P0Kcm0bsP8BFMi9PZFsrmHJnJWMM3d6nEvswAgmCLJs0PZ+TZsSUcWyRJqq2ukDH8Ej/k4mFXqURu7NiHdDqaMDeFpy+X5f1RKeSVdPd1h3XjIHnGj3czKO+yidEKc9ngh7bE69pll+iNetplnAiJzNppZH9o6HZTp2keD26I/ET5KMGmS65+ny/ZHEmkG1e+k3aTKbuK0L2+X2ske6SSEr7tuI7aJAOa1TYiPm9L0q9+rbq3nI77mLZg0IbYvqqqzk5RDMAEAQGzsHKA0C6b0cMpdvgAgmAAAFoUkba3votG0MflhLjdBPZvFZRYGBBMAwEInTHqYm52mkWbFvdwCgWCKpTxPgpYq1vWph1fBN+TaBLpOsVDY/oNq4bwnacA84ME0M02Tl3qoYY1kmQUEwRRLCKavA4KJQTDB1wzBBAAAsYJgAgCAWEEwAQBArCCYAAAgVhBMAAAQKwgmAACIFQQTAADECoIJAABiBcEEAACxgmACAIBYQTABAECsIJhEyWP0XGeGai7+lV79X5vuXmuZTVepxl7G1LzW5H4/AAAIBMFkt7KXtouBtICDqWz7h/RC/z16+ZRt2wEAYg7BZFN+4r4RMsN3aM2mSle5l9Xd8QymFa/dc4cqAEDMIZhMTbTx51rA3KfN28UyfwgmAIDiQTCZTtKWX2oBc482bhLL/CGYAACKB8Fk6qXt+rWi0gZT2cYB2tJ/j/aNsmtTo/eppv8jem7Li65ldWWVtKL2qn6tqFYPTsO+9zO05dUmKnMsz8/6CvDzq7RC/CwAgBh4qIOJB0p+/mHF38c/mBRa0Zyhfa735u7Ti82HXOuZZz0eajtP2pZHMAHAwodgEjtsqSIE02Y+k08NoNd66Jnliv562cpDtOYUC5/RDK1b41xvxaEMVZ+6Squ37KEly9jry/+Tyo/fZdumrrNa8nnauhjKA4AF6KEOJqdSDuVV0pp3jWV+fPx1SfmL9NxZVt5+TFIuc4gq3zfW2b5HLDMgmABgIUIwmUoZTOp769eU7tIG4YzI9MqnRoj0f0hLxTIpa9hu+0timQHBBAALEYLJVMJgWv0hVevvfYdWi2Ucv2nXde1nFT1Te5V2DN63JkwIEEwAsJggmEwlDKZ1l2l3qGB6UX1vdtOvDwQTACwmCCZTCYPJfG/viQrmUN7ZIWsK+As36Mf6es4JEwYM5QHA4oRgMpUymPbQun62zBH3lPBE4mWzvLrlZfP1Zw6xmXfvi8N7qrJj1uQHj2Ay17eHXSGUFhr5dI7m5uYoe62LqsRyAIASQjCZShlMCSrbz86IxOnia16nDT1suO7iHUo+a1uPn0WN3qXNP9pjvLZsGz1be4NeHDE+0y+YEtUfsfum7lNVwyFrunk+70zooWTI0fhJ+5kaAEBpIZhMhQdTvpteDeL1pBdp9Smf60Vq+GzYLATAsz5PO9eeGDFsvJ9nMCWaaIPXDbeuSRY2jSM0bQaTetZ0qcG9DABAiSCYTKUOJs0qeubVj6j6/fv0Ml/ul/eounOInk16nJUke6hS+9cVfEbeL+/T7u7LVL5mlbkd3sGkWtZEa2T/X8ovmBIKtVzOIpgA4GuBYAK5n45Tjg/lnZCUAwCUCIIJnJQKSrX20kSWDeVNj1CDuAwAQAkhmMDimPSgmpmgnp2S5QAASgjBBBYWTLlMmsYH2yilSJYBACgxBBMAAMQKggkAAGIFwQQAALGCYAIAgFhBMAEAQKwgmAAAIFYQTAAAECsIJgAAiBUEEwAAxAqCCQAAYgXBBAAAsYJgYpqr79H/dfxVcI9+U+5eNrwm+k2r+BmaO9TvWhYA4OGEYGIQTAAA8YBgYngwpSvcZZ6UFLUNjlOa/++izGjA/13US2kEEwCAA4KJCRJMyb3tNHAtTdlZ2/8uQjABABQFgokpPJhSNJTmYZSj9JUe6rmSRTABABQJgokpPJgSVNE3QdM3B6htt6L/3XAJwQQAUCwIJiZIMIkQTAAAxYNgYhBMAADxgGBiEEwAAPGAYGIQTAAA8YBgYhBMAADxgGBiEEwAAPGAYGIQTAAA8YBgYhBMAADxgGBiEEwAAPGAYGKCBJMZRL6yNNroXtcJwQQAIEIwMQgmAIB4QDAxQYKpeBBMAAAiBBODYAIAiAcEE4NgAgCIBwQTw4PJCf9aHQBgviGYGAQTAEA8IJgAACBWEEwAABArCCYAAIgVBBMAAMRKQcEEAAAwXxBMAAAQKwgmAACIFQQTAADECoIJAABiBcEEAACxgmACAIBYCRxMTacfoy+nvkenFXcZAABAVAGD6SmanPom0d8eoX/87glqcpUDAABEEzCYVMqTdPePj+jh9NXYk1QplgMAAEQQPJg0u56gL/6ihdM36UGXpBwAACCkcMGk2t//qH7WRPe+Q/+N600AAFAkoYMpkfghZf5gDOn9/fzTknIAAIDgIgRTgipPP2acNX32XXpLUg4AABBUpGBKKP9OD/RrTd+muwck5QAAAAFFC6bE0zT1ezac955YBgAAEFzEYErQuV//M5s6/gNXGQAAQFDRg2nMCCb65AlXGQAAQFAIJgAAiJWiBROG8gAAoBgiB9PkFCY/AABA8UQMpv9g08X/hTK1YhkAAEBwkYIJN9gCAECxRQimp6x7mPBIIgAAKJLQwVTZ9Rj9Qztb+tPjdE5SDgAAEEa4YDL/7cW36PMOSTkAAEBIwYMJ/ygQAABKKGAwPU03P8G/VgcAgNIJGEwJaup/lL763ffpOP45IAAAlEDgYAIAACglBBMAAMQKggkAAGIFwQQAALFSUDB9/NuPTCtWrAAAACiZ/wdI4itFZ2W/GwAAAABJRU5ErkJggg==>

[image28]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAloAAAAfCAYAAAA/UWMcAAADmUlEQVR4Xu3cMW7bSABA0dxCMJIAMRBsEiCwgQAu9wJ7gdR7iLhSkWaP4DZp1eUAqQ2XKdy5zgGMXICr4ZDikDOUKDuzyO6+4gHWSOSIqj5mBn6yWq0aAAB+vifTAQAAfg6hBQBQidACAKhEaAEAVCK0AAAqEVoAAJUILQCASoQWAEAlQgsAoBKhBQBQidACAKjkgaH1vjn78LEwXnZ2dRsdcQ0P8+Pt79HL0+y9Q67vm+b+et29Xrevp58BAJarHlrPP9w2p+/y8V/R922gfHuWj//7PH1QaDXNXbNJxzZ3zd0m/xwAsEzl0PrY/HZ1Wxj/Nf1/Q2uzTazy6lVY1Wrur7NxAOCwo0IrrE6VtgFDTMXxL83z0TXHh9bli4vd9lc6/vlltyWWjIfPXq5Om2/d+PcXT4drnp3PbqP1n//x9rz5PLl3Lw2u0tzx/hfJe+ejOeb095l+168n6TzDvYpzd9LnGL83E1r9bzJ5b93W1F3++WATEiyPsDh8n40DAIPFoXV2dZNsAQ4rWiG+Tnafm4bV9PUBXXBMx/sgGl5ftJ8LoTUEUQyu/u9SyIQA+fo6D5bekhWt3XfpoqUfD9+lHd8jDaIYlBfx9fZe6fedu9fwO+x/jlJohd9mN0cXif17bWbt2SIMUbUujAktANhveWj99SkJqiG03uxWswbDdceE1lw85NEQgihEwzhIhtBKV8VGK1STwJgqh9awYtavHrVzTkLrsMlznLxq52v/3t4rnzfYN/f8c2RzrZJD8on+vRBM1+vpPQZhxWt0dgsAWOTRobU/pI4JrbhNdpmN59HQB9FcaM2tjI3ipqAUWm3ovH61e/1Phtbs3AeeI5urvTauAuafFVoAUMvi0AorV2/+fN+s3n3a/n0znNH640scL1xzbGiFWEq3CfswaIOjD4cQGd0W2GxorebDIlwzbNNtr0mCJKyoTc87haDp547npR4aWvE50vumW3ml0Jqde5U/x/jaPLTi9eVVsHhEa5ONR+WD8vHkVj4OAAwWh1YIqvTAe3oYfrx9eJNcd2xo9bEz3tqabqH14/tCa7p9mK6UZVtxhXl24dMfIO/C6DGhFUNycv/uXqXQmp27kz5HPpbPM/pNkpWyw4fh87NYzmgBwGHLQ4v/tBBbpQPxh7YVAYB5QoudLKr8w1IAeBShBQBQidACAKhEaAEAVCK0AAAqEVoAAJUILQCASoQWAEAlQgsAoJK/AVYivmubwgRrAAAAAElFTkSuQmCC>

[image29]: <data:image/png;base64,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>

[image30]: <data:image/png;base64,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>