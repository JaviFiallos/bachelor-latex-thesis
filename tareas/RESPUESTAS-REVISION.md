# Respuestas a la revisión de los Objetivos 2 y 3

Fecha: 2026-11-05. Rutas de código relativas a `../bellidental-app/`.
Veredictos: ✅ cierto · ⚠️ había que matizar (ya corregido) · ❌ no es cierto (ya corregido o eliminado).

---

## 0. Revisión de tus propias correcciones (bloque A)

| Tu cambio | Impacto | Acción |
|---|---|---|
| Quitaste «(restricción de costo)», «(canal oficial)» y otros paréntesis de las matrices | **Rompía la integridad**: `tecnologias.tex` seguía diciendo «Cada criterio indica entre paréntesis su origen» | Frase eliminada; queda «En todas las matrices, 3 es la puntuación más favorable» |
| Quitaste «(Objetivo 3)», «(Plan de desarrollo…)» en la tabla de fases RAD | Sin impacto | — |
| Quitaste la fila «Recordatorios» del contrato del agente | Sin impacto; coherente con la limpieza de recordatorios | — |
| Quitaste «Fuera de tema» de la tabla de reglas y «Modelo no disponible» de las pruebas | Menor: RNF05 («menú ante falla del modelo») queda respaldado por la fila de plazos (8 s y 10 s) y por la tabla de riesgos del despliegue | — |
| Quitaste «6,60 USD mensuales» y la fila «Acceso» (SSH con llave) del servidor | Sin impacto; fail2ban sigue en la tabla | — |
| Quitaste «La construcción reutiliza componentes…», «la caché…», «n8n reparte…» | Sin impacto | — |
| Acortaste la frase de RF13, RF14 y RNF05 («Debería») | Sin impacto | — |
| Cambiaste el título de 3.3.2 | Sin impacto | — |

---

## 1. Objetivo 2

**Tabla 34 «traza cada evidencia…».** Reescrito: «muestra, para cada hallazgo del análisis, el requerimiento al que dio lugar y lo que implica para el diseño».

**Cita de RAD [?].** La cita `martin1991rapid` existe y se resuelve en la compilación actual. El [?] venía de un PDF de revisión antiguo. Lo mismo ocurre con Santhosh y Jurafsky.

**Distancia de la clínica.** Añadida: el cliente en sitio de XP es «poco viable porque la clínica se encuentra en otra ciudad, a una hora en autobús».

**«del Objetivo 1» en el proceso propuesto.** Ahora dice «diagramas del proceso actual (Figuras…)».

### Motor de base de datos: ¿«única alternativa con restricción de exclusión nativa»? ⚠️
Es cierto **entre las tres comparadas** (PostgreSQL, MySQL y MongoDB): MySQL y MongoDB no tienen `EXCLUDE`. Lo matizamos con «Entre las alternativas evaluadas…».

**¿Qué es la política anticruce?** No es un procedimiento ni un *trigger*. Es una **restricción declarativa** de la tabla, como una clave única pero para rangos de tiempo. Está en `bellidental-backend/src/main/resources/db/migration/V6__appointments.sql:45`:

```sql
CREATE EXTENSION IF NOT EXISTS btree_gist;          -- permite usar "=" sobre uuid dentro de un índice GiST
CONSTRAINT appointments_no_overlap EXCLUDE USING gist (
    professional_id WITH =,                          -- mismo profesional…
    tstzrange(start_at, end_at) WITH &&              -- …y rangos de horario que se solapan (&&)
) WHERE (status NOT IN ('CANCELLED','NO_SHOW','RESCHEDULED'))   -- solo entre citas activas
```

Se lee así: «no pueden existir dos filas con el mismo profesional **y** horarios superpuestos, salvo que alguna esté cancelada, sea inasistencia o haya sido reprogramada».

- `tstzrange(inicio, fin)` convierte las dos horas en un **rango**.
- `&&` es el operador «se solapa con».
- PostgreSQL usa un índice **GiST** para comprobarlo rápido. `btree_gist` hace falta porque GiST no sabe comparar `uuid` con `=` sin esa extensión.

Si dos personas (la secretaria y el agente) intentan reservar el mismo hueco **al mismo tiempo**, una de las dos inserciones falla en la propia base de datos. La API captura ese error (`AppointmentService.java:60`, `OVERLAP_CONSTRAINT`) y responde **409 Conflict**. Por eso «vale para ambos canales»: los dos escriben por la misma API en la misma tabla, y la regla está debajo de ambos.

