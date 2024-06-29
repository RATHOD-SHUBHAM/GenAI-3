# Todo: Load libraries
import os
from dotenv import load_dotenv

# Todo: Getting the access key
load_dotenv()  # take environment variables from .env.
access_key = os.getenv('access_key')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Todo: Import Libraries
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

import time

# Todo: Instantiating the model
model_1 = ChatOpenAI(temperature = 0,
                   openai_api_key=OPENAI_API_KEY,
                   )

memory = ConversationBufferMemory()

# ------------------------------------- User Query -----------------------------------------------------
# Todo: Few Shot Prompt for user query
examples = [
    {
        "query": "Hello",
        "answer": "hello"
    },
    {
        "query": "I think i am feeling sick",
        "answer": "hospital"
    },
    {
        "query": "Can you take me to office ",
        "answer": "office"
    },
    {
        "query": "I am really tired, lets go home",
        "answer": "home"
    },
    {
        "query": "You are running out of charge",
        "answer": "charging station"
    },
    {
        "query": "I am hungry",
        "answer": "hungry"
    },
    {
        "query": "lets grab food",
        "answer": "hungry"
    },
    {
        "query": "Lets go to Indian restaurant",
        "answer": "indian restaurant"
    },
    {
        "query": "I feel like eating biriyani",
        "answer": "indian restaurant"
    },
    {
        "query": "Japanese maybe",
        "answer": "japanese restaurant"
    },
    {
        "query": "Lets grab something hot to drink",
        "answer": "coffee shop"
    },
    {
        "query": "Stop here",
        "answer": "parking"
    },
    {
        "query": "Come pick me",
        "answer": "summon vehicle"
    },
    {
        "query": "I feel a little dizzy today, Can you take me to hospital",
        "answer": "hospital"
    },
    {
        "query": "take me home, i am really tired and done for the day",
        "answer": "home"
    },
    {
        "query": "lets grab a bite",
        "answer": "hungry"
    },
    {
        "query": "You are low on charge.",
        "answer": "charging station"
    },
    {
        "query": "get me from my current location",
        "answer": "summon vehicle"
    },
    {
        "query": "Come pick me at hospital",
        "answer": "hospital"
    },
    {
        "query": "okay stop",
        "answer": "parking"
    },
    {
        "query": "I got some work can you quickly turn towards office",
        "answer": "office"
    }
]


# Todo: Function Call for chaining the prompt
def LLM_Call(query):
    example_template = """
        Input: {query}
        AI: {answer}
    """

    # create a prompt example from above template
    example_prompt = PromptTemplate(
        input_variables=["history", "query", "answer"],
        template=example_template
    )

    # Todo: Feed examples and formatter to FewShotPromptTemplate
    # the prefix is our instructions
    prefix = """
      You are an expert AI assistant for Autonomous Vehicles.
      
      you understand the intent of the query and match it exactly to list of Context below.
    
      Your expertise involves understanding the user query and matching it to Context below.
      You use the examples below to gain understanding and match the query with the Context and respond accordingly
    
      You only respond and align with the words from the list of Context below .
      Context: [home, hungry , hospital, office, parking, charging station, summon vehicle, coffee shop, hello]
      
      If the user says thank you return the response as thank you
      
      If you dont know a particular answer, respond with 'None.'
    
      Here are some examples
    """

    # The suffix our user input and output indicator
    suffix = """
      Input: {query}
      AI: 
    """

    # Now create the few shot prompt template
    prompt = FewShotPromptTemplate(
        examples=examples,
        example_prompt=example_prompt,
        prefix=prefix,
        suffix=suffix,
        input_variables=["query"],
        example_separator="\n\n"
    )

    # Query the prompt
    query = query
    # print(prompt.format(query=query))

    # Passing prompt to LLM
    chain = LLMChain(llm=model_1,
                     prompt=prompt,
                     memory=memory,
                     verbose=False)

    result = chain.run(query)
    # print(result)

    return result


# ------------------------------------- LLM Response -----------------------------------------------------

model_2 = ChatOpenAI(temperature = 0.7,
                     openai_api_key=OPENAI_API_KEY,
                     streaming = True,
                     callbacks = [StreamingStdOutCallbackHandler()]

                   )


