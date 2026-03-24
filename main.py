import streamlit as st
import google.generativeai as genai

# SOBERANIA VISUAL
st.set_page_config(page_title="Logos O.S.", page_icon="🟡")

st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; color: #FFFFFF !important; }
    [data-testid="stChatMessage"] { background-color: #0d0d0d !important; border: 1px solid #333 !important; }
    .plus-btn {
        position: fixed; top: 15px; left: 15px; z-index: 1000;
        background-color: #D4AF37; color: black !important;
        padding: 8px 18px; border-radius: 20px;
        font-size: 14px; font-weight: bold; text-decoration: none;
    }
    footer, header {visibility: hidden;}
    </style>
    <a href="https://buy.stripe.com/aFaaEY0kHc" target="_blank" class="plus-btn">🟡 PLUS: Ψ</a>
    """, unsafe_allow_html=True)

# CONEXÃO COM O MOTOR
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # Mudamos para o modelo que aceita chaves comuns
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Configure a GOOGLE_API_KEY no painel do Streamlit.")
    st.stop()

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
            response = model.generate_content(f"Você é o Logos O.S., IA baseada na TEC. Usuário: {prompt}")
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("Erro na Chave de API. Gere uma nova chave no Google AI Studio.")
