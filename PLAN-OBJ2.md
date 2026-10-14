# Plan de implementación — Objetivo 2

Sección de resultados: **Diseño del sistema de información y de la arquitectura del agente conversacional**.
Archivo destino: `tex/ResultsAndDiscussion/results-ob2.tex` (incluido desde `resultados-discusion.tex`).

## Decisiones tomadas

| # | Decisión | Efecto |
|---|---|---|
| A | Resultados agrupados por objetivo | `\subsection{Objetivo 1...}`, `\subsection{Objetivo 2...}`; niveles internos bajan uno |
| B | Despliegue en VPS | 4.2.8 describe VPS; instalación local como alternativa con el mismo Docker Compose |
| C | Recordatorio con Confirmar / Cancelar / Reprogramar | Ajustar N3 y RF14 del Obj. 1; BPMN to-be ya actualizado |
| D | Se mantiene reprogramar por bot (RF12) | — |
| E | Metodología: Kanban. **No se mencionan asistentes de IA** | 4.2.2 y 4.2.9 |
| F | Sin diagrama de secuencia del registro de la atención | Solo las 2 secuencias del agente |
| G | WhatsApp: pruebas con la cuenta del desarrollador, producción con la de la clínica | Entornos en 4.2.8; limitación en 4.2.10 |
| H | Fundamento: párrafos breves | Fase 1 |
| I | Ajustes al Obj. 1 | Fase 0 |

## Reglas de redacción

- Prima lo visual: tablas, diagramas y frases cortas. Prosa más extensa solo en 4.2.10.
- Citar instrumentos con la convención vigente: `Tabla~\ref{tab:instrumento2}, P1`, `Tabla~\ref{tab:p5_frecuencia}`.
- Nunca usar los códigos internos del backend (D-4, D-9, D-10, O1…): escribir la regla.
- No usar "MVP"; usar "alcance esencial" o "plan de desarrollo".
- Numeración de RF/RNF/BN/N/PC: la de la tesis (no la de `MVP-SCOPE.md`).
- Cifrado: solo "en tránsito (TLS)"; Meta procesa los mensajes como encargado del tratamiento.

---

## Fase 0 — Ajustes al Objetivo 1 (`results-ob1.tex`)

| Línea | Actual | Cambio | Motivo |
|---|---|---|---|
| 234 | BN7: "con comunicación cifrada" | "con comunicación cifrada en tránsito" | Con Cloud API, Meta procesa los mensajes; no hay cifrado extremo a extremo hasta la clínica |
| 397 | RNF03: "con comunicación cifrada" | Ídem | Ídem |
| 280 | N3: "opción de confirmar o cancelar" | "opciones para confirmar, cancelar o reprogramar" | Decisión C |
| 389 | RF14: "opciones para confirmar o cancelar"; origen "PC8; N3; BN7" | "confirmar, cancelar o reprogramar"; origen "PC8; N2, N3; BN7" | Decisión C |
| 336 | "se desarrolla en el capítulo siguiente" | "se desarrolla en el apartado del Objetivo 2" | Está en el mismo capítulo |
| 408 | "sin afectar el alcance mínimo viable" | "sin afectar el alcance esencial" | No usar MVP |
| 399, 403 | Origen "U" (RNF04, RNF06) sin definir | Eliminado | Sin referencia que lo respalde |
| Encabezados | `\subsection` por tema | Envolver en `\subsection{Objetivo 1: ...}` y bajar un nivel (`\subsection`→`\subsubsection`, `\subsubsection`→`\paragraph`) | Decisión A |
| `main.tex` | Sin formato para `\paragraph` | `\setcounter{secnumdepth}{4}` y `\titleformat{\paragraph}[block]` (el índice sigue hasta el 3.er nivel) | Que el 4.º nivel se numere y no quede en línea |

## Fase 1 — Fundamento teórico (breve)

Un párrafo de 3–5 líneas por tema, en `fundamento.tex`:

