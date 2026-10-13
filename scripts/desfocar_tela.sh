#!/bin/bash
# Desfoca só uma área (a tela do notebook/celular) com borda suave. Use quando a foto
# mostra nome, telefone ou dado de cliente. O resto da foto (teclado, fundo) fica nítido.
# Uso: desfocar_tela.sh foto.jpg saida.jpg "x1,y1 x2,y2 x3,y3 x4,y4" [força=4]
# Os pontos são os 4 cantos da tela EM PIXELS DA FOTO ORIGINAL (sup-esq, sup-dir, inf-dir, inf-esq).
# Dica: desenhe o polígono em vermelho antes para conferir:
#   magick foto.jpg -fill none -stroke red -strokewidth 8 -draw "polygon ..." -resize x900 teste.png
set -e
foto="$1"; saida="$2"; pontos="$3"; forca="${4:-4}"
tmp="$(mktemp -t desfoque).png"
magick "$foto" -blur 0x"$forca" \( "$foto" -fill black -colorize 100 -fill white -draw "polygon $pontos" -blur 0x12 \) \
  -alpha off -compose CopyOpacity -composite "$tmp"
magick "$foto" "$tmp" -compose Over -composite -quality 92 "$saida"
rm -f "$tmp"
echo "ok $saida"
