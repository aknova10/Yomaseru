from langchain.agents import create_agent
from langchain_core.messages import BaseMessage
from agents.model_manager import ModelManager


class BaseAgent:

    system_prompt="""Default system prompt to be overridden by inherited agents"""

    def __init__(self, tools, response_format, system_prompt):
        
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
    

    def ainvoke(self, messages, **kwargs) -> dict:
        
        if isinstance(messages, str):
            messages = [{"role" : "user", "content" : "message"}]

        config = kwargs.get("config", {})
        config.setdefault("tags", []).extend(self.tags)

        return self.agent.ainvoke({"messages" : messages}, config=config)
