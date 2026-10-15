#!/bin/sh
# Copia los PNG exportados de draw.io a img/ con el nombre que usa el documento.
# Uso: sh diagramas/sincronizar.sh   (desde la raíz del repositorio)
cd "$(dirname "$0")/.." || exit 1
copiar() {
  if [ -f "diagramas/drawio/$1" ]; then
    cp "diagramas/drawio/$1" "img/$2" && echo "ok  $1 -> img/$2"
  else
    echo "falta diagramas/drawio/$1"
  fi
}
copiar Contexto_C4_1.png        C4_Contexto.png
copiar Contenedores_C4_2.png    C4_Contenedores.png
copiar Modulos_API.png          Modulos.png
copiar ComponentesAgente_C4_3.png C4_Componentes_Agente.png
copiar Despliegue.png           Despliegue.png
# Aviso si dos exportaciones son idénticas (suele indicar una página equivocada)
md5sum diagramas/drawio/*.png | sort | uniq -w32 -D | sed 's/^/IDÉNTICOS: /'
