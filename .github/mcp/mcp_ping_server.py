from typing import Any, Dict
from mcp.server.fastmcp import FastMCP
app = FastMCP("mcp-ping")

@app.tool()
def ping(message: str = "pong") -> Dict[str, Any]:
    "Return the message back (health-check)."
    return {"ok": True, "echo": message}

if __name__ == "__main__":
    # FastMCP 표준 실행 (기본 STDIO) — 최신 SDK 권장 방식
    app.run()
