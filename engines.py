import time
import uuid
import requests
import json
from dotenv import load_dotenv

def create_completion(model, body):
    prompt = body['prompt']
    completion = generate_completion_with_model(prompt, model)
    response = {
        "id": str(uuid.uuid4()),  # Generate a unique ID
        "created": int(time.time()),  # Generate a timestamp
        "model": model,
        "choices": [{"text": completion}]
    }
    return response

def generate_completion_with_model(prompt, model):
    url = f"https://api.openai.com/v1/engines/{model}/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer YOUR_OPENAI_API_KEY"
    }

    data = {
        "prompt": prompt,
        "max_tokens": 60
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()['choices'][0]['text']
    else:
        raise Exception(f"Request to OpenAI API failed with status {response.status_code}. The response was: {response.text}")