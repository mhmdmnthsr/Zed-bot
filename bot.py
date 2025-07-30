from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import click
import os


load_dotenv()
llm = ChatOpenAI()

history = {}

def get_session_id():
    return 10000

def get_history(session_id):
    if session_id not in history:
        history[session_id] = InMemoryChatMessageHistory()
    return history[session_id]

conversation = RunnableWithMessageHistory(
    llm,
    get_session_id=get_session_id,
    get_session_history=lambda session_id: get_history(session_id),
)

@click.command()
def chat():
    print("🤖 Zed: Hello! Ask me anything. Type 'exit' to quit. Type 'wipe' to wipe memory")
    session_id = get_session_id()

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print(" Adios!")
            break
        elif user_input.lower() == "wipe":
            history[session_id] = InMemoryChatMessageHistory()
            print(" Memory wiped!")
            continue

        response = conversation.invoke(
            {"input": user_input},
            config={"configurable": {"session_id": session_id}}
        )
        print("Zed:", response.content)

if __name__ == "__main__":
    chat()