| Tema | Ubicación | Fuente (verificar) |
|---|---|---|
| Metodologías de desarrollo: Scrum, XP, Kanban | Nuevo `\paragraph` en "Sistemas de información en salud" | Sommerville (2016); Schwaber y Sutherland, *Scrum Guide* (2020); Anderson, *Kanban* (2010) |
| Monolito modular | Tras "Arquitectura de microservicios" | Richards y Ford, *Fundamentals of Software Architecture* (2020) |
| Modelo C4 y UML | Tras "Arquitectura de software" | Brown, *C4 model* (c4model.com); OMG, UML 2.5.1 (2017) |
| Diseño guiado por atributos (ADD) | Junto a ISO/IEC 25010 | Cervantes y Kazman (2016) |

---

## Fase 2 — Redacción de `results-ob2.tex`

Leyenda: ✅ listo para redactar · 💬 requiere sesión de preguntas · 📥 espera insumo tuyo

### Introducción ✅
1 párrafo: Obj. 1 → decisiones de diseño; los cuatro elementos del objetivo; el agente opera sobre la agenda centralizada, por eso se diseña también el sistema. Cita: Staras (2021).

### 4.2.1 Impulsores arquitectónicos ✅
- **Tabla de trazabilidad**: Evidencia (instrumento) → N/PC/BN → RF/RNF → Implicación arquitectónica (genérica, sin tecnologías).
- **Tabla de atributos de calidad** (ISO/IEC 25010): seguridad, disponibilidad, mantenibilidad/modularidad, usabilidad → RNF que lo origina.
- **Tabla de restricciones**: un desarrollador, tiempo acotado, MoSCoW, presupuesto de la clínica, VPS, cuenta de WhatsApp.

### 4.2.2 Metodología y marcos de modelado ✅
- Matriz de metodologías (Scrum, XP, Kanban, Scrumban, Cascada). Imperativos: un desarrollador, entregas incrementales, priorización MoSCoW. → **Kanban**.
- Matriz de notaciones (C4 + UML, 4+1, solo UML) → **C4 + UML**; BPMN 2.0 por continuidad con el Obj. 1.

### 4.2.3 Proceso propuesto (BPMN to-be) ✅
| Figura | Archivo | Estado |
|---|---|---|
| Ciclo de atención con el sistema (reemplaza Etapas 1 y 2) | `diagramas/bpmn/ToBe_Atencion.bpmn` | Borrador; revisar en bpmn.io y exportar PDF a `img/` |
| Comunicación con el paciente con el agente | `diagramas/bpmn/ToBe_Comunicacion_P1.bpmn` (grupos 1-2) y `_P2.bpmn` (grupos 3-4) | Borrador (incluye Reprogramar); ídem |

- Tabla as-is vs to-be por tramo (T1–T5) y PC resuelto. Efectos = hipótesis del Obj. 3, no resultados.

### 4.2.4 Selección de tecnologías
- **a) Sistema ✅**: tres matrices de dos tamices (imperativos de RNF01, RNF02, RF07, RNF04; deseables: experiencia, ecosistema, consumo de recursos).
  - Backend: Spring Boot 3.4 / Java 21 vs Django vs Laravel vs NestJS.
  - Frontend: Angular vs React vs Vue.
  - BD: PostgreSQL 16 vs MySQL vs MongoDB.
- **b) Agente 💬**: cuatro decisiones, pendientes de sesión:
  1. Acceso a WhatsApp: Cloud API vs BSP (Twilio) vs no oficiales (Baileys, whatsapp-web.js).
  2. Motor conversacional: módulo propio vs n8n vs Botpress vs Dialogflow vs Rasa.
  3. Comprensión: menú/reglas vs NLP por intenciones vs LLM (Hindelang 2024, Alejandrino 2023).
  4. Exposición del webhook / alojamiento: VPS con HTTPS directo vs túnel (Cloudflare, ngrok) en local.

