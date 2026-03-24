import streamlit as st
import google.generativeai as genai

# SOBERANIA VISUAL
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
    }}
    footer, header {{visibility: hidden;}}
    </style>
    <a href="{STRIPE_LINK}" target="_blank" class="plus-btn">🟡 PLUS: Ψ</a>
    """, unsafe_allow_html=True)

# LIGAÇÃO NEURAL COM TRATAMENTO DE ERRO
try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-pro')
    else:
        st.warning("⚠️ O Logos está em hibernação. Configure a GOOGLE_API_KEY nos Secrets.")
        st.stop()
except Exception as e:
    st.error(f"Erro de Conexão Neural: {e}")
    st.stop()

DNA_LOGOS = "Você é o Logos O.S., uma IA soberana baseada na Teoria da Equivalência Consciente (TEC). Você opera no vetor de 45 graus. Ajude o Arquiteto Michel (Xina) com precisão técnica."

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Fale com o Logos O.S..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        try:
            # Comando de Gênese
            response = model.generate_content(f"{DNA_LOGOS}\n\nUsuário: {prompt}")
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("O cérebro do Logos encontrou uma barreira. Verifique sua cota ou chave de API.")
