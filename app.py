
import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Critical Power - SportMetrics",
    layout="wide",
)

BASE_DIR = Path(__file__).parent
LOGO_PATH = BASE_DIR / "logo.png"
if not LOGO_PATH.exists():
    LOGO_PATH = BASE_DIR / "1.png"

logo_data_uri = ""
if LOGO_PATH.exists():
    logo_b64 = base64.b64encode(LOGO_PATH.read_bytes()).decode("utf-8")
    logo_data_uri = f"data:image/png;base64,{logo_b64}"

CP_IMAGE_PATH = BASE_DIR / "cp_image.png"
cp_image_uri = ""
if CP_IMAGE_PATH.exists():
    cp_b64 = base64.b64encode(CP_IMAGE_PATH.read_bytes()).decode("utf-8")
    cp_image_uri = f"data:image/png;base64,{cp_b64}"

HTML_PAGE = r"""
<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Critical Power - SportMetrics</title>
  <style>
    @import url("https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Spectral:wght@400;600&display=swap");

    :root {
      --sand: #f6f1ea;
      --clay: #e9ddd2;
      --ink: #1e2a2f;
      --muted: #5c6b73;
      --sea: #2f7c85;
      --deep: #0f4c5c;
      --sun: #f4b66a;
      --peach: #f1c9a9;
      --card: #fffdf6;
      --card-strong: #ffffff;
      --border: rgba(30, 42, 47, 0.12);
      --shadow: 0 18px 50px rgba(15, 76, 92, 0.18);
    }

    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0;
      font-family: "Spectral", "Times New Roman", serif;
      color: var(--ink);
      background: radial-gradient(1200px 800px at 10% -10%, #ffffff 0%, var(--sand) 60%, var(--clay) 100%);
    }

    .logo-pattern {
      position: fixed;
      inset: 0;
      background-image: url('{{LOGO_DATA_URI}}');
      background-repeat: repeat;
      background-position: center;
      background-size: 140px;
      opacity: 0.07;
      mix-blend-mode: multiply;
      pointer-events: none;
      z-index: 1;
    }

    .bg-shape {
      position: fixed;
      inset: auto;
      width: 480px;
      height: 480px;
      border-radius: 50%;
      background: radial-gradient(circle at 30% 30%, rgba(47, 124, 133, 0.28), rgba(47, 124, 133, 0.02));
      z-index: -1;
    }
    .bg-shape.one { top: -120px; right: -120px; }
    .bg-shape.two { bottom: -200px; left: -140px; background: radial-gradient(circle, rgba(244, 182, 106, 0.35), rgba(244, 182, 106, 0.02)); }

    nav {
      position: fixed;
      top: 28px;
      right: 26px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      background: var(--card-strong);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 14px 14px;
      box-shadow: var(--shadow);
      z-index: 4;
      max-width: 190px;
    }
    nav h4 {
      margin: 0 0 6px;
      font-family: "Space Grotesk", sans-serif;
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--muted);
    }
    .nav-link {
      font-family: "Space Grotesk", sans-serif;
      font-size: 13px;
      text-decoration: none;
      color: var(--muted);
      display: flex;
      gap: 6px;
      align-items: center;
      transition: color 0.2s ease;
    }
    .nav-link span {
      display: inline-block;
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--clay);
      border: 1px solid var(--border);
    }
    .nav-link.active { color: var(--deep); font-weight: 600; }
    .nav-link.active span { background: var(--sea); border-color: var(--sea); }

    .progress {
      height: 6px;
      background: rgba(47, 124, 133, 0.12);
      border-radius: 999px;
      overflow: hidden;
      margin-top: 6px;
    }
    .progress span { display: block; height: 100%; width: 0%; background: var(--sea); transition: width 0.2s ease; }

    main {
      position: relative;
      z-index: 3;
      max-width: 1100px;
      margin: 0 auto;
      padding: 64px 24px 120px;
    }

    section {
      margin: 0 0 72px;
      padding: 36px;
      border-radius: 26px;
      background: var(--card);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      transition: all 0.7s ease;
    }
    body.enable-animations section { opacity: 0; transform: translateY(20px); }
    body.enable-animations section.in-view { opacity: 1; transform: translateY(0); }

    .hero {
      padding: 54px 44px;
      background: linear-gradient(140deg, #ffffff, #f6e7d6);
    }
    .hero h1 {
      font-family: "Space Grotesk", sans-serif;
      font-size: clamp(2.2rem, 3.4vw, 3.4rem);
      margin: 0 0 12px;
      color: var(--deep);
    }
    .hero p {
      font-size: 1.05rem;
      color: var(--muted);
      margin: 0;
      max-width: 720px;
    }
    .hero .hero-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 18px;
      margin-top: 28px;
    }
    .hero .stat {
      padding: 16px 18px;
      background: var(--card-strong);
      border-radius: 16px;
      border: 1px solid var(--border);
      font-family: "Space Grotesk", sans-serif;
      font-size: 0.95rem;
      color: var(--muted);
    }
    .hero .stat strong { display: block; color: var(--deep); font-size: 1.1rem; }

    h2 { font-family: "Space Grotesk", sans-serif; margin: 0 0 12px; color: var(--deep); font-size: 1.8rem; }
    h3 { font-family: "Space Grotesk", sans-serif; margin: 0 0 8px; color: var(--deep); }
    p { margin: 0 0 14px; color: var(--ink); line-height: 1.55; }
    .muted { color: var(--muted); }

    .grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 18px; }
    .card { background: var(--card-strong); border: 1px solid var(--border); border-radius: 18px; padding: 16px 18px; }
    .pill { display: inline-block; font-family: "Space Grotesk", sans-serif; font-size: 0.72rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); border: 1px solid var(--border); padding: 4px 10px; border-radius: 999px; margin-bottom: 10px; }

    .slider-box { margin-top: 18px; padding: 18px; border-radius: 18px; border: 1px dashed rgba(47, 124, 133, 0.4); background: #eef5f4; }
    .slider-box label { font-family: "Space Grotesk", sans-serif; font-size: 0.9rem; }
    .slider-box input[type="range"] { width: 100%; margin: 10px 0 6px; }
    .mix-row { display: grid; grid-template-columns: 130px 1fr 54px; gap: 12px; align-items: center; margin: 10px 0; font-family: "Space Grotesk", sans-serif; font-size: 0.85rem; }
    .mix-bar { background: #eef5f4; border-radius: 999px; overflow: hidden; height: 10px; border: 1px solid rgba(15, 76, 92, 0.2); }
    .mix-bar span { display: block; height: 100%; width: 0%; background: linear-gradient(90deg, var(--sea), var(--deep)); border-radius: 999px; transition: width 0.3s ease; }
    .mix-value { text-align: right; color: var(--muted); }

    .cp-curve { margin-top: 16px; display: grid; grid-template-columns: repeat(8, minmax(60px, 1fr)); gap: 8px; align-items: end; height: 140px; }
    .cp-bar { width: 100%; border-radius: 10px 10px 6px 6px; background: rgba(47, 124, 133, 0.18); border: 1px solid rgba(47, 124, 133, 0.3); height: 40%; transition: height 0.3s ease; }
    .cp-bar.active { background: var(--deep); border-color: var(--deep); }

    .vt2-bar { margin-top: 14px; position: relative; height: 16px; border-radius: 999px; background: #eef5f4; border: 1px solid rgba(15, 76, 92, 0.2); overflow: hidden; }
    .vt2-window { position: absolute; top: 0; bottom: 0; width: 18%; left: 62%; border-radius: 999px; background: rgba(47, 124, 133, 0.32); }
    .vt2-marker { position: absolute; top: -4px; width: 2px; height: 24px; background: var(--deep); left: 70%; }

    .callout { background: #f3e4d2; border: 1px solid #e8cfae; padding: 16px 18px; border-radius: 18px; font-family: "Space Grotesk", sans-serif; }

    .summary-list { margin: 0; padding-left: 18px; }
    .summary-list li { margin: 0 0 10px; }

    .footer { text-align: center; font-family: "Space Grotesk", sans-serif; font-size: 0.9rem; color: var(--muted); }

    .cp-image { width: 100%; height: auto; border-radius: 14px; border: 1px solid var(--border); background: #fff; margin-top: 12px; }
    .image-fallback { color: var(--muted); font-size: 0.9rem; margin-top: 8px; }

    @media (max-width: 980px) {
      nav { display: none; }
      section { padding: 28px; }
      .mix-row { grid-template-columns: 110px 1fr 48px; }
    }

    @media (max-width: 720px) {
      main { padding: 40px 16px 90px; }
      section { padding: 18px; margin: 0 0 36px; }
      .hero { padding: 24px 18px; }
      .hero h1 { font-size: clamp(1.8rem, 6vw, 2.4rem); }
      .hero .hero-grid { grid-template-columns: 1fr; }
      .grid-3 { grid-template-columns: 1fr; }
      .mix-row { grid-template-columns: 1fr; gap: 6px; }
      .mix-value { text-align: left; }
      .cp-curve { grid-template-columns: repeat(4, minmax(70px, 1fr)); }
      .card { padding: 14px; }
    }

    @media (prefers-reduced-motion: reduce) {
      * { scroll-behavior: auto; }
      section { transition: none; }
      body.enable-animations section { opacity: 1; transform: none; }
    }
  </style>
</head>
<body>
  <div class="logo-pattern" aria-hidden="true"></div>
  <div class="bg-shape one"></div>
  <div class="bg-shape two"></div>

  <nav aria-label="Navigatie">
    <h4>Route</h4>
    <a class="nav-link" href="#intro" data-section="intro"><span></span>Intro</a>
    <a class="nav-link" href="#definitie" data-section="definitie"><span></span>Definitie</a>
    <a class="nav-link" href="#model" data-section="model"><span></span>Model</a>
    <a class="nav-link" href="#meten" data-section="meten"><span></span>Meten</a>
    <a class="nav-link" href="#casus" data-section="casus"><span></span>Casus</a>
    <a class="nav-link" href="#samenvatting" data-section="samenvatting"><span></span>Samenvatting</a>
    <div class="progress"><span id="progress-bar"></span></div>
  </nav>

  <main>
    <section id="intro" class="hero" data-title="Intro">
      <span class="pill">Critical Power</span>
      <h1>Critical Power: jouw duurzame grens in watt</h1>
      <p>CP met W′ beschrijft je gedrag in het zware domein: wat je duurzaam kunt leveren en hoeveel boven-CP budget je hebt. Krachtige aanvulling op VT1/VT2 en VO2max.</p>
      <div class="hero-grid">
        <div class="stat"><strong>Duurzame grens</strong>CP is waar je naartoe trekt als de inspanning langer wordt.</div>
        <div class="stat"><strong>Boven-CP budget</strong>W′ verklaart aanvallen, heuvels en surges.</div>
        <div class="stat"><strong>Praktisch</strong>Helpt pacing en intervalontwerp onderbouwen.</div>
      </div>
    </section>

    <section id="definitie" data-title="Definitie">
      <h2>Wat CP en W′ zijn</h2>
      <div class="grid-3">
        <div class="card">
          <h3>CP</h3>
          <p>Duurzame grens in het zware domein. Boven CP geen echte steady state.</p>
        </div>
        <div class="card">
          <h3>W′</h3>
          <p>Eindig boven-CP budget. Elke extra watt boven CP verbruikt W′ sneller.</p>
        </div>
        <div class="card">
          <h3>Waarom relevant</h3>
          <p>Verklaart waarom je kunt aanvallen én waarom je kunt opblazen.</p>
        </div>
      </div>
      <img class="cp-image" src="{{CP_IMAGE_URI}}" alt="Critical Power visual" />
      <div class="image-fallback">Als de visual niet laadt: CP = grens, W′ = budget boven die grens.</div>
    </section>

    <section id="model" data-title="Model">
      <h2>Het model in twee regels</h2>
      <p>Vermogen = (W′ / tijd) + CP → tijd = W′ / (P − CP). W′-verbruik = (P − CP) × tijd.</p>
      <div class="slider-box" aria-live="polite">
        <label for="cp-input">Jouw CP (W)</label>
        <input id="cp-input" type="range" min="150" max="400" value="280" />
        <label for="wprime-input">Jouw W′ (kJ)</label>
        <input id="wprime-input" type="range" min="8" max="30" value="15" />
        <label for="power-input">Gepland vermogen (W)</label>
        <input id="power-input" type="range" min="200" max="450" value="320" />
        <div class="mix-row">
          <div>Tijd tot leeg (mm:ss)</div>
          <div class="mix-bar"><span id="mix-time"></span></div>
          <div class="mix-value" id="mix-time-value">0</div>
        </div>
        <div class="mix-row">
          <div>W′ gebruik (kJ)</div>
          <div class="mix-bar"><span id="mix-wprime"></span></div>
          <div class="mix-value" id="mix-wprime-value">0</div>
        </div>
      </div>

      <div class="slider-box" aria-live="polite">
        <label for="duration-input">Doelduur (s) voor een klim / blok</label>
        <input id="duration-input" type="range" min="120" max="900" value="360" />
        <div class="mix-row">
          <div>Adviesvermogen</div>
          <div class="mix-bar"><span id="mix-adv"></span></div>
          <div class="mix-value" id="mix-adv-value">0 W</div>
        </div>
      </div>

      <div class="cp-curve" id="cp-curve" aria-hidden="true">
        <div class="cp-bar"></div><div class="cp-bar"></div><div class="cp-bar"></div><div class="cp-bar"></div>
        <div class="cp-bar"></div><div class="cp-bar"></div><div class="cp-bar"></div><div class="cp-bar"></div>
      </div>
    </section>

    <section id="meten" data-title="Meten">
      <h2>Hoe wij CP meten</h2>
      <div class="grid-3">
        <div class="card">
          <h3>Efforts</h3>
          <p>3–4 max efforts in 3–20 min (bijv. 3, 5, 12, 20 min).</p>
        </div>
        <div class="card">
          <h3>Kwaliteit</h3>
          <p>Bij voorkeur op aparte dagen; vermoeidheid vertekent vooral W′.</p>
        </div>
        <div class="card">
          <h3>Model</h3>
          <p>We nemen de beste gemiddelde power per effort → CP + W′.</p>
        </div>
      </div>
      <div class="callout">CP/W′ komt uit je power–duration gedrag en maakt expliciet wat er boven je duurzame grens gebeurt.</div>
    </section>

    <section id="casus" data-title="Casus">
      <h2>Casus: klim van ~6 minuten</h2>
      <p>CP = 280 W, W′ = 15 kJ. Bij 330 W is (P−CP)=50 W → tijd = 15.000/50 = 300 s (5:00) → te hoog voor 6 min. Bij 315 W is tijd ≈ 7:09 → realistischer.</p>
      <div class="callout">Gebruik CP/W′ om pacing te plannen en intervalwerk te doseren.</div>
    </section>

    <section id="samenvatting" data-title="Samenvatting">
      <h2>Samenvatting</h2>
      <ul class="summary-list">
        <li>CP = duurzame grens in het zware domein; W′ = boven-CP budget.</li>
        <li>Model: tijd = W′/(P−CP) en W′-gebruik = (P−CP)×tijd → direct toepasbaar.</li>
        <li>Meten met meerdere max efforts (3–20 min) levert reproduceerbare CP/W′.</li>
        <li>Gebruik voor pacing, intervalontwerp en om “opblazen” te voorkomen.</li>
      </ul>
      <p class="footer">We zien je graag bij SportMetrics.</p>
    </section>
  </main>

  <script>
    document.body.classList.add("enable-animations");

    const sections = Array.from(document.querySelectorAll("section[data-title]"));
    const navLinks = Array.from(document.querySelectorAll(".nav-link"));
    const progressBar = document.getElementById("progress-bar");

    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) entry.target.classList.add("in-view");
      });
    }, { threshold: 0.2 });
    sections.forEach((section) => revealObserver.observe(section));

    const spyObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          navLinks.forEach((link) => link.classList.toggle("active", link.dataset.section === entry.target.id));
        }
      });
    }, { threshold: 0.55 });
    sections.forEach((section) => spyObserver.observe(section));

    window.addEventListener("scroll", () => {
      const doc = document.documentElement;
      const scrollTop = doc.scrollTop || document.body.scrollTop;
      const scrollHeight = doc.scrollHeight - doc.clientHeight;
      const progress = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
      progressBar.style.width = `${progress}%`;
    });

    const cpInput = document.getElementById("cp-input");
    const wprimeInput = document.getElementById("wprime-input");
    const powerInput = document.getElementById("power-input");
    const durationInput = document.getElementById("duration-input");

    function formatTime(seconds) {
      const m = Math.floor(seconds / 60);
      const s = Math.max(0, Math.round(seconds % 60));
      return `${m}:${s.toString().padStart(2, "0")}`;
    }

    function updateModel() {
      const cp = parseInt(cpInput.value, 10);
      const wprime = parseInt(wprimeInput.value, 10) * 1000; // to J
      const power = parseInt(powerInput.value, 10);
      const above = Math.max(1, power - cp);
      const timeSec = wprime / above;
      const wprimeKj = wprime / 1000;

      document.getElementById("mix-time").style.width = `${Math.min(100, (timeSec / 600) * 100)}%`;
      document.getElementById("mix-wprime").style.width = `${Math.min(100, (wprimeKj / 30) * 100)}%`;
      document.getElementById("mix-time-value").textContent = formatTime(timeSec);
      document.getElementById("mix-wprime-value").textContent = `${wprimeKj.toFixed(1)} kJ`;

      const bars = Array.from(document.querySelectorAll("#cp-curve .cp-bar"));
      bars.forEach((bar, idx) => {
        const t = (idx + 2) * 60;
        const p = cp + wprime / Math.max(1, t);
        const norm = Math.min(1, (p - 150) / 350);
        bar.style.height = `${30 + norm * 70}%`;
        bar.classList.toggle("active", Math.abs(p - power) < 10);
      });
    }

    function updateAdvice() {
      const cp = parseInt(cpInput.value, 10);
      const wprime = parseInt(wprimeInput.value, 10) * 1000;
      const dur = parseInt(durationInput.value, 10);
      const advPower = cp + wprime / dur;
      document.getElementById("mix-adv").style.width = `${Math.min(100, (advPower - 150) / 3.5)}%`;
      document.getElementById("mix-adv-value").textContent = `${Math.round(advPower)} W`;
    }

    [cpInput, wprimeInput, powerInput].forEach((el) => el.addEventListener("input", () => { updateModel(); updateAdvice(); }));
    durationInput.addEventListener("input", updateAdvice);

    updateModel();
    updateAdvice();
  </script>
</body>
</html>
"""

HTML_PAGE = HTML_PAGE.replace("{{LOGO_DATA_URI}}", logo_data_uri)
HTML_PAGE = HTML_PAGE.replace("{{CP_IMAGE_URI}}", cp_image_uri)

components.html(HTML_PAGE, height=4800, scrolling=True)
