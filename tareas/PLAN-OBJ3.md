# Plan de redacción — Objetivo 3

> **Objetivo 3:** Implementar el sistema de información centralizado, incluyendo su módulo de agente
> conversacional integrado a una aplicación de mensajería, y evaluar la reducción del tiempo promedio de
> gestión administrativa por paciente.

Archivos: `tex/ResultsAndDiscussion/results-ob3.tex` + `tex/ResultsAndDiscussion/ob3/*.tex` (esqueletos con
guía de llenado en los comentarios `% QUÉ VA / DATOS / NO VA`). Índice de tareas: `tareas/obj3/00-indice.md`.

**Estado:** `results-ob3.tex` todavía **no** está incluido en `resultados-discusion.tex` (para no mostrar
marcadores "Pendiente" en la revisión de mañana). Para verlo, añadir al final de ese archivo:
`\input{tex/ResultsAndDiscussion/results-ob3}`.

---

## 1. Secuencia con los objetivos 1 y 2

El Objetivo 3 ejecuta las dos últimas fases RAD (`tab:ob2_fases_rad`) y cierra la medición pretest-postest
planteada en Métodos (diseño preexperimental de un solo grupo).

| Viene de | Se usa en el Obj. 3 como |
|---|---|
| Obj. 1 — TGA pretest 13,62 min y tramos T1–T5 (`tab:tramos_tga`) | Línea base de `tab:ob3_tga` |
| Obj. 1 — Indicadores de Instrumento 2 y encuesta (mensajes, confirmación, inasistencias, cruces) | Línea base de `tab:ob3_indicadores` |
| Obj. 1 — Requerimientos RF01–RF14, RNF01–RNF06 (`tab:requerimientos`) | Filas de `tab:ob3_verificacion` |
| Obj. 1 — Brechas normativas BN1–BN7 | Tabla de medidas implementadas en verificación |
| Obj. 2 — Plan de desarrollo, 15 tarjetas (`tab:ob2_tarjetas`) | Ejecución real en `tab:ob3_tarjetas` + tablero |
| Obj. 2 — Modelo de datos y módulos | Base de datos implementada |
| Obj. 2 — Prototipo de interfaz | Pantallas finales (mismo orden y nombres) |
| Obj. 2 — Arquitectura del agente y flujo to-be de comunicación | Conversaciones reales del agente |
| Obj. 2 — Despliegue (VPS, modo básico de WhatsApp) | Despliegue y transición |
| Obj. 2 — Atributo de usabilidad: T1 < 3,40 min (`tab:ob2_atributos`) | Criterio de RNF06 en la evaluación |
| Obj. 2 — Hipótesis de la discusión (T4 y T5 desaparecen, T1–T3 bajan) | Se confirman o refutan en la discusión |

Estructura resultante (numeración prevista 3.3.x):

| # | Apartado | Archivo | Fase RAD |
|---|---|---|---|
| 3.3 | Introducción | `ob3/intro.tex` | — |
| 3.3.1 | Construcción (tablero Kanban real) | `ob3/construccion.tex` | Construcción |
| 3.3.2 | Base de datos | `ob3/base-datos.tex` | Construcción |
| 3.3.3 | Implementación del sistema | `ob3/modulos-sistema.tex` | Construcción |
| 3.3.4 | Implementación del agente | `ob3/agente.tex` | Construcción |
| 3.3.5 | Despliegue y transición | `ob3/despliegue-transicion.tex` | Transición |
| 3.3.6 | Verificación de requerimientos | `ob3/verificacion.tex` | Transición |
| 3.3.7 | Evaluación del TGA | `ob3/evaluacion.tex` | — |
| 3.3.8 | Discusión | `ob3/discusion.tex` | — |

---

## 2. Reglas de redacción (las mismas del Obj. 2)

- Tablas y figuras primero; párrafos de 2–4 líneas. La discusión va en prosa, sin tablas.
- Celdas lacónicas: una idea por celda, una línea por fila cuando se pueda.
- Nombres funcionales en español (Agenda, Clínico, Agente). Sin nombres de paquetes, clases ni endpoints.
- Sin "MVP" ni menciones a asistentes de programación. Metodología: enfoque híbrido RAD + Kanban.
- Numeración de requerimientos **de la tesis** (RF01–RF14), nunca la de los repositorios.
- Capturas solo con datos ficticios (LOPDP). Nombres: `img/Ob3_<Pantalla>.png`.
- Pruebas de software: no se documentan. La verificación es aceptación funcional con el personal.
- Fragmentos de código: como máximo dos (restricción anticruce y, si aporta, control de acceso por rol).

---

## 3. Diferencias entre los repositorios y la tesis (manda la tesis)

