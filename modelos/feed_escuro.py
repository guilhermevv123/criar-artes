"""MODELO · Post de feed 4:5 (1080×1350) escuro "tech": céu verde-escuro com brilho, chão quadriculado em perspectiva,
etiqueta, título com palavra em serifa itálica neon, apoio, captura da tela em moldura, rodapé com CTA.

    python3 feed_escuro.py          → png/feed-<nome>.png

É o visual que mais parece "empresa de tecnologia". Uma série inteira usa a mesma moldura (topo e rodapé fixos)
e muda só a cor de destaque (--c) por assunto: neon (geral), #60A5FA (financeiro), #A78BFA (IA/automação),
#FBBF24 (monitoramento), #F87171 (dor/problema).
As telas do exemplo (fotos/tela-*.jpg) são capturas do sistema; na Helioz ficam em ~/helioz-marketing/proposta-comercial/img/.
"""
import sys
from pathlib import Path

D = Path(__file__).resolve().parent
SKILL = Path.home() / '.claude/skills/criar-artes'
sys.path.insert(0, str(SKILL / 'scripts'))
from render import pagina, png  # noqa: E402

MARCA = (SKILL / 'assets/marca-verde.svg').as_uri()

CSS = """
:root{--neon:#00E676;--branco:#F2F7F4;--suave:#A9BDB4;--apagado:#6F857B;--titulo:'Plus Jakarta Sans',Inter,sans-serif;--serifa:'Instrument Serif',Georgia,serif}
body{background:#08130F;font-family:Inter,sans-serif;color:var(--branco)}
.post{width:1080px;height:1350px;position:relative;overflow:hidden;background:#08130F;--c:var(--neon)}
.ceu{position:absolute;inset:0;background:radial-gradient(760px 520px at 88% 4%,color-mix(in srgb,var(--c) 26%,transparent),transparent 65%),
  radial-gradient(900px 640px at -10% 104%,rgba(23,156,102,.32),transparent 60%),linear-gradient(165deg,#0E211A 0%,#0A1712 55%,#06100C 100%)}
.chao{position:absolute;left:-40%;right:-40%;bottom:-70%;height:110%;
  background-image:linear-gradient(rgba(150,255,210,.22) 3px,transparent 3px),linear-gradient(90deg,rgba(150,255,210,.22) 3px,transparent 3px),linear-gradient(180deg,#0F3B4A,#082029);
  background-size:130px 80px,130px 80px,100% 100%;transform:perspective(560px) rotateX(64deg);transform-origin:50% 0;opacity:.55;
  -webkit-mask-image:linear-gradient(180deg,transparent 0%,rgba(0,0,0,.6) 18%,#000 45%)}
.topo{position:absolute;left:84px;right:84px;top:60px;display:flex;justify-content:space-between;align-items:center;font:800 22px/1 var(--titulo);letter-spacing:.2em}
.topo .eu{display:flex;align-items:center;gap:14px}.topo .eu img{width:40px}
.topo .serie{font:700 17px/1 var(--titulo);letter-spacing:.18em;text-transform:uppercase;color:var(--suave);border:1px solid rgba(255,255,255,.16);border-radius:99px;padding:11px 18px}
.conteudo{position:absolute;inset:0;padding:150px 84px}
.etq{display:inline-flex;align-items:center;gap:14px;font:800 20px/1 var(--titulo);letter-spacing:.2em;text-transform:uppercase;color:var(--c)}
.etq::before{content:"";width:44px;height:4px;border-radius:4px;background:var(--c)}
h1{font:800 84px/1.02 var(--titulo);letter-spacing:-.035em;margin-top:28px}
h1 em{font:400 italic 96px/1 var(--serifa);color:var(--c)}
.sub{font-size:31px;line-height:1.45;color:var(--suave);margin-top:26px}.sub b{color:var(--branco)}
.moldura{position:absolute;border-radius:26px;padding:12px;background:linear-gradient(160deg,#16261F,#0B1511);border:1px solid rgba(255,255,255,.14);
  box-shadow:0 50px 100px rgba(0,0,0,.6),0 0 90px color-mix(in srgb,var(--c) 18%,transparent)}
.moldura img{display:block;width:100%;border-radius:16px}
.base{position:absolute;z-index:2;left:84px;right:84px;bottom:60px;display:flex;justify-content:space-between;align-items:center;font:600 19px/1 var(--titulo);color:var(--suave)}
.base b{color:var(--branco)}
.cta{display:flex;align-items:center;gap:10px;background:var(--c);color:#04100B;border-radius:99px;padding:14px 22px;font:800 19px/1 var(--titulo)}
"""


def post(etiqueta, titulo, apoio, tela=None, cor='var(--neon)', serie='Helioz · Série'):
    """titulo: use <em>palavra</em> para o destaque em serifa itálica. tela: captura do sistema (png/jpg) — opcional."""
    moldura = (f'<div class="moldura" style="left:330px;right:-100px;top:620px"><img src="{tela}"></div>' if tela else '')
    return f'''<div class="post" style="--c:{cor}"><div class="ceu"></div><div class="chao"></div>
  <div class="topo"><span class="eu"><img src="{MARCA}">HELIOZ</span><span class="serie">{serie}</span></div>
  <div class="conteudo"><span class="etq">{etiqueta}</span><h1>{titulo}</h1><p class="sub">{apoio}</p></div>
  {moldura}
  <div class="base"><span>Arraste para o lado · <b>helioz.com.br</b></span><span class="cta">Fale com a gente →</span></div>
</div>'''


# ---- troque daqui para baixo ----
POSTS = {
    '01-ampliacao': post('Pós-venda', '70% das ampliações<br>vão para <em>outro</em><br>instalador.',
                         'Seu cliente quer mais placas e <b>nem lembra de você</b>. A Helioz avisa quando é hora de oferecer.',
                         tela='fotos/tela-monitoramento.jpg', cor='#FBBF24'),
    '02-cobranca': post('Financeiro', 'Inadimplência não<br>se resolve com <em>coragem</em>.',
                        'A cobrança sai sozinha no <b>WhatsApp e no e-mail</b>, no dia certo, sem constrangimento.',
                        tela='fotos/tela-financeiro.jpg', cor='#60A5FA'),
}

if __name__ == '__main__':
    for nome in sys.argv[1:] or POSTS:
        png(pagina(CSS, POSTS[nome]), D / 'png' / f'feed-{nome}.png', 1080, 1350, base=D)
