

import requests

url = "http://192.168.100.59:1234/v1/chat/completions"

data = {
    "model": "qwen/qwen3.5-9b",
    "messages": [
        {"role": "user", "content": "你好"}
    ]
}

res = requests.post(url, json=data)
print(res.json())