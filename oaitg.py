import requests
import json

def get_ai_response(prompt, api_key):
    # URL для Together AI API
    url = "https://api.together.xyz/inference"
    
    # Заголовки запроса
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Параметры запроса
    payload = {
        "model": "gpt-3.5-turbo", # или другая доступная модель
        "prompt": prompt,
        "max_tokens": 1000,
        "temperature": 0.7,
        "top_p": 0.9,
    }
    
    try:
        # Отправка POST запроса
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        # Получение результата
        result = response.json()
        return result['output']['text']
        
    except requests.exceptions.RequestException as e:
        return f"Ошибка при отправке запроса: {str(e)}"
    except KeyError as e:
        return f"Ошибка в структуре ответа: {str(e)}"
    except Exception as e:
        return f"Неожиданная ошибка: {str(e)}"

# Пример использования
if __name__ == "__main__":
    api_key = "52b2e6028c662ebdf1d83405c661da6cc0dc45a424a48135945d870a2744259d"
    prompt = "Расскажи мне о Python"
    
    response = get_ai_response(prompt, api_key)
    print(response)
