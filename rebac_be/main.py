import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from rebac_be.api.router import api_router

app = FastAPI(
    title="Rebac Backend",
    version="0.0.1",
    description="FastAPI backend for permit-rebac",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")

@app.get("/") 
async def main_route():     
  return {"message": "Hey, It is me Goku"}

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("rebac_be.main:app", host="0.0.0.0", port=8000, reload=True)
