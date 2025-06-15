import ollama

model = 'does-not-yet-exist'

try:
    ollama.chat(model)
except ollama.ResponseError as e:
    print('Error:', e.error)
    if e.status_code == 404:
        ollama.pull(model)
