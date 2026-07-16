from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_ollama import ChatOllama

load_dotenv()


def main():
    print("Hello from langchain-course!")

    information =""" former public official who is the CEO and largest shareholder of Tesla and SpaceX. Musk has been the wealthiest person in the world since 2025, and became the only trillionaire in terms of US dollars in June 2026; as of July 10, 2026, Forbes estimates his net worth to be US$917 billion.

B
"""

    sum_temp =""" given the information {information} about a person i want you to create :
    1. a short summary
    2. two intersting facts about them
    """

    sum_promt_temp = PromptTemplate(
        input_variables =[ "information" ], template=sum_temp
    )

    llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)
    
    # llm=ChatOllama(temperature=0,model="llama3")
    
    chain = sum_promt_temp | llm
    response = chain.invoke({"information": information})

    print(response.content[0]["text"])
if __name__ == "__main__":
    main()
