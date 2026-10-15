# Especificación de diagramas: arquitectura general del sistema

Diagramas del apartado "Arquitectura general del sistema" (Objetivo 2). Se dibujan en draw.io y se exportan en PDF vectorial a `img/`:

| Diagrama | Archivo de salida | Figura en LaTeX |
|---|---|---|
| 1. Contexto (C4 nivel 1) | `img/C4_Contexto.pdf` | `fig:ob2_c4_contexto` |
| 2. Contenedores (C4 nivel 2) | `img/C4_Contenedores.pdf` | `fig:ob2_c4_contenedores` |
| 3. Módulos de la API | `img/Modulos.pdf` | `fig:ob2_modulos` |

## Notas de estilo (aplican a los tres)

- Colores sobrios, legibles en escala de grises:
  - Persona: relleno `#F2F2F2`, borde `#333333`.
  - Sistema propio o contenedor: relleno `#D9D9D9`, borde `#333333`, texto negro.
  - Sistema externo: relleno blanco, borde `#666666` punteado.
  - Límite (servidor, Docker Compose): sin relleno, borde `#666666` punteado.
  - Módulo implementado: relleno `#D9D9D9`, borde sólido. Módulo planificado: relleno blanco, borde punteado.
- Cada elemento lleva el formato C4: **nombre** en negrita, `[Tipo: Tecnología]` debajo y una descripción de una línea.
- Íconos: SVG monocromos de devicon.dev o simpleicons.org, guardados en una biblioteca propia de draw.io (Biblioteca → Nueva biblioteca). Tamaño 40 a 50 px.
- Tipografía sans-serif (Arial o Helvetica), 10 a 12 pt para los nombres y 9 pt para las etiquetas de las flechas.
- Fondo blanco, sin sombras ni degradados. Ancho máximo de la figura: el ancho del texto (14,5 cm).
- Exportar en PDF con la opción "Transparent Background" desactivada y "Crop" activado. Verificar que el PDF sea vectorial (los textos deben poder seleccionarse).
- Las flechas se dibujan con línea continua para las relaciones y punteada para los eventos. Cada flecha lleva una etiqueta con la acción y, entre paréntesis, el protocolo.

---

## 1. Diagrama de contexto (C4 nivel 1)

**Título sugerido:** Sistema de información de Bellidental: contexto.

### Elementos

| Nombre | Tipo C4 | Tecnología | Descripción | Ícono sugerido |
|---|---|---|---|---|
| Paciente | Persona | — | Agenda, reprograma o consulta por WhatsApp; recibe recordatorios si aceptó el aviso | Ícono de persona (forma "Actor" de draw.io) |
| Secretaria | Persona | — | Gestiona la agenda, los pacientes y los cobros | Ícono de persona |
| Odontólogo | Persona | — | Registra la historia clínica, el odontograma y los tratamientos | Ícono de persona |
| Director (administrador) | Persona | — | Administra catálogos, horarios y la configuración | Ícono de persona |
| Sistema de información Bellidental | Sistema | — | Centraliza la agenda, las historias clínicas y los cobros; incluye el agente | Ícono de servidor (forma "Server" de draw.io) |
| WhatsApp Cloud API | Sistema externo | Meta | Transmite los mensajes mediante webhook y entrega respuestas y recordatorios | WhatsApp (simpleicons.org: `whatsapp`) |
| Google Calendar | Sistema externo | Google | Recibe una copia de solo lectura de la agenda, un calendario por profesional | Google Calendar (simpleicons.org: `googlecalendar`) |
| Google Drive de la clínica | Sistema externo | Google | Almacena los respaldos cifrados de la base de datos | Google Drive (simpleicons.org: `googledrive`) |

### Relaciones

| Origen → destino | Etiqueta | Protocolo |
|---|---|---|
| Paciente → WhatsApp Cloud API | Envía mensajes | WhatsApp |
| WhatsApp Cloud API → Paciente | Entrega respuestas y recordatorios | WhatsApp |
| WhatsApp Cloud API → Sistema de información | Transmite los mensajes entrantes | Webhook HTTPS |
| Sistema de información → WhatsApp Cloud API | Envía respuestas y recordatorios | API HTTPS |
| Secretaria → Sistema de información | Gestiona agenda, pacientes y cobros | HTTPS (navegador) |
| Odontólogo → Sistema de información | Registra atención, historia y odontograma | HTTPS (navegador) |
| Director → Sistema de información | Configura catálogos y horarios | HTTPS (navegador) |
| Sistema de información → Google Calendar | Envía la copia de la agenda (solo lectura) | API HTTPS |
| Sistema de información → Google Drive | Deposita los respaldos cifrados | API HTTPS |

### Límites y agrupaciones

- No hay límites de despliegue en este nivel. Los actores y los sistemas externos quedan fuera de la caja del sistema.

