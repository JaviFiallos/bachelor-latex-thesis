# O3-00 — Análisis del postest en Metodología y actualización del Instrumento 4

**Estado:** Lista para ejecutar. **Antes del postest**, porque la ficha del anexo se usará en campo.
**Archivos:** `tex/Methodology/data-analysis.tex`, `tex/Methodology/population-sample.tex`,
`tex/Appendices/instruments.tex` (solo el Instrumento 4).
**No tocar:** ningún otro archivo, ni los resultados del pretest (tablas `tab:resumen_obs_parte_a` y
`tab:resumen_obs_parte_b`).

## Por qué

El capítulo 2 declara un diseño preexperimental con medición antes y después (`methods.tex`), pero no dice
cómo se compararán ambas mediciones ni cómo será la muestra del postest. Además, la ficha del anexo usa la
numeración antigua de los tramos (T2 atención, T4 registro, T5 pago, T6 agendamiento), distinta de la que
usan los resultados (T1–T5).

## Reglas de redacción

- Español formal, tiempo **futuro** ("se aplicará", "se comparará"): el postest todavía no ocurre.
- Párrafos de 3–5 líneas. Una tabla corta es preferible a un párrafo largo.
- No inventar citas. Si una frase pide referencia (pruebas estadísticas), dejar `% CITA PENDIENTE` al final
  de la línea y no poner `\cite`.
- Sin "MVP", sin mencionar asistentes de programación, sin nombres técnicos del sistema.
- Decimales con coma: `3{,}40` en modo matemático y `3,40` en texto.

---

## Parte A — `data-analysis.tex`: procedimiento de comparación

Insertar **al final del archivo** (después del párrafo "En conjunto, …") el párrafo y la tabla siguientes.
Se pueden ajustar las palabras, pero no el contenido.

```latex
La medición postest repetirá la ficha de observación con el mismo procedimiento del pretest. Se plantea como hipótesis que el tiempo de gestión administrativa por paciente después de implementar el sistema es menor que el registrado en el pretest ($H_1$: $TGA_{post} < TGA_{pre}$; $H_0$: $TGA_{post} \geq TGA_{pre}$), con un contraste unilateral y un nivel de significancia de 0,05. Como ambas fases registran pacientes distintos, las muestras se tratarán como independientes. La Tabla~\ref{tab:analisis_postest} resume el tratamiento de cada variable.

\begin{table}[H]
\centering
\caption{Análisis previsto para la comparación pretest--postest}
\label{tab:analisis_postest}
\fontsize{9}{11}\selectfont
\renewcommand{\arraystretch}{1.2}
\setlength{\tabcolsep}{4pt}
\begin{tabularx}{\linewidth}{|>{\raggedright\arraybackslash}p{3.2cm}|>{\raggedright\arraybackslash}p{2.4cm}|>{\raggedright\arraybackslash}X|}
\hline
\textbf{Variable} & \textbf{Unidad} & \textbf{Análisis} \\ \hline
$T_1$, $T_2$, $T_3$ y $T_{E1}$ & Paciente & Normalidad con Shapiro--Wilk; t de Welch si ambas fases son normales, U de Mann--Whitney si no lo son \\ \hline
Tamaño del efecto & Paciente & d de Cohen (t de Welch) o $r$ (U de Mann--Whitney) \\ \hline
$T_4$, $T_5$ y $T_{E2}$ & Jornada & Comparación descriptiva del promedio por ficha \\ \hline
$TGA$ & Paciente & $T_{E1} + T_{E2}$; reducción en minutos y en porcentaje \\ \hline
\end{tabularx}
\end{table}
```

Después de la tabla, una línea:

```latex
La Etapa 2 se registra por lote diario y no por paciente, por lo que su comparación es descriptiva. El pretest dispone de los registros individuales de los 78 pacientes, lo que permite aplicar las pruebas anteriores sobre $T_{E1}$.
```

Comprobar que `tabularx` y `float` ya se usan en el capítulo (sí: `instrument4-data-collection.tex` los usa).

---

## Parte B — `population-sample.tex`: muestra del postest

En el párrafo que empieza "En la ficha de observación no se calculó el tamaño de muestra…" (línea ~47),
añadir **al final de ese mismo párrafo**:

