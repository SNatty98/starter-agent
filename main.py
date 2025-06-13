from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import asyncio
import os

# Load environment variables (API keys).
load_dotenv()

# Initialise the openai model using LangChain wrapper.
model = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Define how firecrawl will be launched.
server_params = StdioServerParameters(
    command="npx",
    env={
        "FIRECRAWL_API_KEY": os.getenv("FIRECRAWL_API_KEY"),
    },
    args=["firecrawl-mcp"]
)


async def main():
    # Start a subprocess to communicate with firecrawl using stdio.

    async with stdio_client(server_params) as (reader, writer):
        # Start a client session over the subprocess.

        async with ClientSession(reader, writer) as session:
            await session.initialize()  # Initialise the session.

            # Load MCP tools from the running session.
            tools = await load_mcp_tools(session)

            # Create react agent using the model and tools.
            agent = create_react_agent(model, tools)

            # Initial message for agent.
            messages = [
                {
                    "role": "system",
                    "content": "You are a very helpful assistant that will scrape websites, crawl pages and extraxt data using Firecrawl tools. Think step by step and use the best tools to help the user."
                }
            ]
            # Print tools.
            print("Available tools: ", *[tool.name for tool in tools])
            print("-" * 60)

            while True:
                user_input = input("\nYou: ")
                if user_input == "quit":
                    print("Goodbye")
                    break

                # Truncate message if too long, otherwise just add as message.
                messages.append({"role": "user", "content": user_input[:175000]})

                try:
                    # Conversation history sent to agent, await response.
                    agent_response = await agent.ainvoke({"messages": messages})
                    # Pull the last item from the response.
                    ai_message = agent_response["messages"][-1].content
                    print("\nAgent:", ai_message)
                except Exception as e:
                    print("Error:", e)

if __name__ == "__main__":
    asyncio.run(main())