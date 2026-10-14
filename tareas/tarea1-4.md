# Tareas 1–4 — Resumen y revisión

Implementación: Haiku 5.5 (high), en paralelo, un archivo por tarea. Revisión: Opus 5.5 (high).
Estado de compilación: **sin errores, sin referencias ni citas indefinidas, sin overfull boxes** (pdflatex + bibtex, 2026-10-14).
En el índice: 3.2 Objetivo 2 → 3.2.1 Impulsores (p. 64), 3.2.2 Metodología (p. 67), 3.2.3 Proceso propuesto (p. 69).

Cambio previo: el formato numerado de `\paragraph` se movió de `main.tex` a `resultados-discusion.tex` para no numerar los encabezados en línea del fundamento.

---

## Tarea 1 — Fundamento teórico breve
**Archivos:** `tex/Theoretical-foundation/fundamento.tex`, `bib/fundamentacion_teorica.bib`

| Párrafo añadido | Ubicación | Citas |
|---|---|---|
| Metodologías de desarrollo de software | Antes de "Arquitectura de software" | sommerville2016software, schwaber2020scrum, beck2004extreme, anderson2010kanban |
| Modelado de la arquitectura: modelo C4 y UML | Tras "Arquitectura de software" | brown2018c4, omg2017uml, kruchten1995views |
| Monolito modular | Tras "Arquitectura de microservicios" | richards2020fundamentals |
| Diseño guiado por atributos (ADD) | Antes de "ISO/IEC 25010" | cervantes2016designing |

9 entradas bib nuevas, cada una con comentario `% VERIFICAR`.

## Tarea 2 — Introducción + Impulsores arquitectónicos
**Archivo:** `tex/ResultsAndDiscussion/ob2/intro-impulsores.tex`

- Párrafo introductorio (cuatro elementos del objetivo; Staras 2021).
- `tab:ob2_impulsores` — trazabilidad evidencia → origen → requerimiento → implicación (11 filas).
- `tab:ob2_atributos` — atributos de calidad ISO/IEC 25010 (4).
- `tab:ob2_restricciones` — restricciones del proyecto (6).

## Tarea 3 — Metodología y marcos de modelado
**Archivo:** `tex/ResultsAndDiscussion/ob2/metodologia.tex`

- Método de dos tamices (imperativos + deseables ponderados).
- `tab:ob2_matriz_metodologia` — Scrum, XP y Cascada descartados en el 1.er tamiz; Kanban 2,75 vs Scrumban 2,25.
- `tab:ob2_matriz_modelado` — C4 + UML seleccionado; BPMN por continuidad.
- `tab:ob2_artefactos` — artefacto, notación y apartado.

## Tarea 4 — Proceso propuesto (BPMN to-be)
**Archivo:** `tex/ResultsAndDiscussion/ob2/proceso-tobe.tex`

- `fig:ob2_tobe_atencion`, `fig:ob2_tobe_comunicacion_p1`, `fig:ob2_tobe_comunicacion_p2` en landscape (dividido en dos partes), con marcador "Pendiente" hasta exportar `img/ToBe_Atencion.pdf` y `img/ToBe_Comunicacion_P1.pdf` y `img/ToBe_Comunicacion_P2.pdf`.
- `tab:ob2_asis_tobe` — comparación actual vs propuesto por tramo (T1–T5) y necesidades de comunicación.
- Cierre: efectos sobre el TGA como hipótesis del Objetivo 3.

---

## Revisión (Opus 5.5, high)

### Veredicto general
Trabajo sólido: cifras coinciden con las fuentes, códigos PC/BN/N/RF/RNF correctos, reglas del plan cumplidas (sin "MVP", sin códigos internos, sin IA, sin cifrado E2E). Tres riesgos ante el tribunal: **la matriz de metodologías es circular**, **la fila de RNF04 carece de evidencia** y **el BPMN to-be promete más que el alcance**.

