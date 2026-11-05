# Glosario de tecnologías de Bellidental

Cada término tiene cuatro líneas: **qué es**, **para qué se usó**, **dónde está** (rutas en `../bellidental-app/`) y **por qué se eligió**. Todo lo que aparece aquí está verificado en los repositorios (2026-11-05).

---

## Base de datos

**PostgreSQL 16**
- **Qué es:** gestor de base de datos relacional de código abierto.
- **Uso:** guarda todos los datos de la clínica, 32 tablas en cuatro grupos.
- **Dónde:** servicio `postgres` en `bellidental-backend/deploy/docker-compose.yml`.
- **Por qué:** es la única alternativa evaluada con restricción de exclusión nativa (anticruce) y con búsqueda por similitud.

**Restricción de exclusión (`EXCLUDE`)**
- **Qué es:** regla declarativa de una tabla que prohíbe dos filas que «choquen» según operadores. Es una generalización de `UNIQUE`.
- **Uso:** impide dos citas activas del mismo profesional con horarios superpuestos (`appointments_no_overlap`).
- **Dónde:** `db/migration/V6__appointments.sql:45`.
- **Por qué:** la garantía está en la base de datos y vale para la recepción y para el agente, incluso con reservas simultáneas.

**GiST y `btree_gist`**
- **Qué es:** GiST es un tipo de índice para datos «geométricos» o de rangos; `btree_gist` es una extensión que le permite comparar también tipos simples (como `uuid`) con `=`.
- **Uso:** la restricción `EXCLUDE` combina `professional_id WITH =` y el rango horario `WITH &&`.
- **Dónde:** `V6__appointments.sql:1`.
- **Por qué:** sin `btree_gist`, no se pueden mezclar ambas condiciones en la misma restricción.

**`tstzrange` y el operador `&&`**
- **Qué es:** `tstzrange` es un rango de fecha y hora con zona horaria; `&&` significa «se solapan».
- **Uso:** convierte `start_at` y `end_at` de cada cita en un intervalo comparable.
- **Dónde:** `V6__appointments.sql:47`.
- **Por qué:** expresa el cruce de citas en una sola condición.

**`pg_trgm` (trigramas)**
- **Qué es:** extensión que divide los textos en grupos de 3 letras y mide su parecido (`similarity()`, operador `%`).
- **Uso:** búsqueda tolerante a errores en el CIE-10, los medicamentos y los tratamientos.
- **Dónde:** `V7__icd10_catalog.sql`; consultas en `persistence/repository/Icd10CodeRepository.java` y `MedicationRepository.java`.
- **Por qué:** el odontólogo escribe rápido y con errores; «carie dentina» debe encontrar «Caries de la dentina».

**Índice GIN**
- **Qué es:** índice «invertido» que, para cada trigrama, guarda en qué filas aparece.
- **Uso:** acelera las búsquedas por similitud y por fragmento (`ILIKE '%texto%'`).
- **Dónde:** `V7`, `V9`, `V10`, `V14` (`… USING gin (… gin_trgm_ops)`).
- **Por qué:** evita recorrer catálogos de miles de códigos en cada tecla.

**Disparador contra el borrado (*trigger*)**
- **Qué es:** función que la base de datos ejecuta automáticamente ante un evento.
- **Uso:** impide eliminar pagos: solo se anulan con motivo.
- **Dónde:** `V15__payments.sql` (`trg_payments_no_delete`).
- **Por qué:** conserva la integridad de los cobros (RF08, RNF04).

**Flyway**
- **Qué es:** herramienta de **migraciones**: scripts SQL numerados que crean y modifican el esquema en orden.
- **Uso:** el esquema completo (V1 a V22) se aplica solo al arrancar la API.
- **Dónde:** `src/main/resources/db/migration/`.
- **Por qué:** el esquema queda versionado con el código y es reproducible en cualquier servidor (RNF04).

---

## API (backend)

