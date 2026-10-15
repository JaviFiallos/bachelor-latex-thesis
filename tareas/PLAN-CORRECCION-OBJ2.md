# Plan de corrección del Objetivo 2

Numeración de tablas: la del autor (antes de sus eliminaciones).

## Fase 0. Referencias huérfanas (primero)

| Dónde | Qué queda roto | Corrección |
|---|---|---|
| `metodologia.tex` (l. 7), `tecnologias.tex` (l. 3), `tecnologias-agente.tex` (l. 3) | `\ref{tab:ob2_restricciones}` (Tabla 35 eliminada) | Quitar la referencia; una sola frase en los impulsores nombra las tres restricciones que dan peso a los criterios: un único desarrollador, plazo acotado y bajo costo |
| `intro-impulsores.tex` (última frase) | "metodología … y notación de modelado. Ambas decisiones" | "orientan la selección de la metodología de desarrollo" |
| `metodologia.tex` (título) | "y marcos de modelado" (Tabla 37 y Notación de artefactos eliminadas) | Título: "Metodología de desarrollo". C4 y UML se citan una vez al inicio de la arquitectura general |
| `arquitectura-agente.tex` (l. 3) | "más las medidas de seguridad y cumplimiento" (Tabla 58 eliminada) | Quitar |
| `discusion.tex` (trabajos futuros) | `\ref{tab:ob2_fuera_alcance}` | Según la decisión sobre "fuera del alcance" |

## Fase 1. Tablas a reducir o convertir

| Tabla | Acción |
|---|---|
| 34 Atributos de calidad | Una frase que la enlaza con Arcila (verificó atributos ISO/IEC 25010 con pruebas de carga) |
| 45 Motores conversacionales | Quitar columnas Botpress y Dialogflow (su descarte queda en el texto, una frase); más ancho a "Criterio" |
| 51 Módulos | Texto breve del monolito modular: clínica pequeña, un desarrollador, microservicios = complejidad innecesaria. Tabla de 2 columnas (Módulo · Qué hace) con 5–6 módulos esenciales y nombres funcionales en español; sin interfaces ni paquetes (`PatientDirectory`, `notifications`, "ya tienen código") |
| Figura de módulos | Nombres funcionales en español, mismos 4 grupos |
| 52 Tablas por grupo | Sale del capítulo → Anexo 4 (modelo de datos completo, con el ER completo) |
| 53 Tablas principales | Se reemplaza por: figura centrada en **Atención** con sus entidades vecinas + tabla corta (Entidad · Atributos principales · Requerimiento), una línea por fila, nombres conceptuales |
| 54 Principios | Recortar a una línea por principio |
| 55 Capas del agente | Diagrama de estructura lógica (capas) |
| 56 Componentes funcionales | Diagrama de componentes funcionales (cada caja: componente + RF + regla en una línea) |
| Figura estados de la conversación | Rehacer (ver nota) |
| 57 Mecanismos de integración | Recortar a una línea por mecanismo; sincronización de Calendar según decisión |
| 59 Nodos de despliegue | 2 columnas (Nodo · Función), una línea por fila |
| Fuera del alcance | Según decisión |
| 3.2.10 Discusión | Sin tablas: se eliminan cobertura y contraste; cierre en párrafos según decisión |

**Nota sobre los estados de la conversación.** Desajustes con el texto: la identificación aparece antes del menú para todos (solo agendar y reprogramar la necesitan); el aviso aparece siempre (solo en la primera interacción); falta la ruta "no acepta"; el recordatorio no es un estado sino otra entrada; falta la caducidad de 30 min.

## Fase 2. Contenido nuevo

| Sección | Contenido |
|---|---|
| Diseño de la interfaz (nueva, tras el modelo de datos) | Esqueleto con marcadores: paleta de colores, mockups, prototipo HTML con los módulos principales. El autor lo desarrolla |
| Anexo 4. Modelo de datos completo | ER completo (`img/ER_Bellidental.pdf`) y lista de tablas por grupo |

## Fase 3. Cierre

Compilar (0 errores, 0 referencias indefinidas), revisar páginas del Obj. 2, commit en `feat/results-obj2`.

## Decisiones del autor (2026-10-15)

| Duda | Decisión |
|---|---|
| Google Calendar | Unidireccional (solo lectura; agenda del sistema = única fuente, RF07) |
| Fuera del alcance | Párrafo al final de los requerimientos del Obj. 1 |
| Discusión | Cuatro párrafos, sin tablas |
| Diagramas nuevos | Los dibuja Claude (TikZ / PlantUML) |

## Estado: ejecutado

Fases 0–2 aplicadas; compila con 0 errores, 0 referencias indefinidas y sin cajas desbordadas en el Obj. 2. Pendiente del autor: texto e imágenes de «Diseño de la interfaz» (`img/Paleta_Colores.png`, `img/Mockup_Agenda.png`, `img/Mockup_Atencion.png`, `img/Prototipo_Modulos.png`), `img/ER_Bellidental.pdf` (Anexo 4) y reexportar `Despliegue.png` sin la selección de draw.io.
