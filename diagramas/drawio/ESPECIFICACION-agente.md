# Especificación: componentes del agente (C4 nivel 3, simplificado)

| Salida | Figura |
|---|---|
| `img/C4_Componentes_Agente.pdf` | `fig:ob2_c4_componentes` |

> Uso actual: figura de integración del agente (apartado «Mecanismos de integración»). La estructura lógica y los componentes funcionales se dibujan en TikZ.

Paleta y reglas: las de `ESPECIFICACION-arquitectura-general.md`. Solo nombres en las cajas, **sin descripciones ni tecnologías**. Nueve cajas en total.

## Elementos

| Caja | Color | Ubicación |
|---|---|---|
| Paciente | Persona | Izquierda |
| WhatsApp (Meta) | Externo | Izquierda, junto al paciente |
| **Webhook** | Agente (verde) | Dentro de la caja "Agente" |
| **Motor conversacional** | Agente (verde) | Centro de la caja "Agente" |
| **Recordatorios** (ícono de reloj) | Agente (verde) | Debajo del motor |
| **Aviso de privacidad** | Agente (verde) | Junto al motor |
| Pacientes · Profesionales · Agenda · Precios | Contenedor (azul) | Una sola caja a la derecha: "Servicios del sistema" con los cuatro nombres en lista |
| PostgreSQL | Base de datos | Abajo |
| Módulos clínicos y cobros | `#F5F5F5`, borde punteado | Esquina derecha, aislada |

Límite: caja punteada **Agente (módulo de la API)** con las cuatro cajas verdes.

## Flechas (siete)

| Flecha | Etiqueta |
|---|---|
| Paciente ↔ WhatsApp | Mensajes |
| WhatsApp → Webhook | Evento firmado |
| Webhook → Motor | Mensaje |
| Motor → WhatsApp | Respuesta |
| Motor → Servicios del sistema | Consulta / agenda |
| Recordatorios → WhatsApp | Plantilla |
| Agente (borde de la caja) → PostgreSQL | Consentimientos y recordatorios |

- Sin flechas hacia "Módulos clínicos y cobros"; rótulo: "Sin acceso (RNF03)".
- Nota de una línea bajo Recordatorios: "Solo con aviso aceptado".