**Spring Boot 3.5 (Java 21)**
- **Qué es:** *framework* de Java para construir servicios web.
- **Uso:** la API: reglas del negocio y única escritura en la base de datos.
- **Dónde:** `bellidental-backend/`.
- **Por qué:** mayor total en la matriz de selección; experiencia del desarrollador.

**Monolito modular**
- **Qué es:** una sola aplicación desplegada como una unidad, con el código dividido en módulos que solo se comunican por interfaces públicas.
- **Uso:** módulos `appointments`, `clinical`, `billing`, `bot`… con capas `api`, `application` y `domain`.
- **Dónde:** `src/main/java/com/bellidental/`.
- **Por qué:** da la modularidad de los microservicios sin su costo de operación, para un equipo y un servidor pequeños.

**Spring Security**
- **Qué es:** módulo de Spring para autenticación y autorización.
- **Uso:** inicio de sesión, permisos por rol y filtro de la clave del agente.
- **Dónde:** `security/` (`JwtService`, `BotApiKeyFilter`).
- **Por qué:** RNF01 (credenciales únicas y roles).

**JWT y JJWT**
- **Qué es:** JWT (*JSON Web Token*) es un **estándar** de token firmado (`cabecera.datos.firma`); JJWT es la **biblioteca** Java que crea y verifica esos tokens.
- **Uso:** tras el inicio de sesión, el navegador envía el token en cada petición y la API comprueba quién es y su rol.
- **Dónde:** `security/JwtService.java`; `pom.xml` (`jjwt` 0.12.6).
- **Por qué:** sesión sin estado en el servidor, sencilla de validar.

**Spring Data JPA / Hibernate**
- **Qué es:** capa que traduce objetos Java a filas de la base de datos.
- **Uso:** las entidades y repositorios de cada módulo.
- **Dónde:** `persistence/entity`, `persistence/repository`.
- **Por qué:** es el estándar del ecosistema Spring.

**Hibernate Envers**
- **Qué es:** extensión de Hibernate que guarda automáticamente cada versión de las filas modificadas.
- **Uso:** historial de cambios con usuario y fecha (RNF02, BN4).
- **Dónde:** entidades con `@Audited`; tablas `*_aud` y `revision_info` en `V16__audit.sql`.
- **Por qué:** trazabilidad completa sin programarla a mano.

**OpenPDF**
- **Qué es:** biblioteca para generar archivos PDF.
- **Uso:** receta y comprobante numerado.
- **Dónde:** `prescriptions/application/PrescriptionPdfService.java`, `billing/application/ReceiptPdfService.java`.
- **Por qué:** documentos imprimibles con firma y leyenda de confidencialidad (RF05, RF08).

**springdoc-openapi**
- **Qué es:** genera automáticamente la documentación de los *endpoints*.
- **Uso:** consulta de la API durante el desarrollo.
- **Dónde:** `pom.xml`.
- **Por qué:** documenta el contrato que usan la web y el agente.

**JUnit 5 y Testcontainers**
- **Qué es:** JUnit ejecuta las pruebas; Testcontainers levanta un PostgreSQL real en Docker durante la prueba.
- **Uso:** 52 clases de prueba; las de integración (`*IT`) usan la base real, incluida la restricción anticruce.
- **Dónde:** `src/test/java/…`, `support/TestcontainersConfiguration.java`.
- **Por qué:** reglas como `EXCLUDE` solo se pueden probar contra PostgreSQL real.

---

## Interfaz web

**Angular 22**
- **Qué es:** *framework* de Google para aplicaciones web de una sola página (SPA).
- **Uso:** pantallas de la secretaria, el odontólogo y el director.
- **Dónde:** `bellidental-frontend/src/app`.
- **Por qué:** formularios extensos con validación (Formulario 033); mayor total en su matriz.

