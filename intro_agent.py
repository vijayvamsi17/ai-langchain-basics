from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain.agents import create_agent
# from langgraph.checkpoint.memory import InMemorySaver
from langchain.messages import HumanMessage
from langchain_core.runnables import RunnableConfig

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1.0, verbose=True)


@tool
def get_weather(location: str) -> str:
    """Get weather information for a location."""
    return f"Weather in {location}: Sunny, 72°F"


config: RunnableConfig = {"configurable": {"thread_id": "1"}}

agent = create_agent(model=model, tools=[get_weather])

# response = agent.invoke(
#     {"messages": [HumanMessage(content="What is todays weather like in New York?")]},
#     config,
# )

# print(response)
