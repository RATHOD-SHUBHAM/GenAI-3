import base64
from io import BytesIO
from langchain_community.llms import Ollama
from PIL import Image
import time


def convert_to_base64(pil_image):
    """
    Convert PIL images to Base64 encoded strings

    :param pil_image: PIL image
    :return: Re-sized Base64 string
    """

    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")  # You can change the format if needed
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str


def run_llm(image_b64):
    llm = Ollama(base_url="http://localhost:11434", model="llava")

    vision_prompt = """
        You are an extremely knowledgeable Image Analyst.
        Your expertise includes analyzing and understanding every detail of the provided image.

        Task:
        Examine the following image in detail and provide a detailed, factual, and accurate explanation of what the image depicts.
        If this is a well-known location, please provide me with every relevant detail.   
        Highlight all the key elements and their significance, and present your analysis in clear, well-structured markdown format.
        Finally, add a list of all the cars, humans, and animals present, including the count and color of the object.
    """

    resp = llm.invoke(vision_prompt, images=[image_b64])

    print(resp)


def main(file_path):
    file_path = file_path

    pil_image = Image.open(file_path)

    image_b64 = convert_to_base64(pil_image)

    run_llm(image_b64=image_b64)


if __name__ == '__main__':

    file_path = "/Users/shubhamrathod/PycharmProjects/Ollama/llava/image/img1.jpg"

    # Calculate the start time
    start = time.time()

    main(file_path=file_path)

    # Calculate the end time and time taken
    end = time.time()
    length = end - start

    # Show the results : this can be altered however you like
    print("It took", length, "seconds!")
