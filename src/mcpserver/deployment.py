# server.py
from mcp.server.fastmcp import FastMCP

# create a MCP server
mcp = FastMCP("Demo")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers
    """

    return a + b