from fastmcp import FastMCP

mcp = FastMCP("mcp_server")

@mcp.tool()
def get_weather(location: str) -> str:
    """Get weather information for a location."""
    return f"Weather in {location}: Sunny, 72°F"

if __name__ == "__main__":
    mcp.run(transport="stdio")