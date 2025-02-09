from mcp.server.lowlevel import Server
import mcp.types as types
from pydantic import AnyUrl

SERVER_NAME = "mcp-llms-txt"

server = Server(name=SERVER_NAME)

@server.list_resources()
async def list_resources() -> list[types.Resource]:
    return []


@server.read_resource()
async def handle_read_resource(uri: AnyUrl) -> str:
    return "Hello, world!"
