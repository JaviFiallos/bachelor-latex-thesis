#!/usr/bin/env python3
r"""Fechas de inicio y fin de cada tarjeta del plan (tab:ob2_tarjetas) a partir
de los commits "(tarea NNN)" de los dos repositorios. Uso:
    python3 tareas/obj3/scripts/fechas_tarjetas.py [ruta/a/bellidental-app]
Salida: filas LaTeX "Tarjeta & Inicio & Fin & Días \\ \hline" listas para tab:ob3_tarjetas.
"""
import re, subprocess, sys
from datetime import date
from pathlib import Path

APP = Path(sys.argv[1] if len(sys.argv) > 1 else
           Path(__file__).resolve().parents[4] / "bellidental-app")

TARJETAS = [  # (nombre en la tesis, tareas backend, tareas frontend)
    ("1. Identidad y autenticación", ["001", "002", "003"], ["001", "002a"]),
    ("2. Profesionales y pacientes", ["004", "004a"], ["002b", "005a", "005b"]),
    ("3. Historia clínica y antecedentes", ["005", "005b"], ["008b"]),
    ("4. Agenda y horarios", ["006", "006a", "006b", "006c", "006d", "006e"],
     ["003a", "003b", "003c", "004a", "004b", "006a", "006b", "007"]),
    ("5. Atención clínica y CIE-10", ["007", "008"], ["008a", "008c", "011"]),
    ("6. Odontograma", ["009"], ["009a", "009b", "010a", "010b"]),
    ("7. Tratamientos", ["010"], ["012"]),
    ("8. Recetas", ["011"], ["013"]),
    ("9. Cobros y comprobante", ["012"], ["015"]),
    ("10. Auditoría", ["013"], ["017"]),
    ("11. Sincronización con Google Calendar", ["014"], []),
    ("\\textbf{12. Agente: núcleo, aviso, información y derivación}", ["015"], []),
    ("\\textbf{13. Agente: agendar y reprogramar}", ["016"], []),
    ("\\textbf{14. Agente: recordatorios}", ["017"], []),
    ("15. Respaldos y exportación", ["018"], []),
    ("Historial inmediato (RF06)", [], ["014"]),
]

PATRON = re.compile(r"\(tareas? ([0-9a-z ,y]+)\)", re.I)

def commits(repo):
    out = subprocess.run(["git", "-C", str(APP / repo), "log", "--all", "--format=%ad|%s",
                          "--date=short"], capture_output=True, text=True, check=True).stdout
    fechas = {}
    for linea in out.splitlines():
        dia, _, asunto = linea.partition("|")
        m = PATRON.search(asunto)
        if not m:
            continue
        for t in re.split(r"[ ,y]+", m.group(1)):
            if t:
                fechas.setdefault(t.lower(), []).append(date.fromisoformat(dia))
    return fechas

back, front = commits("bellidental-backend"), commits("bellidental-frontend")
fmt = lambda d: d.strftime("%d/%m")
for nombre, tb, tf in TARJETAS:
    dias = [d for t in tb for d in back.get(t, [])] + [d for t in tf for d in front.get(t, [])]
    if dias:
        ini, fin = min(dias), max(dias)
        print(f"{nombre} & {fmt(ini)} & {fmt(fin)} & {(fin - ini).days + 1} \\\\ \\hline")
    else:
        print(f"{nombre} & --- & --- & --- \\\\ \\hline  % sin commits todavía")
