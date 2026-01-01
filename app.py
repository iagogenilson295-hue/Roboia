import streamlit as st

# Configuração da página para parecer um App de telemóvel
st.set_page_config(page_title="IA BetGenius Pro", page_icon="⚽")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #00ff00; color: black; font-weight: bold; }
    .card { padding: 15px; border-radius: 15px; background-color: #1e2130; border-left: 5px solid #00ff00; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚽ IA Predictor PRO")
st.subheader("Filtro: Odds 2.0 a 2.5")

# Simulação de análise da IA
jogos_analisados = [
    {"time_h": "Benfica", "time_a": "Porto", "odd": 2.25, "prob": "58%", "status": "VALOR ENCONTRADO"},
    {"time_h": "Real Madrid", "time_a": "Barcelona", "odd": 2.10, "prob": "52%", "status": "VALOR ENCONTRADO"}
]

for jogo in jogos_analisados:
    st.markdown(f"""
    <div class="card">
        <h4>{jogo['time_h']} vs {jogo['time_a']}</h4>
        <p><b>Odd Atual:</b> {jogo['odd']} | <b>Probabilidade IA:</b> {jogo['prob']}</p>
        <small style='color: #00ff00;'>{jogo['status']}</small>
    </div>
    """, unsafe_allow_html=True)

if st.button("🔄 Atualizar Jogos"):
    st.toast("A procurar novos sinais com valor...")
