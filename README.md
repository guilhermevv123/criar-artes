# criar-artes · skill do Claude Code

Faz o Claude Code criar **artes de marketing prontas para postar**: criativos de anúncio (story 9:16 e feed 4:5), posts, carrosséis, ofertas com preço, artes com foto de pessoa ou do sistema e PDFs A4. Ele escreve a arte em HTML/CSS, gera a imagem pelo Chrome, **olha o resultado e corrige** antes de entregar.

Já vem com a identidade da **Helioz** (verde) e ensina a montar a de outra marca.

![O que os modelos geram](exemplos/modelos.jpg)

## Instalar

```bash
git clone https://github.com/guilhermevv123/criar-artes.git ~/.claude/skills/criar-artes
```

Depois abra uma conversa nova no Claude Code. Para atualizar: `git -C ~/.claude/skills/criar-artes pull`.

Precisa de: **Google Chrome**, **Python 3** e **ImageMagick** (`brew install imagemagick`).

## Usar

É só pedir em português, por exemplo:

- "Faça 6 variações de story *CRM solar completo + IA R$197/mês* com estas fotos do notebook."
- "Crie criativos o mais parecido possível com este aqui, mas com a nossa identidade verde."
- "Uma série de 5 posts de feed escuros sobre inadimplência, com copy provocativa."
- "Transforme este texto num PDF A4 em pé, com capa escura e tabelas."

## O que tem aqui

| Pasta | Conteúdo |
|---|---|
| `SKILL.md` | O passo a passo, o checklist de cada arte e as regras de visual |
| `referencias/` | Formatos e receitas com medidas, marcas, copy, fotos, PDF e erros comuns |
| `modelos/` | Geradores prontos: oferta com notebook, foto com texto (escura e clara), feed escuro |
| `scripts/` | `render.py` (HTML → PNG/PDF), `prancha.sh` (revisar lado a lado), `desfocar_tela.sh` (esconder dado de cliente), `pdf_para_png.swift` |
| `assets/` | Símbolo da Helioz em verde e branco |

Gerar foto de pessoa pela Higgsfield e usar as capturas do sistema da Helioz dependem de pastas e chaves que não estão neste repositório; sem elas, a skill funciona com as fotos que você mandar.
