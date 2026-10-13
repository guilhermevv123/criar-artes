#!/bin/bash
# Junta várias artes lado a lado (altura 800) numa imagem só, para revisar de uma vez.
# Uso: prancha.sh saida.png a.png b.png c.png ...
set -e
saida="$1"; shift
[ $# -gt 0 ] || { echo "Uso: prancha.sh saida.png a.png b.png ..."; exit 1; }
magick "$@" -resize x800 -background '#777' -splice 12x0 +append -quiet "$saida"
echo "ok $saida"
