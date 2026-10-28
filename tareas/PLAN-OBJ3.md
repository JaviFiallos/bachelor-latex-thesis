# Plan del Objetivo 3 (reestructurado 2026-10-28)

Estructura: **3.3 Desarrollo** · **3.4 Implementación** · **3.5 Evaluación del TGA**.

## Reglas comunes
- Redacción breve y precisa; tablas y figuras primero, párrafos de 2–4 líneas.
- Coherencia con Obj. 1 (PC, BN, RF/RNF, N) y Obj. 2 (módulos, tarjetas, contrato, intenciones). No repetir
  figuras ni tablas del Obj. 2: se citan.
- Sin fechas fuera de 3.5. Sin IPs, nombres de instancia ni secretos.
- No mencionar la distinción implementación/implantación.
- RF14 (recordatorios, Debería) y las notificaciones: **no implementados**. Respaldos (tarjeta 15): pendiente
  del autor; el texto deja el marcador `\textit{[...]}`.
- Figuras generadas: fuente en `diagramas/tikz/ob3/*.tex` (standalone, paleta común), PDF en `img/Objetivo3/`.
  Reconstruir: `bash diagramas/tikz/ob3/build.sh`.
- Capturas del sistema (las toma el autor, datos ficticios): `img/Objetivo3/<nombre>.png`; mientras falten, el
  documento muestra un recuadro "Pendiente".

## Tareas

| # | Tarea | Archivos | Figuras |
|---|---|---|---|
| T1 | Reestructura y coherencia: tres subsecciones, intro, tabla RAD y arquitectura del front en Obj. 2, RF14 no implementado, sin fechas | `results-ob3.tex`, `ob3/intro.tex`, `ob2/metodologia.tex`, `ob2/diseno-interfaz.tex`, `ob2/arquitectura-general.tex` | — |
| T2 | 3.3.1 Diseño con el usuario y 3.3.2 Base técnica (árboles del back y del front, dependencias, pruebas) | `ob3/diseno-usuario.tex`, `ob3/base-tecnica.tex` | árboles en LaTeX (`dirtree`) |
| T3 | 3.3.3 Base de datos por grupos, roles × permisos, reglas en la BD | `ob3/base-datos.tex` | 4 ER parciales (generadas) |
| T4 | 3.3.4 Tarjetas principales: back + front por tarjeta | `ob3/tarjetas.tex` | capturas del autor |
| T5 | 3.3.5 Desarrollo del agente: estructura, interfaz interna, LLM, cadena de decisión híbrida | `ob3/agente-desarrollo.tex` | cadena de decisión (generada), árbol del agente |
| T6 | 3.4 Implementación: servidor, contenedores y CI/CD, WhatsApp, LLM, pruebas del agente, transición, verificación y tablero | `ob3/infraestructura.tex`, `ob3/contenedores-cicd.tex`, `ob3/whatsapp.tex`, `ob3/modelo-lenguaje.tex`, `ob3/pruebas-agente.tex`, `ob3/transicion.tex`, `ob3/verificacion.tex` | pipeline (generada), capturas del autor |
| T7 | 3.5 Evaluación (ajustes por RF14) y revisión final: compilación, referencias, fechas, términos | `ob3/evaluacion.tex`, `ob3/discusion.tex` | — |

## Capturas que debe tomar el autor (`img/Objetivo3/`)

| Archivo | Contenido | Sección |
|---|---|---|
| `Ob3_Login_Perfiles.png` | Inicio de sesión y menú lateral de un perfil | 3.3.4 a) |
| `Ob3_Agenda.png` | Agenda del día con el rechazo de una cita superpuesta | 3.3.4 b) |
| `Ob3_Atencion.png` | Atención con antecedentes, diagnósticos y odontograma | 3.3.4 c) |
| `Ob3_Receta.png` | Tratamientos de la atención y receta en PDF | 3.3.4 d) |
| `Ob3_Form033.png` | Formulario 033 generado | 3.3.4 d) |
| `Ob3_Cobro.png` | Ficha de recepción con estado de cuenta y abono | 3.3.4 e) |
| `Ob3_Director.png` | Estadísticas o historial de cambios | 3.3.4 f) |
| `Ob3_Meta_Webhook.png` | Configuración del webhook en la app de Meta | 3.4.3 |
| `Ob3_Agente_Horarios.png` | Aviso, menú y respuesta de horarios | 3.4.5 |
| `Ob3_Agente_Texto_Libre.png` | Mensaje en texto libre interpretado (agendar) | 3.4.5 |
| `Ob3_Agente_Agendamiento.png` | Confirmación de la cita y su aparición en la agenda | 3.4.5 |
| `Ob3_Agente_Derivacion.png` | Consulta clínica o de saldo derivada a recepción | 3.4.5 |
| `Ob3_Tablero_Kanban.png` | Tablero final con las tarjetas completadas | 3.4.7 |
