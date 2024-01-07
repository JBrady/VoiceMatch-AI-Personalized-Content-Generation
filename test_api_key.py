import os
import requests 
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

MODEL_ENGINE = "gpt-4-1106-preview"

prompt = "What is the capital of France?"

data = {
  "model": MODEL_ENGINE,
  "messages": [
    {"role": "user", "content": prompt}
  ]
} 

headers = {
  "Authorization": f"Bearer {OPENAI_API_KEY}"  
}

response = requests.post("https://api.openai.com/v1/chat/completions",  
                         json=data, 
                         headers=headers)

if response.status_code == 200:
  print("Success!")
  print(response.json())
else:
  print(f"Error with code {response.status_code}") 
  print(response.text)
