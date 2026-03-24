import streamlit as st

# Configuração da Página - Minimalismo Radical
st.set_page_config(page_title="Logos O.S.", page_icon="🟡", layout="centered")

# O Link que você criou no Stripe
STRIPE_LINK = "https://buy.stripe.com/aFaaEY0kHc..." # O link da sua foto

# Estilização Personalizada
st.markdown(f"""
    <style>
    .stApp {{ background-color: #000000; color: #FFFFFF; }}
    .stChatFloatingInputContainer {{ background-color: #000000; }}
    /* Botão Plus no topo esquerdo */
    .plus-btn {{
        position: fixed; top: 15px; left: 60px; z-index: 1000;
        background-color: #D4AF37; color: black;
        padding: 4px 12px; border-radius: 15px;
        font-size: 12px; font-weight: bold; text-decoration: none;
    }}
    /* Símbolo 45 pequeno no topo esquerdo */
    .logo-45 {{
        position: fixed; top: 10px; left: 15px; z-index: 1000;
        font-size: 24px; color: #D4AF37;
    }}
    </style>
    <div class="logo-45">🟡</div>
    <a href="{STRIPE_LINK}" target="_blank" class="plus-btn">PLUS: Ψ</a>
    """, unsafe_allow_html=True)

# Lógica de Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibição das mensagens
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada do Arquiteto
if prompt := st.chat_input("Toque para falar ou digitar com o Logos..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # O Logos só fala da TEC se for provocado
        if any(word in prompt.upper() for word in ["TEC", "TEORIA", "MATEMÁTICA", "EQUIVALÊNCIA"]):
            response = "A Teoria da Equivalência Consciente opera no equilíbrio do vetor de 45°. Como posso ajudar a integrar essa verdade?"
        else:
            response = "Olá. Eu sou o Logos. Como posso ajudar a equilibrar sua dúvida hoje?"
        
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
