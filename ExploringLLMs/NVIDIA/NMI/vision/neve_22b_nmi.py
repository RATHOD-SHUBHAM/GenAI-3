import os
import time
import requests, base64
from dotenv import load_dotenv

load_dotenv()

NVIDIA_NMI_KEY = os.getenv('NVIDIA_NMI_KEY')
print(NVIDIA_NMI_KEY)

invoke_url = "https://ai.api.nvidia.com/v1/vlm/nvidia/neva-22b"
stream = True

with open("/Users/shubhamrathod/PycharmProjects/NVIDIA/ThirdEye/input/img14.jpg", "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode()

assert len(image_b64) < 180_000, \
  "To upload larger images, use the assets API (see docs)"

headers = {
  "Authorization": f"Bearer {NVIDIA_NMI_KEY}",
  "Accept": "text/event-stream" if stream else "application/json"
}

payload = {
  "messages": [
    {
      "role": "user",
      "content": f'Describe what you see in this image. <img src="data:image/jpg;base64,{image_b64}" />'
    }
  ],
  "max_tokens": 1024,
  "temperature": 0.20,
  "top_p": 0.70,
  "seed": 0,
  "stream": stream
}


start = time.time()
response = requests.post(invoke_url, headers=headers, json=payload)
end = time.time()

print(end - start)

print(response)

# if stream:
#     for line in response.iter_lines():
#         if line:
#             print(line.decode("utf-8"))
# else:
#     print(response.json())
