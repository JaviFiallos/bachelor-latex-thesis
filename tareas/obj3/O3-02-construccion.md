# O3-02 — Construcción: tablero real y ejecución de las tarjetas

**Estado:** Se puede ejecutar ya para las tarjetas 1–6 (hechas) y **se repite al cerrar la construcción**
(cronograma: 15/11/2026) para completar las tarjetas 7–15.
**Archivo:** `tex/ResultsAndDiscussion/ob3/construccion.tex` (solo este).
**Script:** `tareas/obj3/scripts/fechas_tarjetas.py` (ya probado).

## Qué va en la sección

1. Un párrafo de 2 líneas (ya existe).
2. La captura del tablero (`fig:ob3_tablero`).
3. La tabla `tab:ob3_tarjetas`: una fila por tarjeta, con inicio, fin y días.
4. Un párrafo de 2–4 líneas con las desviaciones respecto al plan.

No va: pruebas, nombres de paquetes, clases ni endpoints, numeración de tareas de los repositorios.

## Pasos

### 1. Fechas de las tarjetas

Desde la raíz de la tesis:

```bash
python3 tareas/obj3/scripts/fechas_tarjetas.py
```

El script lee los commits `(tarea NNN)` de los dos repositorios en `../bellidental-app/` y devuelve una fila
LaTeX por tarjeta. Las tarjetas sin commits salen con `---` y un comentario `% sin commits todavía`.

Si aparece una tarea nueva en los repositorios (por ejemplo `012a`), añadirla a la tarjeta que corresponda
en la lista `TARJETAS` del script. La correspondencia completa está en `tareas/PLAN-OBJ3.md`, sección 4.

### 2. Tabla `tab:ob3_tarjetas`

En `construccion.tex`, reemplazar las filas de ejemplo (`1. Identidad…`, `2. Profesionales…` y la fila
`\multicolumn{4}{…}{[… completar las quince tarjetas]}`) por la salida del script.

- Mantener los nombres exactos de `tab:ob2_tarjetas`. Las tarjetas 12–14 van en negrita, como en el
  Objetivo 2; el script ya lo hace.
- La fila "Historial inmediato (RF06)" es una tarjeta añadida durante la construcción. Se deja como
  última fila y se menciona en el párrafo de desviaciones.
- Mientras la construcción siga abierta, las tarjetas sin fecha quedan con `---`. Al cierre no debe quedar
  ninguna; si una tarjeta no se hizo, poner `No ejecutada` en la columna Fin y declararlo en el párrafo.
- Días = días naturales entre el primer y el último commit, ambos incluidos.

### 3. Captura del tablero

1. Crear el tablero en GitHub Projects (o Trello) con las 4 columnas del diseño: Pendiente, En desarrollo,
   En pruebas y Terminado (`fig:ob2_boceto_kanban`). Una tarjeta por fila de `tab:ob3_tarjetas`, con el
   mismo nombre.
2. En la fecha de corte, hacer la captura a 1366 px de ancho y guardarla como `img/Ob3_Tablero_Kanban.png`.
   La figura la toma sola (`\IfFileExists`).
3. En el párrafo inicial, reemplazar `\textit{[fecha de corte]}` por la fecha en formato
   `15 de noviembre de 2026`.

### 4. Párrafo de desviaciones

Reemplazar el bloque `\textit{[Por completar: …]}` por 2–4 líneas en pasado. Usar solo hechos que se
puedan comprobar en los repositorios (`docs/tasks/` y `git log`). Hechos ya comprobados al 16/10/2026:

| Hecho | Evidencia |
|---|---|
| La agenda (tarjeta 4) se entregó en varias partes: horarios, disponibilidad y ajustes de respuesta | Backend 006a–006e |
| El odontograma (tarjeta 6) se dividió en cuatro entregas: estructura, símbolos, hallazgos y prótesis en rango | Frontend 009a, 009b, 010a, 010b |
| Al integrar la interfaz con el servidor surgieron ajustes no planificados en pacientes, historia clínica y agenda | Backend 004a, 005b, 006c–006e |
| Se añadió el historial inmediato del paciente (RF06) como tarjeta propia | Frontend 014 |
| Las tarjetas 1–6 avanzaron en paralelo entre el 08/10 y el 12/10, con trabajo de interfaz y servidor superpuesto | Salida del script |

Ejemplo de redacción, a ajustar con los datos del cierre:

```latex
Las tarjetas de la agenda y del odontograma se dividieron en varias entregas: la agenda, por los horarios y la disponibilidad; el odontograma, por la simbología del Formulario 033. Al integrar la interfaz con el servidor surgieron ajustes no previstos en pacientes, historia clínica y agenda, y se añadió el historial inmediato del paciente (RF06) como una tarjeta propia.
```

Reglas: no decir que el límite de una tarjeta en desarrollo se respetó si las fechas se superponen. En ese
caso, explicarlo en una frase: la tarjeta seguía abierta mientras se ajustaba su interfaz.

## Verificación

1. Añadir temporalmente `\input{tex/ResultsAndDiscussion/results-ob3}` al final de
   `tex/ResultsAndDiscussion/resultados-discusion.tex`.
2. `latexmk -pdf -interaction=nonstopmode main.tex` → código 0, sin `Overfull` nuevos en
   `Build/main.log`.
3. La tabla tiene 16 filas (15 tarjetas + historial) y ninguna fila `\multicolumn` de relleno.
4. Quitar el `\input` temporal, recompilar y copiar `Build/main.pdf` a `main.pdf`.
5. En `tareas/obj3/00-indice.md`: **Parcial (1–6)** si se ejecutó antes del cierre; **Hecha** después.
