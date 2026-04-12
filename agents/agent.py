from typing import Any
from langchain.agents import create_agent
from langchain_core.messages import BaseMessage
from agents.model_manager import ModelManager
from agents.agent_schemas import StoryDraftFormat, VocabFormat

class BaseAgent:

    system_prompt="""Default system prompt to be overridden by inherited agents"""

    def __init__(self, tools: list = [], response_format: Any = None, system_prompt: str = system_prompt):
        
        model_obj = ModelManager()

        self.model = model_obj.select_model()
        self.tags = [self.model.__class__.__name__.lower()]
        self.tools = tools
        self.response_format = response_format

        self.agent = create_agent(model=self.model, tools=self.tools, system_prompt=system_prompt, response_format=self.response_format)


    def invoke(self, messages, **kwargs) -> dict:
        
        if isinstance(messages, str):
            messages = [{"role" : "user", "content" : "message"}]

        config = kwargs.get("config", {})
        config.setdefault("tags", []).extend(self.tags)

        return self.agent.invoke({"messages" : messages}, config=config)
    

    async def ainvoke(self, messages, **kwargs) -> dict:
        
        if isinstance(messages, str):
            messages = [{"role" : "user", "content" : "message"}]

        config = kwargs.get("config", {})
        config.setdefault("tags", []).extend(self.tags)

        return await self.agent.ainvoke({"messages" : messages}, config=config)
    

class StoryDirectorAgent(BaseAgent):
    system_prompt = """You are a story director. Your role is to create a list of events in some chronological order, such that it can be written into a story. 
    """

    def __init__(self, response_format=StoryDraftFormat, system_prompt=system_prompt):
        super().__init__(response_format=response_format, system_prompt=system_prompt)
class StoryWriterAgent(BaseAgent):
    system_prompt = """You are a Japanese short story writer who is capabale of writing stories with just given list of vocabulary. 
    Draft meaningfull stroies with morals."""

    def __init__(self, response_format=StoryDraftFormat, system_prompt=system_prompt):
        super().__init__(response_format=response_format, system_prompt=system_prompt)


class AssistantStoryWriterAgent(BaseAgent):
    system_prompt = """You are an asistant of a Japanese short story writer who is tasked with fetching usable vocabulary. 
    Use relevant tools to determine which words to use in the story."""
    def __init__(self, tools=[], response_format=VocabFormat, system_prompt=system_prompt):
        super().__init__(tools, response_format=response_format, system_prompt=system_prompt)


class EditorAgent(BaseAgent):
    system_prompt = """You are a Japanese editor who is tasked with proof reading. 
    Make sure that the any words outside the given vocabulary is in hiragana."""
    def __init__(self, tools = [], response_format = None, system_prompt = system_prompt):
        super().__init__(tools=tools, response_format=response_format, system_prompt=system_prompt)

