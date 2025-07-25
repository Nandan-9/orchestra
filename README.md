# Orchestra

## Why this matters
Orchestra provides a modular, extensible framework for exposing multiple AI-powered tools and services over HTTP. By unifying diverse capabilities (such as math, echo, and web search) under a single API, it enables rapid prototyping, integration, and orchestration of intelligent agents. This approach accelerates development, encourages experimentation, and lowers the barrier to building complex, multi-tool applications.

## Goal
The goal of Orchestra is to serve as a unified backend that exposes a collection of composable, streamable microservices ("tools") via HTTP endpoints. Each tool is independently developed but can be managed and orchestrated together, making it easy to build applications that require multiple AI or utility services working in concert.

## Architecture
- **FastAPI-based server**: The core server is built with FastAPI, providing a modern, async web framework for high performance and easy extensibility.
- **Tool modules**: Each tool (e.g., echo, math, web search) is implemented as a separate Python module with its own session management and HTTP interface.
- **Session management**: Tools use async session managers to handle resource allocation and cleanup, coordinated via a combined lifespan context in the main server.
- **Mounting endpoints**: Each tool exposes its own HTTP app, which is mounted under a distinct path (e.g., `/echo`, `/math`, `/web-search`) on the main FastAPI app.
- **Extensibility**: New tools can be added by implementing the required interface and mounting them in the server, without modifying the core logic.

## Local Development Setup

Follow these steps to set up Orchestra for local development:

1. **Clone the repository**
   ```sh
   git clone <repo-url>
   cd orchestra
   ```

2. **Install Python (version 3.13 or higher required)**
   Ensure you have Python 3.13+ installed. You can check your version with:
   ```sh
   python3 --version
   ```

3. **Install dependencies**
   It is recommended to use a virtual environment:
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt  # or use: pip install .
   ```
   If you use `pip install .`, ensure you have [pip](https://pip.pypa.io/en/stable/) and [build](https://pypa-build.readthedocs.io/en/latest/) installed.

4. **Run the server**
   ```sh
   python -m api.server
   ```
   The server will start on [http://localhost:10000](http://localhost:10000) by default.

5. **Access tool endpoints**
   - Echo: `http://localhost:10000/echo`
   - Math: `http://localhost:10000/math`
   - Web Search: `http://localhost:10000/web-search`

---

For development, you can modify or add tools in the `tools/` directory and mount them in `api/server.py`.
