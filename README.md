# mcp-llms-txt

MCP server for [Awesome-llms-txt](https://github.com/SecretiveShell/Awesome-llms-txt). Add documentation directly into your conversation via mcp resources.

## Installation

Setup your claude config like this:

```json
{
    "mcpServers": {
        "mcp-llms-txt": {
            "command": "uvx",
            "args": ["mcp-llms-txt"],
            "env": {
                "PYTHONUTF8": "1"
            }
        }
    }
}
```

## testing

Use [mcp-cli](https://github.com/wong2/mcp-cli) to test the server:

```bash
npx -y "@wong2/mcp-cli" -c config.json
```

The config file is already setup and does not need to be changed since there are no api keys or secrets.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.