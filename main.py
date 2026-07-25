# from unittest import result

from dotenv import load_dotenv
from yarl import Query

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch



llm =ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0,
)

tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    query = "What is the weather in Tokyo?"
    # print("Hello from langchain-course!")
    # print(f"Searching for {query}")
    result = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content="Search for 3 AI Engineer jobs using LangChain in the Bay Area on LinkedIn and list their details."
                )
            ]
        }
    )




if __name__ == "__main__":
    main()
