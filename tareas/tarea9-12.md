# Tareas 9–12 — Resumen y revisión

Implementación: Haiku 5.5 (high), tareas 9–11 en paralelo y la 12 después. Revisión: Opus 5.5 (high).
Modo automático: las decisiones de la tarea 9 (sin sesión de preguntas) salieron de las ya tomadas y del diseño del backend.
Compilación (2026-10-14): **0 errores, 0 referencias/citas indefinidas, 142 páginas**. Cajas desbordadas ≤ 6 pt en `arquitectura-general.tex:98`, `arquitectura-agente.tex:49,52` y `plan-desarrollo.tex:26`.
**No se aplicó ninguna corrección de la revisión** (a pedido del autor, para revisarlas después).

Rama: `feat/results-obj2`.

---

## Tarea 9 — Arquitectura del agente conversacional
**Archivos:** `ob2/arquitectura-agente.tex`, `diagramas/drawio/ESPECIFICACION-agente.md`, `diagramas/plantuml/{estados_conversacion,secuencia_agendar,secuencia_recordatorio}.puml`

| Elemento del objetivo | Contenido | Labels |
|---|---|---|
| Estructura lógica | C4 nivel 3 y tabla por capas | `fig:ob2_c4_componentes`, `tab:ob2_capas` |
| Componentes funcionales | Tabla de ocho componentes (RF, necesidad, evidencia, reglas) y estados de la conversación | `tab:ob2_componentes`, `fig:ob2_estados_conversacion` |
| Mecanismos de integración | Tabla de mecanismos de WhatsApp, agenda y Google Calendar; dos secuencias | `tab:ob2_mecanismos`, `fig:ob2_secuencia_agendar`, `fig:ob2_secuencia_recordatorio` |
| Seguridad y cumplimiento | Tabla de medidas (BN6, BN7, RNF02, RNF03) | `tab:ob2_seguridad` |

Figuras pendientes: `img/C4_Componentes_Agente.pdf` (draw.io) e `img/Estados_Conversacion.pdf`, `img/Secuencia_Agendar.pdf`, `img/Secuencia_Recordatorio.pdf` (renderizar los `.puml`; no hay PlantUML instalado).

## Tarea 10 — Esquema de despliegue
**Archivos:** `ob2/despliegue.tex`, `diagramas/drawio/ESPECIFICACION-despliegue.md`

- `fig:ob2_despliegue` (pendiente `img/Despliegue.pdf`), `tab:ob2_nodos`, `tab:ob2_entornos`, `tab:ob2_respaldo`, `tab:ob2_riesgos`, `tab:ob2_local` (alternativa de instalación local).

## Tarea 11 — Plan de desarrollo
**Archivo:** `ob2/plan-desarrollo.tex`

- `tab:ob2_tarjetas` (15 tarjetas, 6 terminadas, 3 del agente), `tab:ob2_pruebas` (30 clases: 13 de integración y 17 unitarias; 118 métodos), `tab:ob2_fuera_alcance`, `tab:ob2_enlace_obj3` (T1–T5).

## Tarea 12 — Discusión
**Archivo:** `ob2/discusion.tex`

- `tab:ob2_cobertura` (RF01–RF14 y RNF01–RNF06), `tab:ob2_contraste` (9 antecedentes), síntesis, limitaciones y trabajos futuros.

---

## Revisión (Opus 5.5, high)

### Veredicto general
Los cuatro elementos del objetivo aparecen con su título literal; cifras, códigos y atribuciones son correctos en casi todo. Tres problemas que vería el tribunal:
1. Las cinco figuras de las tareas 9 y 10 siguen como «Pendiente».
2. **Los recordatorios se envían a pacientes que nunca aceptaron el aviso** (RF09, BN6).
3. **El párrafo «Cambio frente al Objetivo 1» no es honesto:** atribuye al Objetivo 1 algo que no dice y calla que el VPS choca con lo que el Director pidió (Entrevista 1, P7).

