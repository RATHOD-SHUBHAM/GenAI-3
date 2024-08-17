import os
from langchain_community.utilities import SerpAPIWrapper
from langchain_community.utilities import OpenWeatherMapAPIWrapper
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.agents import Tool
from dotenv import load_dotenv

# Load the env variable
load_dotenv()  # take environment variables from .env.

os.environ["OPENWEATHERMAP_API_KEY"] = os.getenv('OPENWEATHERMAP_API_KEY')
os.environ["SERPAPI_API_KEY"] = os.getenv('SERPAPI_API_KEY')
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')


class MYAGENTS:
    def __init__(self):
        self.llm = OpenAI(temperature=0)

    def run_agent(self, user_input):

        # Todo: Generic Tool  -------------------------------------------------
        template = """
        
        You are a cheerful and humarous AI assistant, you help people brighten up their mood and respond back to user query
        
        query = {query}
        """

        prompt = PromptTemplate(
            input_variables=['query'],
            template=template
        )

        # Create Chain
        generic_llm_chain = LLMChain(
            llm = self.llm,
            prompt = prompt
        )

        # Create Tool
        generic_tool = Tool(
            name = 'Generic Agent',
            description='Use this to answer everything apart from news and weather',
            func = generic_llm_chain.run

        )

        # Todo: News Tool  -------------------------------------------------
        search = SerpAPIWrapper()
        news_tools = Tool(
            name="news-agent",
            description="Use this tool to get the latest news",
            func=search.run,
        )

        # Todo: Weather Tool   -------------------------------------------------
        weather = OpenWeatherMapAPIWrapper()
        weather_tools = Tool(
            name="weather-agent",
            description="Use this to answer weather related query",
            func=weather.run,
        )

        # Todo: Combine Tools  -------------------------------------------------
        tools = [news_tools, weather_tools, generic_tool]

        # Todo: Create Agents  -------------------------------------------------
        agent_chain = initialize_agent(
            tools=tools,
            llm=self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=False
        )

        # Todo : Run Agent  -------------------------------------------------
        response = agent_chain(user_input)
        print(response)

        return response['output']