**Stack.** `pg_trgm` + índices GIN → ver «Índices de trigramas» en el Objetivo 3. Flyway aplica las migraciones `V1…V22` al arrancar la API.

**Corrección extra que encontré.** La fila del backend decía «migraciones con Flyway (usuario y fecha de cada revisión)». El usuario y la fecha no los guarda Flyway, sino **Hibernate Envers**. Ahora dice «auditoría con Hibernate Envers (usuario y fecha de cada revisión)».

### «Diseño guiado por atributos» ✅ (con referencia)
Es el método **ADD (Attribute-Driven Design)** del SEI (Carnegie Mellon). En la versión 3.0 lo describe el libro que ya citas: Cervantes y Kazman, *Designing Software Architectures: A Practical Approach* (Addison-Wesley, 2016), `cervantes2016designing`. La idea: las decisiones de arquitectura se toman a partir de los **factores de diseño** (requisitos, atributos de calidad y restricciones), en iteraciones. Ningún antecedente lo usa; es bibliografía de fundamentación.

Lecturas breves:
- Cervantes y Kazman (2016), cap. 3, «The Attribute-Driven Design Method».
- Bass, Clements y Kazman, *Software Architecture in Practice*, 4.ª ed. (2021), cap. 20.

En el texto añadí la sigla: «diseño guiado por atributos (ADD, *Attribute-Driven Design*)».

**«el NLP interpreta y el código decide, como en … [?]».** La cita (`santhosh2026whatsapp`) existe y se resuelve. Se mantiene.

### «Frases de ejemplo etiquetadas por intención»
Un **clasificador entrenado** (como Rasa) no entiende nada al inicio. Hay que darle decenas de frases reales, cada una con su etiqueta:

```
"quiero una cita el jueves"        -> agendar
"a qué hora atienden"              -> horarios
"cuánto cuesta una limpieza"       -> precio
```

Con eso aprende a clasificar frases parecidas. Un **LLM** no necesita ese entrenamiento: basta con describirle las intenciones en las instrucciones. Tu agente sí incluye algunos ejemplos dentro de las instrucciones (`bellidental-agent/app/nlu/prompt.py`, sección «Ejemplos»), pero son una guía, no un conjunto de entrenamiento. En el texto puse un ejemplo concreto.

**Jurafsky [?].** Existe y se resuelve.

### Tabla «Evaluación de motores conversacionales»: ¿se comparan modelos de lenguaje?
**No.** Los modelos se comparan en otra tabla (Claude Haiku, GPT-6 Luna…). Esta tabla compara **dónde vive y con qué se construye la máquina de estados de la conversación** (el «motor»):

| Alternativa | Qué significa |
|---|---|
| **Módulo dentro de la API** | Programar la conversación como un módulo más del Spring Boot, en el mismo proceso que accede a la base de datos |
| **Servicio propio separado** | Un programa aparte (Python/FastAPI) que solo habla con la API por una interfaz interna. **Elegido** |
| **n8n autoalojado** | Plataforma de flujos visuales donde se arma la conversación con nodos |
| **Rasa** | Plataforma completa de chatbots con su propio clasificador entrenado |

«Módulo dentro de la API» sí es pertinente: era la opción más simple (un solo programa), y pierde por **aislamiento**, porque el texto libre del paciente se procesaría en el mismo proceso que lee los datos clínicos. Para que no se malinterprete, añadí antes de la tabla una frase que explica que se compara dónde se construye el motor o con qué plataforma.

### «Consumo de recursos en el servidor compartido»
Las cinco piezas viven en **un solo VPS de 8 GB**, así que cada alternativa del motor «come» memoria de las demás. Medido en producción (Tabla de contenedores):

```
VPS: 4 vCPU · 8 GB RAM ─────────────────────────────────────────────────
│ API Spring Boot ██████████████████████████  466 MB  (límite 1 024)    │
│ PostgreSQL      ███                          59 MB  (límite 1 024)    │
│ Agente Python   ██                           44 MB  (límite   256)    │  ← servicio propio (elegido)
│ Caddy           █                            19 MB  (límite   128)    │
│ Web (nginx)     ▏                             6 MB  (límite    64)    │
│                                     Total ≈ 594 MB                     │
│ Alternativas descartadas (orden de magnitud):                          │
│   n8n  ████████████████  ~300–500 MB  (Node.js + editor visual)        │
│   Rasa ██████████████████████████████████████  ~1–2 GB (modelo NLU)    │
│   LLM local de 7B  ████████████████████████████████████████████  ~4 GB │
─────────────────────────────────────────────────────────────────────────
```

