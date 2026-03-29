from pydantic import BaseModel, Field

class StoryDraftFormat(BaseModel):
    event_list: list = Field(description="list of events that happen in the story")
    story_draft: str = Field(description="events placed in chronological order to make the story")

class VocabFormat(BaseModel):
    vocab_list: list = Field(description="list of vocab that can be used in the story")

