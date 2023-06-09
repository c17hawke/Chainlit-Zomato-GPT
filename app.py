import chainlit as cl
from src.llm import ask_order_bot, messages


@cl.on_message
def main(message: str):
    # Your custom logic goes here...
    messages.append({"role": "user", "content": message})
    response = ask_order_bot(messages)
    messages.append({"role": "assistant", "content": response})
    # Send a response back to the user
    cl.Message(
        content=response,
    ).send()

