# Especificación de diagramas: arquitectura del agente conversacional

Diagrama del apartado "Arquitectura del agente conversacional" (Objetivo 2). Se dibuja en draw.io y se exporta en PDF vectorial a `img/`:

| Diagrama | Archivo fuente | Archivo de salida | Figura en LaTeX |
|---|---|---|---|
| C4 nivel 3: componentes del agente | `diagramas/drawio/Componentes_Agente.drawio` | `img/C4_Componentes_Agente.pdf` | `fig:ob2_c4_componentes` |

Las figuras de estados y de secuencia se generan desde PlantUML (`diagramas/plantuml/`) y no se dibujan en draw.io.

## Notas de estilo

- Colores sobrios, legibles en escala de grises:
  - Persona: relleno `#F2F2F2`, borde `#333333`.
  - Componente propio: relleno `#D9D9D9`, borde `#333333`, texto negro.
  - Servicio de otro módulo (dependencia): relleno blanco, borde `#333333`.
  - Sistema externo: relleno blanco, borde `#666666` punteado.
  - Límite del agente y capas: sin relleno, borde `#666666` punteado.
  - Elemento prohibido (módulos clínicos y de cobros): sin flechas; caja `#F2F2F2` con borde punteado.
- Cada componente lleva el formato C4: **nombre** en negrita, `[Componente: Tecnología]` debajo y una descripción de una línea.
- Los componentes internos usan la forma "Componente" de draw.io. Los íconos se reservan para sistemas externos y tecnologías: WhatsApp (simpleicons.org: `whatsapp`), Meta (simpleicons.org: `meta`), Google Calendar (simpleicons.org: `googlecalendar`), PostgreSQL (devicon: `postgresql-original`), Spring (devicon: `spring-original`). Tamaño 40 a 50 px. Guardarlos en la biblioteca propia de draw.io.
- Tipografía sans-serif (Arial o Helvetica), 10 a 12 pt para los nombres y 9 pt para las etiquetas de las flechas.
- Fondo blanco, sin sombras ni degradados. Ancho máximo de la figura: el ancho del texto (14,5 cm).
- Exportar en PDF con la opción "Transparent Background" desactivada y "Crop" activado. Verificar que el PDF sea vectorial (los textos deben poder seleccionarse).
- Las relaciones se dibujan con línea continua; los eventos de dominio, con línea punteada. Cada flecha lleva una etiqueta con la acción y, entre paréntesis, el protocolo o el tipo de llamada.

---

## Diagrama de componentes del agente (C4 nivel 3)

**Título sugerido:** Agente conversacional: componentes.

### Elementos

