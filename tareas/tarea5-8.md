# Tareas 5–8 — Resumen y revisión

Implementación: Haiku 5.5 (high). Revisión: Opus 5.5 (high).
Compilación (2026-10-14): **0 errores, 0 referencias/citas indefinidas**; queda una caja desbordada de 5,6 pt en la tabla de módulos.

Cambios previos del orquestador:
- Cita `msp2016reglamento` → `msp5216a` (`fundamento.tex`).
- Porcentajes unificados al cálculo exacto: 46,7 % y 62,9 % (8 ocurrencias en Inst. 3, análisis de datos, Obj. 1 y Obj. 2).
- `\usetikzlibrary{babel,arrows.meta,positioning}` en `main.tex` (el diagrama TikZ fallaba por el conflicto entre babel en español y TikZ: 48 errores).
- Anchos de tablas ajustados en `arquitectura-general.tex` y `modelo-datos.tex`.

Decisiones del autor para la tarea 6: Cloud API oficial · módulo propio en Spring Boot · menú + palabras clave · proxy inverso nginx + Let's Encrypt.

---

## Tarea 5 — Tecnologías del sistema
**Archivo:** `ob2/tecnologias.tex`

| Matriz | Resultado |
|---|---|
| `tab:ob2_matriz_backend` | Spring Boot 2,25 · Django 2,20 · NestJS 2,15 · Laravel 1,90 |
| `tab:ob2_matriz_frontend` | Angular 2,50 · Vue 2,15 · React 1,95 |
| `tab:ob2_matriz_bd` | PostgreSQL 2,80 · MySQL 2,05 · MongoDB descartado (1.er tamiz) |
| `tab:ob2_stack` | Resumen del stack con versiones |

## Tarea 6 — Tecnologías del agente
**Archivo:** `ob2/tecnologias-agente.tex`

| Matriz | Resultado |
|---|---|
| `tab:ob2_matriz_whatsapp` | Cloud API 2,80 · BSP 2,15 · no oficiales descartadas |
| `tab:ob2_matriz_motor` | Módulo propio 2,60 · n8n 1,80 · Botpress 1,55 · Rasa 1,35 · Dialogflow descartado |
| `tab:ob2_matriz_comprension` | Menú 2,60 · NLP 1,95 · LLM descartado |
| `tab:ob2_webhook` | Cualitativa: proxy inverso + Let's Encrypt |
| `tab:ob2_stack_agente` | Resumen |

## Tarea 7 — Arquitectura general
**Archivos:** `ob2/arquitectura-general.tex`, `diagramas/drawio/ESPECIFICACION-arquitectura-general.md`

- Contexto C4 (`fig:ob2_c4_contexto`, `tab:ob2_contexto`), contenedores (`fig:ob2_c4_contenedores`, `tab:ob2_contenedores`), monolito modular (`fig:ob2_modulos`, `tab:ob2_modulos`).
- Figuras pendientes: `img/C4_Contexto.pdf`, `img/C4_Contenedores.pdf`, `img/Modulos.pdf` (dibujar en draw.io según la especificación).

## Tarea 8 — Modelo de datos
**Archivo:** `ob2/modelo-datos.tex`

- ER (`fig:ob2_er`, pendiente `img/ER_Bellidental.pdf`), 32 tablas en 12 grupos (`tab:ob2_tablas_modulo`), tablas principales (`tab:ob2_tablas_principales`), principios (`tab:ob2_principios`), estados de la cita en TikZ (`fig:ob2_estados_cita`).

---

## Revisión (Opus 5.5, high)

### Veredicto general
Bien estructurado, reglas del plan respetadas y aritmética de las matrices correcta. Cuatro problemas que un tribunal detectaría: **la matriz de backend se invierte con dos puntuaciones corregidas**, **los criterios del motor conversacional favorecen al módulo propio por construcción**, **la tabla de módulos contradice el código (falta clinical → clinicalrecords)** y **la auditoría (RNF02) está incompleta**.

