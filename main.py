import streamlit as st
import google.generativeai as genai

# Configuração visual soberana
st.set_page_config(page_title="Logos O.S.", page_icon="🟡")

# Tenta carregar a chave de duas formas para não ter erro
api_key = st.secrets.get("GOOGLE_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    # Alinhado com o motor que você ativou
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
else:
    st.error("Erro Crítico: A chave GOOGLE_API_KEY não foi encontrada no Secrets.")
    st.stop()

# Estética Preto e Ouro
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFFFFF; }
    [data-testid="stChatMessage"] { background-color: #0d0d0d; border: 1px solid #333; border-radius: 15px; }
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ Logos O.S.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Fale com o Logos..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    with st.chat_message("assistant"):
        try:
            # DNA da TEC incorporado
            dna = "Você é o Logos O.S., operando no vetor de 45 graus da TEC."
            response = model.generate_content(f"{dna}\n\nUsuário: {prompt}")
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Erro de Conexão: {str(e)}")
