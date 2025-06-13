# Firecrawl REACT Agent CLI

This project is a CLI-based AI assistant that leverages **LangChain**, **LangGraph**, and **Firecrawl MCP tools** to scrape websites, crawl pages, and extract data using a REACT-style agent architecture powered by **OpenAI's GPT-3.5-turbo**.

---

# Features

- Uses **LangGraph's ReAct agent** to perform tool-augmented reasoning.
- Interfaces with **Firecrawl MCP tools** via a subprocess using `npx`.
- Designed for **terminal use** — type prompts and get intelligent responses.
- Loads `.env`-based secrets for API key management.
- Dynamically prints available tools and uses them intelligently.

---

# Getting Started

# 1. Clone the Repository

git clone https://github.com/SNatty98/starter-agent.git
cd firecrawl-agent-cli

# 2. Create a .env file with the following:

OPENAI_API_KEY=your-openai-api-key
FIRECRAWL_API_KEY=your-firecrawl-api-key

# 3. Ensure dependencies are installed

uv add langchain-openai langgraph python-dotenv langchain-mcp-adapters
Node.js
Python 3.7+

# 4. Run the agent

uv run main.py / pip run main.py


## Usage

Once running, the CLI will prompt for an input, the assistant will then 
reason through the task, pick the appropriate firecrawl tool and then return
whatever results.

This assistant has been designed specifically to scrape and crawl websites for data,
similar to an enhanced search engine.

To exit, type 'quit'

### Care

This tool uses the OpenAI and Firecrawl APIs, so using this assistant may incur 
charges. It would be best to monitor API usage to ensure costs are not too high!

