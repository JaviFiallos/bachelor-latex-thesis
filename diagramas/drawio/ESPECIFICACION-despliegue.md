# Especificación: despliegue (UML, simplificado)

| Salida | Figura |
|---|---|
| `img/Despliegue.pdf` | `fig:ob2_despliegue` |

Paleta y reglas: las de `ESPECIFICACION-arquitectura-general.md`. Tres zonas en columnas; solo nombres e íconos, **sin artefactos ni descripciones**. El detalle (tamaño del VPS, puertos, dominio, claves) está en la tabla de nodos.

## Zonas y nodos

| Zona (izquierda → derecha) | Nodos (forma de cubo `«device»` o nube) | Color |
|---|---|---|
| **Usuarios** | Equipos de la clínica (navegador) · Teléfono del paciente (WhatsApp) | Persona |
| **VPS de la clínica** | Caja punteada "Docker Compose" con: nginx · API Spring Boot (franja verde "Agente") · PostgreSQL · Respaldo | Contenedor / BD |
| **Servicios en la nube** | WhatsApp (Meta) · Google Calendar · Google Drive | Externo |

## Flechas (seis)

| Flecha | Etiqueta |
|---|---|
| Equipos de la clínica → nginx | HTTPS |
| Teléfono del paciente ↔ WhatsApp | Mensajes |
| WhatsApp → nginx | Webhook HTTPS |
| API → WhatsApp | Respuestas |
| API → Google Calendar | Agenda |
| Respaldo → Google Drive | Respaldo cifrado |

Las flechas internas del VPS (nginx → API → PostgreSQL ← Respaldo) se dibujan cortas y sin etiqueta.

Elementos del agente (franja "Agente", flechas de WhatsApp) en verde para distinguirlos.
