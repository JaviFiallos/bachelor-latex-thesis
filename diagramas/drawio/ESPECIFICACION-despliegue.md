# Especificación de diagrama: esquema de despliegue tecnológico

Diagrama del apartado "Esquema de despliegue tecnológico" (Objetivo 2). Es un diagrama de despliegue UML que se dibuja en draw.io y se exporta en PDF vectorial a `img/`:

| Diagrama | Archivo de salida | Figura en LaTeX |
|---|---|---|
| Despliegue UML | `img/Despliegue.pdf` | `fig:ob2_despliegue` |

Archivo fuente sugerido: `diagramas/drawio/despliegue.drawio`, con la biblioteca de íconos incluida.

## Notas de estilo

- Colores sobrios, legibles en escala de grises (mismos criterios que `ESPECIFICACION-arquitectura-general.md`):
  - Nodo de hardware (equipo, servidor): forma de cubo, relleno `#F2F2F2`, borde `#333333`.
  - Nodo de entorno de ejecución (Docker, contenedor): relleno `#D9D9D9`, borde `#333333`.
  - Artefacto desplegado: forma de documento o rectángulo con el estereotipo `«artifact»`, relleno blanco, borde `#333333`.
  - Nodo externo (Meta, Google): borde `#666666` punteado.
  - Límite (VPS, Docker Compose): sin relleno, borde `#666666` punteado.
  - Elementos agregados por el agente: borde grueso (3 px) y nota "Agregado por el agente".
- Cada nodo lleva el estereotipo UML entre `«»` en la primera línea, el nombre en negrita y, debajo, la tecnología entre corchetes.
- Íconos: SVG monocromos de devicon.dev o simpleicons.org, guardados en una biblioteca propia de draw.io (Biblioteca → Nueva biblioteca). Tamaño 40 a 50 px. Convertir a escala de grises antes de guardarlos.
- Tipografía sans-serif (Arial o Helvetica), 10 a 12 pt para los nombres y 9 pt para las etiquetas de las flechas.
- Fondo blanco, sin sombras ni degradados. Ancho máximo de la figura: el ancho del texto (14,5 cm).
- Exportar en PDF con "Transparent Background" desactivado y "Crop" activado. Verificar que el PDF sea vectorial (los textos deben poder seleccionarse).
- Las relaciones se dibujan con línea continua. Los eventos (envío de eventos del webhook) se dibujan punteados. Cada flecha lleva una etiqueta con la acción y, entre paréntesis, el protocolo.

---

## Título sugerido

Sistema de información de Bellidental: despliegue.

## Elementos

### Nodos de hardware (forma de cubo, `«device»`)

| Nodo | Estereotipo | Tecnología | Contenido o artefactos | Ícono sugerido |
|---|---|---|---|---|
| Equipos de la clínica | `«device»` | Navegador web | Artefacto: aplicación web (SPA Angular). Equipos de recepción, consultorios y dirección | Ícono de computadora portátil (forma "Laptop" de draw.io) |
| Servidor virtual (VPS) | `«device»` | Contratado a nombre de la clínica | Contiene el nodo Docker Compose | Ícono de servidor (forma "Server" de draw.io) |

### Entorno de ejecución dentro del VPS

| Nodo | Estereotipo | Tecnología | Artefacto desplegado | Ícono sugerido |
|---|---|---|---|---|
| Docker Compose | `«execution environment»` | Docker y Docker Compose | Ninguno (agrupa los cuatro contenedores) | Docker (devicon: `docker-original`) |
| Proxy inverso | `«execution environment»` | nginx con Let's Encrypt | Artefacto: configuración de TLS y rutas (`/api` y webhook) | nginx (devicon: `nginx-original`); candado para Let's Encrypt (simpleicons.org: `letsencrypt`) |
| API del sistema | `«execution environment»` | Spring Boot 3.4, Java 21 | Artefacto: `bellidental-api.jar`, con el módulo del agente | Spring (devicon: `spring-original`) |
| Base de datos | `«execution environment»` | PostgreSQL 16 | Artefacto: esquema `bellidental` en el volumen `postgres_data` | PostgreSQL (devicon: `postgresql-original`) |
| Servicio de respaldo | `«execution environment»` | `pg_dump` programado | Artefacto: script de volcado cifrado diario | Ícono de Docker, o ninguno |

