"""MODELO · Anúncio de oferta: foto do notebook com o sistema + caixa branca com preço + lista com check + botão verde.

Copie este arquivo para a pasta do projeto, troque FOTOS/textos e rode:
    python3 oferta_notebook.py            → png/oferta-<nome>.png (1080×1920)
    python3 oferta_notebook.py 2-ia       → só uma

Origem: formato de anúncio validado ("CRM completo + IA R$197/mês · VEJA FUNCIONANDO EM 30 MIN").
A foto ideal: celular em pé, notebook na metade de baixo, fundo escuro liso (cortina/parede) na metade de cima.
Sem foto, ele monta uma cena escura em CSS só para testar.
"""
import sys
from pathlib import Path

D = Path(__file__).resolve().parent
SKILL = Path.home() / '.claude/skills/criar-artes'
sys.path.insert(0, str(SKILL / 'scripts'))
from render import pagina, png  # noqa: E402

CSS = """
.c{position:relative;width:1080px;height:1920px;overflow:hidden;background:#141618;font-family:'Plus Jakarta Sans',sans-serif}
.foto{position:absolute;left:0;width:1080px;height:1920px;object-fit:cover}
.bloco{position:absolute;left:0;right:0;display:flex;flex-direction:column;align-items:center;gap:26px}
.tit{background:#fff;border-radius:26px;padding:26px 44px 24px;text-align:center;color:#111;white-space:nowrap;font-weight:800;line-height:1.1;letter-spacing:-.02em}
.lista{display:flex;flex-direction:column;align-items:flex-start;gap:12px}
.item{display:flex;align-items:center;gap:12px;background:rgba(214,247,229,.94);border-radius:10px;padding:8px 18px 8px 10px;font-weight:700;font-size:32px;color:#0E2A1D;white-space:nowrap}
.ok{width:40px;height:40px;border-radius:9px;background:#2DBE6C;display:grid;place-items:center;color:#fff;font-size:30px;font-weight:800;line-height:1}
.cta{background:#2DBE6C;border-radius:26px;padding:18px 44px;text-align:center;color:#fff;font-weight:800;font-size:64px;line-height:1.1;white-space:nowrap}
"""


def fundo(foto, desce):
    """Foto descida `desce` px; o buraco de cima é preenchido com a mesma foto espelhada (a emenda some na cortina)."""
    if not foto or not (D / foto).exists():
        return ('<div style="position:absolute;inset:0;background:linear-gradient(170deg,#5D6064,#232527 55%,#16181A)"></div>'
                '<div style="position:absolute;left:60px;right:-200px;top:1000px;height:760px;border-radius:18px;background:#0C0D0E;padding:16px;transform:rotate(-3deg)">'
                '<div style="width:100%;height:100%;border-radius:6px;background:linear-gradient(90deg,#F4F7F5,#E6EEEA)"></div></div>')
    return (f'<img class="foto" src="{foto}" style="top:{desce - 1920}px;transform:scaleY(-1)">'
            f'<img class="foto" src="{foto}" style="top:{desce}px">')


def criativo(foto, titulo, itens, cta='VEJA FUNCIONANDO<br>EM 30 MIN 👇', tam=72, topo=150, desce=170):
    """titulo: use <br> para quebrar em 2–3 linhas. tam: diminua (64–66) se o título tiver 3 linhas ou palavra longa."""
    lista = ''.join(f'<div class="item"><span class="ok">✓</span>{t}</div>' for t in itens)
    return f'''<div class="c">{fundo(foto, desce)}
  <div class="bloco" style="top:{topo}px">
    <div class="tit" style="font-size:{tam}px">{titulo}</div>
    <div class="lista">{lista}</div>
    <div class="cta">{cta}</div>
  </div>
</div>'''


# ---- troque daqui para baixo ----
P = 'R$197/mês'
CRIATIVOS = {
    '1-financeiro': criativo('fotos/pipeline.jpg', f'CRM solar completo +<br>Financeiro {P}', [
        'Funil de vendas feito para energia solar', 'Multiatendimento WhatsApp + Instagram',
        'Proposta pela conta de luz em minutos', 'Cobrança automática no WhatsApp', 'Comissão e DRE sem planilha']),
    '2-ia': criativo('fotos/relatorios.jpg', f'CRM solar completo +<br>IA {P}', [
        'IA nativa que responde e qualifica 24 h', 'Multiatendimento WhatsApp + Instagram',
        'Painel ao vivo da sua equipe', 'Proposta pela conta de luz em minutos', 'Funil de vendas feito para energia solar']),
    '3-tudo': criativo('fotos/dashboard.jpg', f'CRM solar + Financeiro<br>+ IA + Monitoramento<br>{P}', [
        'IA nativa que responde e qualifica 24 h', 'Cobrança automática no WhatsApp',
        'Monitoramento das usinas dos seus clientes', 'Multiatendimento WhatsApp + Instagram',
        'Proposta pela conta de luz em minutos'], tam=66),
}

if __name__ == '__main__':
    for nome in sys.argv[1:] or CRIATIVOS:
        png(pagina(CSS, CRIATIVOS[nome]), D / 'png' / f'oferta-{nome}.png', 1080, 1920, base=D)
