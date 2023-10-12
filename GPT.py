import requests
import json
import os

def promptGPT2(system, text, temp):
  url = "https://api.openai.com/v1/chat/completions"
  headers = {
    "Content-Type": "application/json",
    "Authorization": os.getenv("OPENAI_API_KEY")
    }
  data = {
        "model": "gpt-3.5-turbo",
        "messages": [
          {
            "role": "system",
            "content": system,
          },

          {"role": "user", "content": text}],
        "temperature": temp,
    }
  response = requests.post(url, headers=headers, json=data)
  output = response.json()['choices'][0]['message']['content']

  return output

def getEmbeddings(text):
    url = 'https://api.openai.com/v1/embeddings'
    headers = {
      "Content-Type": "application/json",
      "Authorization": os.getenv("OPENAI_API_KEY")
      }
    data = { 
        "input": text,
        "model": "text-embedding-ada-002"
    }
    response = requests.post(url, headers=headers, json=data)
    
    return response.json()