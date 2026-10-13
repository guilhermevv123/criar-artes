"""MODELO · Anúncio com foto de pessoa + texto (estilo agência), em duas versões: ESCURA e CLARA.

    python3 foto_com_texto.py          → png/foto-escura.png e png/foto-clara.png (1080×1920)

ESCURA: foto ocupa tudo; degradê da cor escura da marca cobre só o topo (texto branco, 1 palavra neon, botão neon).
CLARA:  fundo branco com quadriculado verde no topo; a foto aparece embaixo; título grafite com 1 palavra verde.

Regra que não pode quebrar: o degradê/caixa TERMINA ANTES DO ROSTO. Meça onde começa a cabeça na foto
(em px da arte 1080×1920) e ponha o fim do degradê ~60 px acima. Se o texto não cabe, desça a foto
(top:+Npx) e/ou diminua a fonte — nunca deixe o texto em cima do rosto.
"""
import sys
from pathlib import Path

D = Path(__file__).resolve().parent
SKILL = Path.home() / '.claude/skills/criar-artes'
sys.path.insert(0, str(SKILL / 'scripts'))
from render import pagina, png  # noqa: E402

NEON, VERDE, ESCURO, GRAFITE, FUNDO = '#00E676', '#179C66', '#0B6B44', '#1E2226', '#07140F'
MARCA = (SKILL / 'assets/marca-verde.svg').as_uri()

CSS = """.c{position:relative;width:1080px;height:1920px;overflow:hidden}
.t{font-family:'Plus Jakarta Sans',sans-serif}.i{font-family:Inter,sans-serif}
.foto{position:absolute;left:0;width:1080px;height:1920px;object-fit:cover}"""


def logo(cor='#fff', tam=36):
    return (f'<span class="t" style="display:inline-flex;align-items:center;gap:14px;font-weight:800;font-size:{tam}px;'
            f'line-height:1;letter-spacing:.2em;color:{cor}"><img src="{MARCA}" style="width:{tam * 1.3:.0f}px">HELIOZ</span>')


def escura(foto, titulo, apoio, cta, desce=230, fim_degrade=640):
    """titulo: HTML com <br> e <b style="color:NEON">palavra</b>. desce: quanto a foto desce. fim_degrade: px onde o escuro acaba."""
    return f'''<div class="c" style="background:{FUNDO}">
  <img class="foto" src="{foto}" style="top:{desce}px">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,{FUNDO} 0px,{FUNDO} {fim_degrade}px,rgba(7,20,15,.75) {fim_degrade + 60}px,rgba(7,20,15,0) {fim_degrade + 140}px,rgba(7,20,15,0) 1750px,rgba(7,20,15,.4) 1920px)"></div>
  <div style="position:absolute;inset:0;background:radial-gradient(700px 480px at 50% 18%,rgba(0,230,118,.16),transparent 70%)"></div>
  <div style="position:absolute;left:0;right:0;top:70px;text-align:center;color:#fff">
    <p class="t" style="font-weight:500;font-size:70px;line-height:1.12;letter-spacing:-.02em">{titulo}</p>
    <p class="i" style="font-weight:500;font-size:34px;line-height:1.38;margin:24px auto 0;max-width:800px;color:#D3E3DB">{apoio}</p>
    <div class="t" style="margin:36px auto 0;width:620px;height:104px;border-radius:16px;background:{NEON};display:grid;place-items:center;font-weight:800;font-size:36px;color:#04100B;box-shadow:0 0 60px rgba(0,230,118,.35)">{cta}</div>
    <div style="margin-top:34px">{logo()}</div>
  </div>
</div>'''


def clara(foto, titulo, apoio, cta, desce=120, fim_branco=1000):
    return f'''<div class="c" style="background:#fff">
  <img class="foto" src="{foto}" style="top:{desce}px">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,#fff 0px,#fff {fim_branco}px,rgba(255,255,255,0) {fim_branco + 90}px)"></div>
  <div style="position:absolute;inset:0;background-image:linear-gradient(#E3EEE8 2px,transparent 2px),linear-gradient(90deg,#E3EEE8 2px,transparent 2px);background-size:120px 120px;-webkit-mask-image:linear-gradient(180deg,#000 0px,#000 {fim_branco - 20}px,transparent {fim_branco + 60}px)"></div>
  <div style="position:absolute;left:170px;top:84px">{logo(GRAFITE, 38)}</div>
  <div style="position:absolute;left:170px;right:110px;top:200px;color:{GRAFITE}">
    <p class="t" style="font-weight:600;font-size:94px;line-height:1.1;letter-spacing:-.03em">{titulo}</p>
    <p class="i" style="font-size:42px;line-height:1.32;margin-top:28px;color:#3C4A43">{apoio}</p>
    <div class="t" style="margin-top:46px;width:730px;height:132px;border-radius:18px;background:linear-gradient(90deg,{VERDE},{ESCURO});display:flex;align-items:center;justify-content:center;gap:22px;font-weight:800;font-size:44px;color:#fff">{cta} <span style="font-size:52px">↘</span></div>
  </div>
</div>'''


# ---- troque daqui para baixo (as fotos ficam em fotos/ ao lado deste arquivo) ----
ARTES = {
    'foto-escura': escura('fotos/tecnico.jpg',
                          f'<b style="font-weight:800">Usina solar</b><br>sem monitoramento<br>pode <b style="font-weight:800;color:{NEON}">parar</b> sem<br><b style="font-weight:800">você saber</b>',
                          'Tenha alertas, geração em tempo real e o app do cliente direto no celular.',
                          'Fale com um especialista'),
    'foto-clara': clara('fotos/cliente-dormindo.jpg',
                        f'<b style="font-weight:800">Sua proposta</b> é<br><b style="font-weight:800;color:{VERDE}">lenta</b> e seus <b style="font-weight:800">clientes</b><br><b style="font-weight:800">sentem isso…</b>',
                        f'Com a <b style="font-weight:700;color:{ESCURO}">Helioz</b>,<br>a proposta sai pela conta de luz,<br>com a sua marca e em minutos.',
                        'Quero conhecer'),
}

if __name__ == '__main__':
    for nome in sys.argv[1:] or ARTES:
        png(pagina(CSS, ARTES[nome]), D / 'png' / f'{nome}.png', 1080, 1920, base=D)
