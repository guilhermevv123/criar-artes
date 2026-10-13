# Erros que já aconteceram (e a correção)

| Erro | Correção |
|---|---|
| Texto/degradê **tampando o rosto** das pessoas | Medir onde começa a cabeça (px na arte final); degradê sólido termina ~60–140 px antes; descer a foto (`top:+Npx`) e compactar o texto |
| Logo em cima do cabelo da pessoa | Logo no topo (arte clara) ou logo abaixo do botão longe da foto |
| Bloco de texto cobrindo a **tela do notebook** | Descer a foto ~170 px e preencher o topo com a foto espelhada; botão 64 px em vez de 76; itens 32 px |
| Etiqueta/selo quebrando em 2 linhas | `white-space:nowrap` + fonte menor |
| Ilustração com elementos soltos (boneco longe da bola) | Posicionar em px até encostar; conferir na imagem |
| Cor da agência/referência copiada junto | Copiar só a estrutura; cores sempre da paleta da marca |
| Promessa que o plano não tem ("IA" no plano sem IA) | Lista e título só com o que o produto entrega |
| Preço com condição inventada | Escrever o preço exatamente como o dono mandou |
| Palavra proibida ("integradora") | Procurar no gerador antes de renderizar: `grep -i integrador gerador.py` |
| Dado de cliente legível na foto | `scripts/desfocar_tela.sh` + conferir recorte ampliado |
| `-composite` com máscara desfocando a foto inteira | Usar o método do `desfocar_tela.sh` (CopyOpacity e depois Over) |
| Vários Chrome rodando juntos → PNG em branco ou não sai | Renderizar em sequência (ou no máximo 3 em paralelo); `pkill -f "headless=new"` se travar |
| Fonte padrão no PNG (Google Fonts não carregou) | `--virtual-time-budget=10000` (o render já usa); rodar de novo |
| Escrever arquivo sem ler antes dá "modified since read" | Ler o arquivo, depois escrever |
| PDF: capa vazando para a página 2 | `@page capa{margin:0}` + `page:capa` |
| PDF: fundo some depois da 8ª página | Um JPG de fundo por página, nunca um screenshot alto |
| PDF pesado/lento | Tirar `filter`/`blur`/sombra; JPG 85% |
| `\uXXXX` virou caractere ao escrever arquivo | Escrever o caractere direto (✓, 👇) ou gerar com `chr()` em Python |
| Entregar sem olhar | SEMPRE `prancha.sh` + Read na imagem antes de mandar |
