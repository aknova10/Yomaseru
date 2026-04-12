from fastapi import FastAPI
from fastapi.responses import JSONResponse
from agents.graph import Orchestrator
from backend.app.schema.payload_schemas import LevelSchema

import asyncio


app = FastAPI()

@app.post("/generate-story")
def generate_story(payload : LevelSchema):
    orc = Orchestrator(tools=[])
    graph = orc.build_graph(tools=[])

    result = asyncio.run(graph.ainvoke({"task" : f"write a Japanese story using vocabulary from {payload.level} level"}))
    # return Response({"story" : result.get("structured_response").story_draft})
    return JSONResponse(content={"story" : result.get("story_board")}, status_code=200)