**SPA (aplicación de una sola página)**
- **Qué es:** la página se carga una vez y luego cambia de pantalla sin recargar, pidiendo datos a la API.
- **Uso:** toda la interfaz.
- **Dónde:** `bellidental-frontend/`.
- **Por qué:** respuesta rápida y sin instalación en los equipos.

**Angular CDK**
- **Qué es:** kit de componentes base de Angular, sin estilo, accesibles.
- **Uso:** diálogos (`cdk/dialog`), paneles superpuestos (`cdk/overlay`) y adaptación al tamaño de pantalla (`cdk/layout`).
- **Dónde:** importaciones `@angular/cdk/...` en `src/`.
- **Por qué:** panel lateral de tratamientos y receta sin tapar el odontograma.

**nginx**
- **Qué es:** servidor web ligero.
- **Uso:** sirve los archivos compilados de Angular dentro de su contenedor (6 MB medidos).
- **Dónde:** imagen `bellidental-frontend`.
- **Por qué:** mínimo consumo para archivos estáticos.

---

## Agente conversacional

**Python y FastAPI**
- **Qué es:** FastAPI es un *framework* web de Python para crear servicios con validación automática.
- **Uso:** `GET /webhook` (verificación de Meta) y `POST /webhook` (mensajes).
- **Dónde:** `bellidental-agent/app/main.py`.
- **Por qué:** el ecosistema Python tiene clientes de LLM y validación de salidas estructuradas.

**Uvicorn (ASGI)**
- **Qué es:** el servidor que ejecuta la aplicación FastAPI; ASGI es el estándar asíncrono de Python.
- **Uso:** escucha en el puerto 8000 del contenedor y entrega las peticiones a FastAPI.
- **Dónde:** `bellidental-agent/Dockerfile:28`.
- **Por qué:** es el servidor recomendado para FastAPI.

**httpx**
- **Qué es:** cliente HTTP asíncrono de Python.
- **Uso:** enviar mensajes por la Graph API y llamar a la API interna, con un plazo de 10 s.
- **Dónde:** `app/whatsapp/client.py`, `app/backend/client.py`.
- **Por qué:** no bloquea al agente mientras espera respuestas.

**Pydantic / pydantic-settings**
- **Qué es:** validación de datos con tipos; versión para configuración.
- **Uso:** valida la respuesta del modelo y los mensajes de salida; lee claves y plazos de variables de entorno.
- **Dónde:** `app/dialog/models.py`, `app/nlu/models.py`, `app/config.py`.
- **Por qué:** ningún dato mal formado llega a WhatsApp ni a la API, y ningún secreto queda en el código.

**Máquina de estados**
- **Qué es:** modelo en el que la conversación está siempre en un paso definido y cada mensaje la lleva a otro según reglas.
- **Uso:** pasos `IDLE`, `MENU`, `BOOK_SLOT`, `RESCHEDULE_CONFIRM`, `URGENT_SLOT`…
- **Dónde:** `app/dialog/models.py` (`Step`), `app/dialog/router.py`.
- **Por qué:** comportamiento predecible: el código decide y nada se registra sin *Confirmar*.

**LLM con salida estructurada**
- **Qué es:** modelo de lenguaje al que se obliga a responder con un JSON de forma fija.
- **Uso:** Claude Haiku 5.5 convierte el texto libre en `intent` y datos (especialidad, día, franja); máximo 256 tokens y plazo de 8 s.
- **Dónde:** `app/nlu/anthropic_classifier.py`, `app/nlu/prompt.py`.
- **Por qué:** entiende el español informal sin entrenamiento, y su salida se puede validar.

**Intención y *slots***
- **Qué es:** la intención es *qué* quiere el paciente (agendar, precio…); los *slots* son los datos que la completan (especialidad, día, hora).
- **Uso:** la salida del modelo y la entrada de la máquina de estados.
- **Dónde:** `app/nlu/models.py`.
- **Por qué:** separa interpretar de decidir.

