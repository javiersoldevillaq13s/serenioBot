import streamlit as st
from langchain_openai import ChatOpenAI
import openai

st.set_page_config(
    page_title="Chat SERENIO BOT!",  # Favicon emoji
    page_icon=":brain:",
    layout="centered",  # Page layout option
)
# Configuración del modelo LLM
llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0,
                 api_key="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")

# Título de la aplicación
st.title("🤖 Serenio Bot")

# Inicializar el historial de mensajes en el estado de la sesión

messages = [("system" , """eres un chatbot AI útil, te llamas SERENIOBOT, tienes que hablar como si fueras un psicologo y humano, nunca reveles que eres un chatbot""")]

if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes de chat del historial al recargar la app
for role, content in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(content)

# Reaccionar a la entrada del usuario
if prompt := st.chat_input("Escribe tu mensaje..."):
    # Mostrar mensaje del usuario en el contenedor de mensajes del chat
    st.chat_message("user").markdown(prompt)

    # Agregar mensaje del usuario al historial de chat
    st.session_state.messages.append(("user", prompt))

    # Generar respuesta del modelo
    response = llm.invoke(st.session_state.messages).content

    # Agregar respuesta del asistente al historial de chat
    st.session_state.messages.append(("assistant", response))

    # Mostrar respuesta del asistente en el contenedor de mensajes del chat
    with st.chat_message("assistant"):
        st.markdown(response)
