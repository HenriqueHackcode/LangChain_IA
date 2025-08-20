from langchain_core.chat_history import InMemoryChatMessageHistory

memoria = InMemoryChatMessageHistory()

memoria.add_user_message("O que é Python?")
memoria.add_ai_message("Não sei, só sei que nada sei")

print(memoria.messages)