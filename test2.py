from langchain.agents import create_agent


def weather_agent(city:str) -> str:
    return f"the whether in {city} is sunny"


agent = create_agent(
    tools=[weather_agent],
    model="gpt-3.5-turbo",
    system_prompt="you are a helpful assistant"
)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in New York?"}]}
)

print(response)