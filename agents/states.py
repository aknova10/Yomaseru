from typing_extensions import TypedDict

class AgentState(TypedDict):
    level: str
    vocabulary: list
    story_board: list
    final_draft: str