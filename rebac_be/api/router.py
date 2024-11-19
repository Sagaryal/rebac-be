from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.responses import JSONResponse
import httpx

from rebac_be.utils import format_resources
from rebac_be.config import settings

api_router = APIRouter()

PERMIT_API_URL = f"{settings.permit_api_url}/schema/{settings.permit_proj_id}/{settings.permit_env}/resources"
HEADERS = {"Authorization": f"Bearer {settings.permit_api_key}"}

@api_router.get("/permit-data") 
async def permit_data():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(PERMIT_API_URL, headers=HEADERS)
            response.raise_for_status()
            data = response.json()
        
        formatted_data = format_resources(data)
        return JSONResponse(content=formatted_data)

    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

