import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
import os

from dotenv import load_dotenv
load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")

if OPENAI_KEY is None:
    st.error("API Key not found. Please check your .env file and ensure it contains OPENAI_API_KEY.")
else:
    llm = ChatOpenAI(temperature=0.7, openai_api_key=OPENAI_KEY, model="gpt-4o-mini")

    st.title("Chat GPT Fake")

    if "messages" not in st.session_state:
        st.session_state.messages = [SystemMessage(content="Eres un asistente encado a la investigación")]

    for smg in st.session_state.messages[1:]:
        with st.chat_message("user" if isinstance(smg, HumanMessage) else "assistant"):
            st.markdown(smg.content)

    if prompt := st.chat_input("Ingrese su mensaje"):
        user_msg = HumanMessage(content=prompt)
        st.session_state.messages.append(user_msg)

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            with st.spinner("Pensando..."):
                response = llm(st.session_state.messages)
            message_placeholder.markdown(response.content)

        st.session_state.messages.append(response)