### Hallazgos — Tarea 1
| Sev. | Lugar | Problema | Corrección |
|---|---|---|---|
| Media | fundamento.tex:115 | Scrumban y Cascada se evalúan en la matriz pero no se definen en el fundamento; Scrumban sin cita | Una frase cada una; citar Ladas, *Scrumban* (2009) |
| Media | bib `brown2018c4` | Mezcla Leanpub con c4model.com; año dudoso | Citar el sitio con fecha de acceso o el artículo de Brown en InfoQ (2018) |
| Baja | bib `richards2020fundamentals` | La 1.ª ed. trata el monolito modular de pasada | Verificar el capítulo; la 2.ª ed. (2025) le dedica uno |
| Baja | bib `omg2017uml`, `schwaber2020scrum` | Faltan número de documento y fecha de acceso | Añadir `formal/17-12-05`, URL y `note={Accessed: ...}`; quitar `% VERIFICAR` |
| Baja | fundamento.tex:142 | "la vista 4+1" frente a "cinco perspectivas" | Escribir "el modelo de vistas 4+1" |
| Baja | fundamento.tex:194–196 | La misma cita dos veces seguidas | Dejar una |

Entradas correctas: Sommerville (2016), Beck y Andres (2004), Anderson (2010), Kruchten (1995), Cervantes y Kazman (2016).

### Hallazgos — Tarea 2
| Sev. | Línea | Problema | Corrección |
|---|---|---|---|
| **Alta** | 33 | "Requerimiento expreso del director" no está en ningún instrumento de la tesis; cita circular a RNF04 | Trazar a BN2 y al AM 0009-2017, art. 7 (integridad y disponibilidad) |
| Media | 23–33 | Faltan RF03–RF06, RF08, PC4–PC6, BN5, RNF06 | Añadir una frase: solo se trazan los requerimientos con impacto arquitectónico |
| Media | 37, 55–58 | Escenarios "verificables" sin medida de respuesta | Añadir medida (p. ej., ≤ N pasos, respuesta < X s) o quitar "verificable" |
| Media | 56 | Disponibilidad es subcaracterística de Fiabilidad (ISO/IEC 25010:2011); falta RNF04 | "Fiabilidad (disponibilidad, recuperabilidad): RNF05, RNF04"; añadir RNF02 a Seguridad |
| Baja | 29 | El 35,2 % se usa en el Obj. 1 para N4, no para RF13 | Moverlo a la fila de N4 |
| Baja | 24 | La demora > 46 min ocurre en alta afluencia, no fuera de horario | "Respuesta inmediata en todo horario" |
| Baja | 27 | "Considera útil un recordatorio" no es lo que mide el ítem | "Le habría evitado un problema" |
| Baja | 80–82 | MoSCoW repetido; "presupuesto reducido" sin evidencia | Fusionar; atribuir el presupuesto a una decisión de la clínica |

### Hallazgos — Tarea 3
| Sev. | Línea | Problema | Corrección |
|---|---|---|---|
| **Alta** | 24–27 | Criterios deseables escritos a medida de Kanban; "flujo continuo" y "baja carga de ceremonias" miden lo mismo (50 % del peso) | Criterios como necesidades del proyecto (adaptación a cambios de prioridad, visibilidad del avance para tutor y clínica, sobrecarga de gestión, MoSCoW) y pesos justificados |
| Media | 3 vs 49–56 | Se dice que el método se reutiliza, pero la matriz de modelado es cualitativa | Declararla cualitativa o aplicarle los dos tamices |
| Media | 32 | "XP exige programación en pareja" es discutible | "Se apoya en prácticas de equipo (pareja, cliente en sitio)" |
| Baja | 32 | Cascada no impide medir; retrasa la validación | Matizar |
| Baja | 55 | Esfuerzo de C4+UML "Medio", igual que solo UML | Ajustar valoraciones |
| Baja | 34 | Repite los totales de la tabla | Recortar |