### 4.2.5 Arquitectura general del sistema ✅
| Diagrama | Herramienta | Contenido |
|---|---|---|
| C4 nivel 1 (contexto) | draw.io | Actores: paciente, secretaria, odontólogos, director. Externos: WhatsApp Cloud API (Meta), Google Calendar |
| C4 nivel 2 (contenedores) | draw.io | SPA Angular (nginx), API Spring Boot (incluye módulo del agente), PostgreSQL, servicio de respaldo; todo en el VPS |
| Diagrama de módulos | draw.io | identity, patients, professionals, clinicalrecords, appointments, clinical, odontogram, treatments, prescriptions, billing, calendar, whatsapp; dependencias solo por interfaces públicas |

- Texto breve: monolito modular frente a microservicios (Roca 2020, Arcila 2022); continuidad con JWT; matiz: esquema de BD compartido.

### 4.2.6 Modelo de datos 📥
- ER por módulos desde `schema.dbml` (diseño completo, 32 tablas), **no** desde `bellidental_estructura.sql` (22 implementadas). Completo en anexo.
- Tabla de tablas principales (patients, appointments, professional_schedules, privacy_consents, appointment_reminders, users).
- Tabla de principios del modelo → norma/RNF: separación clínico/identificación (BN3, art. 38), anulación lógica sin borrado (RNF04), saldo calculado (RF08), auditoría (RNF02).
- Diagrama de estados de la cita (PlantUML): PENDING, CONFIRMED, ATTENDED, CANCELLED, NO_SHOW, RESCHEDULED (de `AppointmentTransitions`).

### 4.2.7 Arquitectura del agente conversacional 💬
| Elemento | Entregables |
|---|---|
| a) Estructura lógica | C4 nivel 3 por capas (canal, conversación, servicios de dominio consumidos, tareas programadas); el agente no accede a módulos clínicos ni de cobros |
| b) Componentes funcionales | Tabla de intenciones (aviso, identificación, menú, información, agendar, reprogramar, recordatorio, derivación) con RF, N, evidencia y reglas; diagrama de estados de la conversación (PlantUML) |
| c) Mecanismos de integración | Tabla de mecanismos de WhatsApp; integración con la agenda y con Google Calendar; secuencias "agendar por WhatsApp" y "recordatorio y respuesta" (PlantUML) |
| d) Seguridad y cumplimiento | Aviso previo y aceptación registrada, minimización, usuario técnico auditado, derivación, Meta como encargado, cifrado en tránsito |

### 4.2.8 Esquema de despliegue tecnológico ✅
- Diagrama de despliegue UML (draw.io, con íconos): VPS con Docker Compose (nginx + Angular, Spring Boot, PostgreSQL, respaldo), navegadores de la clínica, Meta, Google, Google Drive de la clínica (respaldos).
- Tabla de entornos:

| Entorno | WhatsApp | Infraestructura |
|---|---|---|
| Desarrollo | Número de prueba de Meta | Local |
| Pruebas | Número real en la cuenta del desarrollador | VPS |
| Producción | Cuenta y número de la clínica (solo cambia la configuración) | VPS a nombre de la clínica |

- Tabla de riesgos y mitigaciones: impago del VPS (cuenta de la clínica + respaldos externos), caída de internet en la clínica (ficha rápida en papel), pérdida del servidor (dump diario cifrado y restauración probada), datos de salud en un tercero (contrato de encargado; **verificar** transferencia internacional en la LOPDP).
- Recursos estimados: ≈0,6–1 GB de RAM en total; el agente no añade carga relevante (sin modelo de IA).

### 4.2.9 Plan de desarrollo ✅
- Tablero Kanban: Pendiente → En desarrollo → En pruebas → Terminado; WIP = 1.
- Tabla de tarjetas (tareas 001–018 reagrupadas) con RF cubierto, prioridad MoSCoW y dependencias; marcar las del agente.
- Estrategia de pruebas: integración por tarea con endpoints, unitarias de reglas, pruebas de la máquina de pasos del agente.
- Fuera de alcance (→ recomendaciones): pacientes nuevos por bot, recordatorio del mismo día, impresión del 033, firma electrónica, HL7 FHIR.
- Enlace con el Obj. 3: tramos del TGA que se medirán.