| Nombre | Capa | Tipo C4 | Tecnología | Responsabilidad | Ícono o forma sugerida |
|---|---|---|---|---|---|
| Paciente | Externo | Persona | — | Escribe desde WhatsApp | Ícono de persona |
| WhatsApp Cloud API | Externo | Sistema externo | Meta | Transmite los eventos del webhook y entrega los mensajes | WhatsApp (simpleicons.org) |
| Webhook de WhatsApp | Canal | Componente | Controlador HTTP (Spring Web MVC) | Comprueba el token y devuelve `hub.challenge` al registrar la URL; valida la firma `X-Hub-Signature-256` y entrega el mensaje al motor | Forma "Componente" |
| Cliente de WhatsApp Cloud API | Canal | Componente | Cliente HTTP (Graph API) | Envía texto, listas, botones y plantillas; registra el identificador del mensaje | Forma "Componente" |
| Motor de pasos | Conversación | Componente | Máquina de estados (Java) | Decide la respuesta según el paso, la entrada y el estado; aplica las reglas de derivación | Forma "Componente" |
| Almacén de estado | Conversación | Componente | Caché en memoria (Caffeine) | Guarda el paso actual, el paciente identificado, la selección parcial y la marca de derivación; caduca a los 30 min por teléfono | Forma "Componente" (cilindro) |
| Identificación de pacientes | Conversación | Componente | Servicio | Busca pacientes activos por teléfono en formato E.164 y valida la cédula cuando hay varios | Forma "Componente" |
| Consentimiento de privacidad | Conversación | Componente | Servicio | Registra la aceptación del aviso con su versión y su fecha; la aceptación habilita los recordatorios | Forma "Componente" |
| Flujo de información | Conversación | Componente | Servicio | Responde horarios y formas de pago desde la configuración, y precios desde el catálogo | Forma "Componente" |
| Flujo de agendamiento y reprogramación | Conversación | Componente | Servicio | Ofrece horarios, registra la cita o su reprogramación y aplica la respuesta del recordatorio (confirmar, cancelar o reprogramar) | Forma "Componente" |
| Derivación a recepción | Conversación | Componente | Servicio | Arma el mensaje con el horario de atención y el enlace de recepción | Forma "Componente" |
| PatientDirectory | Dominio | Componente de otro módulo | Interfaz pública del módulo de pacientes | Consulta pacientes por teléfono | Forma "Componente" con borde blanco |
| ProfessionalDirectory | Dominio | Componente de otro módulo | Interfaz pública del módulo de profesionales | Consulta profesionales y especialidades | Ídem |
| AppointmentScheduler | Dominio | Componente de otro módulo | Interfaz pública del módulo de agenda | Consulta límites, registra, confirma, cancela y reprograma citas | Ídem |
| TreatmentDirectory (solo precios) | Dominio | Componente de otro módulo | Interfaz pública del módulo de tratamientos | Entrega precios referenciales en solo lectura | Ídem |
| Configuración de la clínica | Dominio | Componente | Propiedades de la aplicación | Horarios, formas de pago, número de recepción y hora del recordatorio | Forma "Componente" |
| Programador de recordatorios | Tareas programadas | Componente | Tarea programada, cada 5 min | Busca recordatorios vencidos y envía la plantilla de categoría utility | Forma "Componente" (reloj) |
| Receptor de eventos de cita | Tareas programadas | Componente | Escucha de eventos de dominio | Crea el recordatorio al crear una cita activa, solo si el teléfono del paciente aceptó el aviso; lo cancela al cancelar o reprogramar | Forma "Componente" |
| Repositorio de consentimientos | Persistencia | Componente | Spring Data JPA | Guarda y consulta la tabla `privacy_consents` | Forma "Componente" |
| Repositorio de recordatorios | Persistencia | Componente | Spring Data JPA | Guarda y consulta la tabla `appointment_reminders` | Forma "Componente" |
| Base de datos | Persistencia | Contenedor | PostgreSQL 16 | Almacena los datos de la clínica; aplica la restricción de exclusión de citas | PostgreSQL (devicon) |

Notas sobre los elementos:

- Los servicios de dominio (PatientDirectory, ProfessionalDirectory, AppointmentScheduler, TreatmentDirectory) pertenecen a otros módulos. Se dibujan con borde blanco para distinguirlos de los componentes del agente.
- Módulos clínicos y de cobros (atención clínica, odontograma, recetas y cobros): **no se dibujan como componentes del agente**. Se muestran en una caja aparte, sin flechas, con la nota "Sin relación con el agente (RNF03)".
- Google Calendar no se dibuja en este nivel. Pertenece al diagrama de contenedores.

### Relaciones