### Disposición sugerida

- Centro: Sistema de información.
- Izquierda: Paciente y, entre ambos, WhatsApp Cloud API.
- Arriba: Secretaria, Odontólogo y Director.
- Derecha: Google Calendar y Google Drive.

### Leyenda

Persona (ícono) · Sistema propio (rectángulo gris) · Sistema externo (rectángulo punteado) · Relación (flecha con protocolo).

---

## 2. Diagrama de contenedores (C4 nivel 2)

**Título sugerido:** Sistema de información de Bellidental: contenedores.

### Elementos

| Nombre | Tipo C4 | Tecnología | Descripción | Ícono sugerido |
|---|---|---|---|---|
| Usuario de la clínica | Persona | — | Personal que accede desde un navegador | Ícono de persona |
| Paciente | Persona | — | Escribe desde WhatsApp | Ícono de persona |
| Proxy inverso y servidor web | Contenedor | nginx con Let's Encrypt | Termina TLS, sirve los archivos de la aplicación web y expone solo `/api` y el webhook | nginx (devicon: `nginx-original`); candado para Let's Encrypt (simpleicons.org: `letsencrypt`) |
| Aplicación web | Contenedor (en el navegador) | Angular 22.1 (SPA) | Se ejecuta en el navegador del personal; no es un contenedor Docker | Angular (devicon: `angular-original`) |
| API del sistema | Contenedor | Spring Boot 3.5 con Java 21 | Lógica de negocio por módulos, JWT y motor conversacional del agente | Spring (devicon: `spring-original`) |
| Base de datos | Contenedor (base de datos) | PostgreSQL 16 | Almacena los datos de la clínica en un esquema compartido | PostgreSQL (devicon: `postgresql-original`) |
| Servicio de respaldo | Contenedor | pg_dump programado en Docker | Genera un volcado diario cifrado y lo copia a Google Drive | Docker (devicon: `docker-original`) |
| WhatsApp Cloud API | Sistema externo | Meta | Mensajería; transmite los eventos mediante webhook | WhatsApp (simpleicons.org: `whatsapp`) |
| Google Calendar | Sistema externo | Google | Copia de solo lectura de la agenda | Google Calendar (simpleicons.org: `googlecalendar`) |
| Google Drive de la clínica | Sistema externo | Google | Almacenamiento de respaldos | Google Drive (simpleicons.org: `googledrive`) |

### Relaciones

| Origen → destino | Etiqueta | Protocolo |
|---|---|---|
| Usuario de la clínica → Aplicación web | Usa la aplicación | Navegador |
| Paciente → WhatsApp Cloud API | Escribe | WhatsApp |
| WhatsApp Cloud API → Paciente | Entrega respuestas y recordatorios | WhatsApp |
| WhatsApp Cloud API → Proxy inverso | Envía eventos del webhook | HTTPS (443) |
| Proxy inverso → Aplicación web | Entrega los archivos de la SPA | HTTPS (443) |
| Aplicación web → API del sistema | Llama a `/api` con JWT | HTTPS a través del proxy |
| Proxy inverso → API del sistema | Reenvía `/api` y el webhook | HTTP interno |
| API del sistema → Base de datos | Lee y escribe datos | Spring Data JPA (TCP 5432) |
| API del sistema → WhatsApp Cloud API | Envía mensajes y recordatorios | API HTTPS |
| API del sistema → Google Calendar | Envía la copia de la agenda | API HTTPS |
| Servicio de respaldo → Base de datos | Genera el volcado (`pg_dump`) | TCP 5432 |
| Servicio de respaldo → Google Drive | Sube la copia cifrada | API HTTPS |

### Límites y agrupaciones

- **Servidor virtual (VPS)**: caja punteada. Su título incluye la nota "contratado a nombre de la clínica".
- **Docker Compose**: caja punteada anidada dentro del VPS que agrupa los cuatro contenedores Docker (nginx, API, base de datos y respaldo).
- **Navegador**: caja punteada fuera del VPS, junto al usuario de la clínica, que contiene la aplicación web (SPA).
- Los sistemas externos y los actores quedan fuera del VPS.

### Disposición sugerida

- Izquierda: usuario de la clínica y su navegador con la SPA; debajo, el paciente.
- Centro: caja del VPS con nginx arriba, la API en el medio y la base de datos y el respaldo abajo.
- Derecha: WhatsApp Cloud API, Google Calendar y Google Drive, alineados con las flechas que reciben.

### Leyenda

Persona (ícono) · Contenedor (rectángulo gris con tecnología) · Sistema externo (rectángulo punteado) · Límite VPS / Docker Compose (caja punteada) · Relación (flecha con protocolo).

---

## 3. Diagrama de módulos de la API

**Título sugerido:** API del sistema: módulos del monolito modular.

