import ollama

# Analysing multiple image
img_path_1 = '/Users/shubhamrathod/PycharmProjects/Ollama/llava/image/img1.jpg'
img_path_2 = '/Users/shubhamrathod/PycharmProjects/Ollama/llava/image/img3.jpg'

res = ollama.chat(
    model="llava",
    messages=[
        {
            'role': 'user',
            'content': 'Describe this image:',
            'images': [img_path_1, img_path_2]
        }
    ]
)

print(res['message']['content'])
