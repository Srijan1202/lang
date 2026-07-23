from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain.core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-pro-preview",
    project="your-project-id",
    vertexai=True,
)

def main():
    print("Hello from langchain-course!")


if __name__ == "__main__":
    main()
