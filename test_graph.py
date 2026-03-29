import asyncio
from langgraph.graph import StateGraph, START, END
from agents.states import AgentState
from agents.nodes import story_node, vocab_node
from agents.graph import Orchestrator


    
if __name__=="__main__":
    orc = Orchestrator(tools=[])
    graph = orc.build_graph(tools=[])

    result = asyncio.run(graph.ainvoke({"task" : "write a Japanese story using vocabulary from N3 level"}))

    print("\n\n\n",result)