Verificado sin problemas: conteos de pruebas (30 clases, 118 métodos), estado de las seis tarjetas terminadas y sus dependencias, cifras (7,32 / 13,62 / 26–50 / 31–60 / 35,2 %), atribuciones a Arcila, Alejandrino, Hindelang, Tudor Car, Hmadchayyapum, Wong-Pérez, Martínez y Staras; sin «bot», «MVP» ni códigos internos.

### Tarea 9
| Sev. | Lugar | Problema | Corrección |
|---|---|---|---|
| **Alta** | :11, 69, 109, 116 | Cinco figuras sin generar | Renderizar los `.puml` y dibujar el C4 |
| **Alta** | :62; estados:13; secuencia_recordatorio | El recordatorio llega a pacientes registrados en recepción que no aceptaron el aviso; además Meta exige consentimiento previo (opt-in) para mensajes iniciados por la empresa | Registrar la aceptación en la filiación o enviar solo a teléfonos con aceptación; reflejarlo en tabla y diagramas |
| Media | :3 | «Cuatro elementos… y seguridad» no son los cuatro del objetivo | «Tres de los cuatro elementos del objetivo, más seguridad; el despliegue, en el apartado siguiente» |
| Media | :60–61 | Las reglas (1 cita por paciente y especialidad, 3 por teléfono, 14 días, 2 h) figuran junto a la evidencia, pero son parámetros del autor; falta «creadas por el agente» y que recepción no tiene límites (N4) | Nota «valores iniciales que se validan con la clínica» |
| Media | :91, :139 | La firma X-Hub-Signature-256 se atribuye a RNF01 (control de acceso del personal) | BN7/RNF03 (art. 10, lit. j) |
| Media | :90–97 | Sin citas a Meta (ventana de 24 h, plantillas, topes); el tope lo fija Meta, no es «configurable»; coexistencia app + Cloud API desde 2025 (verificar) | Citar la documentación de Meta; número exclusivo como decisión de diseño; «devuelve `hub.challenge`» |
| Media | ESPEC-agente:81–90 | Flecha de eventos invertida; ProfessionalDirectory sin relaciones; falta la ruta de respuesta del recordatorio; dice «JDBC» y el backend usa Spring Data JPA | Corregir relaciones |
| Baja | estados_conversacion.puml | Faltan `[*]→Identificación`, Recordatorio→Derivar (< 2 h) y Agendar sin horarios; estados usados antes de declararse | Añadirlas y declarar arriba |
| Baja | secuencias | En agendar, la identificación va tras el menú y falta la confirmación; en recordatorio se omite el webhook, «ENVIADO» en lugar de SENT, la regla de 2 h solo cubre Reprogramar | Alinear con especificación y texto |
| Baja | :49 | Columna «Necesidad» con BN desborda | «Origen», 0,10\linewidth |
| Baja | :101 | Shaikh «en la aplicación»: los antecedentes no lo dicen | «Sin restricción en la base de datos reportada» |
| Baja | :30 | `privacy_consents` en el agente, pero `tab:ob2_modulos` lo pone en `patients` | Unificar |

