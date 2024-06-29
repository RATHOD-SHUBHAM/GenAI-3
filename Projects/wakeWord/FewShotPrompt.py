import os

# LLM
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

access_key = os.getenv('access_key')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Todo: LLM ---------------------------------------------------------------------------------------------------

def LLM_Call(query):
    # Todo: Using an example set
    # create our examples set
    examples = [
        {
            "query": "I think i am feeling sick.",
            "answer": "Hospital."
        },
        {
            "query": "Can you take me to office ",
            "answer": "Office."
        },
        {
            "query": "I am really tired, can you go to a hotel",
            "answer": "Hotel."
        },
        {
            "query": "I feel a little dizzy today, Can you take me to hospital",
            "answer": "Hospital."
        },
        {
            "query": "I am hungry, go to the nearest hotel",
            "answer": "Hotel."
        },
        {
            "query": "You are running out of charge.",
            "answer": "charging station."
        },
        {
            "query": "Come pick me",
            "answer": "Summon Vehicle."
        },
        {
            "query": "Come pick me at hospital",
            "answer": "Hospital."
        },
        {
            "query": "Stop here",
            "answer": "Parking Lot."
        },
        {
            "query": "I got some work can you quickly turn towards office",
            "answer": "Office."
        }
    ]

    # Todo: Create a formatter for the few-shot examples
    # create a example template
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

    # now break our previous prompt into a prefix and suffix
    # the prefix is our instructions
    prefix = """
    The following is a expert conversation with an Autonomous Vehicle's AI assistant. The assistant is accurate and always extract the words from the context below. If the agent doesnt know a particular answer, then it says I dont know in a sarcastic way and suggest one of the simlary word from context below.
    
    Context: [Hotel , Hospital, Office, parking lot, charging station, summon vehicle]

    Extract the information from the input based on the above context.
    
    Here are some examples
    """

    # and the suffix our user input and output indicator
    suffix = """
    Input: {query}
    AI: """

    # now create the few shot prompt template
    prompt = FewShotPromptTemplate(
        examples=examples,
        example_prompt=example_prompt,
        prefix=prefix,
        suffix=suffix,
        input_variables=["query"],
        example_separator="\n\n"
    )

    # Query the prompt
    # query = "Dont take left hear, take the third right"
    # query = "Me and my friend want to go clubbing, take me to the nearest club"
    # query = "Road seems super busy, so take the next left"
    query = query
    # print(prompt.format(query=query))

    # Todo: Passing prompt to LLM

    model = ChatOpenAI()

    chain = LLMChain(llm=model, prompt=prompt)

    result = chain.run(query)

    print(result)

if __name__ == '__main__':
    query = input("Enter the prompt here: ")
    LLM_Call(query)