### Nodos externos

| Nodo | Estereotipo | Tecnología | Artefacto o contenido | Ícono sugerido |
|---|---|---|---|---|
| Meta (WhatsApp Cloud API) | `«cloud»` | Plataforma de Meta | Artefacto: plantillas de mensajes aprobadas. Número de WhatsApp de la clínica | WhatsApp (simpleicons.org: `whatsapp`); Meta (simpleicons.org: `meta`) |
| Google (Calendar) | `«cloud»` | Google Calendar API | Artefacto: calendario por profesional (solo lectura) | Google Calendar (simpleicons.org: `googlecalendar`) |
| Almacenamiento externo | `«cloud»` | Google Drive de la clínica | Artefacto: respaldos cifrados de la base de datos | Google Drive (simpleicons.org: `googledrive`) |

## Relaciones

| Origen → destino | Etiqueta | Protocolo | Tipo de línea |
|---|---|---|---|
| Equipos de la clínica → Proxy inverso | Usa la aplicación web | HTTPS (443) | Continua |
| Meta (WhatsApp Cloud API) → Proxy inverso | Envía eventos del webhook | HTTPS (443) | Punteada; agregada por el agente |
| Proxy inverso → Aplicación web (artefacto) | Entrega los archivos de la SPA | HTTP interno | Continua |
| Proxy inverso → API del sistema | Reenvía `/api` y el webhook | HTTP interno | Continua |
| API del sistema → Base de datos | Lee y escribe datos | JDBC (TCP 5432) | Continua |
| API del sistema → Meta (WhatsApp Cloud API) | Envía respuestas y recordatorios | API HTTPS | Continua; agregada por el agente |
| API del sistema → Google (Calendar) | Envía la copia de la agenda | API HTTPS | Continua |
| Servicio de respaldo → Base de datos | Lee el volcado | TCP 5432 | Continua |
| Servicio de respaldo → Almacenamiento externo | Sube la copia cifrada | API HTTPS | Continua |

## Límites y agrupaciones

- **Servidor virtual (VPS)**: caja punteada que contiene el nodo Docker Compose. Su título incluye la nota "contratado a nombre de la clínica".
- **Docker Compose**: caja punteada anidada dentro del VPS que agrupa los cuatro contenedores (proxy inverso, API, base de datos y servicio de respaldo).
- Los equipos de la clínica, Meta, Google y el almacenamiento externo quedan fuera del VPS.
- La aplicación web se dibuja como artefacto del proxy inverso, porque nginx la sirve.

## Agregados por el agente

Destacar con borde grueso y una nota junto a cada elemento:

- Relación Meta → Proxy inverso: nota "Webhook por HTTPS (exigido por Meta)".
- Nodo Meta: nota "Número de WhatsApp exclusivo del agente y plantillas aprobadas (recordatorios fuera de la ventana de 24 horas)".
- Artefacto `bellidental-api.jar`: nota "Incluye el módulo del agente; sin acceso a módulos clínicos ni de cobros".

## Leyenda

Nodo de hardware (cubo) · Entorno de ejecución (rectángulo gris) · Artefacto (rectángulo blanco con `«artifact»`) · Nodo externo (rectángulo punteado) · Límite VPS y Docker Compose (caja punteada) · Relación (flecha continua con protocolo) · Evento (flecha punteada) · Elemento agregado por el agente (borde grueso).

## Entregables

1. Un archivo draw.io (`diagramas/drawio/despliegue.drawio`) con la biblioteca de íconos incluida.
2. Un PDF vectorial en `img/Despliegue.pdf`. Al existir, la figura del apartado se muestra automáticamente (la compilación usa `\IfFileExists`).