### Tarea 10
| Sev. | Lugar | Problema | Corrección |
|---|---|---|---|
| **Alta** | :110 | El Objetivo 1 nunca dice «funciona sin internet» (eso estaba en el plan del backend); se calla que el VPS reintroduce la dependencia de un proveedor que el Director rechazó (P7, origen de RNF04); RNF05 queda sujeto a internet | «Frente a la instalación local prevista inicialmente…»; reconocer la tensión con P7 y mitigarla (cuenta de la clínica, exportación abierta, mismo Compose local); RNF05 condicionado |
| Media | :104; agente:141 | Encargados y transferencia internacional solo para el VPS; Meta, Google Calendar (nombre del paciente) y Drive también tratan datos fuera del Ecuador; «verificar» en el texto | Fila «terceros encargados» con el capítulo de transferencia internacional de la LOPDP |
| Media | :27 | «Cuatro contenedores» pero `tab:ob2_contenedores` tiene cinco filas | Aclarar que la SPA es un artefacto servido por nginx |
| Media | nodos; especificación | Faltan: dominio a nombre de la clínica (Let's Encrypt y Meta), puertos (80/443), SO y tamaño del VPS, renovación del certificado, custodia de la clave de los respaldos, dispositivo del paciente | Añadir |
| Media | :129 | «Disponibilidad permanente» con un único servidor | «Continua, sujeta al proveedor y a la conexión» |
| Baja | :105 | La derivación no mitiga un bloqueo (mismo número) | Número de recepción como canal alterno |
| Baja | :56 | «Cambia solo la configuración»: una WABA nueva exige reaprobar plantillas y nombre visible | Matizar |
| Baja | :3 vs :34; :50 | Se repite lo que agrega el agente; en desarrollo falta el túnel del webhook | Fusionar; añadir túnel |
| Baja | espec.:71, 39 vs 79 | «Lee el volcado»; SPA en dos nodos | «Genera (pg_dump)»; un solo nodo |

### Tarea 11
| Sev. | Lugar | Problema | Corrección |
|---|---|---|---|
| Media | :58 | «La reprogramación a un horario ocupado también se rechaza»: ninguna prueba lo cubre (`AppointmentOverlapIT` prueba reprogramar sobre el propio horario) | Añadir la prueba o reformular |
| Media | :56 | «Integración por tarjeta», pero el plan del backend deja sin integración las tarjetas 7, 8, 9 y 12–14 | «En los módulos críticos» |
| Media | :78–79 | «Citas por terceros» fuera de alcance contradice N4 (14,3 % por familiar) y la identificación con varios pacientes; «cédula… que el agente no trata» contradice que la pide | Precisar o quitar |
| Baja | :3, :5 | «Cada tarjeta corresponde a un módulo» (no en 2, 10 y 15); «Al 2026-10» | Matizar; «a octubre de 2026» |
| Baja | :102–106 | Misma frase cinco veces; la tarjeta 11 no reduce $T_3$ | Columna «Línea base (min)» |

### Tarea 12
| Sev. | Lugar | Problema | Corrección |
|---|---|---|---|
| **Alta** | :29, :24, :5 | RF06 «Implementado», pero la tarjeta 2 lo marca parcial (resumen clínico y estado de tratamientos pendientes); RF01 incluye tratamientos y recetas del 033 (tarjetas 7 y 8) | RF06 y RF01 «parcial»; rehacer el conteo |
| Media | :39, :99 | «El diseño vigente registra el usuario y la fecha de cada revisión»: no hay Envers ni `revision_info` migrados | «Diseñado: Envers con `*_aud`; sin implementar» |
| Media | :42 | RNF05 solo cubre al agente | Añadir el sistema en horario, sujeto a internet |
| Media | :68 | «La modularidad se conserva sin el costo…» choca con la limitación de persistencia compartida (:91) | Matizar |
| Baja | :86–104 | Faltan limitaciones: reglas no validadas, consentimiento de los recordatorios, terceros fuera del país, servidor único | Añadir |
| Baja | :110–117 | Seis trabajos futuros frente a ocho exclusiones | Unificar |
| Baja | :82 | PC3 no es un «error de lectura» | Corregir |

### Correcciones prioritarias
1. Generar las cinco figuras (PlantUML y draw.io).
2. Diseñar el consentimiento y el opt-in previos al recordatorio, en texto y diagramas.
3. Reescribir «Cambio frente al Objetivo 1» con P7 y RNF05.
4. RF06 y RF01 a parcial en la cobertura; corregir auditoría y RNF05.
5. Corregir la frase de los «cuatro elementos» en `arquitectura-agente.tex:3`.
6. Presentar las reglas del agente como parámetros por validar, «creadas por el agente».
7. Terceros encargados y transferencia internacional (Meta, Google, VPS).
8. Atribuir la firma a BN7/RNF03 y citar a Meta.
9. Corregir el criterio anticruce en la reprogramación y las pruebas de integración por tarjeta.
10. Completar el despliegue: dominio, puertos, tamaño, claves.
11. Corregir relaciones de la especificación del agente y cajas desbordadas.

### Decisiones pendientes del autor (tareas 9–12)
1. **Aceptación para recordatorios:** ¿se registra en recepción al filiar o solo se recuerda a quien aceptó por WhatsApp?
Solo se lo recuerda a quien acepto por whatsapp
2. **Valores de las reglas** (2 h, 1 por especialidad, 3 por teléfono, 14 días): ¿se validan con la clínica?
Si me parecen bien los valores
3. **VPS frente a la P7 del Director:** ¿se mantiene? De ser así, actualizar §1 y la decisión sobre el servidor en `IMPLEMENTATION-PLAN.md` del backend, que aún dicen «PC de recepción».
Si se mantien el vps, no modifiques nada en el backen ya lo hare yo tu solo plasmalo en el documento
4. **Prueba piloto del Objetivo 3:** ¿con la cuenta del desarrollador y datos reales? Eso lo convierte en encargado del tratamiento.
Esto no lo menciones aun
5. **Proveedor y región del VPS** y la base de la transferencia internacional.

6. **«Citas por terceros»:** qué significa y si se mantiene fuera del alcance.
Son citas que pueden ser agendadas por familiares no relizada por el propio paciente, y si queda fuera es mas ni siquiera lo menciones, me parece que eso lo borre del obj 1 quedan rescoldos pero en general no  deb mencionarse

Las decisiones pendientes de las tareas 5–8 están en `tareas/tarea5-8.md`.

---

## Correcciones aplicadas (2026-10-14, según las decisiones del autor)
- **Recordatorios solo a teléfonos con aviso aceptado en el agente:** tabla de componentes, `privacy_consents`, mecanismos (opt-in de Meta), seguridad, cobertura, limitaciones, especificación del agente, estados, secuencia del recordatorio y anotación del BPMN P2.
- **Reglas del agente** (2 h, 1 por especialidad, 3 por teléfono, 14 días) se mantienen; se aclara que aplican solo a las citas del agente. La regla de 2 h cubre cancelar y reprogramar.
- **VPS frente a P7:** párrafo reescrito («Cambio frente a la instalación local prevista inicialmente») con la tensión, cuatro mitigaciones y RNF05 condicionado. Backend sin cambios.
- **Piloto del Objetivo 3:** no se menciona.
- **Proveedor y región del VPS:** sin respuesta; el texto se mantiene genérico (acuerdo de encargado y régimen de transferencia internacional de la LOPDP).
- **Citas por terceros:** eliminadas (fila de fuera de alcance, carril «Paciente / Familiar» → «Paciente» en BPMN P1, actor del C4, «por familiar» en proceso to-be e impulsores, N4 en el Objetivo 1).
- Frase de los «cuatro elementos»; columna «Origen»; firma atribuida a RNF03/BN7; citas a Meta (`meta2026optin`, `meta2026pricing`, `meta2026limits`, nuevas en `fundamentacion_teorica.bib`); tope fijado por Meta; número exclusivo como decisión de diseño; Shaikh corregido; terceros encargados (Meta, Google, VPS).
- Despliegue: dispositivo del paciente, dominio, VPS 2 vCPU/4 GB, puertos 80/443, renovación del certificado, custodia de la clave, túnel en desarrollo, matiz del paso a producción, canal alterno, disponibilidad «continua».
- Plan: integración en módulos críticos, prueba de reprogramación sobre horario ocupado con la tarjeta 13, «a octubre de 2026», columna «Línea base (min)», T3 sin la tarjeta 11.
- Discusión: RF01 y RF06 parciales (6 implementados, 3 parciales), RNF02 y RNF05 corregidos, PC3, modularidad matizada, cuatro limitaciones nuevas, trabajos futuros unificados con la tabla de exclusiones.
- Figuras: renderizadas con PlantUML (1.2025.4, SVG → PDF vectorial) `img/Estados_Conversacion.pdf`, `img/Secuencia_Agendar.pdf`, `img/Secuencia_Recordatorio.pdf`; BPMN P1 y P2 regenerados desde el SVG.
- Compilación: 0 errores, 0 referencias/citas indefinidas, 145 páginas; sin cajas desbordadas en el Objetivo 2.

**Pendiente (requiere draw.io / dbdiagram.io):** `C4_Contexto`, `C4_Contenedores`, `Modulos`, `C4_Componentes_Agente`, `Despliegue`, `ER_Bellidental`.
