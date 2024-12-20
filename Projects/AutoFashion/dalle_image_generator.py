from openai import AzureOpenAI, OpenAIError
import json
import requests
import io

client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint="",
    api_key="",
)

def prompt_generate(prompt):
    result = client.images.generate(
        model="dall-e-3", # the name of your DALL-E 3 deployment
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )

    image_url = json.loads(result.model_dump_json())['data'][0]['url']

    image_response = requests.get(image_url)

    # Save the image to an in-memory file
    image_bytes = io.BytesIO(image_response.content)
    print("Image generated and saved to memory")
    return image_bytes.getvalue()
    