### 4.2.10 Discusión ✅ (al final)
- Contraste con antecedentes: Roca y Arcila (microservicios), Shaikh (cruce en la app vs en la BD), Alejandrino y Hindelang (reglas vs NLP), Tudor Car (mensajería masiva; vacío en carga del personal), Hmadchayyapum (LINE), Wong-Pérez (HL7 FHIR), Martínez (auditoría).
- Matriz de cobertura RF/RNF → componente.
- Limitaciones: esquema compartido, VPS dependiente de internet, cuenta de WhatsApp inicial del desarrollador, el agente no amplía cupos.

---

## Inventario de diagramas

| # | Diagrama | Sección | Herramienta | Fuente | Quién |
|---|---|---|---|---|---|
| 1 | BPMN to-be atención | 4.2.3 | bpmn.io | `diagramas/bpmn/ToBe_Atencion.bpmn` | Borrador listo; tú revisas |
| 2 | BPMN to-be comunicación | 4.2.3 | bpmn.io | `diagramas/bpmn/ToBe_Comunicacion_P1.bpmn` (grupos 1-2) y `_P2.bpmn` (grupos 3-4) | Borrador listo; tú revisas |
| 3 | C4 contexto | 4.2.5 | draw.io | `diagramas/drawio/` | Yo: contenido · Tú: dibujo |
| 4 | C4 contenedores | 4.2.5 | draw.io | ídem | ídem |
| 5 | Módulos | 4.2.5 | draw.io | ídem | ídem |
| 6 | ER por módulos | 4.2.6 | dbdiagram.io | `schema.dbml` | Tú |
| 7 | Estados de la cita | 4.2.6 | PlantUML | `diagramas/plantuml/` | Yo |
| 8 | C4 componentes del agente | 4.2.7 | draw.io | `diagramas/drawio/` | Yo: contenido · Tú: dibujo |
| 9 | Estados de la conversación | 4.2.7 | PlantUML | `diagramas/plantuml/` | Yo |
| 10 | Secuencia: agendar por WhatsApp | 4.2.7 | PlantUML | ídem | Yo |
| 11 | Secuencia: recordatorio y respuesta | 4.2.7 | PlantUML | ídem | Yo |
| 12 | Despliegue UML | 4.2.8 | draw.io | `diagramas/drawio/` | Yo: contenido · Tú: dibujo |

Íconos en draw.io: SVG de devicon.dev o simpleicons.org (monocromos si se imprime en grises) guardados como biblioteca propia; exportar en PDF vectorial a `img/`.

---

## Orden de trabajo

- [x] Fase 0 — ajustes al Obj. 1 y encabezados (hecho 2026-10-14; compila sin errores)
- [ ] Fase 1 — párrafos del fundamento + entradas bib (verificar fuentes)
- [ ] Crear `results-ob2.tex` e incluirlo
- [ ] Introducción, 4.2.1, 4.2.2
- [ ] 4.2.3 — revisar BPMN en bpmn.io, exportar PDF, redactar tabla as-is vs to-be
- [ ] 4.2.4 a)
- [ ] Sesión de preguntas 4.2.4 b) → redactar
- [ ] 4.2.5 — contenido C4 → dibujo en draw.io
- [ ] 4.2.6 — imágenes de dbdiagram + PlantUML de estados de la cita
- [ ] Sesión de preguntas 4.2.7 → redactar + PlantUML + C4 nivel 3
- [ ] 4.2.8 — diagrama de despliegue + tablas
- [ ] 4.2.9
- [ ] 4.2.10 + matriz de cobertura
- [ ] Compilar y revisar referencias cruzadas
- [ ] (Opcional) Renumerar `MVP-SCOPE.md` y `CONTEXT.md` del backend a la numeración de la tesis
