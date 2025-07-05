from langgraph.graph import StateGraph

from AgentState import AgentState
from greeting_node import greeting_node

graph = StateGraph(AgentState)
graph.add_node("greeter", greeting_node)
graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

app = graph.compile()