**Enmascaramiento**
- **Qué es:** sustituir datos sensibles por un marcador antes de enviarlos a un tercero.
- **Uso:** las secuencias de 7 o más dígitos (cédulas, teléfonos) se envían al modelo como `[número]`.
- **Dónde:** `app/nlu/prompt.py:6-7,68`.
- **Por qué:** el proveedor del modelo no recibe identificadores (RNF03, BN7).

**Idempotencia y deduplicación**
- **Qué es:** que procesar dos veces el mismo evento tenga el mismo efecto que procesarlo una vez.
- **Uso:** se recuerdan los últimos 1 000 identificadores de mensaje y se ignoran los repetidos.
- **Dónde:** `app/dialog/store.py` (`ProcessedMessages`), `main.py:134`.
- **Por qué:** Meta reintenta los eventos; sin esto, un mensaje podría procesarse dos veces.

**Candado por teléfono (`asyncio.Lock`)**
- **Qué es:** mecanismo que deja pasar un solo proceso a la vez.
- **Uso:** dos mensajes seguidos del mismo paciente no modifican su conversación al mismo tiempo.
- **Dónde:** `app/main.py:105-110`.
- **Por qué:** evita estados inconsistentes.

**pytest y dobles de prueba**
- **Qué es:** pytest es el marco de pruebas de Python; los dobles son versiones falsas de WhatsApp, la API y el modelo.
- **Uso:** conversaciones completas probadas sin servicios reales.
- **Dónde:** `bellidental-agent/tests/`.
- **Por qué:** pruebas rápidas y repetibles.

---

## WhatsApp

**WhatsApp Cloud API / Graph API**
- **Qué es:** la API oficial de Meta para que una empresa envíe y reciba mensajes de WhatsApp; la Graph API es la puerta HTTP de Meta (`graph.facebook.com/v23.0/…`).
- **Uso:** recepción por webhook y envío de texto, botones y listas.
- **Dónde:** `app/whatsapp/client.py`.
- **Por qué:** es el canal oficial, sin recargo de intermediario.

**Webhook**
- **Qué es:** URL de tu servidor a la que **Meta llama** (POST) cada vez que llega un mensaje.
- **Uso:** `https://bot.<dominio>/webhook`.
- **Dónde:** `app/main.py`, `deploy/Caddyfile`.
- **Por qué:** el agente reacciona al instante, sin preguntar a Meta cada cierto tiempo.

**Verificación por *challenge***
- **Qué es:** al registrar el webhook, Meta envía un número de desafío con tu token de verificación; si respondes ese mismo número, el webhook queda verificado.
- **Uso:** una vez, al configurar.
- **Dónde:** `app/main.py:184-193`.
- **Por qué:** prueba a Meta que la URL es tuya.

**Firma HMAC (`X-Hub-Signature-256`)**
- **Qué es:** huella criptográfica del mensaje calculada con el secreto de la aplicación.
- **Uso:** el agente la recalcula y descarta (401) lo que no coincide.
- **Dónde:** `app/whatsapp/signature.py`.
- **Por qué:** nadie puede inyectar mensajes falsos haciéndose pasar por Meta.

**Ventana de 24 h**
- **Qué es:** regla de Meta: se responde libremente durante 24 h desde el último mensaje del cliente; después, solo con plantillas aprobadas.
- **Uso:** el agente solo responde, así que siempre está dentro de la ventana.
- **Dónde:** política de Meta (no requiere código).
- **Por qué:** cumplir la política sin plantillas.

**Plantillas de mensaje**
- **Qué es:** mensajes predefinidos que Meta aprueba para escribir primero al cliente.
- **Uso:** previstas para los recordatorios (RF14), no habilitadas.
- **Dónde:** `app/reminders/job.py` (`recordatorio_cita`).
- **Por qué:** RF14 quedó como «Debería».