### Elementos

Cada módulo es una caja con el nombre del paquete (`com.bellidental.<módulo>`), su interfaz pública y su responsabilidad en una línea. Sin íconos en este diagrama.

| Módulo | Estado | Interfaz pública | Responsabilidad |
|---|---|---|---|
| identity | Implementado | Ninguna | Usuarios, roles y autenticación con JWT |
| patients | Implementado | `PatientDirectory` | Datos de identificación e historial inmediato |
| professionals | Implementado | `ProfessionalDirectory` | Profesionales, especialidades y horarios |
| clinicalrecords | Implementado | `ClinicalRecordDirectory` | Historia clínica y antecedentes |
| appointments | Implementado | `AppointmentScheduler` | Agenda única y validación anticruce |
| clinical | Implementado | `ClinicalDirectory` | Atenciones y diagnósticos (CIE-10) |
| odontogram | Implementado | Ninguna | Odontograma por pieza y cara |
| treatments | Planificado | `TreatmentDirectory` | Catálogo de tratamientos y precios |
| prescriptions | Planificado | Ninguna | Recetas y su impresión |
| billing | Planificado | `BillingDirectory` | Abonos, saldo calculado y comprobante interno |
| calendar | Planificado | Ninguna | Copia de solo lectura en Google Calendar |
| whatsapp | Planificado | Ninguna (webhook de entrada) | Motor conversacional del agente, aviso de privacidad, webhook y recordatorios |

### Disposición sugerida

- Ubicar en la parte superior los módulos sin dependencias (identity, patients, professionals, treatments).
- En el centro, appointments y clinicalrecords; debajo, clinical (depende de ambos).
- En la parte inferior, odontogram, prescriptions, billing, calendar y whatsapp.
- Evitar cruces de flechas: las dependencias deben ir hacia arriba.

### Relaciones

Las flechas solo representan dependencias por interfaz pública. Etiqueta: nombre de la interfaz.

| Origen → destino | Etiqueta | Tipo de línea |
|---|---|---|
| clinicalrecords → patients | `PatientDirectory` | Continua |
| appointments → patients | `PatientDirectory` | Continua |
| appointments → professionals | `ProfessionalDirectory` | Continua |
| clinical → appointments | `AppointmentScheduler` | Continua |
| clinical → clinicalrecords | `ClinicalRecordDirectory` | Continua |
| odontogram → clinical | `ClinicalDirectory` | Continua |
| odontogram → patients | `PatientDirectory` | Continua |
| prescriptions → clinical | `ClinicalDirectory` | Continua |
| billing → clinical | `ClinicalDirectory` | Continua |
| billing → treatments | `TreatmentDirectory` | Continua |
| billing → patients | `PatientDirectory` | Continua |
| whatsapp → patients | `PatientDirectory` | Continua |
| whatsapp → professionals | `ProfessionalDirectory` | Continua |
| whatsapp → appointments | `AppointmentScheduler` | Continua |
| whatsapp → treatments | `TreatmentDirectory` (solo precios) | Continua |
| calendar → professionals | `ProfessionalDirectory` | Continua |
| appointments → calendar | Publica eventos de dominio | Punteada |
| appointments → whatsapp | Publica eventos de dominio (recordatorios) | Punteada |

**Importante:** no dibujar ninguna flecha desde whatsapp hacia clinical, odontogram, prescriptions ni billing.

### Límites y agrupaciones

- **API Spring Boot 3.5 (monolito modular)**: caja exterior que contiene los doce módulos. Subtítulo: "Un único despliegue".
- **Nota de nombres**: en el código, el paquete del agente y la sincronización se llama `notifications` y existe además `dashboard`; el diagrama usa los nombres funcionales.
- **Persistencia compartida**: franja horizontal en la parte inferior de la caja de la API, con el texto "Entidades y repositorios compartidos (esquema único de PostgreSQL)". Conectar con una línea punteada a la base de datos del diagrama de contenedores, o simplemente rotularla.

### Destacar el agente

- Borde grueso en la caja de whatsapp.
- Nota junto a la caja: "Sin dependencia de módulos clínicos ni de cobros (RNF03)".

### Leyenda

Módulo implementado (borde sólido) · Módulo planificado (borde punteado) · Dependencia por interfaz pública (flecha continua con nombre de la interfaz) · Evento de dominio (flecha punteada) · Franja de persistencia compartida.

---

## Entregables

1. Tres archivos draw.io (`diagramas/drawio/`), uno por diagrama, con la biblioteca de íconos incluida.
2. Tres PDF vectoriales en `img/`: `C4_Contexto.pdf`, `C4_Contenedores.pdf` y `Modulos.pdf`. Al existir, las figuras del apartado se muestran automáticamente (la compilación usa `\IfFileExists`).
