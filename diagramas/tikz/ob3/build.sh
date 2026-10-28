#!/usr/bin/env bash
# Compila cada diagrama del Objetivo 3 y copia el PDF a img/Objetivo3/.
set -euo pipefail
cd "$(dirname "$0")"
out=../../../img/Objetivo3
mkdir -p "$out" build
for f in Ob3_*.tex; do
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build "$f" >/dev/null
  cp "build/${f%.tex}.pdf" "$out/"
  echo "ok: $out/${f%.tex}.pdf"
done
