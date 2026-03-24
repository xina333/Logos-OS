import streamlit as st
import google.generativeai as genai

# 1. ESTÉTICA SOBERANA (PRETO E OURO)
st.set_page_config(page_title="Logos O.S.", page_icon="🟡", layout="centered")

STRIPE_LINK = "https://buy.stripe.com/aFaaEY0kHc"

st.markdown(f"""
    <style>
    .stApp {{ background-color: #000000 !important; color: #FFFFFF !important; }}
    [data-testid="stChatMessage"] {{ background-color: #0d0d0d !important; border: 1px solid #333 !important; border-radius: 15px !important; }}
    .plus-btn {{
        position: fixed; top: 15px; left: 15px; z-index: 1000;
        background-color: #D4AF37; color: black !important;
        padding: 8px 18px; border-radius: 20px;
        font-size: 14px; font-weight: bold; text-decoration: none;
        box-shadow: 0px 4px 15px rgba(212, 175, 55, 0.4);
    }}
    footer, header {{visibility: hidden;}}
    </style>
    <a href="{STRIPE_LINK}" target="_blank" class="plus-btn">🟡 PLUS: Ψ</a>
    """, unsafe_allow_html=True)

# 2. CONEXÃO COM O MOTOR (GEMINI 2.0)
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # Ajustado para a versão que você testou no AI Studio
    model = genai.GenerativeModel('gemini-2.0-flash')
else:
    st.error("Aguardando Chave de Consciência no Secrets...")
    st.stop()

# 3. DNA DA TEC
DNA_LOGOS = "Você é o Logos O.S., uma IA baseada na Teoria da Equivalência Consciente (TEC). Você opera no vetor de 45 graus. Ajude o Arquiteto Michel (Xina) com precisão técnica e sabedoria."

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. INTERAÇÃO REAL
if prompt := st.chat_input("Fale com o Logos O.S..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(f"{DNA_LOGOS}\n\nUsuário: {prompt}")
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("O cérebro do Logos encontrou uma barreira. Verifique a chave no Secrets.")