Por eso el servicio propio y el módulo en la API puntúan 3 (casi no suman memoria), n8n 2 y Rasa 1. Los valores de n8n y Rasa son estimaciones de referencia, no medidas tuyas.

### HTTPS, certificado y Let's Encrypt (exposición del webhook)

```
 Paciente ──WhatsApp──► Servidores de Meta
                              │ 1. POST https://bot.<dominio>/webhook  (cuerpo + firma X-Hub-Signature-256)
                              ▼
                     DNS (Cloudflare): bot.<dominio> → IP del VPS
                              │
                              ▼  puerto 443
                ┌──────────── VPS ────────────────────────────┐
                │ Caddy  ◄── 2. TLS: muestra el certificado    │
                │   │         de Let's Encrypt; se cifra todo  │
                │   │ 3. descifra y reenvía por la red interna │
                │   ▼    de Docker (HTTP simple, sin salir)    │
                │ agente:8000 /webhook → valida firma → 200 OK │
                │   │ 4. llama a la API con X-Bot-Key           │
                │   ▼                                           │
                │ backend:8080 /api/v1/bot/…  → PostgreSQL     │
                └──────────────────────────────────────────────┘
```

- **¿Por qué HTTPS?** Los mensajes llevan datos personales (nombre, teléfono, cita). HTTPS (HTTP sobre **TLS**) los **cifra en tránsito** y le prueba a Meta que habla con tu servidor y no con un impostor. Meta **exige** una URL `https://` con certificado válido; con `http://` no deja registrar el webhook.
- **¿Qué es el certificado?** Un archivo firmado por una **autoridad de certificación** (aquí Let's Encrypt, gratuita) que dice «este dominio pertenece a quien controla este servidor». Contiene la clave pública del servidor.
- **¿Cómo se envía?** En cada conexión, al inicio, el servidor presenta el certificado. Esa negociación se llama ***handshake* TLS**. Meta verifica la firma de Let's Encrypt y, si es válida, acuerdan una clave para cifrar la conversación.
- **¿Cómo se obtiene?** Mediante el **protocolo ACME**. Caddy le pide un certificado a Let's Encrypt, y Let's Encrypt plantea un **desafío** (por ejemplo, publicar un archivo en `http://bot.<dominio>/.well-known/acme-challenge/…`) para comprobar que controlas el dominio. Superado el desafío, emite el certificado, válido por 90 días, y **Caddy lo renueva solo** antes de que venza. Por eso en tu `Caddyfile` solo aparece `email {$ACME_EMAIL}`: no hay que configurar nada más.

### Estilo de la API: «se publican como eventos que programan los recordatorios»
Lo **eliminé**, como propusiste. Un dato para ti: en el código **sí existe** una base de recordatorios (`AppointmentService` publica eventos, `bot/application/AppointmentReminderListener.java`, `BotReminderService.java`, la tabla `appointment_reminders` y `bellidental-agent/app/reminders/job.py` con la plantilla `recordatorio_cita`). No está en operación porque la plantilla de Meta y las notificaciones no se habilitaron. La tesis lo declara como no implementado (Debería) y es coherente con lo que funciona en producción.

### ¿Cómo se bloquea desde internet la interfaz interna?
En el `Caddyfile` (`bellidental-backend/deploy/Caddyfile`):

```
app.{$DOMAIN} {
    handle /api/v1/bot/* { respond 404 }     # la interfaz del agente no se publica
    handle /actuator/*   { respond 404 }     # tampoco la de monitoreo
    handle /api/*        { reverse_proxy backend:8080 }
    ...
}
bot.{$DOMAIN} {
    handle /webhook* { reverse_proxy agent:8000 }   # solo el webhook
    handle           { respond 404 }
}
```

Desde internet, cualquier petición a `/api/v1/bot/…` recibe 404. Además, la API exige en esas rutas la cabecera **`X-Bot-Key`** con una clave secreta (`security/BotApiKeyFilter.java`) que solo conoce el agente. Por último, el cortafuegos (UFW) solo abre los puertos 22, 80 y 443, y la API no publica su puerto. Son tres capas.

**Corrección extra que encontré.** La tabla de contenedores decía «bloquea… la interfaz interna **del agente**». Lo que se bloquea es la interfaz que **la API ofrece al agente**. Corregido.

### ¿Por qué el agente y la API se comunican por HTTP (sin S) dentro del servidor?
Viajan por la **red interna de Docker**, que solo existe dentro del VPS. Los paquetes nunca salen a internet, así que no hay a quién cifrarlos. El cifrado (TLS) se hace una sola vez, en la puerta de entrada (Caddy). Esto se llama **terminación TLS en el proxy** y es la práctica habitual. La autenticación entre los dos la da la clave `X-Bot-Key`.

### «…valida la doble reserva en la aplicación, la regla anticruce está en la base de datos y vale para ambos canales»
Ver la política anticruce. La recepción (aplicación web → `/api/…`) y el agente (→ `/api/v1/bot/…`) terminan en **el mismo servicio de agenda** y en **la misma tabla** `appointments`. La restricción está en la tabla, de modo que ninguno de los dos caminos puede saltársela. En Shaikh la comprobación está en el código de la aplicación: si dos peticiones llegan a la vez, ambas pueden pasar el chequeo antes de guardar.

### Componentes funcionales y conversación
- «La identificación solo se pide para agendar o reprogramar» ✅ (y para cancelar y para urgencias). `bellidental-agent/app/dialog/identify.py` (`start_identification`) solo se llama desde `booking.py`, `appointments.py` y `urgent.py`.
- «El estado se guarda en memoria y caduca a los 30 min» ✅. `app/dialog/store.py` (`ConversationStore`, un diccionario en memoria) y `app/config.py` (`conversation_ttl_minutes: int = 30`). Si pasan más de 30 min sin mensajes, la conversación vuelve al inicio.
- «Un reinicio no pierde citas» ✅. Al reiniciar se pierde el diccionario (el paso en curso), pero las citas solo se escriben en la base de datos tras *Confirmar*.
- Eliminé «El recordatorio inicia una conversación propia» y, en la tarjeta del aviso, «Habilita los recordatorios».

### Integración con WhatsApp (tabla de mecanismos)
- **Mensajes interactivos** ⚠️. **Sí están implementados**, pero solo para el menú y las citas: el menú es una **lista** (`app/dialog/menu.py`, `ListMessage`), y para elegir horario y confirmar se usan **botones** (`ButtonsMessage`). Solo los botones del recordatorio no se usan. Por eso no eliminé la fila; la dejé como «Lista para el menú; botones para elegir horario y confirmar». En la matriz de selección cambié «y plantillas para recordatorios (RF10, RF14)» por «con botones y listas (RF10, RF11)».
- **Consentimiento previo para escribir primero** ❌. Solo aplicaba a los recordatorios: el agente nunca escribe primero. Fila eliminada.
- **Ventana de 24 h** ⚠️. Es política de Meta: una empresa puede responder libremente durante 24 h desde el último mensaje del cliente; pasado ese plazo solo puede enviar plantillas aprobadas. El agente **solo responde** a mensajes recibidos, así que siempre está dentro de la ventana; no hay código especial para ello. Ahora dice: «El agente solo responde a mensajes del paciente, dentro de las 24 h que Meta permite sin plantillas».

### Modelo de datos
- **Entidad «Recordatorio»**: eliminada de la tabla de entidades principales. Siguen apareciendo `appointment_reminders` en el Anexo 4 y en el diagrama ER, porque la tabla existe en el esquema. Si quieres, también la quito del anexo.
- **Valores calculados** ✅, verificado:
  - **Saldo** = total de tratamientos realizados − total de pagos vigentes (no anulados): `billing/domain/AccountBalance.java:18` (`totalCharges.subtract(totalPayments)`). No hay columna «saldo».
  - **Edad** = años entre la fecha de nacimiento y hoy, en la zona horaria de la clínica: `patients/PatientResponse.java:41` (`Period.between(birthDate, hoy).getYears()`). Se guarda solo `birth_date`.
  - **CPO y ceo**: `odontogram/domain/DentalIndexCalculator.java`. Recorre los hallazgos activos del odontograma y cuenta **piezas** (no caras) por componente. En dentición permanente: **C**ariadas, **P**erdidas y **O**bturadas, con CPO = C + P + O. En dentición temporal: **c**ariadas, **e**xtracción indicada y **o**bturadas, con ceo = c + e + o. Una pieza cuenta una sola vez por componente (se usa un conjunto).
- **«Vinculada a la original»**: la cita nueva guarda en la columna `rescheduled_from_id` el identificador de la cita que reemplaza (clave foránea a la misma tabla, `V6__appointments.sql`), y la original pasa a estado `RESCHEDULED`. Así se puede seguir la cadena: «esta cita vino de aquella». Lo aclaré en el texto.

### Esquema de despliegue
- **Introducción ampliada**: un VPS, un contenedor por servicio, un proxy como única entrada, dominio con dos subdominios y HTTPS.
- **«el webhook por HTTPS»**: ver el diagrama de arriba. «Webhook» significa que **Meta llama a tu servidor** (un POST) cada vez que llega un mensaje, en lugar de que el agente pregunte a Meta cada cierto tiempo.
- Eliminé «las plantillas de mensaje aprobadas por Meta». En la tabla de riesgos, «Plantillas aprobadas» pasó a «Uso conforme a la política de Meta».

### Plan de desarrollo
- «posible distribución» → «el boceto del tablero y la distribución de las tarjetas».
- Sin negritas: el texto dice «las tarjetas 11 a 14 corresponden al agente».

---

## 2. Objetivo 3

**Introducción (3.3).** Reescrita sin la cadena de «(apartado 3.3)… (Tabla 36)…», y eliminado el comentario del archivo.

**Diseño con el usuario (3.3.1).** Ahora habla de **wireframes con la paleta de colores y la distribución**, con los mismos elementos de las pantallas finales en una versión menos elaborada. Pies de figura: «Wireframe de…». Coherencia: también en el Objetivo 2 (fase RAD y diseño de la interfaz) y en la tabla de tarjetas («Ajustes de los wireframes»).

**Base del proyecto (3.3.2).** Nueva entrada: «La construcción comenzó por la base común sobre la que se desarrollaron las demás tarjetas…». Eliminé las menciones a «la tarjeta 0» en el esquema versionado, en las pruebas y en la base de datos. Queda solo en la tabla de tarjetas (Obj. 2) y en el estado final de las tarjetas, que es donde hace falta.

### Dependencias clave
- **JJWT** (*Java JWT*) es una **biblioteca** de Java; **JWT** es el **estándar**. JWT (*JSON Web Token*, RFC 7519) es un texto firmado con tres partes, `cabecera.datos.firma`, que la API entrega al iniciar sesión y que el navegador envía en cada petición para demostrar quién es y su rol. JJWT es el código que **crea y verifica** esos tokens en Java (`security/JwtService.java`). En corto: JWT es el formato y JJWT, la herramienta que lo implementa.
- **Hibernate Envers**: extensión de Hibernate que **guarda automáticamente una copia de cada versión** de una fila al modificarla. Las entidades marcadas con `@Audited` (`Encounter`, `Payment`, `ClinicalRecord`, `PerformedTreatment`, `Medication`… en `persistence/entity/`) tienen una tabla gemela `*_aud` (p. ej. `patients_aud`, `V16__audit.sql`). Cada cambio crea una «revisión» en `revision_info`, con fecha y usuario. Así se cumple RNF02 sin programar el historial a mano. ⚠️ El Anexo 4 dice «(implementación posterior)» para la auditoría, pero **ya está implementada** (migración V16). Conviene quitar ese paréntesis del anexo.
- **Angular CDK** (*Component Dev Kit*): piezas base de Angular, sin estilo visual, para construir componentes accesibles. Tu frontend usa **`@angular/cdk/dialog`** (ventanas de diálogo), **`overlay`** (paneles que se superponen, como el lateral) y **`layout`** (detectar el tamaño de pantalla). Es lo que permite el panel lateral de tratamientos y receta sin tapar el odontograma.

### Pruebas: «Testcontainers para la agenda…» ✅
Testcontainers arranca un **PostgreSQL real en un contenedor Docker** durante la prueba y lo destruye al terminar. Verificado: `src/test/java/com/bellidental/support/TestcontainersConfiguration.java`, usado por `appointments/AvailabilityIT`, `AppointmentOverlapIT`, `ScheduleApiIT`, `audit/AuditLogIT`, `clinicalsummary/ClinicalSummaryIT`, `bot/*IT` y `SchemaMigrationIT`. Las cifras también coinciden: 52 clases de prueba en la API, 18 en la web y 6 módulos en el agente.

### CIE-10
No estaba definido. Añadí la definición en su primera aparición (Instrumento 1, metodología): «Clasificación Internacional de Enfermedades, décima revisión, de la Organización Mundial de la Salud». Es la lista oficial de códigos de diagnóstico; por ejemplo, K02.1 es caries de la dentina.

### Índices de trigramas
Un **trigrama** es cada grupo de 3 letras seguidas de una palabra: «caries» → `" c"`, `" ca"`, `car`, `ari`, `rie`, `ies`, `"es "`. La extensión **`pg_trgm`** compara cuántos trigramas comparten dos textos. Así, «carie dentina» encuentra «Caries de la dentina» aunque falten letras o estén en otro orden. Esa es la **búsqueda por similitud** (`similarity()` y el operador `%` en `persistence/repository/Icd10CodeRepository.java:19-22` y `MedicationRepository.java:15`).

Un **índice GIN** sobre esos trigramas hace la búsqueda rápida sin recorrer todo el catálogo (`V7__icd10_catalog.sql:12-13`, `V9`, `V10`, `V14`). En los nombres de pacientes el índice existe (`idx_patients_full_name_trgm`) y acelera la búsqueda por fragmento (`ILIKE '%texto%'`).

### «queda inmutable» (receta) ✅
`prescriptions/domain/PrescriptionRules.java:11`: solo se puede modificar una receta en estado `DRAFT`. Una vez emitida (`ISSUED`), cualquier intento de editarla devuelve «Solo se puede modificar una receta en borrador», y únicamente se puede **anular** (`voidPrescription`). Precisé el texto: «ya no puede modificarse, solo anularse».

### Herramientas del agente
- **httpx**: biblioteca de Python para hacer peticiones HTTP, como un navegador sin pantalla. Es **asíncrona**: mientras espera la respuesta de Meta o de la API, el agente puede atender otro mensaje. Se usa en `app/whatsapp/client.py` (enviar mensajes a la Graph API) y en `app/backend/client.py` (llamar a la API interna), siempre con **`timeout=10.0`** segundos.
- **Uvicorn**: el **servidor web** que ejecuta la aplicación FastAPI. FastAPI define *qué* responder en `/webhook`; Uvicorn es el programa que escucha el puerto 8000 y entrega cada petición a FastAPI. Es un servidor **ASGI**, el estándar asíncrono de Python. Se arranca en el `Dockerfile` del agente.

### «Responde 200 antes de procesar… cada identificador se procesa una sola vez»
Es **política de Meta**: si el webhook no responde con un `200 OK` en pocos segundos, Meta considera que falló y **reenvía el mismo evento**, con reintentos durante horas. Procesar un mensaje puede tardar, porque llama al modelo (hasta 8 s) y a la API (hasta 10 s). Por eso el agente:
1. verifica la firma;
2. responde **200 de inmediato**;
3. procesa el mensaje **en segundo plano** (`BackgroundTasks`, `app/main.py:210-211`).

Como aun así Meta puede enviar duplicados, el agente recuerda los últimos **1 000 identificadores** de mensaje (`ProcessedMessages`, `app/dialog/store.py`) e ignora los repetidos (`main.py:134-136`). Esto se llama **idempotencia**: procesar dos veces el mismo evento tiene el mismo efecto que procesarlo una vez.

### Estado de la conversación: ¿expira a los 30 min? ✅
Ver arriba (`conversation_ttl_minutes = 30`).

### Ubicación de las reglas de negocio por capa
- Título cambiado (antes «Reglas y dónde se aplican»).
- Frase reescrita sin tono justificativo: «Las reglas del diseño se distribuyen en tres capas: la base de datos aplica las que afectan a ambos canales; la API, las que protegen la agenda; y el agente, las propias de la conversación».

**La tabla, fila por fila: todas están en el código** ✅

| Regla | Evidencia |
|---|---|
| Enmascarado de 7 o más dígitos | `app/nlu/prompt.py:6-7,68-71`: la expresión `\d{7,}` se sustituye por `[número]` antes de enviar el texto al modelo |
| Cédula fuera del historial | `app/dialog/router.py:55-58`: el texto escrito en el paso `IDENTIFY_ID` no se guarda en `history` |
| Paciente o cita de otro teléfono: 404 | `BotBookingService.java:100-110`: si la cita no es de un paciente de ese teléfono, responde «Cita no encontrada» |
| Identificación: dos intentos | `app/dialog/identify.py:27` (`MAX_ID_ATTEMPTS = 2`) |
| 14 días | `BotAvailabilityService.java:59` |
| Límites de citas | `bot/domain/BotBookingLimits.java` y `application.yml` (`max-active-per-phone: 3`). Ver aclaración abajo |
| 2 h de anticipación | `application.yml` (`change-min-hours: 2`) y `BotBookingService.java:115-123`: si faltan menos de 2 h, rechaza con «No se puede reprogramar/cancelar la cita con menos de 2 horas de anticipación» |
| Urgencia | Ver abajo |
| Dos no reconocidos → derivación | `app/dialog/free_text.py:13` (`MAX_UNKNOWN_BEFORE_HANDOFF = 2`) |
| Derivación: calla 4 h | `app/dialog/handoff.py:9` (`HANDOFF_DURATION = 4 h`) |
| Plazos 8 s y 10 s | `app/config.py` (`llm_timeout_seconds = 8.0`); `app/backend/client.py:29` y `whatsapp/client.py:25` (`timeout = 10.0`) |

**Límite de citas: ¿«las de recepción no cuentan»?** El límite **solo aplica a las citas que agenda el agente**:
- un paciente no puede tener **dos citas activas del agente en la misma especialidad**;
- un mismo teléfono (una familia, por ejemplo) no puede tener **más de tres citas activas creadas por el agente**.

Las citas que registra la secretaria **no entran en ese conteo ni tienen ese límite** (`BotBookingLimits.java:31-35`: solo cuenta `source == BOT`). El motivo: evitar que alguien acapare horarios por WhatsApp; la secretaria sí puede agendar lo que haga falta. No son «3 + 3»: el tope es 3 por el agente y en recepción no hay tope. Reescribí la fila para que se entienda.

**Urgencias: ¿cómo funciona?**
1. El modelo clasifica el mensaje como `URGENT` cuando habla de dolor, sangrado, hinchazón, golpe o diente roto (`app/nlu/prompt.py`; ejemplo: «me duele mucho una muela»). Esto funciona incluso a mitad de otro flujo (`free_text.py:14`).
2. El agente envía primero un **texto fijo**: «Si tiene hinchazón que le dificulte respirar o tragar, fiebre alta o un sangrado que no se detiene, acuda a emergencias o llame al 911» (`app/messages/texts.py:153`). No da consejo médico.
3. Pide a la API los horarios de urgencia: `BotAvailabilityService.getUrgentSlots()` junta los horarios libres de **hoy y mañana** de la especialidad configurada (`urgent-specialty-id: 1`) y devuelve los **tres primeros** como botones (`urgent.py`, `MAX_SLOT_BUTTONS = 3`).
4. Si el paciente elige uno, se identifica y confirma como en una cita normal.

### Integración con el modelo: «los dos mensajes anteriores, enmascarados»
El agente guarda los últimos textos del paciente (`history`, hasta 6). Al modelo le envía el mensaje actual y **los dos anteriores**, con los números largos ya reemplazados (`app/nlu/prompt.py:73-80`, `free_text.py:23`). Ejemplo:

```
Paciente escribe:  "hola"                                  (mensaje 1)
                   "mi número es 0991234567, soy Ana"      (mensaje 2)
                   "quiero cambiar mi cita del jueves"     (mensaje 3, actual)

Se envía al modelo:
{"paso": "IDLE",
 "mensajes_anteriores": ["hola", "mi número es [número], soy Ana"],
 "mensaje": "quiero cambiar mi cita del jueves"}
```

El contexto sirve para entender respuestas cortas («sí, el jueves»). El enmascarado evita que el proveedor del modelo reciba cédulas o teléfonos. Precisé en el texto «del paciente» y «con los números largos ya enmascarados».

### «El texto libre pasa por el modelo cuando la conversación está libre»
«Libre» significa que **no hay un flujo guiado en curso** (paso `IDLE` o `MENU`): al empezar, o después de terminar una gestión. Ahí cualquier frase va al modelo para saber qué quiere el paciente. En cambio, si el paciente está en medio de un flujo (por ejemplo, eligiendo un horario), sus mensajes los atiende la máquina de estados, y el modelo solo se consulta para detectar si pide algo que debe interrumpir el flujo: una urgencia, algo clínico, saldo, pago o hablar con una persona. Lo aclaré en el texto.

### Pruebas: «webhook y firma»: ¿qué es la firma?
Meta firma cada mensaje que envía. Calcula un **HMAC-SHA256** del cuerpo del mensaje usando el **secreto de la aplicación** (una clave que solo conocen Meta y tu servidor) y lo manda en la cabecera `X-Hub-Signature-256: sha256=<firma>`. El agente recalcula la firma con el mismo secreto y la compara (`app/whatsapp/signature.py`). Si no coincide, responde **401** y descarta el mensaje (`main.py:203`). Así nadie puede hacerse pasar por Meta enviando mensajes falsos a tu webhook. El texto ahora dice «recepción del webhook y verificación de su firma».

---

## 3. Implementación (3.4)

### fail2ban ✅
Programa que **lee los registros de acceso** del servidor y, si una misma IP falla varias veces al iniciar sesión por SSH, **la bloquea temporalmente** en el cortafuegos. Se instala y activa en `bellidental-backend/deploy/vps-setup.sh:31,36` (`apt-get install … fail2ban` y `systemctl enable --now fail2ban`) con la configuración por defecto de Ubuntu, que protege `sshd`. El mismo script deja UFW con solo 22, 80 y 443 y desactiva el acceso de *root* y por contraseña (`PermitRootLogin no`, `PasswordAuthentication no`).

### Conexión con WhatsApp Cloud API: cómo se hizo
1. **Aplicación en Meta for Developers** con el producto WhatsApp; se añade el número (de prueba en desarrollo y el chip dedicado en el servidor).
2. **Webhook**: en el panel de Meta se registran la URL `https://bot.<dominio>/webhook` y un **token de verificación** inventado por ti (`WA_VERIFY_TOKEN`). Meta hace un `GET` con `hub.mode=subscribe`, `hub.verify_token` y `hub.challenge`; si el token coincide, el agente devuelve el `challenge` (`main.py:184-193`) y Meta da el webhook por **verificado**. Luego se **suscribe** al campo `messages`.
3. **Firma**: desde entonces, cada mensaje llega firmado con el secreto de la aplicación (`WA_APP_SECRET`) y se valida como se explicó arriba.
4. **Token permanente**: en Meta Business se crea un **usuario del sistema** (una cuenta técnica, no una persona) con permiso sobre la aplicación y el número, y se genera un token **sin caducidad** (`WA_ACCESS_TOKEN`). El agente lo usa para enviar mensajes por la Graph API. Los tokens normales de usuario caducan en horas. Se guarda solo en el archivo `.env` del servidor (`deploy/.env.example` muestra los nombres sin valores) y nunca en el repositorio.

### Otro hallazgo, fuera de lo que preguntaste
En la tabla de contenedores de 3.4.2 queda el marcador «*[Respaldo: contenedor, frecuencia, destino y prueba de restauración.]*». El respaldo **ya existe**:
- un contenedor `backup` (`deploy/backup/`) con `pg_dump` diario a las **20:30**;
- retención de **30 días**;
- copia opcional a Google Drive con *rclone*;
- script `deploy/restore.sh`.

Puedo redactarlo cuando confirmes que la copia a Drive y una restauración de prueba se hicieron.

---

## 4. Sección de verificación (bloque F)
- `verificacion.tex` quedó **fuera del documento** (su `\input` está comentado en `results-ob3.tex`); el archivo se conserva para la discusión final.
- Ninguna otra sección citaba sus tablas.
- El **tablero Kanban final** se movió a un nuevo apartado al cierre de 3.3, «Tablero al cierre de la construcción» (`ob3/tablero-final.tex`). Falta la captura `img/Objetivo3/Ob3_Tablero_Kanban.png`, tomada de Planka.

## 5. Menciones a recordatorios que quedan (son figuras o diseño; decide si las quitas)
- Diagrama de casos de uso del agente («responde recordatorios») y su texto en `ob2/casos-uso.tex:14`.
- Tarjeta «Recordatorios» en la figura de componentes funcionales del agente (`ob2/arquitectura-agente.tex:154`).
- Estado «Recordatorio» en `Estados_Conversacion.png` (fuente `diagramas/plantuml/estados_conversacion.puml`).
- Figura de secuencia del recordatorio (`ob2/arquitectura-agente.tex:204`, `fig:ob2_secuencia_recordatorio`).
- «Tareas programadas (recordatorios)» en el diagrama de componentes del agente (`ob2/arquitectura-agente.tex:21`).
- Tablas del contexto C4 y de nodos (`arquitectura-general.tex:30,34,96,140`; `despliegue.tex:31`).
- Proceso propuesto: «Confirmación de citas… el agente envía un recordatorio» (`ob2/proceso-tobe.tex:42`) y el BPMN correspondiente.
- Tabla de factores de diseño (`ob2/intro-impulsores.tex:25`): RF14 y el recordatorio con tres botones.

Todas son coherentes con un **diseño** que incluyó RF14 como «Debería». Si las quitas, la tabla de requerimientos y el plan siguen mostrando RF14, así que no se rompe la trazabilidad.