### Hallazgos — Tarea 4
| Sev. | Lugar | Problema | Corrección |
|---|---|---|---|
| **Alta** | ToBe_Atencion.bpmn (anotación final) | "El Formulario 033 y el historial digital quedan completos": la impresión y la firma están fuera de alcance | "La historia clínica digital, con los campos del 033, queda registrada al cerrar la atención" (AM 00115-2021; AM 0009-2017, Transitoria 2.ª) |
| Media | 41 + BPMN | La derivación de pacientes no registrados limita N2/RF11 y no se declara | Declararlo en el texto |
| Media | BPMN derivación | El "enlace de WhatsApp de recepción" supone un segundo número no mencionado | Aclararlo o dejarlo para el apartado de la decisión de acceso a WhatsApp |
| Media | 32 | "La secretaria no accede a la historia clínica", pero ve los tratamientos | "No edita datos clínicos; solo ve tratamientos y valores (RNF01)" |
| Media | 32, 81–82 | "La Etapa 2 desaparece" se afirma como hecho | "En el diseño se elimina…" |
| Baja | BPMN | La réplica en Google Calendar choca con "única fuente" | Indicar que es una copia de solo lectura |
| Baja | 7 vs 10 | "Llegada, cobro y agendamiento" omite la filiación | Incluirla |
| Baja | 70, 91 | La columna "Tramo" mezcla necesidades; T1–T5 fuera de modo matemático | "Tramo o necesidad"; `$T_1$ a $T_5$` |
| Baja | 26, 51 | Figuras pendientes | Exportar los PDF |

**Hallazgo previo (Obj. 1):** 49/105 = 46,7 % y 66/105 = 62,9 %. El Obj. 1 y el Instrumento 3 suman porcentajes ya redondeados (46,6 % y 62,8 %), y `data-analysis.tex:11` dice 46,7 %. Conviene unificar.

### Respuesta a las dudas
- **a) RNF04 y el director:** no tiene respaldo en ningún instrumento; eliminarlo y trazar a BN2 y al AM 0009-2017, art. 7.
  > **Nota del orquestador:** la queja sí existe en la entrevista cruda (`bellidental-backend/proy-infor/interview-v2.txt:154–155`: experiencias con sistemas en la nube o por suscripción que dejan de funcionar a los 6–7 meses y rechazo del SaaS de 200 USD/mes), pero no aparece en las tablas de entrevistas de la tesis. **Decisión tuya:** añadir ese fragmento a la tabla de la entrevista al Director (Instrumento 1) y citarlo, o trazar RNF04 solo a la norma.
- **b) Mantenibilidad sin RNF:** no añadir un RNF07 a posteriori; atribuirla a la restricción "un desarrollador y evolución futura" y a RF07 (ADD lo admite).
- **c) Costo de WhatsApp:** sí falta. Las plantillas de utilidad fuera de la ventana de 24 h (recordatorios) se cobran por mensaje y requieren aprobación; añadir la restricción y verificar la tarifa vigente para Ecuador.
- **d) Puntuaciones Kanban/Scrumban:** no son defendibles tal como están (ver hallazgo Alta de la Tarea 3).
- **e) Reglas nuevas del BPMN:** "por teléfono" sí tiene respaldo (llamada 5,7 %, Tabla p8; "llamadas" en Inst. 2, P1); citarlo. "09:00" → "hora configurable". "Hasta 2 h antes" es regla nueva: exponerla en el texto y validarla con la clínica, o quitarla. "Nueva versión del aviso" es buena práctica LOPDP; mencionarla en el texto o en el apartado del agente.

### Correcciones prioritarias
1. Rehacer la fila de RNF04 sin "requerimiento del director" (o respaldarla en la entrevista; ver nota en a).
2. Reformular criterios deseables y pesos de la matriz de metodologías; añadir Scrumban, con cita, al fundamento.
3. Corregir la anotación "Formulario 033 completo" del BPMN de atención.
4. Declarar en el texto las reglas nuevas del BPMN: derivación de no registrados, 2 h, hora del recordatorio y enlace de recepción.
5. Fiabilidad (RNF04, RNF05) y RNF02 en atributos de calidad; medidas en los escenarios; restricción del costo de WhatsApp.
6. Explicar por qué no figuran RF03–RF06 y RF08 en la trazabilidad.
7. Rehacer `brown2018c4` y completar las referencias de UML y Scrum.

---