| # | Repositorios (`docs/`) | Tesis | Qué hacer |
|---|---|---|---|
| D1 | Servidor = PC de recepción | VPS a nombre de la clínica; local como alternativa | Desplegar en VPS; si al final es local, justificarlo con `tab:ob2_local` |
| D2 | RF10 aviso … RF15 reprogramar | RF09 aviso … RF14 recordatorio | Traducir siempre a la numeración de la tesis |
| D3 | WhatsApp de desarrollo con número de prueba | Número real del desarrollador en modo básico | Usar el número propio en desarrollo |
| D4 | Perfil Director con estadísticas y auditoría (front P16, P17) | No está en el diseño | Omitir estadísticas; auditoría solo como evidencia de RNF02 |
| D5 | "Más del 033": campos completados después de la consulta | Registro único durante la atención | **Riesgo para T_E2**: si se completa después, cronometrarlo en el postest (parte B) |
| D6 | Backend: 18 tareas; frontend: 17 pantallas | 15 tarjetas | Usar el mapeo de la sección 4 |
| D7 | "Sin internet funciona todo salvo bot" | Con VPS, sin internet no hay acceso | Ya cubierto en riesgos del despliegue |

---

## 4. Mapeo tarjeta de la tesis → tareas de los repositorios

| Tarjeta (tesis) | Backend | Frontend | Estado al 15/10 |
|---|---|---|---|
| 1. Identidad y autenticación | 001, 002, 003 | 001, 002a | Hecha |
| 2. Profesionales y pacientes | 004, 004a | 002b, 005a, 005b | Hecha |
| 3. Historia clínica y antecedentes | 005, 005b | 008b | Hecha |
| 4. Agenda y horarios | 006, 006b–006e | 003a–c, 004a–b, 006a–b, 007 | Hecha |
| 5. Atención clínica y CIE-10 | 007, 008 | 008a, 008c, 011 (Más del 033) | Hecha (011 pendiente) |
| 6. Odontograma | 009 | 009a, 009b, 010a, 010b | Hecha |
| 7. Tratamientos | 010 | 012 | Pendiente |
| 8. Recetas | 011 | 013 | Pendiente |
| 9. Cobros y comprobante | 012 | 015 | Pendiente |
| 10. Auditoría | 013 | 017 | Pendiente |
| 11. Google Calendar | 014 | — | Pendiente |
| 12. Agente: núcleo, aviso, información, derivación | 015 | — | Pendiente |
| 13. Agente: agendar y reprogramar | 016 | — | Pendiente |
| 14. Agente: recordatorios | 017 | — | Pendiente |
| 15. Respaldos y exportación | 018 | — | Pendiente |
| (RF06 historial inmediato) | clinical-summary | 014 | Pendiente |

**Orden recomendado de lo que falta** (prioriza el TGA y la seguridad de los datos reales):
7 → 8 → 9 (T1 y T2) → 15 (respaldos antes de cargar datos reales) → historial → 12 → 13 → 14 → 10 → 11.
Si el tiempo no alcanza, 10 y 11 son las primeras en ceder (no afectan el TGA); declararlo en verificación.

---

## 5. Cronograma propuesto (ajustar a tus fechas reales)

| Semanas | Construcción / campo | Redacción en paralelo |
|---|---|---|
| 16/10 – 15/11 | Tarjetas 7–15 | O3-00, O3-01, O3-03, O3-04 (pantallas ya listas), O3-08a |
| 16/11 – 22/11 | Despliegue, carga inicial, capacitación | O3-02 (cierre del tablero), O3-05 |
| 23/11 – 06/12 | Estabilización (mín. 2 semanas de uso real) | O3-06, O3-07 |
| 07/12 – 12/12 | **Postest**: 3 jornadas de alta afluencia: martes 08/12, jueves 10/12 y sábado 12/12 (pretest: 22, 24 y 26/09) | — |
| 13/12 – 20/12 | Análisis | O3-08b, O3-09, O3-10, O3-11 |

La medición es el punto crítico: sin al menos dos semanas de uso estable, el postest mide la curva de
aprendizaje y no el sistema.

---

## 6. Cómo obtener cada dato

| Dato | Fuente | Cómo |
|---|---|---|
| Fechas de cada tarjeta | git de ambos repos | `git log --reverse --format='%ad %s' --date=short` y filtrar por número de tarea |
| Captura del tablero | GitHub Projects / Trello | Cargar las 15 tarjetas con sus fechas; captura en la fecha de corte |
| Migraciones | `bellidental-backend/src/main/resources/db/migration` | Listar archivos `V*__*.sql`; agrupar por módulo |
| Fragmento anticruce | Migración de la agenda (V6) | Copiar el `EXCLUDE USING gist (...)` |
| Pantallas | Sistema en desarrollo con datos ficticios | Misma resolución (1366 px), sin datos reales |
| Conversaciones del agente | WhatsApp del desarrollador | Capturas del móvil; montar 2x2 |
| Consumo del servidor | VPS | `docker stats --no-stream` en jornada normal |
| Carga de pacientes antes de cada jornada | Fichas digitales que la secretaria prepara el día anterior | Script de carga a la BD; no se cronometra (en el pretest la preparación tampoco se midió) |
| T1–T3, espera, retraso (postest) | Instrumento 4, parte A | Por paciente, mismo observador |
| T4–T5 o tarea diferida (postest) | Instrumento 4, parte B | Por jornada; si no hay lote, registrar 0 y anotar |
| Cruces, citas por origen, inasistencias | Base de datos | Consultas por estado y origen de la cita en el periodo |
| Indicadores del agente | Base de datos (conversaciones, recordatorios) | Conteos en el periodo de evaluación |
| Mensajes y tiempo de confirmación de la secretaria | Instrumento 2 aplicado de nuevo | Mismas preguntas P1–P5 |

