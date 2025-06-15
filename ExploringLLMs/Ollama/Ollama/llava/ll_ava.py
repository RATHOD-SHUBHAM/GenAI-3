'''
    :docs: https://github.com/ollama/ollama/blob/main/docs/api.md
'''

import time
import base64
from PIL import Image
import requests
import json
import os
import ollama


class ProcessImage:
    def __init__(self):
        self.url = 'http://localhost:11434/api/generate'

    # Todo: Image Preprocessing
    def image_preprocessing(self, image_path):
        '''
        Resize the image,
        Do this if only needed
        :return: creates a new image with name inputImage.jpg
        '''

        image = Image.open(image_path)
        image = image.convert('RGB')
        new_image = image.resize((1024, 1024))
        new_image.save('inputImage.jpg')

    # Todo: Decode image
    def encode_image(self, image_path):
        '''
        Convert the image to base64 format
        :param image_path:
        :return: image decoded to base64 format
        '''
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode('utf-8')

    # Todo: Get Model:
    def get_model(self, model:str):
        """
        :type model: string
        """

        try:
            ollama.chat(model)
            return True
        except ollama.ResponseError as e:
            print('Error:', e.error)
            if e.status_code == 404:
                ollama.pull(model)

            return True

    # Todo: Run Model
    def run_model(self, model, base64_image):
        vision_prompt = """
            You are an extremely knowledgeable Image Analyst.
            Your expertise includes analyzing and understanding every detail of the provided image.
            
            Task:
            Examine the following image in detail and provide a detailed, factual, and accurate explanation of what the image depicts.
            If this is a well-known location, please provide me with every relevant detail.   
            Highlight all the key elements and their significance, and present your analysis in clear, well-structured markdown format.
            Finally, add a list of all the cars, humans, and animals present, including the count and color of the object.
        """

        payload = {
            "model": model,
            "prompt": vision_prompt,
            "stream": False,
            "images": [base64_image]
        }

        result = requests.post(
            self.url,
            data=json.dumps(payload)
        )

        # print('#----------------------------#')
        # print(payload)
        # print('#----------------------------#')
        # print(result)
        # print('#----------------------------#')
        # print(result.text)
        # print('#----------------------------#')

        data = json.loads(result.text)
        response = data["response"]
        # print(response)
        return response


if __name__ == '__main__':
    HOME = os.getcwd()
    # print(HOME)
    ROOT = os.path.dirname(HOME)
    # print(ROOT)

    input_image_path = f'{HOME}/image/img1.jpg'

    # Calculate the start time
    start = time.time()

    # Todo: Image Analysis Object
    im_analysis = ProcessImage()

    # Todo: Preprocess the image
    im_analysis.image_preprocessing(image_path=input_image_path)

    # Todo: Encode image
    # image_path = '/Users/shubhamrathod/PycharmProjects/Ollama/llava/image/img1.jpg'
    image_path = f'{HOME}/inputImage.jpg'
    base64_image = im_analysis.encode_image(image_path=image_path)

    # Todo: Check if model is present
    model_name = "llava"
    status = im_analysis.get_model(model=model_name)
    print(status)


    # Todo: Analyze image
    response = im_analysis.run_model(model =model_name, base64_image=base64_image)
    print(response)

    # Calculate the end time and time taken
    end = time.time()
    length = end - start

    # Show the results : this can be altered however you like
    print("It took", length, "seconds!")