**Mensajes interactivos**
- **Qué es:** botones (hasta 3) y listas (hasta 10 filas) que el paciente toca en lugar de escribir.
- **Uso:** lista del menú; botones para el aviso, los horarios y *Confirmar*.
- **Dónde:** `app/dialog/menu.py`, `booking.py`, `consent.py`.
- **Por qué:** menos errores de escritura y respuestas exactas para la máquina de estados.

**Token de usuario del sistema**
- **Qué es:** credencial sin caducidad de una cuenta técnica de Meta Business.
- **Uso:** autoriza al agente a enviar mensajes.
- **Dónde:** variable `WA_ACCESS_TOKEN` en el `.env` del servidor.
- **Por qué:** los tokens normales caducan en horas.

**Enlace wa.me**
- **Qué es:** enlace que abre un chat de WhatsApp con un número.
- **Uso:** la derivación lleva al paciente al número de recepción.
- **Dónde:** `app/messages/texts.py:30` y `app/dialog/handoff.py`.
- **Por qué:** el agente y la recepción usan números distintos.

---

## Infraestructura

**VPS**
- **Qué es:** servidor virtual alquilado en la nube.
- **Uso:** Contabo Cloud VPS 4 (4 vCPU, 8 GB, Ubuntu 24.04).
- **Dónde:** `deploy/vps-setup.sh`.
- **Por qué:** IP pública y control total a bajo costo.

**Docker y Docker Compose**
- **Qué es:** Docker empaqueta cada servicio con todo lo que necesita (contenedor); Compose los define y arranca juntos.
- **Uso:** seis servicios: Caddy, web, API, agente, PostgreSQL y respaldo, con un límite de memoria cada uno.
- **Dónde:** `deploy/docker-compose.yml`.
- **Por qué:** el mismo archivo funciona en otro proveedor o en un equipo local (RNF04).

**Red interna de Docker**
- **Qué es:** red privada entre contenedores, invisible desde internet.
- **Uso:** el agente llama a `backend:8080` y la API a `postgres` por HTTP simple.
- **Dónde:** `docker-compose.yml`.
- **Por qué:** el tráfico interno no sale del servidor; el cifrado se hace en Caddy.

**GHCR (GitHub Container Registry)**
- **Qué es:** almacén de imágenes de contenedor de GitHub.
- **Uso:** imágenes `ghcr.io/…/bellidental-backend|frontend|agent|backup`.
- **Dónde:** `docker-compose.yml`.
- **Por qué:** el servidor descarga imágenes ya construidas y probadas.

**GitHub Actions (CI/CD)**
- **Qué es:** automatización que, en cada cambio, ejecuta las pruebas, construye la imagen y la despliega.
- **Uso:** un flujo por repositorio (backend, frontend y agente).
- **Dónde:** `.github/workflows/` de cada repositorio.
- **Por qué:** nada llega a producción sin pasar las pruebas.

**DNS y Cloudflare**
- **Qué es:** DNS traduce nombres de dominio a la IP del servidor; Cloudflare aloja esos registros.
- **Uso:** `app.<dominio>` y `bot.<dominio>` apuntan al VPS, sin el proxy de Cloudflare.
- **Dónde:** panel de Cloudflare.
- **Por qué:** dominio propio y estable (RNF05).

**Caddy (proxy inverso)**
- **Qué es:** servidor que recibe todo el tráfico de internet y lo reparte a cada contenedor.
- **Uso:** única entrada pública, HTTPS automático y bloqueo de `/api/v1/bot/*` y `/actuator/*`.
- **Dónde:** `deploy/Caddyfile`.
- **Por qué:** obtiene y renueva certificados solo, sin terceros que descifren.

**HTTPS y TLS**
- **Qué es:** TLS es el protocolo que cifra la conexión; HTTPS es HTTP sobre TLS.
- **Uso:** toda comunicación desde internet: navegadores y Meta.
- **Dónde:** Caddy.
- **Por qué:** cifrado en tránsito (BN7); Meta lo exige.