## Pendiente de tu decisión antes de aplicar correcciones
1. **RNF04:** ¿añado el fragmento de la entrevista del Director (vendor lock-in) a la tabla del Instrumento 1, o trazo RNF04 solo a la norma?
2. **Regla de 2 h** para cancelar/reprogramar por bot: ¿la validas con la clínica y se mantiene, o se quita?
3. **Número de recepción para la derivación** (segundo número de WhatsApp): ¿se mantiene? Se puede decidir en la sesión de la tarea 6.
4. **Porcentajes 46,6/46,7 y 62,8/62,9:** ¿unifico al cálculo exacto (46,7 % y 62,9 %) en toda la tesis?
5. **Figuras BPMN:** abrir los `.bpmn` en bpmn.io y exportar a `img/ToBe_Atencion.pdf` y `img/ToBe_Comunicacion_P1.pdf` y `img/ToBe_Comunicacion_P2.pdf`.

---

## Correcciones aplicadas (2026-10-14)

Decisiones del autor: 1 respaldar en la entrevista · 2 reformular la matriz, **sin Scrumban** · 3 corregir · 4 no declarar reglas (ya están en el diagrama) · 5 sí · 6 omitir · 7 sí.

| # | Corrección | Archivo |
|---|---|---|
| 1 | Nueva fila **P7** en la Entrevista 1 (cierre abierto: costo ≈ 200 USD, sistemas por suscripción que dejaron de funcionar a los 6–7 meses, autonomía frente a proveedores), tomada del fragmento 16 de la entrevista cruda. RNF04 se traza a `Tabla ent1, P7` + BN2 | `instrument1-data-collection.tex`, `ob2/intro-impulsores.tex` |
| 2 | Matriz sin Scrumban. Imperativo: solo entregas incrementales (descarta Cascada). Deseables como necesidades del proyecto con pesos justificados por las restricciones: un desarrollador 30 %, cambios de prioridad 25 %, esfuerzo de gestión 25 %, visibilidad 20 %. **Totales: Scrum 1,65 · XP 1,95 · Kanban 2,80** (Scrum gana en visibilidad). XP "se apoya en prácticas de equipo"; Cascada "retrasa la medición". Matriz de modelado declarada cualitativa, esfuerzos ajustados, "modelo de vistas 4+1" | `ob2/metodologia.tex` |
| 3 | Anotación del BPMN: "la historia clínica digital, con los campos del Formulario 033, queda registrada al cerrar la atención". Texto: "En el diseño se elimina la Etapa 2…"; la secretaria "no edita datos clínicos y solo ve tratamientos y valores (RNF01)"; filiación incluida; Google Calendar como copia de solo lectura; columna "Tramo o necesidad"; $T_1$ a $T_5$ | `ToBe_Atencion.bpmn`, `ob2/proceso-tobe.tex` |
| 5 | Atributos: Seguridad (+RNF02, trazabilidad) y **Fiabilidad (disponibilidad, recuperabilidad): RNF05, RNF04**; escenarios con medida (100 % de rechazos de edición clínica por secretaria; pérdida máx. 24 h; $T_1$ < 3,40 min). Restricciones: MoSCoW fusionado, costo bajo trazado a P7, **nueva fila: costo por mensaje de las plantillas de WhatsApp**. Filas ajustadas: 35,2 % movido a N4; "le habría evitado un problema"; "respuesta inmediata en todo horario" | `ob2/intro-impulsores.tex` |
| 7 | `brown2018c4` → artículo de InfoQ (jun. 2018) con fecha de acceso; `omg2017uml` con `formal/17-12-05` y URL; `schwaber2020scrum` con URL y fecha de acceso. Comentarios `% VERIFICAR` retirados salvo Richards y Ford (capítulo del monolito modular). Cita duplicada de Cervantes eliminada | `bib/fundamentacion_teorica.bib`, `fundamento.tex` |
| — | Figuras: PDF copiados de `diagramas/bpmn/` a `img/`; las tres figuras pasan a `sidewaysfigure` (página completa en vertical, imagen girada) | `ob2/proceso-tobe.tex` |
| — | Anchos de tablas corregidos (impulsores y as-is/to-be ya no desbordan) | `ob2/*.tex` |

**Compilación:** 0 errores; figuras incluidas. Avisos que **ya existían** antes de estas tareas: cita `msp2016reglamento` sin entrada en la bib (`fundamento.tex:273, 279`) y cajas desbordadas en dos tablas del Objetivo 1 (`results-ob1.tex`, tabla de necesidades 11,6 pt y requerimientos 1,8 pt).

**Pendiente sin decisión:** unificar 46,6/46,7 % y 62,8/62,9 %.
