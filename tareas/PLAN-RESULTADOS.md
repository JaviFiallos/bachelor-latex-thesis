# Plan — 3.6 Resultados (subsección final del Capítulo III; aprobado)

Idea: un resultado por objetivo, condensado, que hilvana
**antecedente → indicador del diagnóstico (instrumento) → respuesta del sistema → evidencia obtenida**.
Cada evidencia declara su nivel, sin justificarse:

| Nivel | Qué es | Fuente |
|---|---|---|
| Medido en operación | Dato real del uso del sistema en la clínica | Fichas del postest, base de datos de producción (solo agregados) |
| Verificado en prueba controlada | Prueba con participantes de prueba y números propios | Registro del agente y de la API |
| No evaluado | Depende de que el agente atienda pacientes reales | Trabajo futuro |

## Estructura propuesta

3.6.1 Diagnóstico del proceso (Obj. 1) — síntesis: problemas → requerimientos (1 tabla breve)
3.6.2 Diseño (Obj. 2) — síntesis: requerimiento → decisión de diseño → antecedente (sin tabla nueva; prosa + remisión)
3.6.3 Sistema y agente (Obj. 3)
  - Cobertura de requerimientos (rescata verificacion.tex, condensada)
  - TGA: 13,63 → 9,75 min (−28,5 %), contraste (figura ya hecha)
  - Agente: prueba controlada con participantes de prueba
3.6.4 Matriz de cierre: indicador del diagnóstico → valor inicial → valor obtenido → nivel de evidencia (tabla central del capítulo)
3.6.5 Discusión (rescata borrador-discusion-ob3.tex)

## Matriz de cierre (borrador de contenido)

| Indicador del diagnóstico | Inicial | Obtenido | Nivel |
|---|---|---|---|
| TGA por ciclo (I4) | 13,63 min | 9,75 min | Medido en operación |
| Conflictos de horario (I2-P5) | 2 al mes | 0 (restricción en la base) | Medido en operación — consultar BD |
| Inasistencias (I2-P4) | 3–5 por semana | tasa del tablero del sistema | Medido en operación — consultar BD |
| Ficha 033 diferida (Etapa 2) | 7,33 min/ciclo | 0 | Medido en operación |
| Tiempo de respuesta por WhatsApp (I2-P3, I3-P2) | > 46 min | segundos (mediana de la prueba) | Prueba controlada |
| Consultas de precio/horario (I2-P1; I3-P6, P7) | 26–50/día manuales | tareas resueltas sin recepción (%) | Prueba controlada |
| Agendar/reprogramar (I3-P5) | 58,1 % dispuesto | tareas completadas (%) y tiempo por tarea | Prueba controlada |
| Confirmación de citas (I2-P2) y olvidos (I3-P3, P4) | 31–60 min/día; recordatorio | — | No evaluado (RF14 no implementado) |

## Prueba controlada del agente (sugerencia del tutor)

Materiales: tareas/prueba-controlada/ (guion, tarjeta de tareas, hoja de registro).

- 8–12 participantes de prueba (no pacientes) con sus propios números, datos ficticios.
- 5 tareas guionizadas: consultar precio, consultar horario, agendar, reprogramar, consulta que debe derivarse.
- Métricas desde el registro: tarea completada (sí/no), tiempo por tarea, mensajes por tarea, derivaciones correctas, tiempo de respuesta del agente.
- Al terminar, los ítems P5–P7 del Instrumento 3 adaptados a «me resultó fácil…» (Likert 1–5).
- Se declara como prueba con participantes de prueba; no se presenta como uso por pacientes de la clínica.

## Datos que faltan del autor

- [x] Aprobación del planteamiento.
- [ ] Consulta agregada a producción: citas registradas, conflictos, tasa de inasistencia desde la puesta en uso.
- [ ] Ejecución de la prueba controlada (fecha, participantes, resultados).
