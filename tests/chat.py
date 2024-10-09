import requests
import json

# Get a response using a prompt without streaming
payload = {
    "model": "./dist/TinyLlama-1.1B-Chat-MLC/",
    "prompt": "What is the capital of France?",   
}

response = requests.post("http://127.0.0.1:8000/v1/completions", json=payload)

if response.status_code != 200:
   print(f"Error: {response.status_code} - {response.text}")

response = json.loads(response.text)
print(response)