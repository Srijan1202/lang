# from unittest import result
from typing import List
from unittest import result
from pydantic import BaseModel,Field


from dotenv import load_dotenv
from yarl import Query

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch


class Job(BaseModel):
    title: str = Field(description="Job title")
    company: str = Field(description="Company name")
    location: str = Field(description="Job location")
    description: str = Field(description="Short description")
    salary: str = Field(description="Salary if available")
    url: str = Field(description="Application URL")


class AgentResponse(BaseModel):
    jobs: List[Job]

    
llm =ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0,
)

tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    query = "What is the weather in Tokyo?"
    # print("Hello from langchain-course!")
    # print(f"Searching for {query}")
    result = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content="Search for 3 AI Engineer jobs using LangChain in benaglore on LinkedIn and list their details within last 2 weeks."
                )
            ]
        }
    )

    print(result)
    print(type(result))


if __name__ == "__main__":
    main()
