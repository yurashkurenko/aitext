import openai

def ask_openai(prompt):
    # Укажите ваш API ключ
    openai.api_key = "52b2e6028c662ebdf1d83405c661da6cc0dc45a424a48135945d870a2744259d"
    # Замените 'your-api-key-here' на ваш реальный API-ключ

    try:
        # Запрос к OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Можно указать другую модель, например, gpt-4
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Извлечь ответ из ответа API
        answer = response['choices'][0]['message']['content']
        return answer

    except Exception as e:
        return f"Произошла ошибка: {str(e)}"

# Пример использования функции
if __name__ == "__main__":
    user_input = "Какова столица Франции?"
    response = ask_openai(user_input)
    print("Ответ нейросети:", response)
