# Especificación: arquitectura general del sistema

Diagramas sencillos: solo nombre y tecnología en cada caja, **sin descripciones**. El detalle está en las tablas del documento.

| Diagrama | Salida | Figura |
|---|---|---|
| 1. Contexto (C4 nivel 1) | `img/C4_Contexto.pdf` | `fig:ob2_c4_contexto` |
| 2. Contenedores (C4 nivel 2) | `img/C4_Contenedores.pdf` | `fig:ob2_c4_contenedores` |
| 3. Módulos de la API | `img/Modulos.pdf` | `fig:ob2_modulos` |

## Paleta común (todos los diagramas de draw.io)

| Elemento | Relleno | Borde |
|---|---|---|
| Persona | `#FFE6CC` | `#D79B00` |
| Sistema propio / contenedor | `#DAE8FC` | `#6C8EBF` |
| Agente conversacional | `#D5E8D4` | `#82B366` |
| Base de datos | `#E1D5E7` | `#9673A6` |
| Sistema externo | `#F5F5F5` | `#666666` (punteado) |
| Límite (VPS, Docker) | sin relleno | `#999999` (punteado) |

Reglas:
- Máximo 8–10 cajas por diagrama. Texto de 11–12 pt; etiquetas de flechas de 1 a 3 palabras, 10 pt.
- Íconos de 32 px solo en tecnologías y sistemas externos (devicon / simpleicons, a color).
- Orientación horizontal; ancho final 14,5 cm. Exportar PDF con "Crop".

---

## 1. Contexto (C4 nivel 1) — se mantiene

| Elemento | Tipo | Texto en la caja |
|---|---|---|
| Paciente | Persona | Paciente |
| Personal de la clínica | Persona | Secretaria · Odontólogo · Director (una sola caja con tres íconos, o tres pequeñas) |
| Sistema Bellidental | Sistema propio | **Sistema Bellidental** (incluye el agente) |
| WhatsApp Cloud API | Externo | WhatsApp (Meta) |
| Google Calendar | Externo | Google Calendar |
| Google Drive | Externo | Google Drive |

| Flecha | Etiqueta |
|---|---|
| Paciente ↔ WhatsApp | Mensajes |
| WhatsApp ↔ Sistema | Webhook / API |
| Personal → Sistema | Navegador |
| Sistema → Google Calendar | Copia de la agenda |
| Sistema → Google Drive | Respaldos |

Disposición: Paciente y WhatsApp a la izquierda; personal arriba; sistema al centro; Google a la derecha.

---

## 2. Contenedores (C4 nivel 2)

| Elemento | Color | Texto en la caja |
|---|---|---|
| Personal de la clínica | Persona | Personal |
| Paciente | Persona | Paciente |
| Aplicación web | Contenedor | **Aplicación web** [Angular] — dibujada en una caja "Navegador" |
| nginx | Contenedor | **nginx** [proxy + archivos web] |
| API | Contenedor | **API** [Spring Boot] — con una franja verde interna "Agente" |
| PostgreSQL | Base de datos | **PostgreSQL** |
| Respaldo | Contenedor | **Respaldo** [pg_dump] |
| WhatsApp, Google Calendar, Google Drive | Externos | Solo el nombre |

| Flecha | Etiqueta |
|---|---|
| Personal → Aplicación web | Usa |
| Aplicación web → nginx | HTTPS |
| WhatsApp → nginx | Webhook |
| nginx → API | `/api` |
| API → PostgreSQL | Datos |
| API → WhatsApp | Mensajes |
| API → Google Calendar | Agenda |
| Respaldo → PostgreSQL | Volcado |
| Respaldo → Google Drive | Copia cifrada |
| Paciente ↔ WhatsApp | Mensajes |

Límites: caja punteada **VPS · Docker Compose** con nginx, API, PostgreSQL y Respaldo. Fuera: personas, navegador y externos.

---

## 3. Módulos de la API (simplificado)

> **Reemplazado:** la figura `fig:ob2_modulos` ahora se dibuja en TikZ dentro de `arquitectura-general.tex`, con nombres funcionales en español. Esta especificación queda solo como referencia.

Sin interfaces, sin responsabilidades. Cuatro grupos de color con los nombres de los módulos dentro, y **solo cinco flechas entre grupos**.

| Grupo (caja) | Color | Módulos (texto) |
|---|---|---|
| Base | Contenedor (azul) | identity · patients · professionals |
| Agenda | Contenedor (azul) | appointments · calendar |
| Clínico y cobros | `#FFF2CC` / `#D6B656` | clinicalrecords · clinical · odontogram · treatments · prescriptions · billing |
| Agente | Agente (verde) | whatsapp |

| Flecha entre grupos | Etiqueta |
|---|---|
| Agenda → Base | usa |
| Clínico y cobros → Base | usa |
| Clínico y cobros → Agenda | usa |
| Agente → Agenda | agenda citas |
| Agente → Base | identifica |

- Franja inferior gris: "Esquema PostgreSQL compartido".
- Nota junto al agente, una línea: "Sin acceso a datos clínicos (RNF03)". Ninguna flecha entre Agente y Clínico.
- Módulos planificados en cursiva (treatments, prescriptions, billing, calendar, whatsapp). En el código, el agente usará el paquete `notifications`.