# model_2 = ChatOpenAI(temperature = 1,
#                    openai_api_key=OPENAI_API_KEY,
#                    )


# Todo: Few Shot Prompt for response
reply_examples = [
    {
        "query": "hello",
        "answer": "Hey there, Welcome, my friend! It's truly delightful to have you here. How may I be of service to you today?"
    },
    {
        "query": "home",
        "answer": "On our way to Home."
    },
    {
        "query": "restaurant",
        "answer": "Heading to Indian restaurant"
    },
    {
        "query": "hospital",
        "answer": "Driving to Hospital."
    },
    {
        "query": "office",
        "answer": "Heading to Office."
    },
    {
        "query": "charging station",
        "answer": "Navigating to Charging Station."
    },
    {
        "query": "summon vehicle",
        "answer": "Picking you up from current location."
    },
    {
        "query": "parking",
        "answer": "Stopping at the nearest Parking spot."
    },
    {
        "query": "coffee shop",
        "answer": "Heading to a cafe."
    },
    {
        "query": "thank you",
        "answer": "It's been a pleasure assisting you, my friend! If you ever require help again, don't hesitate to reach out. Take care and goodbye!"
    },
]


# Todo: Function Call for chaining the prompt
def LLM_responce(query):
    example_template = """
        Input: {query}
        AI: {answer}
    """

    # create a prompt example from above template
    example_prompt = PromptTemplate(
        input_variables=["query", "answer"],
        template=example_template
    )

    # Todo: Feed examples and formatter to FewShotPromptTemplate
    # the prefix is our instructions
    prefix = """
      You are an AI assistant for Autonomous Vehicles ready to infuse a touch of creativity and politeness into your response.
      Your goal is to provide engaging and inventive interactions, following the given example.
      
      When the user greets you, you greet the user back in a sweet and polite way.
      
      
      There are three restaurants on the map, Japanese, Indian, Mexican.
      
      When the user specifies the type, then you should respond by saying you are navigating to that specific restaurant.
      
      you can use the example below to respond to the user, infuse a touch of creativity and politeness into your response.
      

      Here are some examples
    """

    # Suffix our user input and output indicator
    suffix = """
      Input: {query}
      AI: 
    """

    # Now create the few shot prompt template
    prompt = FewShotPromptTemplate(
        examples=reply_examples,
        example_prompt=example_prompt,
        prefix=prefix,
        suffix=suffix,
        input_variables=["query"],
        example_separator="\n\n"
    )

    # Query the prompt
    query = query
    # print(prompt.format(query=query))

    # Passing prompt to LLM
    chain = LLMChain(llm=model_2,
                     prompt=prompt
                     )

    result = chain.run(query)
    return result


# ------------------------------------- Main Function -----------------------------------------------------

# def print_animated_text(text):
#     for char in text:
#         print(char, end="", flush=True)
#         # time.sleep(0.02)


if __name__ == '__main__':

    previous_command = 'dummy'
    memory.clear()

    while True:

        query = input("Enter the prompt here: ")

        llm_result = LLM_Call(query)
        print('The key Word is: ', llm_result)

        first_word = llm_result.split()[0]
        # print(first_word)

        if first_word == 'None.':
            print("I'm here to help with certain tasks like driving you home, restaurant , office, or coffee shop, guide you to hospital, , parking station, charging station, I can also summon the vehicle for you. However, feel free to ask for assistance with any of those specific tasks!")
            # llm_response = "I'm here to help with certain tasks like driving you home, restaurant , office, or coffee shop, guide you to hospital, , parking station, charging station, I can also summon the vehicle for you. However, feel free to ask for assistance with any of those specific tasks!"
            # print_animated_text(llm_response)
            # print("\n")
            continue
        elif first_word == 'thank' or first_word == 'Thank':
            llm_response = LLM_responce(first_word)
            for chunk in llm_response:
                continue
            # print_animated_text(llm_response)
            # print("\n")
            break
        else:
            if previous_command == first_word:
                print('Hold on, the task is already in progress')
                continue
            else:
                previous_command = first_word

                LLM_responce(first_word)

                print('\n')