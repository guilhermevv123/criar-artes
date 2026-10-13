# Fotos

## Ordem de preferência

1. **Foto que o dono mandou** (celular, luz real) — a mais confiável em anúncio.
2. **Captura real do sistema** (vitrine com dados de exemplo).
3. **Foto gerada por IA — só de PESSOA ou cena sem marca**, que serve para qualquer peça. Nunca gerar arte com texto, logo ou tela de sistema por IA.

## Gerar foto por IA (Higgsfield, conta do dono)

- Script: `~/blender-higgsfield/gerar_imagem.mjs --nome <nome> --formato 9:16|3:4|1:1 --modelos grok --prompt "..."` → `~/blender-higgsfield/imagens/<nome>_grok_1.png` (720×1280).
- **Antes de gerar: cotar e pedir OK com o valor total** (o dono reclamou de gasto). Preços por imagem: z-image turbo US$ 0,015 · qwen US$ 0,04 · grok US$ 0,06 · marketing-studio US$ 0,109. Comparação feita: grok é o mais realista e vale o preço; zturbo serve para rascunho.
- Ampliar para 1080×1920: `magick in.png -filter Lanczos -resize 1080x1920^ -gravity center -extent 1080x1920 -quality 92 fotos/x.jpg`.
- Sem chave? Usar o cofre: `chave rodar <lugar> -- node gerar_imagem.mjs ...` (nunca imprimir a chave).

### Como escrever o prompt (em inglês)

`Photorealistic vertical photograph of <quem: idade, aparência brasileira, roupa> <fazendo o quê, emoção> at <onde>. Natural soft daylight, neutral true-to-life colors, no color cast, shallow depth of field, sharp details on face and hands. The <pessoa> occupies the lower half of the frame; the upper half is <fundo desfocado> left empty. No text, no logos, no watermark.`

- **"lower half / upper half empty"** é o que deixa espaço para o texto sem tampar o rosto.
- Luz natural e cor neutra: a cor da marca entra depois, pelo degradê do HTML (assim a foto serve para qualquer marca).
- Exemplo usado: técnico de usina de capacete branco olhando um tablet, painéis desfocados atrás.

## Desfocar dado de cliente

Foto de tela com nome, telefone, valor de cliente real → `scripts/desfocar_tela.sh foto.jpg saida.jpg "x1,y1 x2,y2 x3,y3 x4,y4"`.
- Os 4 cantos da tela em px da foto original. Desenhe o polígono em vermelho antes e confira.
- Força 4 (padrão) deixa colunas, cores e etiquetas visíveis, mas o texto ilegível. Telas só com totais (dashboard) podem ficar nítidas.
- Conferir com um recorte ampliado (`magick saida.jpg -crop 700x500+X+Y teste.png`) que nada ficou legível e que o teclado/fundo continuam nítidos.

## Fotos repetidas

Quando o dono manda várias fotos, compare o md5 (`md5 -q *.jpg`) — é comum vir a mesma foto 3–4 vezes. Use cada foto diferente uma vez antes de repetir.