---

## 7. Evaluación: método estadístico (para O3-00 y O3-09)

- **Hipótesis:** H0: TGA_post ≥ TGA_pre; H1: TGA_post < TGA_pre (unilateral, α = 0,05).
- **Muestras independientes:** pacientes distintos en pretest y postest. Se dispone de las 78 fichas pretest
  individuales: la comparación es de medias, pero la prueba necesita la dispersión de cada fase, la
  normalidad (Shapiro–Wilk) y, si no es normal, los rangos (Mann–Whitney); con solo el promedio no se
  puede saber si la diferencia supera la variación natural entre pacientes.
- **T_E1 por paciente:** Shapiro–Wilk por fase → t de Welch (normal) o U de Mann–Whitney (no normal);
  tamaño del efecto (d de Cohen o r).
- **T_E2 por jornada:** comparación descriptiva (es un lote, no un dato por paciente).
- **TGA:** T_E1 + T_E2; reducción absoluta y porcentual; minutos liberados por jornada (26 atenciones).
- **RNF06:** se cumple si T1_post < 3,40 min (escenario de `tab:ob2_atributos`).
- **Herramienta:** JASP, R o Python; hoja o script en anexos.

---

## 8. Tareas de redacción

| # | Tarea | Archivo | Cuándo | Terminado cuando |
|---|---|---|---|---|
| O3-00 | Procedimiento de análisis postest en Metodología | `tex/Methodology/data-analysis.tex` (+ `population-sample.tex`) | Ya | Hipótesis, prueba y muestra postest declaradas en el cap. 2 |
| O3-01 | Introducción + figura de secuencia | `ob3/intro.tex` | Ya | 1 párrafo + figura TikZ |
| O3-02 | Construcción: tablero real y ejecución de tarjetas | `ob3/construccion.tex` | Al cerrar la construcción | Tablero, 15 filas con fechas, desviaciones |
| O3-03 | Base de datos | `ob3/base-datos.tex` | Ya (actualizar al final) | Tabla de migraciones + fragmento anticruce |
| O3-04 | Pantallas del sistema | `ob3/modulos-sistema.tex` | Por pantalla terminada | 7 capturas con 2–3 líneas cada una |
| O3-05 | Agente | `ob3/agente.tex` | Tras tarjetas 12–14 | Plantillas + figura 2x2 |
| O3-06 | Despliegue y transición | `ob3/despliegue-transicion.tex` | Tras la estabilización | Hitos con fechas + consumo medido |
| O3-07 | Verificación de requerimientos y brechas | `ob3/verificacion.tex` | Tras la transición | 20 requerimientos + 7 brechas con estado |
| O3-08a | Evaluación: procedimiento y definiciones operativas | `ob3/evaluacion.tex` | Ya | `tab:ob3_definiciones` acordada |
| O3-08b | Evaluación: resultados por tramo | `ob3/evaluacion.tex` | Tras el postest | `tab:ob3_tga` + barras apiladas |
| O3-09 | Contraste estadístico e indicadores | `ob3/evaluacion.tex` | Tras el postest | Prueba + `tab:ob3_indicadores` |
| O3-10 | Discusión | `ob3/discusion.tex` | Al final | 4 párrafos, sin tablas |
| O3-11 | Integración y anexos | `resultados-discusion.tex`, `appendices.tex` | Al final | Compila sin referencias indefinidas; anexos: fichas postest, script |

---

## 9. Decisiones y pendientes de revisión

| # | Tema | Decisión (16/10/2026) | Tarea |
|---|---|---|---|
| 1 | Datos pretest por paciente | Existen las 78 fichas individuales → prueba de muestras independientes | O3-00, O3-09 |
| 2 | Días del pretest | Martes 22, jueves 24 y sábado 26/09/2026 → postest en martes, jueves y sábado | O3-00, O3-08a |
| 3 | Pacientes existentes | La secretaria ordena las fichas el día anterior; se pedirán las digitales y un script las cargará en la BD. En jornada solo se cronometra el registro | O3-00, O3-06 |
| 4 | Instrumento 4 con numeración antigua | Actualizar el anexo a T1–T5 y separar T4 y T5 en la parte B | O3-00 (parte C) |
| 5 | **Pendiente de revisión:** registro del odontólogo con el sistema | Registra los datos de la ficha rápida de la secretaria y los tratamientos con sus códigos, con ligeras variaciones; puede sumarse un tiempo extra a T1. **No se considera todavía**: el autor mide la semana del 19/10/2026 y con eso se ajusta la redacción | O3-00 (nota), O3-08a |
| 6 | "Más del 033" | Sigue abierto: si se completa después de la consulta, es T_E2 residual (parte B) | O3-08a |
