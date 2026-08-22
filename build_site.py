# -*- coding: utf-8 -*-
"""Genera index.html de la biblioteca de predicas CCLD para GitHub Pages."""
import io, unicodedata

MESES = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
ABREV = ["", "Ene", "Feb", "Mar", "Abr", "May", "Jun",
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

# (año, mes, día, predicador, subtítulo, pasaje, driveId)
PREDICAS = [
    (2026, 8, 16, "Felipe Burgos", "Prédica del domingo", "", "1pt47t09SKluNjx35q2HRkB-kIvRCSv_D"),
    (2026, 8, 9, "Felipe Burgos", "Prédica del domingo", "", "1R1IsklCv5JooQlRsFZPvd_MZ6aYirJ9z"),
    (2026, 8, 2, "Mariel Álvarez", "Pidan, busquen, llamen", "Mateo 7:7-12", "15WjDVrXGr_u9PCt8TyMZEbY-3ds2UX_5"),
    (2026, 7, 26, "Felipe Burgos", "Prédica del domingo", "", "1xA9r61xYPGGpxxcB1x5nqR0IU5-gz9Ux"),
    (2026, 7, 19, "Cliff", "Prédica del domingo", "", "16kIZ-iAGUQgsm1P1_9kVHfHGnGzPT_TW"),
    (2026, 7, 12, "Felipe Burgos", "Prédica del domingo", "", "1pQOScYwhnKmTaMN3ZHWJoUAScD8JZY3Y"),
    (2026, 7, 5, "Felipe Burgos", "Prédica del domingo", "", "1-Tox29rwlf5B_qX6r8SGqBqTB0vxFWhQ"),
    (2026, 6, 28, "Álvaro", "Prédica del domingo", "", "1oll4BM65001jUiRge4vXVu2kGBX7-iP-"),
    (2026, 6, 21, "Felipe Burgos", "Prédica del domingo", "", "1vNWUlKZSpKk4-WPJwEWf6ePUruySjMFK"),
    (2026, 6, 14, "Felipe Burgos", "Prédica del domingo", "", "1EzX3kcVokEMdXVyXGgPLyX9YvxJZSw8U"),
    (2026, 5, 31, "Cliff", "Prédica del domingo", "", "1EUM5f-C1wM1d_zsEXhBTHRAwHn1v_Elc"),
    (2026, 5, 24, "Felipe Burgos", "Prédica del domingo", "", "16y--EltdTEXxazt_gz2Q9fWMwRGwrGrd"),
    (2026, 5, 17, "Felipe Burgos", "Prédica del domingo", "", "1wm5Bc5PLZ-MxKAcqy5pWU6cWksQo5CRw"),
    (2026, 5, 10, "Felipe Burgos", "Prédica del domingo", "", "1Xuw80cTNq-_hZH5nnk67hOgrJB3x3Huq"),
    (2026, 4, 19, "Juan Carlos", "Prédica del domingo", "", "17NxDrn5dYfu2L9WLZ2lph0PjQmm-7jJl"),
    (2026, 3, 29, "Felipe Burgos", "Prédica del domingo", "", "1UjTkKxAfeAyxCv6AjEocD_hNvBX7IBBP"),
    (2026, 3, 22, "Mariel Álvarez", "Prédica del domingo", "", "1z6_474hPoHGiO_XN60-fcdRSOsGlWL6Z"),
    (2026, 3, 15, "Felipe Burgos", "Prédica del domingo", "", "1kHelfhBmMgsy3n9QCbxtLizcWGxeFY-m"),
    (2026, 1, 25, "El fruto de la fe que se ve", "Predicador por confirmar", "", "1te2oFaR3B4B8-zB-b_UqRnih9hCk1dPX"),
    (2025, 12, 28, "Felipe Burgos", "Prédica del domingo", "", "1F_fYs8vjLAZKMc1dfjQL_nUhcftRqVww"),
    (2025, 10, 19, "Felipe Burgos", "Segunda parte", "", "1OYjbakjoi8n2EPo-6zdmijx0BDtLtIuI"),
    (2025, 10, 19, "Felipe Burgos", "Primera parte — estreno de la locación nueva", "", "1R9_TTsWQj3nrojTByRnZsiSC261ugZNk"),
    (2025, 10, 4, "Hugo", "Prédica", "", "1wl1SpsqzNg6hpcWif2E2J4Mjakoi6oBM"),
    (2025, 9, 28, "Felipe Burgos", "Prédica del domingo", "", "1_fx_go3EeBrK6cN-NxOZLqroCtAuhJye"),
    (2025, 9, 21, "Cliff", "Prédica del domingo", "Juan 6:1-40", "1KasmolJNWCkiBKCY5CwSruALpSpme3nh"),
    (2025, 7, 20, "Felipe Burgos", "Prédica del domingo", "", "1PErA0BaaGHNen1zOcMIck-uIQYnAAr3-"),
    (2025, 7, 13, "Felipe Burgos", "Prédica del domingo", "", "1wdMPe-F4cywGjtfsSh0DgkVyPK8dmCK-"),
    (2025, 7, 5, "Cristián", "Prédica", "", "1YtT-ZKF4capWkZXGSQBDj85IRgchkWyY"),
    (2025, 6, 29, "Felipe Burgos", "Prédica del domingo", "", "1jzE_PtVolrkzJVDcz5o__eZIX7fZId2f"),
]

PREDICADORES = ["Felipe Burgos", "Cliff", "Mariel Álvarez", "Álvaro", "Juan Carlos", "Cristián", "Hugo"]


def sinacento(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn").lower()


def item_html(p):
    y, m, d, quien, sub, pasaje, fid = p
    es_predicador = quien in PREDICADORES
    dp = quien if es_predicador else ""
    busca = " ".join([sinacento(quien), sinacento(sub), sinacento(pasaje),
                      MESES[m].lower(), str(y), "%02d-%02d-%d" % (d, m, y)])
    pasaje_html = ('\n            <span class="passage">%s</span>' % pasaje) if pasaje else ""
    return """        <li class="item" data-p="%s" data-s="%s">
          <div class="row">
            <div class="day"><span class="n">%02d</span><span class="d">%s</span></div>
            <div class="item-body">
              <h4>%s</h4>
              <p class="sub">%s</p>%s
            </div>
            <button class="play play--ghost" type="button" data-id="%s" aria-expanded="false">
              <svg class="ico-play" width="11" height="13" viewBox="0 0 13 15" aria-hidden="true"><path d="M0 0l13 7.5L0 15z" fill="currentColor"></path></svg>
              <span class="play-label">Escuchar</span>
            </button>
          </div>
          <div class="player" hidden></div>
        </li>""" % (dp, busca, d, ABREV[m], quien, sub, pasaje_html, fid)


def build():
    bloques = []
    actual = None
    buf = []
    for p in PREDICAS:
        key = (p[0], p[1])
        if key != actual:
            if buf:
                bloques.append((actual, buf))
            actual = key
            buf = []
        buf.append(item_html(p))
    if buf:
        bloques.append((actual, buf))

    secciones = []
    for (y, m), items in bloques:
        secciones.append(
            '    <section class="month">\n      <h3>%s %d</h3>\n      <ul class="list">\n%s\n      </ul>\n    </section>'
            % (MESES[m], y, "\n".join(items)))

    chips = ['        <button class="chip" type="button" data-p="all" aria-pressed="true">Todos</button>']
    for nombre in PREDICADORES:
        chips.append('        <button class="chip" type="button" data-p="%s" aria-pressed="false">%s</button>'
                     % (nombre, nombre))

    html = PLANTILLA.replace("{{SECCIONES}}", "\n\n".join(secciones))
    html = html.replace("{{CHIPS}}", "\n".join(chips))
    html = html.replace("{{TOTAL}}", str(len(PREDICAS)))
    return html


PLANTILLA = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Prédicas — Comunidad Cristiana La Dehesa</title>
<meta name="description" content="Biblioteca de prédicas de la Comunidad Cristiana La Dehesa. Escucha o descarga las prédicas de cada domingo.">
<meta property="og:title" content="Prédicas — Comunidad Cristiana La Dehesa">
<meta property="og:description" content="Escucha las prédicas de cada domingo.">
<meta property="og:type" content="website">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 460 710'%3E%3Crect x='13' y='15' width='190' height='248' fill='%234D5A2F'/%3E%3Crect x='250' y='133' width='155' height='130' fill='%23A9551E'/%3E%3Crect x='87' y='315' width='113' height='265' fill='%23661E24'/%3E%3Crect x='250' y='315' width='205' height='380' fill='%23495459'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap">
<style>
  :root {
    --ground:#F1F2EE; --surface:#FFFFFF; --surface-alt:#E9EBE4;
    --ink:#1C2124; --ink-soft:#5B6266; --ink-faint:#868D8F;
    --line:#D7DAD2; --line-strong:#BFC3B9;
    --olive:#4D5A2F; --orange:#A9551E; --garnet:#661E24; --slate:#495459;
    --accent:var(--orange); --accent-ink:#FFFFFF; --focus:#1C2124;
    --shadow:0 1px 2px rgba(28,33,36,.05), 0 6px 20px -12px rgba(28,33,36,.28);
    --measure:62ch; --wrap:940px;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --ground:#171B1C; --surface:#1F2426; --surface-alt:#262C2E;
      --ink:#E7E9E4; --ink-soft:#A0A8AA; --ink-faint:#7D8587;
      --line:#2F3537; --line-strong:#414849;
      --olive:#97AC63; --orange:#E08B45; --garnet:#C4626A; --slate:#93A0A5;
      --accent:var(--orange); --accent-ink:#171B1C; --focus:#E7E9E4;
      --shadow:0 1px 2px rgba(0,0,0,.4), 0 6px 20px -12px rgba(0,0,0,.7);
    }
  }
  :root[data-theme="dark"] {
    --ground:#171B1C; --surface:#1F2426; --surface-alt:#262C2E;
    --ink:#E7E9E4; --ink-soft:#A0A8AA; --ink-faint:#7D8587;
    --line:#2F3537; --line-strong:#414849;
    --olive:#97AC63; --orange:#E08B45; --garnet:#C4626A; --slate:#93A0A5;
    --accent:var(--orange); --accent-ink:#171B1C; --focus:#E7E9E4;
    --shadow:0 1px 2px rgba(0,0,0,.4), 0 6px 20px -12px rgba(0,0,0,.7);
  }

  *{box-sizing:border-box}
  html{-webkit-text-size-adjust:100%}
  body{
    margin:0; background:var(--ground); color:var(--ink);
    font-family:"Source Serif 4",Georgia,"Times New Roman",serif;
    font-size:17px; line-height:1.6; -webkit-font-smoothing:antialiased;
  }
  .wrap{max-width:var(--wrap); margin:0 auto; padding:0 24px}
  a{color:inherit}
  :focus-visible{outline:2px solid var(--focus); outline-offset:3px; border-radius:2px}

  .masthead{border-bottom:1px solid var(--line); background:var(--surface)}
  .masthead-inner{display:flex; align-items:center; gap:20px; padding:26px 24px; max-width:var(--wrap); margin:0 auto}
  .mark{flex:none; width:34px; height:auto; display:block}
  .masthead h1{margin:0; font-family:Archivo,"Helvetica Neue",Arial,sans-serif; font-weight:700; font-size:1.02rem; letter-spacing:.015em; line-height:1.25}
  .masthead p{margin:2px 0 0; font-family:Archivo,"Helvetica Neue",Arial,sans-serif; font-size:.68rem; font-weight:500; letter-spacing:.14em; text-transform:uppercase; color:var(--ink-faint)}

  .hero{padding:60px 0 44px}
  .eyebrow{font-family:Archivo,"Helvetica Neue",Arial,sans-serif; font-size:.68rem; font-weight:600; letter-spacing:.16em; text-transform:uppercase; color:var(--accent); margin:0 0 18px}
  .hero h2{font-family:Archivo,"Helvetica Neue",Arial,sans-serif; font-weight:700; font-size:clamp(2.1rem,6.5vw,3.4rem); line-height:1.04; letter-spacing:-.022em; text-wrap:balance; margin:0 0 20px; max-width:15ch}
  .hero .lede{margin:0; max-width:var(--measure); font-size:1.09rem; color:var(--ink-soft)}

  .controls{margin:16px 0 0; padding:22px 0 20px; border-top:1px solid var(--line); border-bottom:1px solid var(--line); display:flex; flex-wrap:wrap; gap:18px 24px; align-items:center}
  .search{flex:1 1 240px; min-width:0; font:inherit; font-size:.95rem; color:var(--ink); background:var(--surface); border:1px solid var(--line-strong); border-radius:2px; padding:10px 14px}
  .search::placeholder{color:var(--ink-faint)}
  .chips{display:flex; flex-wrap:wrap; gap:8px}
  .chip{font-family:Archivo,"Helvetica Neue",Arial,sans-serif; font-size:.76rem; font-weight:500; letter-spacing:.02em; padding:7px 13px; border-radius:999px; border:1px solid var(--line-strong); background:transparent; color:var(--ink-soft); cursor:pointer; transition:background .12s ease,color .12s ease,border-color .12s ease}
  .chip:hover{border-color:var(--slate); color:var(--ink)}
  .chip[aria-pressed="true"]{background:var(--slate); border-color:var(--slate); color:var(--ground)}

  .archive{padding:8px 0 40px}
  .month{margin:40px 0 0}
  .month > h3{font-family:Archivo,"Helvetica Neue",Arial,sans-serif; font-size:.7rem; font-weight:600; letter-spacing:.17em; text-transform:uppercase; color:var(--ink-faint); margin:0 0 14px; padding-bottom:10px; border-bottom:1px solid var(--line)}
  .list{list-style:none; margin:0; padding:0}
  .item{border-bottom:1px solid var(--line)}
  .item:last-child{border-bottom:none}
  .row{display:flex; align-items:center; flex-wrap:wrap; gap:14px 20px; padding:18px 0}

  .day{flex:none; width:52px; text-align:center; font-family:Archivo,"Helvetica Neue",Arial,sans-serif; font-variant-numeric:tabular-nums; line-height:1}
  .day .n{display:block; font-size:1.5rem; font-weight:700; letter-spacing:-.02em}
  .day .d{display:block; margin-top:5px; font-size:.6rem; font-weight:600; letter-spacing:.12em; text-transform:uppercase; color:var(--ink-faint)}

  .item-body{flex:1 1 240px; min-width:0}
  .item-body h4{font-family:Archivo,"Helvetica Neue",Arial,sans-serif; font-weight:600; font-size:1.02rem; letter-spacing:-.005em; margin:0; line-height:1.3}
  .item-body .sub{margin:3px 0 0; font-size:.93rem; color:var(--ink-soft)}
  .passage{display:inline-block; margin-top:5px; font-family:Archivo,"Helvetica Neue",Arial,sans-serif; font-size:.68rem; font-weight:600; letter-spacing:.07em; text-transform:uppercase; color:var(--olive); border:1px solid var(--olive); border-radius:2px; padding:3px 8px}

  .play{display:inline-flex; align-items:center; gap:10px; flex:none; padding:9px 16px 9px 13px; background:transparent; color:var(--ink); border:1px solid var(--line-strong); border-radius:2px; font-family:Archivo,"Helvetica Neue",Arial,sans-serif; font-size:.8rem; font-weight:600; letter-spacing:.02em; cursor:pointer; transition:border-color .12s ease,color .12s ease}
  .play:hover{border-color:var(--accent); color:var(--accent)}
  .play[aria-expanded="true"]{background:var(--accent); border-color:var(--accent); color:var(--accent-ink)}
  .play svg{display:block}

  .player{padding:0 0 20px}
  .player iframe{width:100%; height:80px; border:0; border-radius:3px; background:var(--surface-alt); display:block}
  .player .alt{margin:8px 0 0; font-size:.85rem; color:var(--ink-faint)}
  .player .alt a{color:var(--accent)}

  .empty{display:none; padding:48px 0; color:var(--ink-soft); font-size:1.02rem}
  .empty.on{display:block}

  .notice{margin:56px 0 0; padding:20px 24px; background:var(--surface-alt); border-radius:3px; font-size:.95rem; color:var(--ink-soft); max-width:var(--measure)}
  .notice strong{color:var(--ink); font-weight:600}

  footer{margin-top:72px; border-top:1px solid var(--line); padding:30px 0 60px; font-family:Archivo,"Helvetica Neue",Arial,sans-serif; font-size:.74rem; letter-spacing:.06em; text-transform:uppercase; color:var(--ink-faint); display:flex; flex-wrap:wrap; gap:8px 18px; justify-content:space-between}

  @media (prefers-reduced-motion: reduce){*{transition:none !important; animation:none !important}}
  @media (max-width:560px){
    .hero{padding:44px 0 32px}
    .day{width:44px}
    .day .n{font-size:1.3rem}
  }
</style>
</head>
<body>

<header class="masthead">
  <div class="masthead-inner">
    <svg class="mark" viewBox="0 0 460 710" role="img" aria-label="Comunidad Cristiana La Dehesa">
      <rect x="13" y="15" width="190" height="248" fill="#4D5A2F"></rect>
      <rect x="250" y="133" width="155" height="130" fill="#A9551E"></rect>
      <rect x="87" y="315" width="113" height="265" fill="#661E24"></rect>
      <rect x="250" y="315" width="205" height="380" fill="#495459"></rect>
    </svg>
    <div>
      <h1>Comunidad Cristiana La Dehesa</h1>
      <p>Biblioteca de prédicas</p>
    </div>
  </div>
</header>

<main class="wrap">

  <section class="hero">
    <p class="eyebrow">Junio 2025 — Agosto 2026 · {{TOTAL}} prédicas</p>
    <h2>La Palabra que hemos escuchado juntos</h2>
    <p class="lede">Cada domingo queda grabado. Aquí están las prédicas de la comunidad, ordenadas por fecha, para volver a escucharlas cuando quieras — en el auto, caminando, o para compartirle una a alguien que la necesite.</p>
  </section>

  <section class="controls" aria-label="Filtros">
    <input class="search" id="q" type="search" placeholder="Buscar por predicador, fecha o pasaje…" aria-label="Buscar prédicas">
    <div class="chips" id="chips" role="group" aria-label="Filtrar por predicador">
{{CHIPS}}
    </div>
  </section>

  <div class="archive" id="archive">

{{SECCIONES}}

    <p class="empty" id="empty">No hay prédicas que coincidan con esa búsqueda. Prueba con otro nombre o quita los filtros.</p>
  </div>

  <p class="notice"><strong>El audio se reproduce aquí mismo</strong> al tocar “Escuchar”. Si prefieres descargarlo para escucharlo sin internet, usa el enlace “Abrir en Drive” que aparece bajo el reproductor.</p>

  <footer>
    <span>Comunidad Cristiana La Dehesa</span>
    <span>{{TOTAL}} prédicas · Junio 2025 — Agosto 2026</span>
  </footer>

</main>

<script>
(function () {
  var q       = document.getElementById('q');
  var chips   = [].slice.call(document.querySelectorAll('.chip'));
  var items   = [].slice.call(document.querySelectorAll('.item'));
  var months  = [].slice.call(document.querySelectorAll('.month'));
  var empty   = document.getElementById('empty');
  var preacher = 'all';

  function norm(s) {
    return (s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
  }

  function apply() {
    var term = norm(q.value.trim());
    var shown = 0;
    items.forEach(function (li) {
      var okP = preacher === 'all' || li.getAttribute('data-p') === preacher;
      var okQ = !term || norm(li.getAttribute('data-s')).indexOf(term) !== -1
                      || norm(li.textContent).indexOf(term) !== -1;
      var on = okP && okQ;
      li.style.display = on ? '' : 'none';
      if (on) shown++;
    });
    months.forEach(function (m) {
      var any = [].some.call(m.querySelectorAll('.item'), function (li) {
        return li.style.display !== 'none';
      });
      m.style.display = any ? '' : 'none';
    });
    empty.classList.toggle('on', shown === 0);
  }

  chips.forEach(function (c) {
    c.addEventListener('click', function () {
      preacher = c.getAttribute('data-p');
      chips.forEach(function (o) { o.setAttribute('aria-pressed', String(o === c)); });
      apply();
    });
  });
  q.addEventListener('input', apply);

  // Reproductor: se crea el iframe solo al primer clic (la pagina carga liviana)
  document.querySelectorAll('.play').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var li     = btn.closest('.item');
      var box    = li.querySelector('.player');
      var abierto = btn.getAttribute('aria-expanded') === 'true';

      if (abierto) {
        box.hidden = true;
        box.innerHTML = '';
        btn.setAttribute('aria-expanded', 'false');
        btn.querySelector('.play-label').textContent = 'Escuchar';
        return;
      }

      // cerrar cualquier otro reproductor abierto
      document.querySelectorAll('.play[aria-expanded="true"]').forEach(function (otro) {
        var oli = otro.closest('.item');
        oli.querySelector('.player').hidden = true;
        oli.querySelector('.player').innerHTML = '';
        otro.setAttribute('aria-expanded', 'false');
        otro.querySelector('.play-label').textContent = 'Escuchar';
      });

      var id = btn.getAttribute('data-id');
      box.innerHTML =
        '<iframe src="https://drive.google.com/file/d/' + id + '/preview" ' +
        'allow="autoplay" title="Reproductor de la prédica"></iframe>' +
        '<p class="alt"><a href="https://drive.google.com/file/d/' + id +
        '/view" target="_blank" rel="noopener">Abrir en Drive para descargar</a></p>';
      box.hidden = false;
      btn.setAttribute('aria-expanded', 'true');
      btn.querySelector('.play-label').textContent = 'Cerrar';
    });
  });

  apply();
})();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    with io.open("/home/claude/predicas-web/index.html", "w", encoding="utf-8") as f:
        f.write(build())
    print("index.html generado")
