import streamlit as st
from modelo_openai import chain_memoria, conversas


def abrir_chat(prompt, chain_memoria, conversas):
    area = st.selectbox("Selecione qual área do Python quer tirar dúvida?", options=["Dados", "Sites", "Automações"])
    config = {"configurable": {"session_id": area}}

    if prompt:
        chain_memoria.invoke({"mensagem": prompt}, config=config)

    if area in conversas:
        for mensagem in conversas[area].messages:
            if mensagem.type != "system":
                with st.chat_message(mensagem.type):
                    st.write(mensagem.content)

            
def meu_app():
    st.header("Master Python", divider=True)
    st.markdown("#### Tire suas dúvidas sobre Python")
    prompt = st.chat_input("Digite aqui seu prompt")
    abrir_chat(prompt, chain_memoria, conversas)
    

        

if __name__ == "__main__":
    meu_app()