### Tarea 5 — tecnologias.tex
| Sev. | Línea | Problema | Corrección |
|---|---|---|---|
| **Alta** | 23–29 | Sin la experiencia, Spring queda último. "Pruebas con BD real" no tiene origen y puntúa mal a Django (prueba contra BD real por defecto; Testcontainers existe para Python, Node y PHP). Con Django = 3 gana Django | Django 3 en pruebas; Spring 3 en auditoría (Envers ≈ django-simple-history) → Spring 2,40 vs Django 2,30. Declarar la experiencia como criterio decisivo (un desarrollador, plazo) |
| **Alta** | 3; 23–28; 51–55; 78–81 | Sin frase que justifique los pesos; criterios sin origen | Una frase de pesos por matriz y el origen entre paréntesis en cada criterio |
| Media | 51–52 | "Estructura integrada" + "TypeScript nativo" = 40 % y describen Angular | Vincular a RF01/RNF06 (formularios extensos del 033) o fusionarlos |
| Media | 76, 86 | Imperativo "licencia OSI" solo aquí (la SSPL no impide uso interno) | Mismo imperativo que las demás ("sin licencias de pago") |
| Media | 100 | "Campos de auditoría de creación y modificación" exagera (sin `updated_by`; Envers no implementado) | "Hibernate Envers (historial con usuario y fecha), planificado" |
| Media | 100 | Spring Boot 3.4 parece fuera de soporte OSS desde finales de 2025 (verificar) | Decisión del autor |
| Baja | 78 | Criterio redactado como la característica de PostgreSQL | "Garantía de no cruce ante reservas concurrentes, en la propia BD (RF07)" |
| Baja | 33 | Relleno | Reescribir; aclarar que 3 = más favorable |

### Tarea 6 — tecnologias-agente.tex
| Sev. | Línea | Problema | Corrección |
|---|---|---|---|
| **Alta** | 46–50 | n8n/Botpress/Rasa invocarían la API, que valida en su transacción; puntuar n8n = 1 en "cambios en reglas" es erróneo y "aprendizaje de una plataforma adicional" es tautológico: 65 % del peso a favor del ganador | "Reglas de agenda en un único lugar, sin duplicarlas en el motor"; n8n 2–3. El módulo propio sigue ganando (≈ 2,60 vs 2,35) |
| Media | 43–44 | Botpress actual es SaaS; la v12 autoalojable está discontinuada | Precisarlo o marcar "No cumple" |
| Media | 5 | "Las revisiones asocian…" se apoya solo en Tudor Car; con Cloud API solo se cobran plantillas | "Una revisión de alcance…"; "se paga por plantilla (recordatorios)" |
| Media | 3 vs 82 | Se anuncian cuatro decisiones con el mismo método, pero el webhook es cualitativo | Explicar la excepción |
| Media | 30 | "El motor debe validar…" en un criterio deseable | "Conviene…" |
| Baja | 97 | Cloudflare Tunnel es gratuito y descifra el tráfico en su red (BN7) | Corregir costo y añadir argumento |
| Baja | 57, 80 | "Modelo local inviable" sin cifra de RAM; Alejandrino combina reglas y NLP; errata | Completar y corregir |
| Baja | 116–117 | Faltan RF09, RF11, RF12 (acceso) y RF12, RF14 (motor) | Completar |

### Tarea 7 — arquitectura-general.tex y especificación
| Sev. | Línea | Problema | Corrección |
|---|---|---|---|
| **Alta** | 91, 101; spec 154 | `EncounterService` usa `ClinicalRecordDirectory`: clinical también depende de clinicalrecords; "corresponden al código implementado" es falso | Añadir la dependencia en tabla y especificación |
| Media | 103, 107 | Los módulos comparten el paquete `persistence` (appointments usa `EncounterRepository`) | "Comparten esquema y capa de persistencia"; opcional ArchUnit/Spring Modulith en el plan |
| Media | 94–96 | Sobra prescriptions → treatments; faltan calendar → professionals y billing → patients | Ajustar tabla y especificación |
| Media | 87 | patients con "consentimiento", pero `privacy_consents` está en el grupo del agente | Unificar en whatsapp |
| Media | 105 | "Conserva la separación… sin su costo" promete demasiado; "conserva" ×3; extensión sin tocar el núcleo es de Roca | Reescribir y atribuir |
| Media | spec 79, 94, 106 | La SPA como contenedor Docker; en C4 corre en el navegador y nginx sirve sus archivos | Un nginx (proxy + estáticos), 4 contenedores, SPA en el navegador |
| Baja | spec | Falta WhatsApp → Paciente; sin disposición sugerida en diagramas 1–2; `angularjs-original` es AngularJS; "lee el volcado" → "genera (pg_dump)" | Completar |
| Baja | 98 | Caja desbordada 5,6 pt (columna "Requerimientos") | Encabezado "RF/RNF" o `\tabcolsep` 3 pt |

