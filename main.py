# from unittest import result

from dotenv import load_dotenv
from yarl import Query

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from tavily import TavilyClient

tavily = TavilyClient()

@tool
def search(query: str) -> str:

    """
Tool that searches for the weather in Tokyo. This is a mock implementation and does not perform a real search.
args:
    query (str): The search query.
returns:
    str: The search result.
"""

    print(f"Searching for {query}")
    return "Tokyo weather is sunny"


llm =ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0,
)

tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    query = "What is the weather in Tokyo?"
    print("Hello from langchain-course!")
    print(f"Searching for {query}")
    result = tavily.search(query=query)
    print(result)



if __name__ == "__main__":
    main()
