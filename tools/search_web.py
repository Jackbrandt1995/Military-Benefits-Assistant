import httpx
from typing import List

class SearchWebTool:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.endpoint = "https://google.serper.dev/search"

    async def search(self, query: str) -> List[str]:
        headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }
        payload = { "q": query, "num": 3 }
        async with httpx.AsyncClient() as client:
            response = await client.post(self.endpoint, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            return [f"{item['title']}\n{item['link']}" for item in data.get("organic", [])]
