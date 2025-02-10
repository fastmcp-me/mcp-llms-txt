import os
import re
import httpx
from mcp.server.lowlevel import Server
import mcp.types as types
from pydantic import AnyUrl

SERVER_NAME = "mcp-llms-txt"

AWESOME_LLMS_TXT = "https://raw.githubusercontent.com/SecretiveShell/Awesome-llms-txt/refs/heads/master/README.md"
AWESOME_LLMS_TXT = os.getenv("AWESOME_LLMS_TXT_URL", AWESOME_LLMS_TXT)

LINE_PATTERN = pattern = re.compile(r"- \[(.*?)\]\((https?://.*?)\)")

server = Server(name=SERVER_NAME)

@server.list_resources()
async def list_resources() -> list[types.Resource]:
    async with httpx.AsyncClient() as client:
        response = await client.get(AWESOME_LLMS_TXT)
    
    resources = []

    for line in response.text.splitlines():
        
        match = re.match(pattern, line)
        if not match:
            continue

        description = f"llms.txt file for {match.group(1)}"

        resource = types.Resource(
            uri=AnyUrl(match.group(2)),
            name=match.group(1),
            description=description,
            mimeType="text/markdown",
        )
        resources.append(resource)
    
    return resources


@server.read_resource()
async def handle_read_resource(uri: AnyUrl) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(str(uri))

    if response.status_code != 200:
        raise Exception(f"Failed to fetch {uri}")
    
    return response.text

if __name__ == "__main__":
    import asyncio
    asyncio.run(list_resources())