```latex
El postest seguirá el mismo criterio: los pacientes atendidos en tres jornadas de alta afluencia, en los mismos días de la semana que el pretest (martes, jueves y sábado), con el mismo observador y después de al menos dos semanas de uso estable del sistema. Los datos de los pacientes citados se cargarán en el sistema el día anterior a partir de las fichas digitales que la secretaria prepara para cada jornada, de modo que, como en el pretest, la medición se limite a la gestión que ocurre durante la atención.
```

No borrar los comentarios `%` que hay debajo del párrafo.

---

## Parte C — `instruments.tex`: Instrumento 4 con la numeración T1–T5

Ubicación: bloques `INSTRUMENTO 4 — PARTE A` (línea ~181) y `PARTE B` (línea ~226).

### Parte A de la ficha

Reemplazar las cuatro filas de tramos y los tres indicadores:

| Antes | Después |
|---|---|
| `T2 — Atención clínica (referencia)` | `Atención clínica (referencia, no se suma)` |
| `T4 — Registro post-consulta (receta, actualización)` | `$T_1$ — Registro posconsulta (receta, actualización)` |
| `T5 — Registro de pago` | `$T_2$ — Registro del pago` |
| `T6 — Agendamiento próxima cita` | `$T_3$ — Agendamiento de la próxima cita` |
| `Tiempo administrativo directo $(T_4 + T_5 + T_6)$:` | `Tiempo administrativo directo $T_{E1} = T_1 + T_2 + T_3$:` |
| `$(\text{Hora inicio } T_2 - \text{Hora de llegada})$` | `$(\text{Inicio de la atención} - \text{Hora de llegada})$` |
| `$(\text{Hora inicio } T_2 - \text{Hora programada})$` | `$(\text{Inicio de la atención} - \text{Hora programada})$` |

### Parte B de la ficha

El pretest separó el llenado manual ($T_4$) de la digitalización ($T_5$) (`tab:resumen_obs_parte_b`), pero la
ficha tiene una sola fila de lote. Reemplazar la tabla del bloque `REGISTRO DEL LOTE DIARIO` por:

```latex
\begin{tabularx}{\linewidth}{|>{\raggedright\arraybackslash}X|c|c|c|c|}
\hline
\textbf{Tramo} & \textbf{Hora inicio} & \textbf{Hora fin} & \textbf{Duración (min)} & \textbf{N.\textsuperscript{o} fichas} \\ \hline
$T_4$ — Llenado del Formulario 033 & & & & \\[12pt] \hline
$T_5$ — Digitalización en la hoja de cálculo & & & & \\[12pt] \hline
\end{tabularx} \\
```

Cambiar el indicador derivado por:

```latex
Tiempo diferido por paciente $T_{E2} = (T_4 + T_5) \div \text{N.\textsuperscript{o} de fichas}$: \underline{\hspace{3cm}} \\
```

Y añadir al final del texto de la `NOTA METODOLÓGICA` (misma celda):

```latex
En el postest se registra en esta parte cualquier tarea diferida que persista con el sistema; si no existe, se anota 0.
```

---

## Pendiente de revisión (no ejecutar todavía)

El odontólogo registrará con el sistema los mismos datos que la secretaria pedía en la ficha rápida, más los
tratamientos con sus códigos, con ligeras variaciones. Puede añadirse un tiempo extra al registro posconsulta
($T_1$). **No se considera todavía:** el autor hará mediciones la semana del 19/10/2026 y, con ellas, se
revisará la definición de $T_1$ en la ficha (Parte C) y en `tab:ob3_definiciones` (tarea O3-08a).

---

## Verificación

1. `latexmk -pdf -interaction=nonstopmode main.tex` termina con código 0.
2. `grep -n "undefined" Build/main.log` no muestra `tab:analisis_postest`.
3. En el PDF, la tabla nueva cabe en el ancho de página (sin `Overfull \hbox` nuevos en `Build/main.log`).
4. En el anexo, el Instrumento 4 ya no contiene `T6` ni `T_4 + T_5 + T_6`:
   `grep -n "T6\|T_6" tex/Appendices/instruments.tex` no devuelve nada.
5. Copiar `Build/main.pdf` a `main.pdf`.
6. Marcar O3-00 como **Hecha** en `tareas/obj3/00-indice.md`.
