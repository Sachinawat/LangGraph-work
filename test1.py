import warnings
warnings.filterwarnings('ignore', category=UserWarning, module='langchain_core._api.deprecation')

from langgraph.graph import StateGraph, MessagesState, START, END

def mock_llm(state: MessagesState):
    return {"messages": [{"role": "ai", "content": "hello world"}]}

graph = StateGraph(MessagesState)
graph.add_node(mock_llm)
graph.add_edge(START, "mock_llm")
graph.add_edge("mock_llm", END)
graph = graph.compile()


result = graph.invoke({"messages": [{"role": "user", "content": "hi!"}]})
print(result)