### Tarea 8 — modelo-datos.tex
| Sev. | Línea | Problema | Corrección |
|---|---|---|---|
| **Alta** | 93 | `revision_info` sola no dice qué cambió; RNF02 exige usuario de cada modificación | Envers con `revision_info` + tablas `*_aud` (citas, pacientes, atenciones, diagnósticos, hallazgos, tratamientos, recetas, pagos, historia), marcado como planificado, nota "no se muestran en el ER" |
| Media | 3, 12 | "Doce módulos" que no coinciden con los de la arquitectura | "Doce grupos de tablas" |
| Media | 90 | `patients.blood_type` (dato de salud) y `admin_notes` en la tabla de identificación que ve recepción: contradice arts. 27/38 | Mover a `clinical_records` o justificar |
| Baja | 40 | RF10 asignado al agente, pero los precios están en `treatment_catalog` | Mover RF10 a Tratamientos |
| Baja | 128–138 | "Reprogramar" sin "(sin llegada)"; doble borde no es UML; "el agente recorre los estados" impreciso | Leyenda o estado final UML; "las citas del agente siguen los mismos estados" |
| Baja | 45, 68 | "bot" y "agente" mezclados | Usar "agente" |
| Baja | 92 | Saldo por paciente vs RF08 "por sesión"; cálculo precio × cantidad | Precisar |

Verificado sin problemas: 32 tablas, campos y reglas vs `schema.dbml`; restricción de exclusión; estados vs `AppointmentTransitions`; atribuciones a Hindelang, Hmadchayyapum, Arcila (JWT) y Alejandrino.

### Correcciones prioritarias
1. Dependencia clinical → clinicalrecords en tabla y especificación; corregir la frase de la línea 101.
2. Matriz de backend: Django 3 en pruebas, Spring 3 en auditoría; declarar la experiencia como criterio decisivo.
3. Reformular criterios del motor conversacional y recalcular.
4. Justificar pesos y dar origen a cada criterio en las tres matrices del sistema.
5. Auditoría con Envers descrita como diseño (planificado); alinear la tabla de stack.
6. Imperativo de licencia uniforme en BD; corregir Botpress, la cita de Tudor Car y el costo por mensaje.
7. Matizar que se comparte la capa de persistencia; corregir dependencias de diseño.
8. SPA en el navegador en C4 contenedores; "doce grupos"; caja desbordada; "bot" → "agente".

---

## Decisiones pendientes del autor
1. **Spring Boot 3.4** (posible fin de soporte OSS): ¿actualizar a 3.5/4.0 o justificar la versión?
2. **Art. 38 del AM 5216-A:** añadirlo a BN3 en `results-ob1.tex` (recomendado; el texto normativo ya lo invoca) o quitarlo del modelo de datos.
3. **`blood_type` y `admin_notes`:** ¿se mueven a la historia clínica o se justifica que queden en la tabla de pacientes?
4. **Tablas `*_aud`:** ¿se añaden a `schema.dbml` o solo se mencionan en una nota?
5. **Contenedores:** ¿un solo nginx (proxy + archivos de la SPA) o un contenedor web separado?
6. **Nombres de paquetes:** el código tiene `notifications`/`dashboard`; la tesis usa `whatsapp`, `calendar`, etc. ¿Renombrar en el código o dejar una nota?
