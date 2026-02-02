from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

# 加载 .env
load_dotenv()

#1 Initialize the OPENAI MODEL
llm = ChatOpenAI(
    model = "gpt-4o",
    temperature = 0
)

#2 Define your tools
tools = [TavilySearch(max_results = 3,)]

#3 Creat the agent
agent = create_agent(
    model = llm,
    tools = tools,
    system_prompt = "You are a helpful search assistant that uses tools to find informations"
)

#4 Invoke the agent
input_data = {"messages": [("user","Elon Musk 最近在做什么?")]}
response = agent.invoke(input_data)

print(response["messages"][-1].content)
