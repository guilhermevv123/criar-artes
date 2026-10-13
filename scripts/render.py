#!/usr/bin/env python3
"""Renderiza HTML em PNG ou PDF com o Chrome headless.

Linha de comando:
    python3 render.py arte.html saida.png 1080 1920
    python3 render.py --pdf documento.html saida.pdf

Dentro de outro script:
    import sys; sys.path.insert(0, '<pasta da skill>/scripts')
    from render import png, pdf, pagina
    png(pagina(css, corpo), 'png/arte-1.png', 1080, 1920, base=Path(__file__).parent)

`pagina()` monta o documento completo; `base` é a pasta de onde saem as imagens relativas (fotos/...).
"""
import os, shutil, subprocess, sys, tempfile, time
from pathlib import Path

CANDIDATOS = [
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Chromium.app/Contents/MacOS/Chromium',
    shutil.which('google-chrome') or '', shutil.which('chromium') or '', shutil.which('chromium-browser') or '',
]
CHROME = os.environ.get('CHROME') or next((c for c in CANDIDATOS if c and Path(c).exists()), None)

FONTES = ("@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800"
          "&family=Inter:wght@400;500;600;700&family=Instrument+Serif:ital@1&display=swap');")


def pagina(css, corpo, fontes=True):
    return (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{FONTES if fontes else ""}'
            f'*{{box-sizing:border-box;margin:0;padding:0}}body{{overflow:hidden}}{css}</style></head><body>{corpo}</body></html>')


def _html_temporario(html, base):
    base = Path(base or Path.cwd())
    tmp = base / f'.render-{os.getpid()}-{time.time_ns()}.html'
    tmp.write_text(html, encoding='utf-8')
    return tmp


def png(html_ou_arquivo, saida, w, h, base=None, espera=10000):
    """Salva um PNG w×h. Aceita o HTML em texto ou o caminho de um .html."""
    if not CHROME:
        sys.exit('Chrome não encontrado: instale o Google Chrome ou defina CHROME=/caminho/do/chrome')
    saida = Path(saida).resolve()
    saida.parent.mkdir(parents=True, exist_ok=True)
    saida.unlink(missing_ok=True)
    arq = Path(html_ou_arquivo) if str(html_ou_arquivo).endswith('.html') and Path(html_ou_arquivo).exists() else None
    tmp = None if arq else _html_temporario(html_ou_arquivo, base)
    alvo = (arq or tmp).resolve().as_uri()
    p = subprocess.Popen([CHROME, '--headless=new', '--disable-gpu', f'--user-data-dir={tempfile.mkdtemp(prefix="arte-")}',
                          '--hide-scrollbars', '--force-device-scale-factor=1', f'--window-size={w},{h}',
                          f'--virtual-time-budget={espera}', '--run-all-compositor-stages-before-draw',
                          f'--screenshot={saida}', alvo], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    fim = time.time() + 90
    while time.time() < fim and p.poll() is None and not saida.exists():
        time.sleep(.4)
    time.sleep(1)  # o Chrome às vezes termina de gravar depois de criar o arquivo
    if p.poll() is None:
        p.terminate()
    if tmp:
        tmp.unlink(missing_ok=True)
    if not saida.exists():
        sys.exit(f'falhou: {saida.name} (rode de novo; se repetir, feche outros Chrome headless: pkill -f "headless=new")')
    print('ok', saida.name)
    return saida


def pdf(html_ou_arquivo, saida, base=None, espera=10000):
    """Salva um PDF. O tamanho da página vem do CSS: @page{size:A4;margin:...}."""
    saida = Path(saida).resolve()
    saida.unlink(missing_ok=True)
    arq = Path(html_ou_arquivo) if str(html_ou_arquivo).endswith('.html') and Path(html_ou_arquivo).exists() else None
    tmp = None if arq else _html_temporario(html_ou_arquivo, base)
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={saida}',
                    f'--virtual-time-budget={espera}', (arq or tmp).resolve().as_uri()], capture_output=True, timeout=180)
    if tmp:
        tmp.unlink(missing_ok=True)
    print('ok', saida.name, f'{saida.stat().st_size // 1024} KB')
    return saida


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['--pdf'] and len(a) == 3:
        pdf(a[1], a[2])
    elif len(a) == 4:
        png(a[0], a[1], int(a[2]), int(a[3]))
    else:
        sys.exit(__doc__)
