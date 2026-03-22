from typing_extensions import TypedDict

class AgentState(TypedDict):
    vocabulary: list
    story_board: list
    final_draft: str