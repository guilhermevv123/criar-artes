---
name: criar-artes
description: Cria artes de marketing bonitas e prontas para postar — criativos de anúncio (story 9:16, feed 4:5), posts de Instagram, carrosséis, ofertas com preço, artes com foto de pessoa ou do sistema, e PDFs A4 bem diagramados — escrevendo HTML/CSS e renderizando com o Chrome headless. Use quando pedirem "arte", "criativo", "post", "story", "anúncio", "carrossel", "peça", "banner", "criativo igual a esse", "PDF bonito" ou mandarem uma referência visual para copiar. Já vem com a identidade da Helioz (verde) e ensina a montar a de outra marca.
---

# Criar artes

Arte boa aqui = **HTML + CSS escrito à mão → PNG/PDF pelo Chrome headless → olhar a imagem → corrigir → entregar**.
Nada de Canva, nada de gerar a arte inteira por IA de imagem. IA de imagem só faz **foto** (de pessoa ou cena), nunca texto.

Leia antes de começar:
- `referencias/formatos.md` — receitas prontas com medidas (oferta com notebook, foto + texto da agência, feed escuro, carrossel, PDF A4).
- `referencias/marcas.md` — cores, fontes, logo da Helioz e como montar o perfil de outra marca.
- `referencias/copy.md` — como escrever o texto (curto, provocativo, palavras proibidas, preço).
- `referencias/fotos.md` — de onde vem a foto, quanto custa gerar, desfoque de dado de cliente.
- `referencias/pdf.md` — regras que só valem para PDF.
- `referencias/erros-comuns.md` — os erros que já aconteceram e como evitar.

## O fluxo (sempre nesta ordem)

1. **Entender o pedido em 1 frase**: formato (story 1080×1920, feed 1080×1350, quadrado 1080×1080, PDF A4 em pé), público, oferta/mensagem, quantas variações.
2. **Se veio referência visual, copiar a estrutura, não o conteúdo**: onde fica o título, a caixa, a lista, o botão, a foto; proporção de cada bloco; tamanhos de letra relativos. Escrever essas medidas antes de codar (ver "Como copiar uma referência" em `formatos.md`).
3. **Escolher a marca** em `marcas.md` (padrão: Helioz). Nunca inventar cor fora da paleta.
4. **Escrever a copy** (`copy.md`) antes do layout. Título curto, uma ideia por arte.
5. **Foto**: primeiro o que o dono mandou ou capturas reais do sistema; gerar por IA só foto de pessoa/cena, com orçamento aprovado (`fotos.md`).
6. **Montar um gerador Python** a partir de um modelo em `modelos/` (um arquivo `.py` por série, cada arte = um bloco de HTML num dicionário). Rodar com `python3 gerador.py [nome]` para refazer só uma.
7. **Renderizar** com `scripts/render.py` (já faz a espera certa, mata o Chrome e aceita várias de uma vez).
8. **Conferir olhando**: `scripts/prancha.sh` junta as artes lado a lado; abrir a imagem com a ferramenta Read e passar o checklist abaixo. Nunca entregar sem olhar.
9. **Corrigir e renderizar de novo** até passar no checklist.
10. **Entregar**: mandar os PNG/PDF (SendUserFile), dizer em 3–6 linhas o que tem em cada um e onde está o gerador para mudar texto depois.

## Checklist antes de entregar (olhando a imagem)