| Origen → destino | Etiqueta | Protocolo o tipo |
|---|---|---|
| Paciente → WhatsApp Cloud API | Envía mensajes y pulsa botones | WhatsApp |
| WhatsApp Cloud API → Paciente | Entrega respuestas y recordatorios | WhatsApp |
| WhatsApp Cloud API → Webhook de WhatsApp | Transmite los eventos (firmados) | HTTPS POST |
| Webhook de WhatsApp → Motor de pasos | Entrega el mensaje validado | Llamada interna |
| Motor de pasos → Almacén de estado | Lee y escribe el paso | Llamada interna |
| Motor de pasos → Identificación de pacientes | Identifica al paciente | Llamada interna |
| Motor de pasos → Consentimiento de privacidad | Registra la aceptación | Llamada interna |
| Motor de pasos → Flujo de información | Ejecuta la rama elegida | Llamada interna |
| Motor de pasos → Flujo de agendamiento y reprogramación | Ejecuta la rama elegida | Llamada interna |
| Motor de pasos → Derivación a recepción | Ejecuta la derivación | Llamada interna |
| Motor de pasos → Repositorio de recordatorios | Registra la respuesta al recordatorio | Spring Data JPA |
| Motor de pasos → Cliente de WhatsApp Cloud API | Solicita el envío | Llamada interna |
| Cliente de WhatsApp Cloud API → WhatsApp Cloud API | Envía texto, listas, botones y plantillas | API HTTPS |
| Identificación de pacientes → PatientDirectory | Busca pacientes por teléfono | Interfaz pública |
| Flujo de agendamiento y reprogramación → ProfessionalDirectory | Consulta especialidades, profesionales y horarios | Interfaz pública |
| Flujo de agendamiento y reprogramación → AppointmentScheduler | Consulta límites; registra, confirma, cancela o reprograma citas | Interfaz pública |
| Flujo de información → TreatmentDirectory | Consulta precios | Interfaz pública (solo lectura) |
| Flujo de información → Configuración de la clínica | Lee horarios y formas de pago | Lectura |
| Derivación a recepción → Configuración de la clínica | Lee el número de recepción | Lectura |
| Programador de recordatorios → Repositorio de recordatorios | Lee pendientes y registra el envío | Spring Data JPA |
| Programador de recordatorios → Cliente de WhatsApp Cloud API | Envía la plantilla | Llamada interna |
| AppointmentScheduler → Receptor de eventos de cita | Publica eventos de cita (creada, cancelada, reprogramada) | Evento de dominio (punteada) |
| Receptor de eventos de cita → Repositorio de consentimientos | Verifica la aceptación del teléfono | Spring Data JPA |
| Receptor de eventos de cita → Repositorio de recordatorios | Crea o cancela recordatorios | Spring Data JPA |
| Consentimiento de privacidad → Repositorio de consentimientos | Guarda la aceptación | Spring Data JPA |
| Repositorios → Base de datos | Lee y escribe | Spring Data JPA (TCP 5432) |

**Importante:** no dibujar ninguna flecha desde el agente hacia módulos clínicos ni de cobros.

### Disposición sugerida

- **Izquierda:** Paciente y WhatsApp Cloud API, fuera del límite del agente.
- **Centro izquierdo:** capa Canal (Webhook y Cliente de WhatsApp).
- **Centro:** capa Conversación, con el Motor de pasos en el medio y los flujos alrededor.
- **Derecha:** capa Dominio (PatientDirectory, ProfessionalDirectory, AppointmentScheduler, TreatmentDirectory, configuración). Ubicar a la derecha, fuera de la capa, la caja de módulos clínicos y de cobros, sin conexiones.
- **Centro inferior:** capa Tareas programadas.
- **Inferior:** capa Persistencia (dos repositorios) y Base de datos debajo.
- Evitar cruces de flechas: el Motor de pasos debe quedar entre el Webhook y los flujos.

### Límites y agrupaciones

- **Agente conversacional (módulo whatsapp):** caja exterior punteada que contiene las cuatro capas del agente. Subtítulo: "Módulo del monolito modular".
- **Capas:** cajas internas sin relleno, con el nombre de la capa en la parte superior: Canal, Conversación, Tareas programadas y Persistencia.
- **Dominio:** caja aparte, a la derecha del límite del agente, con el título "Servicios de otros módulos (solo interfaces públicas)".

### Destacar la restricción

- Borde grueso en la caja del agente.
- Nota junto a la caja de módulos clínicos y de cobros: "Sin relación con el agente (RNF03)".

### Leyenda

Persona (ícono) · Componente propio (rectángulo gris) · Servicio de otro módulo (rectángulo blanco) · Sistema externo (rectángulo punteado) · Relación (flecha continua con protocolo) · Evento de dominio (flecha punteada) · Límite del agente y capas (caja punteada).

---

## Entregables

1. Un archivo draw.io (`diagramas/drawio/Componentes_Agente.drawio`) con la biblioteca de íconos incluida.
2. Un PDF vectorial en `img/`: `C4_Componentes_Agente.pdf`. Al existir, la figura del apartado se muestra automáticamente (la compilación usa `\IfFileExists`).
