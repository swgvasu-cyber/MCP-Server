import json
import aiohttp
from fastmcp import FastMCP

API_BASE = "http://localhost:8000"

mcp = FastMCP("security-scanner")

async def post_json(path: str, payload: dict):
    url = f"{API_BASE}{path}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as resp:
                if resp.status != 200:
                    return {"error": f"Backend returned {resp.status}"}
                return await resp.json()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
async def scan_hash(hash: str) -> str:
    """Scan a file hash using backend /scan/hash endpoint"""
    backend_response = await post_json("/scan/hash", {"hash": hash})
    return json.dumps(backend_response, indent=2)

if __name__ == "__main__":
    mcp.run()
