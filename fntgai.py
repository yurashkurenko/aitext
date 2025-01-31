from openai import OpenAI
import os
def getcontent(query):
    TOGETHER_API_KEY = "52b2e6028c662ebdf1d83405c661da6cc0dc45a424a48135945d870a2744259d"
    client = OpenAI(api_key=TOGETHER_API_KEY,base_url='https://api.together.xyz',)
    chat_completion = client.chat.completions.create(
    messages=[
    {
      "role": "system",
      "content": "Ты писатель на Русском языке",
    },
    {
      "role": "user",
      "content": query,
    }
    ],
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    max_tokens=4096
    )
    return chat_completion.choices[0].message.content

#print(getcontent("Напиши книгу самоучитель python"))