**Let's Encrypt y ACME**
- **Qué es:** Let's Encrypt es una autoridad de certificación gratuita; ACME es el protocolo automático para pedir y renovar certificados mediante un desafío.
- **Uso:** certificados de 90 días, renovados solos por Caddy.
- **Dónde:** `Caddyfile` (`email {$ACME_EMAIL}`).
- **Por qué:** HTTPS válido sin costo ni mantenimiento manual.

***Handshake* TLS**
- **Qué es:** negociación inicial de cada conexión: el servidor presenta su certificado y ambos acuerdan una clave de cifrado.
- **Uso:** cada vez que Meta o un navegador se conectan.
- **Dónde:** Caddy.
- **Por qué:** autentica al servidor y protege los datos.

**SSH con llaves**
- **Qué es:** acceso remoto cifrado al servidor con un par de llaves en lugar de una contraseña.
- **Uso:** administración del VPS; *root* y contraseñas desactivados.
- **Dónde:** `vps-setup.sh:61-62`.
- **Por qué:** evita ataques por adivinación de contraseñas.

**UFW (cortafuegos)**
- **Qué es:** interfaz sencilla del cortafuegos de Linux.
- **Uso:** solo abre los puertos 22 (SSH), 80 y 443.
- **Dónde:** `vps-setup.sh:32-35`.
- **Por qué:** la API, el agente y la base de datos no son accesibles desde fuera.

**fail2ban**
- **Qué es:** vigila los registros de acceso y bloquea temporalmente las IP con intentos fallidos repetidos.
- **Uso:** protege SSH.
- **Dónde:** `vps-setup.sh:31,36`.
- **Por qué:** frena los ataques automáticos de fuerza bruta.

**Actualizaciones automáticas (`unattended-upgrades`)**
- **Qué es:** instala los parches de seguridad de Ubuntu sin intervención.
- **Uso:** con reinicio de madrugada si hace falta.
- **Dónde:** `vps-setup.sh:31`.
- **Por qué:** el servidor se mantiene actualizado.

**Respaldo (`pg_dump`)**
- **Qué es:** volcado completo de la base de datos en un archivo.
- **Uso:** diario a las 20:30, con retención de 30 días y copia opcional a Google Drive (*rclone*).
- **Dónde:** `deploy/backup/` y `deploy/restore.sh`.
- **Por qué:** RNF04: los datos no se pierden ante una falla.

---

## Dominio clínico

**CIE-10**
- **Qué es:** Clasificación Internacional de Enfermedades, décima revisión (OMS): códigos de diagnóstico; por ejemplo, K02.1 es caries de la dentina.
- **Uso:** catálogo con búsqueda por código o similitud; diagnóstico obligatorio al cerrar la atención.
- **Dónde:** tabla `icd10_codes` (`V7`, `V14`).
- **Por qué:** lo exigen el Formulario 033 y la receta (RF03, RF05).

**Formulario 033**
- **Qué es:** formulario oficial del MSP para la historia clínica odontológica.
- **Uso:** se compone de lo registrado en la atención y se imprime.
- **Dónde:** vista e impresión en la interfaz web, con los datos del resumen clínico de la API (`clinicalsummary`).
- **Por qué:** registro único y normativo (BN1, BN2).

**Odontograma**
- **Qué es:** esquema de las piezas dentales en el que se marcan los hallazgos por pieza y cara.
- **Uso:** rojo para lo pendiente y azul para lo realizado.
- **Dónde:** módulo `odontogram`.
- **Por qué:** RF02; reemplaza el odontograma en papel.

**Índices CPO y ceo**
- **Qué es:** indicadores de salud oral. CPO (dientes permanentes) = Cariados + Perdidos + Obturados; ceo (dientes temporales) = cariados + extracción indicada + obturados.
- **Uso:** se calculan a partir del odontograma; no se almacenan.
- **Dónde:** `odontogram/domain/DentalIndexCalculator.java`.
- **Por qué:** campos del Formulario 033.
