# Marcas

Toda arte usa UM perfil de marca. Nunca inventar cor fora da paleta; quando faltar uma cor, use transparência da cor da marca.

## Helioz (padrão)

Software para empresas de energia solar (CRM + IA + Financeiro + Monitoramento). Site helioz.com.br.

| Papel | Cor | Uso |
|---|---|---|
| Grafite | `#1E2226` | texto escuro, fundos escuros neutros, menu |
| Verde | `#179C66` | cor principal no fundo claro, botões, destaques no claro |
| Verde-escuro | `#0B6B44` | títulos em fundo claro, degradê de botão (Verde → Verde-escuro) |
| Neon | `#00E676` | destaque no fundo escuro (1–2 palavras), botão no escuro, brilho |
| Menta | `#45C98F` | detalhes, ilustração |
| Fundo escuro | `#07140F` / `#08130F` / `#0B3D2B` | fundos de arte escura, degradês sobre foto |
| Faixa clara de lista | `rgba(214,247,229,.94)` com texto `#0E2A1D` | itens com check |
| Verde do check/CTA de anúncio | `#2DBE6C` | quadradinho do ✓ e botão "VEJA FUNCIONANDO" |
| Cinza de apoio | `#5B6670` (claro) · `#A9BDB4` (escuro) | texto secundário |

Cores por assunto (feed escuro): geral neon `#00E676` · Financeiro `#60A5FA` · IA/automação `#A78BFA` · Monitoramento `#FBBF24` · Dor/problema `#F87171`.

**Fontes**: Plus Jakarta Sans (títulos, botões, etiquetas — pesos 700/800) · Inter (texto corrido — 400/500/600) · Instrument Serif itálico (1 palavra de destaque no feed escuro). Todas via Google Fonts (`render.py` já importa).

**Logo**: `assets/marca-verde.svg` (símbolo verde, usar em fundo escuro e claro) e `assets/marca-branca.svg`. Escrito ao lado: "HELIOZ" em Plus Jakarta 800, `letter-spacing:.2em`. Tamanho 34–42 px de altura de letra. Sempre pequeno.

**Nomes dos produtos**: Helioz CRM · Helioz Flow (automação/IA) · Helioz Financeiro · Helioz Monitoramento · app do cliente.

**Palavras**: NUNCA "integradora" (escrever "sua empresa", "empresa de energia solar", "dono de empresa solar"). Público = dono de empresa de energia solar com 3 a 15 vendedores.

**Capturas reais do sistema** (vitrine, dados de exemplo — podem ir para anúncio): `~/helioz-marketing/proposta-comercial/img/*.jpg` (negocios, conversas, flow-fluxos, fin-regua, mon-painel, mon-usina, propostas, instalacoes, cel-cliente…). Fotos do dono com o notebook: `~/helioz-marketing/criativos-oferta/fotos/` (já com a tela desfocada onde tinha dado de cliente).

**Exemplos prontos para copiar o estilo**:
- `~/helioz-marketing/criativos-oferta/oferta.py` — 8 variações de oferta com notebook.
- `~/helioz-marketing/criativos-agencia/criativos.py` — 5 criativos com foto de pessoa (estilo agência) + ilustração em HTML (bola morro acima).
- `~/helioz-marketing/instagram/feed-escuro/feed.py` — série de feed escura com celular, cartões de vidro, logos dos apps.
- `~/helioz-marketing/estrategias-oficiais/gerar.py` e `~/helioz-marketing/icp-e-planos/gerar.py` — PDFs A4 em pé.

## Como montar o perfil de outra marca

Pergunte (ou tire do site/Instagram da marca) e escreva uma seção igual à da Helioz:
1. **3 cores**: uma escura (fundo/texto), uma principal (botão), uma de destaque que brilha no escuro. Teste o contraste: texto branco na escura e texto escuro na clara.
2. **2 fontes** do Google Fonts: uma forte para título (Plus Jakarta, Montserrat, Poppins, Sora, Space Grotesk) e uma neutra para texto (Inter, DM Sans).
3. **Logo** em SVG ou PNG transparente.
4. **Palavras proibidas e obrigatórias** (como o "integradora" da Helioz).
5. **Público** em uma frase e o **CTA padrão**.
Troque as constantes no topo do gerador (`NEON, VERDE, ESCURO, GRAFITE, FUNDO`, `MARCA`) — o resto do modelo continua igual.
