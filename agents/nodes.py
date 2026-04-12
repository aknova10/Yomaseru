from agents.states import AgentState

from agents.agent import StoryWriterAgent, AssistantStoryWriterAgent
from langchain_mcp_adapters.client import MultiServerMCPClient

async def story_node(state: AgentState):

    print("#####Writer Node Accessed####")
    story_agent = StoryWriterAgent()
    print("writer state \n\n",state)
    response = await story_agent.ainvoke(messages=f"{state}")
    print(state)
    return {"story_board" : response.get("structured_response").story_draft}

async def vocab_node(state: AgentState):
    print("#####Assistant Node Accessed####")
    client = MultiServerMCPClient({
        "Yomaseru MCP" : {
            "transport" : "streamable-http",
            "url" : "http://127.0.0.1:9000/mcp",
        }
    })

    tools = await client.get_tools()

    assistant_agent = AssistantStoryWriterAgent(tools=tools)
    response = await assistant_agent.ainvoke(messages=f"{state}")
    print(response.get("structured_response"))
    return {"vocabulary" : response.get("structured_response").vocab_list}