# PDF bonito (A4)

Gerar com `scripts/render.py --pdf doc.html saida.pdf` (Chrome `--print-to-pdf`). Exemplos: `~/helioz-marketing/icp-e-planos/gerar.py` (Markdown → PDF), `~/helioz-marketing/estrategias-oficiais/gerar.py` (funis desenhados em SVG).

## Regras

- **A4 em pé** por padrão: `@page{size:A4;margin:18mm 16mm}`. Paisagem só se pedirem.
- **Capa de página inteira**: `@page capa{margin:0}` + `.capa{page:capa;width:210mm;height:297mm;box-sizing:border-box;break-after:page}`. (Margem negativa NÃO funciona: a capa vaza para a página 2.)
- `-webkit-print-color-adjust:exact; print-color-adjust:exact` no `html,body` (senão o fundo some).
- **Nada de `filter`, `blur`, `backdrop-filter`, `mask` e sombra grande** em PDF: deixa o arquivo pesado e lento para abrir. Se precisar desse efeito, faça um JPG do fundo (screenshot do HTML) e use como imagem — **um JPG por página** (um screenshot alto único quebra a partir da ~8ª página).
- Imagens em JPG ~85% e na largura que vai aparecer (não 4000 px). Meta: PDF de até ~3 MB.
- `break-inside:avoid` em tabela e caixa; `break-after:avoid` em título.
- Coluna curta de tabela (preço, sim/não) com `white-space:nowrap`.
- Título sem "Marca — " repetido; primeira letra maiúscula.

## Conferir

Renderizar as páginas em PNG e olhar: no Mac, `swift scripts/pdf_para_png.swift doc.pdf pasta/` (PDFKit, salva `e-1.png`, `e-2.png`…); ou `magick -density 80 doc.pdf p-%d.png` se o Ghostscript existir. Juntar com `prancha.sh` e conferir: capa sem vazar, nenhuma página com 1 linha sozinha, tabelas inteiras, fundo em todas as páginas.
