import openai
from src.sys_config import system_instruction

messages = [
    {"role": "system", "content": system_instruction}
]

def ask_order_bot(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
    )

    return response.choices[0].message["content"]