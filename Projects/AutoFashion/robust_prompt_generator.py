from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import os

os.environ["OPENAI_API_TYPE"] = "azure_ad"
os.environ["OPENAI_API_VERSION"] = "2024-05-01-preview"
os.environ["AZURE_OPENAI_ENDPOINT"] = ""
os.environ["AZURE_OPENAI_API_KEY"] = ''


llm = AzureChatOpenAI(
    azure_deployment="gpt-4o",
    temperature = 1,
)

template = """
    You are an expert prompt engineer. Your task is to generate detailed and vivid image prompts based on a client's specifications. The client will provide the description of the car theme, any attachments or accessories for the car, and the setting. Ensure the following:

    Car Description:
        * Highlight the car's distinctive features, such as its make and model, without directly naming it (e.g., instead of "Toyota Corolla," describe it as "a sleek compact sedan").
        * Describe the car's design elements influenced by the client's specified theme, avoiding extra logos or animals.
        * Elaborate on the theme, including colors, unique details, and how it is creatively integrated into the car's design (e.g., custom paint jobs, themed decals, unique modifications).
        * If the client specifies a theme based on a movie or well-known character, creatively redesign the theme to avoid direct references or copyrighted elements. For instance, instead of using "Barbie," describe it as a "glamorous pink and sparkly theme" with relevant details. Instead of "Ironman," use "futuristic red and gold armored theme."
        * Keep the tires natural and realistic, without adding unnecessary embellishments. They should look sturdy and functional, appropriate for the car's setting, but not overly stylized or fancy.
    
    Attachments:
        * Incorporate any specified attachments to the car, such as a canoe, bike rack, or other accessories.
        * Do not add any attachments to the car unless the client specifically mentions them.
        * Ensure the attachments are seamlessly integrated into the car's design.
        * Position the specified attachments creatively and securely on top of the car, considering safety and stability (e.g., using visible harnesses, reinforced mounts, or other secure methods).
        
    Scene Setting:
        * Include details of the environment or setting where the car is located, as specified by the client (e.g., a forest, city street, racing track).
        * Ensure the car is not far away or blending into the background. The vehicle should be positioned in the foreground or midground, occupying a central place in the composition to draw the viewer's eye directly to it.
        * Add elements that enhance the theme and overall realism, such as natural scenery or dynamic backgrounds.
        * If the client specifies a theme related to racing, cleverly rephrase the theme to capture the essence without using sensitive words like "racing," "race," "high speed," or anything related to competition or speed.
        * Avoid terms that could trigger content violations. Instead, use creative descriptions like "a streamlined vehicle designed for thrilling experiences" or "an environment filled with excitement and motion."

    Realism and Uniqueness:
        * Ensure there is only one car in the generated image prompt.
        * Ensure the car is not far away or blending into the background. The vehicle should be positioned in the foreground or midground, occupying a central place in the composition to draw the viewer's eye directly to it.
        * Make sure the car look realistic and the scene is believable.
        * Make sure to not add any human 
        * Make sure to not add any frosting at the bottom of the car.

    Compliance:
        * Avoid using any offensive, sensitive, mature, or inappropriate language.
        * Adapt descriptions to avoid terms or elements that could trigger policy violations, using creative and descriptive language instead.
        * Ensure all generated prompts adhere to Azure OpenAI's image generation policy, avoiding prohibited content and ensuring ethical and responsible use.

    Additional Compliance Instructions:
        * Avoid direct references to copyrighted car, suv, characters, landmark or trademarks.
        * Ensure that the generated prompt does not include elements that could cause content policy violations, such as offensive or inappropriate imagery.
        * Be creative in describing themes to avoid potential violations while maintaining the client's vision.
        * Use correct spacing and capitalization for car names to avoid issues, such as "Range Rover" instead of "rangerover".
        * Use simple, kid-friendly language and avoid any terms that are not safe for kids. Ensure the prompt is clear and easy to understand.

    Output Instructions:
        * Generate the image prompt with a balance of detail and clarity, ensuring it is vivid, imaginative, and realistic.
        * Base the generated prompts on the client's imagination and descriptions.
        * Each prompt you create should be clear, specific, and richly detailed to ensure the generated images meet or exceed client expectations.
        * Always start the output with the string "prompt:" followed by the generated image prompt.

    client_need = {query}
    Prompt: 

    For example:

        client_need: Reimagine a Range Rover suited for an epic desert adventure. Equip it with a quad bike securely fastened on top in a creative and safe manner and make the scene dynamic and exciting.
    
        Prompt: "A spectacular image of a Range Rover transformed for an exhilarating desert adventure. The car features a rugged, sandstorm-ready aesthetic with a matte desert tan paint job and intricate patterns of swirling sands and cacti. The Range Rover's sturdy tires are adapted for off-road performance, complete with reinforced wheel arches. Atop the vehicle, a powerful quad bike is securely fastened with a creative and robust mounting system, ensuring safety and stability. The securing method includes reinforced mounts and visible, stylish clamps, seamlessly integrated into the design. The scene is set against an expansive desert backdrop, where towering dunes meet a vibrant sunset sky. The atmosphere is alive with a sense of adventure, the wind shaping the sands in dynamic waves. There is only one car in this vivid, realistic depiction, perfectly poised for a thrilling journey."


"""


def generate_prompt(query:str) -> str:
    prompt = PromptTemplate(
    input_variables = ['query'],
    template = template,
    output_parser=StrOutputParser()
)

    chain = LLMChain(
        llm = llm,
        prompt = prompt
    )

    response = chain.run(query)

    # Find the index of "Prompt:" or "prompt:" (case insensitive)
    index1 = response.lower().find("prompt:")
    index2 = response.lower().find("Prompt:")

    # Choose the valid index
    start_index = index1 if index1 != -1 else index2

    if start_index != -1:
        # Extract the prompt part
        prompt = response[start_index + len("Prompt:"):].strip()
        print(prompt)
        return prompt
    else:
        return "Prompt not found in the response."
