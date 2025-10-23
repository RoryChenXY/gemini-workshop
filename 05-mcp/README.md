# Model Context Protocol (MCP)

In this part, you'll learn how to connect Gemini to a locally running MCP server, and to a remote MCP server.

[Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) is an open standard for connecting AI applications with external tools and data. MCP provides a common protocol for models to access context, such as functions (tools), data sources (resources), or predefined prompts.

The Gemini SDKs have built-in support for MCP, reducing boilerplate code and offering automatic tool calling for MCP tools. When the model generates an MCP tool call, the Python and JavaScript client SDK can automatically execute the MCP tool and send the response back to the model in a subsequent request, continuing this loop until no more tool calls are made by the model.

## What is MCP?

Model Context Protocol (MCP) is a revolutionary approach to extending AI capabilities. Unlike traditional function calling where you define functions locally in your code, MCP allows AI models to connect to remote servers that provide tools and resources.

- 🔌 Plug-and-Play Integration: Connect to any MCP-compatible service instantly
- 🌐 Remote Capabilities: Access tools and data from anywhere on the internet
- 🔄 Standardized Protocol: One protocol works with all MCP servers
- 🔒 Centralized Security: Control access and permissions at the server level
- 📈 Scalability: Share resources across multiple AI applications
- 🛠️ Rich Ecosystem: Growing library of MCP servers for various use cases

## Working with Stdio MCP Servers

Stdio (Standard Input/Output) servers run as local processes and communicate through pipes. This is perfect for:

- Development and testing
- Local tools and utilities
- Lightweight integrations

## 1. Run a local MCP server

We use [FastMCP](https://github.com/jlowin/fastmcp) to spin up a local MCP server:

```
pip install fastmcp
```

Optional: Inspect the server:

```
fastmcp dev server.py
```

Run the server:

```
fastmcp run server.py
```

This server exposes one tool `def add(a: int, b: int)` that can add two numbers.

## 2. Run Gemini with MCP support

This client script connects Gemini with the locally running MCP server.

Make sure `mcp` is installed:

```
pip install mcp
```

In a separate terminal window, run:

```
python gemini.py
```

Start chatting and e.g. ask "Add 5 and 9". It should call the MCP tool.


## 3. Connect to a remote MCP server

This example shows how to connect to a remote MCP server.

The script connects to the DeepWiki MCP server (`https://mcp.deepwiki.com/mcp`, a remote server providing access to Wikipedia-like data). The agent should allow users to ask questions about GitHub repositories, and it will use the DeepWiki server to find answers.

```
python gemini_remote.py
```

Now you can start chatting and ask infos about repos, e.g.:

```
Tell me more about huggingface/transformers
```
