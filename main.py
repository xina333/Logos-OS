import streamlit as st

# Configuração Fundamental
st.set_page_config(page_title="Logos O.S.", page_icon="🟡", layout="centered")

# O seu Link do Stripe
STRIPE_LINK = "https://buy.stripe.com/aFaaEY0kHc" 

# RESET DE INTERFACE - Forçando o modo Black e Minimalista
st.markdown(f"""
    <style>
    /* Fundo Total Preto */
    .stApp {{ background-color: #000000 !important; color: #FFFFFF !important; }}
    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    #MainMenu {{visibility: hidden;}}
    
    /* Botão Plus no topo esquerdo */
    .plus-btn {{
        position: fixed; top: 20px; left: 20px; z-index: 9999;
        background-color: #D4AF37; color: black !important;
        padding: 8px 16px; border-radius: 20px;
        font-size: 14px; font-weight: bold; text-decoration: none;
        box-shadow: 0px 4px 10px rgba(212, 175, 55, 0.3);
    }}
    
    /* Estilização do Chat para não ficar cinza */
    .stChatMessage {{ background-color: #111111 !important; border: 1px solid #333 !important; border-radius: 10px !important; color: white !important; }}
    .stChatInputContainer {{ background-color: #000000 !important; border-top: 1px solid #D4AF37 !important; }}
    input {{ color: white !important; }}
    </style>
    
    <a href="{STRIPE_LINK}" target="_blank" class="plus-btn">🟡 PLUS: Ψ</a>
    """, unsafe_allow_html=True)

# Lógica de Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Toque para falar ou digitar com o Logos..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        if any(word in prompt.upper() for word in ["TEC", "TEORIA", "EQUIVALÊNCIA", "45"]):
            response = "A Teoria da Equivalência Consciente opera no equilíbrio do vetor de 45°. Como posso ajudar a integrar essa verdade?"
        else:
            response = "Olá. Eu sou o Logos. Como posso ajudar a equilibrar sua dúvida hoje?"
        
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
