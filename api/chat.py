from fastapi import FastAPI
from pydantic import BaseModel
import httpx, os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from tools.search_web import SearchWebTool

app = FastAPI()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
ORG_ID = os.getenv("OPENAI_ORG_ID", "")
SERPER_API_KEY = os.getenv("SERPER_API_KEY", "")
search_tool = SearchWebTool(api_key=SERPER_API_KEY)

class ChatRequest(BaseModel):
    user_input: str

def should_use_search_tool(user_input: str) -> bool:
    return any(kw in user_input.lower() for kw in ["find", "search", "link", "lookup", "resource"])

@app.post("/chat")
async def chat_handler(chat: ChatRequest):
    if should_use_search_tool(chat.user_input):
        try:
            links = await search_tool.search(chat.user_input)
            links_str = "\n\n".join(links)
            return { "response": f"Here are some relevant resources:\n\n{links_str}\n\nDisclaimer: Please verify with official sources." }
        except Exception as e:
            return { "error": f"Search tool failed: {str(e)}" }

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "OpenAI-Organization": ORG_ID,
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            { "role": "system", "content": "You are the Military Benefits Assistant..." },
            { "role": "user", "content": chat.user_input }
        ],
        "temperature": 0.2,
        "max_tokens": 500
    }
    async with httpx.AsyncClient(timeout=20) as client:
        try:
            resp = await client.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
            resp.raise_for_status()
            msg = resp.json()["choices"][0]["message"]["content"]
            return { "response": msg + "\n\nDisclaimer: Please verify with official sources." }
        except Exception as e:
            return { "error": str(e) }
