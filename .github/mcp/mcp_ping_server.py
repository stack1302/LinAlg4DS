import asyncio
from typing import Any, Dict
from mcp.server.fastmcp import FastMCP
app = FastMCP("mcp-ping")
@app.tool()
def ping(message: str = "pong") -> Dict[str, Any]:
    return {"ok": True, "echo": message}
@app.resource("readme")
def readme() -> str:
    return "MCP sample server is running."
if __name__ == "__main__":
    asyncio.run(app.run_stdio())
