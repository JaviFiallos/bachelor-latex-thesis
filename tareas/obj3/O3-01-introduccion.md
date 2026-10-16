# O3-01 — Introducción del Objetivo 3 y figura de secuencia

**Estado:** Lista para ejecutar.
**Archivo:** `tex/ResultsAndDiscussion/ob3/intro.tex` (solo este).

## Qué hay

El archivo ya tiene un párrafo redactado y, debajo, un comentario `% FIGURA OPCIONAL`. Falta la figura y la
referencia a ella desde el párrafo.

## Pasos

1. **No cambiar** el bloque de comentarios del inicio (`% QUÉ VA …`).
2. Al final del párrafo existente, añadir esta frase:

   ```latex
   La Figura~\ref{fig:ob3_secuencia} resume la secuencia entre los tres objetivos.
   ```

3. Reemplazar el comentario `% FIGURA OPCIONAL (recomendada): …` (las 4 líneas) por la figura. El código
   ya está probado con los márgenes de la tesis: no cambiar tamaños ni distancias.

   ```latex
   \begin{figure}[H]
   \centering
   \begin{tikzpicture}[
     font=\footnotesize,
     fase/.style={draw, rounded corners=2pt, line width=0.6pt, align=center,
                  minimum height=1.7cm, text width=2.4cm, inner sep=3pt},
     flecha/.style={-{Stealth[length=2.2mm]}, line width=0.7pt, draw=dExternoB},
     obj/.style={font=\scriptsize\bfseries, text=dExternoB}
   ]
   \node[fase, fill=dPersonaF, draw=dPersonaB] (diag) {\textbf{Diagnóstico}\\ $TGA$ pretest\\ RF y RNF};
   \node[fase, fill=dSistemaF, draw=dSistemaB, right=0.25cm of diag] (dis) {\textbf{Diseño}\\ arquitectura, datos e interfaz};
   \node[fase, fill=dAgenteF, draw=dAgenteB, right=0.25cm of dis] (cons) {\textbf{Construcción}\\ tablero Kanban};
   \node[fase, fill=dAgenteF, draw=dAgenteB, right=0.25cm of cons] (tran) {\textbf{Transición}\\ despliegue y capacitación};
   \node[fase, fill=dClinicoF, draw=dClinicoB, right=0.25cm of tran] (eval) {\textbf{Evaluación}\\ $TGA$ postest};
   \foreach \a/\b in {diag/dis, dis/cons, cons/tran, tran/eval} \draw[flecha] (\a) -- (\b);
   \node[obj, above=2pt of diag] {Objetivo 1};
   \node[obj, above=2pt of dis] {Objetivo 2};
   \node[obj, above=2pt of $(cons.north)!0.5!(eval.north)$] {Objetivo 3};
   \draw[flecha, dashed] (eval.south) -- ++(0,-0.45) -| node[pos=0.25, below, font=\scriptsize]{contraste pretest--postest} (diag.south);
   \end{tikzpicture}
   \caption{Secuencia de los objetivos de la investigación}
   \label{fig:ob3_secuencia}
   \end{figure}
   ```

   Los colores (`dPersonaF`, `dSistemaF`, …) y las bibliotecas TikZ (`positioning`, `arrows.meta`, `calc`)
   ya están definidos en `main.tex`, líneas 127–135. No agregar paquetes.

4. Revisar el párrafo con estas reglas, sin alargarlo:
   - Debe mencionar $TGA = 13{,}62$ min con `Tabla~\ref{tab:tramos_tga}` y la tabla de fases RAD
     `Tabla~\ref{tab:ob2_fases_rad}`. Ya lo hace: no duplicar.
   - Sin resultados ni cifras del postest (no existen todavía).
   - Sin "MVP" ni nombres técnicos.

## Verificación

`results-ob3.tex` **no** está incluido en la tesis. Para probar:

1. Añadir temporalmente `\input{tex/ResultsAndDiscussion/results-ob3}` al final de
   `tex/ResultsAndDiscussion/resultados-discusion.tex`.
2. `latexmk -pdf -interaction=nonstopmode main.tex` → código 0.
3. `grep -n "Overfull\|undefined" Build/main.log | grep -i "ob3\|secuencia"` → sin resultados.
4. Mirar la figura en el PDF: cinco cajas en una fila, etiquetas "Objetivo 1/2/3" encima y flecha
   discontinua debajo.
5. **Quitar** el `\input` temporal, recompilar y copiar `Build/main.pdf` a `main.pdf`. La inclusión
   definitiva del Objetivo 3 es la tarea O3-11.
6. Marcar O3-01 como **Hecha** en `tareas/obj3/00-indice.md`.
