import streamlit as st

# Definindo informações dos bots
bots_info = [
    {
        "nome": "Fortune Tiger",
        "descricao": "O Fortune Tiger é um bot de previsão de mercado altamente preciso, projetado para ajudar os investidores a identificar oportunidades lucrativas.",
        "link_telegram": "https://t.me/sinais_tigre",
        "imagem": "Fotos/FT1.jpeg",
        "button": "https://wa.me/5527997602355"
    },
    {
        "nome": "Jungle Delight",
        "descricao": "O Jungle Delight é um bot de cassino online com uma ampla variedade de processamento para encontrar a brecha perfeita do jogo.",
        "link_telegram": "https://t.me/+Hgr-vsIrt0Q2YTRh",
        "imagem": "Fotos/PG3.jpg",
        "button": "https://wa.me/5527997602356"
    },
    {
        "nome": "Fortune Ox",
        "descricao": "O Fortune Ox é um bot de negociação automatizada que utiliza algoritmos avançados para realizar operações de forma eficiente.",
        "link_telegram": "https://t.me/sinais_tigre",
        "imagem": "Fotos/FT2.jpg",
        "button": "https://wa.me/5527997602357"
    },
    {
        "nome": "Fortune Rabbit",
        "descricao": "O Fortune Rabbit é um bot de investimento que oferece uma variedade de opções de portfólio para atender às necessidades de um apostador a longo prazo.",
        "link_telegram": "https://t.me/+Hgr-vsIrt0Q2YTRh",
        "imagem": "Fotos/FT4.png",
        "button": "https://wa.me/5527997602358"
    },
]

# Configurando a página para dispositivos móveis
st.set_page_config(
    page_title="Informações dos Bots",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Título e subtítulo
st.title('Informações dos Bots')

# Exibindo informações de cada bot
for idx, bot_info in enumerate(bots_info):
    st.markdown(f"## {bot_info['nome']}")
    
    # Dividindo a largura da tela em colunas
    col1, col2 = st.columns([2, 3])
    
    with col1:
        # Exibindo a imagem do bot
        st.image(bot_info['imagem'], width=240, use_column_width=False)
    
    with col2:
        # Exibindo as informações do bot
        st.write(bot_info['descricao'])
        st.markdown(f"Link do Telegram: [{bot_info['nome']}]({bot_info['link_telegram']})")
        st.button(f"Adquirir {bot_info['nome']}", key=f"button_{idx}")
    
    st.markdown("---")

# Definindo informações de contato do desenvolvedor
contato_desenvolvedor = {
    "Email": "davidbecam006@gmail.com",
    "Telefone": "+55 027 997602355",
    "Github": "https://github.com/Daviqr1",
    "Linkedin": "https://www.linkedin.com/in/davi-rezende-09540b222/",
    "Instagram": "https://www.instagram.com/davi_b.rezende/",
}

# Título e subtítulo
st.title('Contato do Desenvolvedor')
st.markdown('Entre em contato com o desenvolvedor para mais informações sobre o projeto')

# Exibindo informações de contato com animações
for meio_contato, valor in contato_desenvolvedor.items():
    with st.sidebar.expander(f"{meio_contato}"):
        st.markdown(f"**{meio_contato}:** {valor}")

# Rodapé
st.sidebar.text('Desenvolvido por Davi Rezende 👋')
