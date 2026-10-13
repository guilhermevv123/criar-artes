# Formatos e receitas

## Tamanhos

| Peça | Tamanho | Observação |
|---|---|---|
| Story / Reels / anúncio vertical | 1080×1920 | deixar ~220 px no topo e embaixo sem texto crucial (interface do Instagram) |
| Feed / anúncio de feed | 1080×1350 (4:5) | o que mais ocupa tela no feed |
| Quadrado | 1080×1080 | carrossel antigo, LinkedIn |
| Carrossel | 1080×1350 cada | mesma moldura em todas; 1ª = gancho, última = CTA |
| PDF | A4 em pé (210×297 mm) | ver `pdf.md`; paisagem só se pedirem |

## Como copiar uma referência (criativo "igual a esse")

1. Meça a referência em proporção: divida a posição de cada bloco pela altura (ex.: caixa do título de 23% a 36% da altura, lista de 38% a 55%, botão de 58% a 69%). Multiplique por 1920 (story) para ter os px.
2. Anote: cor do fundo, se o texto fica em caixa (branca? arredondada?), peso da fonte (quase sempre 800), alinhamento (centro? esquerda?), quantas linhas, onde está o logo, o que tem na foto e onde fica o rosto/produto.
3. Copie a ESTRUTURA e o ritmo; troque as cores pela paleta da marca e o texto pela copy nova. "O máximo parecido possível" = mesma composição, não as mesmas palavras.
4. Renderize ao lado da referência (`prancha.sh comparar.png referencia.png nova.png`) e compare bloco a bloco.

## Receita 1 · Oferta com notebook (anúncio de tráfego que mais converte)

Modelo: `modelos/oferta_notebook.py`. Referência validada: "CRM completo + IA R$197,00/mês" + 5 itens com ✅ + "VEJA FUNCIONANDO EM 30 MIN 👇".
- Foto: celular em pé, notebook aberto com o sistema na metade de baixo, fundo escuro liso em cima (cortina, parede). Foto real do dono > montagem.
- Foto descida ~170 px; o topo vazio é preenchido com a própria foto espelhada (`scaleY(-1)`) — em cortina/parede a emenda não aparece.
- Bloco centralizado a partir de y≈150: caixa branca (título 64–76 px, 800, 2–3 linhas, `nowrap`) → lista (5 itens, 32 px, faixa menta, quadradinho verde com ✓) → botão verde `#2DBE6C` com 2 linhas em 64 px, maiúsculas, emoji 👇 no fim.
- O bloco termina antes do meio da tela do notebook — a tela tem que aparecer.
- Variações: mesmo layout, muda o título (ex.: "+ Financeiro", "+ IA", "+ Monitoramento", "+ Financeiro + IA + Monitoramento"), a foto e os itens. 6–8 variações numeradas.
- Preço: escrever do jeito que o dono mandar (ex.: só "R$197/mês"). Não inventar condição.

## Receita 2 · Foto de pessoa + texto (estilo agência)

Modelo: `modelos/foto_com_texto.py` (versões escura e clara).
- Foto de pessoa com emoção clara ligada à dor (técnico olhando o tablet, cliente dormindo esperando, família feliz com o vendedor).
- Texto no terço de cima; degradê sólido da cor escura até ~640 px e sumindo até ~780 px; **a cabeça começa abaixo disso**. Se não couber, desça a foto (`top:+230px`) e compacte o texto.
- Título 70–94 px com 1–2 palavras na cor de destaque; apoio 34–42 px; botão largo (620–730 px × 104–132 px).
- Logo: abaixo do botão (escura) ou no topo à esquerda (clara) — nunca em cima do cabelo/rosto.
- Faixa no topo "EMPRESA DE ENERGIA SOLAR" (caixa neon ou branca, 54–58 px, `nowrap`) chama o público certo.

## Receita 3 · Ilustração feita em HTML (sem foto)

Quando a ideia é uma metáfora (esforço, crescimento, gargalo): formas em CSS + figura em SVG.
- Ex.: "inadimplência alta não é falta de esforço" = ladeira (`div` com `skewY(-17deg)` verde), bola grande (`radial-gradient`), boneco em SVG empurrando (traços grossos, `stroke-linecap:round`, degradê menta→verde).
- Os elementos precisam se TOCAR (boneco encostado na bola, bola apoiada na ladeira). Conferir na imagem.
- Texto em cima, ilustração no terço de baixo.

## Receita 4 · Feed escuro "tech" (4:5)

Modelo: `modelos/feed_escuro.py`.
- Fundo: céu verde-escuro com brilho da cor do assunto no canto + chão quadriculado em perspectiva.
- Moldura fixa da série: logo + nome da série no topo; "Arraste para o lado · site" + botão no rodapé.
- Etiqueta com tracinho (20 px, maiúsculas, cor do assunto) → título 84 px com 1 palavra em Instrument Serif itálico na cor → apoio 31 px.
- Prova visual: captura do sistema numa moldura escura, saindo pela borda direita; ou celular (`border-radius:52px`) com a tela do app; ou cartões de vidro (`rgba(255,255,255,.055)` + borda `.12`).
- Comparação "sem × com": coluna com X vermelho `#F87171` e coluna com ✓ neon.

## Receita 5 · Carrossel

- 1ª lâmina: gancho provocativo (título grande, sem lista). 2ª–(n-1): uma ideia por lâmina, com número ("1/5"). Última: CTA + o que a pessoa ganha.
- Mesma moldura e mesma posição de título em todas (o olho acostuma).
- Gere todas com um gerador só e confira na prancha em sequência.

## Receita 6 · PDF A4 (proposta, estratégia, relatório)

Ver `pdf.md`. Capa escura de página inteira (página nomeada `@page capa{margin:0}`), miolo claro com margens 16–18 mm, títulos verde-escuros, tabelas com cabeçalho menta, caixas de destaque com borda verde à esquerda.
