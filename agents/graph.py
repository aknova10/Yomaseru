import asyncio
from langgraph.graph import StateGraph, START, END
from agents.states import AgentState
from agents.nodes import story_node, vocab_node


class Orchestrator:
    def __init__(self, tools):
        self.tools = tools

    def route():
        return "end"
    
    def build_graph(self, tools):

        builder = StateGraph(AgentState)

        builder.add_node("writer", story_node)
        builder.add_node("assistant", vocab_node)

        builder.add_edge(START, "assistant")
        builder.add_edge("assistant", "writer")
        builder.add_edge("writer", END)
        # builder.add_conditional_edges("writer", self.route, {
        #     "map" : "map",
        #     "end" : END
        # })

        graph = builder.compile()
        return graph
    
if __name__=="__main__":
    orc = Orchestrator(tools=[])
    graph = orc.build_graph(tools=[])

    result = asyncio.run(graph.ainvoke({"task" : "write a Japanese story using vocabulary from N3 level"}))

    print(result)
