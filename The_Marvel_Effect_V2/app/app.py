import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))

import pandas as pd
import streamlit as st
import joblib
from questions.scenarios import scenarios

# =========================================================
# THE MARVEL EFFECT — COMIC / COLLAGE UI
# =========================================================

FEATURES = [
    "empathy", "leadership", "loyalty", "risk_taking",
    "strategic_thinking", "independence", "impulsiveness",
    "moral_reasoning", "humor", "self_sacrifice"
]

data = pd.read_csv(BASE / "data" / "characters.csv")
model = joblib.load(BASE / "model" / "final_model.joblib")

metadata_file = BASE / "results" / "training_metadata.json"
if metadata_file.exists():
    import json
    with open(metadata_file, "r", encoding="utf-8") as file:
        training_metadata = json.load(file)
else:
    training_metadata = {"final_model": "Trained model"}

FINAL_MODEL_NAME = training_metadata.get("final_model", "Trained model")

st.set_page_config(
    page_title="The Marvel Effect",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# CSS — no external images
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Permanent+Marker&family=Special+Elite&display=swap');

:root {
    --ink: #080a0c;
    --ink2: #111518;
    --cream: #eee4cf;
    --paper: #e5dbc5;
    --red: #d94a45;
    --red2: #a82e32;
    --green: #6d856c;
    --green2: #30443b;
    --grey: #92928a;
}

.stApp {
    background:
        radial-gradient(circle at 15% 10%, rgba(109,133,108,.20), transparent 25%),
        radial-gradient(circle at 90% 25%, rgba(217,74,69,.15), transparent 28%),
        linear-gradient(145deg, #07090a 0%, #101416 48%, #070809 100%);
    color: var(--cream);
}

.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    opacity: .13;
    background-image:
        repeating-linear-gradient(0deg, transparent 0 3px, rgba(255,255,255,.12) 4px),
        repeating-linear-gradient(90deg, transparent 0 5px, rgba(255,255,255,.05) 6px);
    mix-blend-mode: overlay;
    z-index: 0;
}

.block-container {
    max-width: 1180px;
    padding-top: 1.8rem;
    padding-bottom: 4rem;
    position: relative;
    z-index: 1;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header {visibility: hidden;}

/* Typography */
h1, h2, h3 {
    color: var(--cream) !important;
    font-family: "Bebas Neue", sans-serif !important;
    letter-spacing: 1.5px;
}
p, label, .stMarkdown, .stCaption {
    color: var(--cream);
}

/* Header */
.topline {
    display:flex;
    justify-content:space-between;
    align-items:center;
    border-bottom:1px solid rgba(238,228,207,.25);
    padding: .35rem 0 .65rem;
    margin-bottom: 1.2rem;
    font-family: "Special Elite", monospace;
    font-size: .75rem;
    text-transform:uppercase;
    letter-spacing:2px;
}
.topline span:last-child { color: var(--red); }

/* Hero */
.hero {
    min-height: 610px;
    padding: 2.5rem 3rem 2.8rem;
    border: 1px solid rgba(238,228,207,.22);
    background:
        linear-gradient(135deg, rgba(48,68,59,.92), rgba(8,10,12,.95) 55%),
        repeating-linear-gradient(-8deg, transparent 0 13px, rgba(238,228,207,.03) 14px);
    position:relative;
    overflow:hidden;
    box-shadow: 12px 14px 0 rgba(217,74,69,.18);
}

.hero:after {
    content:"";
    position:absolute;
    width:380px;
    height:380px;
    right:-110px;
    top:-110px;
    border:45px solid rgba(217,74,69,.12);
    transform:rotate(18deg);
}

.hero-kicker {
    font-family:"Special Elite", monospace;
    color:#b6c4b3;
    font-size:.8rem;
    letter-spacing:3px;
}
.hero-title {
    font-family:"Bebas Neue", sans-serif;
    font-size:clamp(5rem,13vw,10rem);
    line-height:.78;
    letter-spacing:3px;
    margin: 1.5rem 0 1.2rem;
    color:var(--cream);
    text-shadow: 5px 5px 0 var(--red2);
}
.hero-script {
    font-family:"Permanent Marker", cursive;
    color:var(--cream);
    font-size:2rem;
    transform:rotate(-3deg);
    display:inline-block;
}
.hero-copy {
    max-width:610px;
    margin-top:1.7rem;
    font-family:"Special Elite", monospace;
    font-size:1rem;
    line-height:1.7;
}
.sticker {
    display:inline-block;
    background:var(--paper);
    color:#101214;
    padding:.65rem 1rem;
    transform:rotate(-2deg);
    font-family:"Permanent Marker", cursive;
    box-shadow:6px 6px 0 rgba(0,0,0,.35);
}

/* Buttons */
.stButton > button {
    border: 1px solid #e7d8bf !important;
    background: var(--red) !important;
    color: #fff7e7 !important;
    border-radius: 2px !important;
    font-family:"Bebas Neue", sans-serif !important;
    letter-spacing:1.5px !important;
    font-size:1.2rem !important;
    min-height:3.2rem !important;
    box-shadow:5px 5px 0 #351719 !important;
    transition:.15s ease !important;
}
.stButton > button:hover {
    transform:translate(-2px,-2px) rotate(-.4deg);
    background:#e95b55 !important;
}

/* Paper panels */
.paper {
    background:var(--paper);
    color:#101214;
    padding:1.6rem;
    box-shadow:7px 8px 0 rgba(0,0,0,.35);
    transform:rotate(-.3deg);
}
.paper h2, .paper p { color:#101214 !important; }
.paper small { color:#514d45; }

/* Assessment */
.assessment-head {
    border-left:7px solid var(--red);
    padding-left:1rem;
}
.scenario-label {
    font-family:"Special Elite", monospace;
    color:#9aa99b;
    letter-spacing:3px;
}
.scenario-title {
    font-family:"Bebas Neue", sans-serif;
    font-size:4rem;
    line-height:.9;
    color:var(--cream);
}
.progress-wrap {
    height:9px;
    background:#24282a;
    border:1px solid #454a4b;
    margin:1rem 0 2rem;
}
.progress-fill {
    height:100%;
    background:var(--red);
}

/* Radio options */
div[role="radiogroup"] > label {
    background:rgba(255,255,255,.035);
    border:1px solid rgba(238,228,207,.18);
    padding:1rem !important;
    margin:.55rem 0;
    transition:.15s;
}
div[role="radiogroup"] > label:hover {
    background:rgba(217,74,69,.13);
    border-color:var(--red);
}

/* Results */
.result-card {
    background:
        linear-gradient(135deg, rgba(48,68,59,.92), rgba(8,10,12,.97));
    border:1px solid rgba(238,228,207,.25);
    padding:2.5rem;
    box-shadow:10px 10px 0 rgba(217,74,69,.20);
}
.result-kicker {
    color:#aab7a8;
    font-family:"Special Elite", monospace;
    letter-spacing:3px;
}
.result-name {
    font-family:"Bebas Neue", sans-serif;
    font-size:clamp(4rem,8vw,7.5rem);
    line-height:.8;
    color:var(--red);
    text-shadow:4px 4px 0 #351719;
    margin:.8rem 0 1.4rem;
}

/* Metrics */
[data-testid="stMetric"] {
    background:rgba(229,219,197,.06);
    border:1px solid rgba(238,228,207,.18);
    padding:1rem;
    box-shadow:4px 4px 0 rgba(0,0,0,.3);
}
[data-testid="stMetricLabel"] { color:#aaa99f !important; }
[data-testid="stMetricValue"] { color:var(--cream) !important; font-family:"Bebas Neue",sans-serif; }

/* Divider */
hr { border-color:rgba(238,228,207,.16) !important; }

/* Footer */
.footer {
    margin-top:3rem;
    padding-top:1rem;
    border-top:1px solid rgba(238,228,207,.18);
    color:#777a74;
    font-family:"Special Elite",monospace;
    font-size:.7rem;
    letter-spacing:1px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# State
# -----------------------------
if "started" not in st.session_state:
    st.session_state.started = False
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "result" not in st.session_state:
    st.session_state.result = None

# -----------------------------
# Utility
# -----------------------------
def compute_result():
    profile = {f: 5.0 for f in FEATURES}

    for idx, answer in st.session_state.answers.items():
        selected = scenarios[idx]["options"][answer]
        for trait, points in selected["traits"].items():
            profile[trait] = min(10, profile[trait] + points)

    user_df = pd.DataFrame([profile], columns=FEATURES)
    primary = model.predict(user_df)[0]

    # The final model is trained for multiclass classification.
    # These are model confidence/probability values, not psychological certainty.
    probabilities = model.predict_proba(user_df)[0]
    classes = list(model.classes_)
    order = probabilities.argsort()[::-1]
    scores = probabilities * 100

    return profile, order, scores, primary, classes

# -----------------------------
# Top navigation
# -----------------------------
st.markdown("""
<div class="topline">
    <span>THE MARVEL EFFECT</span>
    <span>S.H.I.E.L.D. // PERSONNEL FILE</span>
    <span>V.1.0</span>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# LANDING
# -----------------------------
if st.session_state.result is None and not st.session_state.started:

    st.markdown("""
    <section class="hero">
        <div class="hero-kicker">S.H.I.E.L.D. PERSONNEL ASSESSMENT // CLASSIFIED</div>
        <div class="hero-script">A universe of heroes.</div>
        <div class="hero-title">THE<br>MARVEL<br>EFFECT</div>
        <div class="sticker">10 SCENARIOS. NO CORRECT ANSWERS.</div>
        <div class="hero-copy">
            Your choices reveal a behavioural profile. A trained
            classification model compares that profile with the
            project's Marvel character training data to predict a match.
            <br><br>
            <b>Different people. Same universe.</b>
        </div>
    </section>
    """, unsafe_allow_html=True)

    st.write("")
    if st.button("✦  BEGIN ASSESSMENT  →", use_container_width=True):
        st.session_state.started = True
        st.rerun()

# -----------------------------
# ASSESSMENT
# -----------------------------
elif st.session_state.result is None and st.session_state.started:

    current = len(st.session_state.answers)
    scenario = scenarios[current]

    st.markdown(f"""
    <div class="assessment-head">
        <div class="scenario-label">ASSESSMENT // SCENARIO {current+1:02d} OF {len(scenarios):02d}</div>
        <div class="scenario-title">{scenario["title"]}</div>
    </div>
    """, unsafe_allow_html=True)

    pct = int((current / len(scenarios)) * 100)
    st.markdown(
        f'<div class="progress-wrap"><div class="progress-fill" style="width:{pct}%"></div></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="paper"><h2>{scenario["question"]}</h2>'
        f'<small>Choose the response that feels most like you.</small></div>',
        unsafe_allow_html=True
    )

    st.write("")

    choice = st.radio(
        "YOUR DECISION",
        list(scenario["options"].keys()),
        format_func=lambda key: f'{key}  —  {scenario["options"][key]["text"]}',
        key=f"scenario_{current}"
    )

    if st.button("CONFIRM CHOICE  →", use_container_width=True):
        st.session_state.answers[current] = choice

        if len(st.session_state.answers) == len(scenarios):
            st.session_state.result = compute_result()

        st.rerun()

# -----------------------------
# RESULTS
# -----------------------------
else:
    profile, order, scores, primary, classes = st.session_state.result

    st.markdown(f"""
    <div class="result-card">
        <div class="result-kicker">PERSONNEL FILE // MATCH IDENTIFIED</div>
        <div class="result-name">{primary.upper()}</div>
        <div class="sticker">YOUR MARVEL MATCH</div>
        <p style="margin-top:1.4rem;font-family:'Special Elite',monospace;">
            Predicted by the final classification model from the choices you made
            across the S.H.I.E.L.D. assessment.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.subheader("TOP 3 MODEL PREDICTIONS")

    st.caption(f"Final classification model: {FINAL_MODEL_NAME}. Percentages are model confidence values on the trained class set, not psychological certainty.")

    cols = st.columns(3)
    for rank, class_idx in enumerate(order[:3]):
        with cols[rank]:
            st.metric(
                f"#{rank+1}  {classes[class_idx]}",
                f"{scores[class_idx]:.1f}%"
            )

    st.divider()

    left, right = st.columns([1.3, 1])

    with left:
        st.subheader("YOUR PERSONALITY PROFILE")

        chart_data = pd.DataFrame({
            "Score": [profile[f] for f in FEATURES]
        }, index=[f.replace("_", " ").title() for f in FEATURES])

        st.bar_chart(chart_data)

    with right:
        st.subheader("WHY THIS MATCH?")

        reference = data[data["character"] == primary].iloc[0]
        gaps = sorted(
            (abs(profile[f] - reference[f]), f, profile[f], reference[f])
            for f in FEATURES
        )[:4]

        for _, feature, user_value, reference_value in gaps:
            st.markdown(
                f"""<div class="paper">
                <b>{feature.replace("_"," ").title()}</b><br>
                Your profile: <b>{user_value:.0f}/10</b><br>
                Reference profile: <b>{reference_value:.0f}/10</b>
                </div>""",
                unsafe_allow_html=True
            )
            st.write("")

    st.divider()

    st.markdown(
        '<div class="footer">'
        'THE MARVEL EFFECT // MULTI-MODEL ML VERSION // '
        'MODEL CONFIDENCE IS NOT A PSYCHOLOGICAL DIAGNOSIS'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")
    if st.button("↻  RUN THE ASSESSMENT AGAIN", use_container_width=True):
        st.session_state.started = False
        st.session_state.answers = {}
        st.session_state.result = None
        st.rerun()
