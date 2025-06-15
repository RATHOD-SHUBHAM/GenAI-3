import base64
from mimetypes import guess_type
from openai import AzureOpenAI
import os

os.environ["OPENAI_API_TYPE"] = "azure_ad"
os.environ["OPENAI_API_VERSION"] = "2024-05-01-preview"
os.environ["AZURE_OPENAI_ENDPOINT"] = ""
os.environ["AZURE_OPENAI_API_KEY"] = ''


class ImageAnalyst:
    def __init__(self):
        self.client = AzureOpenAI(
        azure_deployment="gpt-4o",
    )

    # Function to encode a local image into data URL
    def local_image_to_data_url(self, image_path):
        # Guess the MIME type of the image based on the file extension
        mime_type, _ = guess_type(image_path)
        if mime_type is None:
            mime_type = 'application/octet-stream'  # Default MIME type if none is found

        # Read and encode the image file
        with open(image_path, "rb") as image_file:
            base64_encoded_data = base64.b64encode(image_file.read()).decode('utf-8')

        # Construct the data URL
        return f"data:{mime_type};base64,{base64_encoded_data}"

    def analyseImage(self, data_url):
        system_prompt = """
          You are an expert media analyst. Your expertise includes analyzing and understanding every detail that is present in the media.
          Make sure to include every small details and dynamic objects such as traffic signals, historic sites, road signs, and animals.

          Your Task:
          Carefully examine the following media in detail and provide a detailed, factual, and accurate explanation of what the media depicts.
          If this is a well-known location, please provide me with every relevant detail.
          Highlight all the key elements and their significance, and present your analysis in clear, well-structured markdown format.
        """

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system",
                 "content": system_prompt
                 },
                {"role": "user",
                 "content": [
                     {
                         "type": "text",
                         "text": "Describe this image: "
                     },
                     {
                         "type": "image_url",
                         "image_url":
                             {
                                 "url": data_url
                             }
                     }
                 ]}
            ],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def pipe(self, image_path):
        data_url = self.local_image_to_data_url(image_path)
        response = self.analyseImage(data_url=data_url)
        return response