- [ ] Texto **não tampa rosto** de ninguém nem a parte importante da tela/produto.
- [ ] Nenhuma palavra cortada, nenhuma linha quebrando feio (usar `white-space:nowrap` em selo/etiqueta; diminuir a fonte em vez de quebrar).
- [ ] Contraste: texto claro em fundo escuro ou caixa branca com texto escuro. Nada de verde claro em fundo branco.
- [ ] No máximo **3 níveis** de texto (título, apoio, botão). Lista de no máximo 5 itens.
- [ ] Botão/CTA único, grande, com verbo ("Fale com um especialista", "Veja funcionando em 30 min").
- [ ] Logo presente e pequeno (não compete com o título).
- [ ] Margem mínima de ~60 px nas bordas (story: deixar 220 px livres no topo e embaixo por causa da interface do Instagram, quando o texto for importante).
- [ ] Nada de dado pessoal de cliente legível (nome, telefone) — desfocar (`scripts/desfocar_tela.sh`).
- [ ] Palavras proibidas da marca fora (Helioz: nunca "integradora").
- [ ] Tamanho certo do arquivo (`magick identify`): 1080×1920, 1080×1350 etc.

## Regras de ouro do visual

- **Uma ideia por arte.** Se precisa de duas, são duas artes (ou carrossel).
- **Hierarquia por tamanho e peso**, não por cor: título 70–96 px peso 800; apoio 32–42 px peso 500; botão 36–76 px peso 800.
- **Destaque com a cor da marca em 1–2 palavras** do título (Helioz: neon `#00E676` no escuro, verde `#179C66` no claro). Nunca o título inteiro colorido.
- **Foto real > ilustração > ícone.** Captura de tela real do sistema vende mais que mockup bonito.
- **Fundo escuro**: degradê do escuro da marca para transparente por cima da foto, terminando ANTES do rosto/tela (medir em px, não em %).
- **Caixa branca com cantos 22–26 px** é o formato que mais funciona em anúncio de tráfego (título com preço).
- **Lista com check verde** em faixas claras (`rgba(214,247,229,.94)`), alinhadas à esquerda, largura do texto.
- **Variações**: mesma estrutura, muda título/foto/lista — numerar (`oferta-1-financeiro`, `oferta-2-...`) para o teste A/B.
- Fontes do Google por `@import` (Plus Jakarta Sans para título, Inter para texto). Esperar a fonte carregar (o render já usa `--virtual-time-budget`).

## Ferramentas

- `scripts/render.py` — `python3 render.py arte.html saida.png 1080 1920` ou `--pdf arte.html saida.pdf`. Também importável: `from render import png, pdf`.
- `scripts/prancha.sh` — `prancha.sh saida.png a.png b.png c.png` (lado a lado, altura 800) para revisar.
- `scripts/desfocar_tela.sh` — `desfocar_tela.sh foto.jpg saida.jpg "x1,y1 x2,y2 x3,y3 x4,y4"` desfoca só o polígono (a tela do notebook) com borda suave.
- `scripts/pdf_para_png.swift` — (Mac) `swift pdf_para_png.swift doc.pdf pasta/` salva cada página do PDF como `e-1.png`, `e-2.png`… para conferir.
- `modelos/oferta_notebook.py` — anúncio "foto do notebook + caixa branca com preço + lista + botão verde".
- `modelos/foto_com_texto.py` — anúncio com foto de pessoa + degradê da marca + título + CTA (estilo agência).
- `modelos/feed_escuro.py` — post de feed 4:5 escuro, com etiqueta, título com palavra em destaque e moldura de tela.

Precisa de: Google Chrome instalado, Python 3, ImageMagick (`magick`). No Mac o Chrome fica em `/Applications/Google Chrome.app/...` (o `render.py` acha sozinho; em Linux usa `google-chrome`/`chromium`).

## Começar uma série nova (passo a passo rápido)

```bash
mkdir -p ~/projeto/artes/fotos && cd ~/projeto/artes
cp ~/.claude/skills/criar-artes/modelos/oferta_notebook.py gerador.py   # ou foto_com_texto.py / feed_escuro.py
# pôr as fotos em fotos/, trocar os textos no fim do gerador.py
python3 gerador.py
~/.claude/skills/criar-artes/scripts/prancha.sh revisar.png png/*.png
```
Depois abrir `revisar.png` com Read, passar o checklist e corrigir.
