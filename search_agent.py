# This agent uses the remote Exa MCP server to search the web.
# Exa's endpoint speaks the Streamable HTTP transport only (SSE is not served),
# so it must be configured with MCPStreamableHttp.

import os
import sys
from any_agent import AgentConfig, AnyAgent
from any_agent.config import MCPStreamableHttp

# The public endpoint works without a key (rate limited); a key lifts the limits.
exa_api_key = os.environ.get("EXA_API_KEY")
exa_headers = {"x-api-key": exa_api_key} if exa_api_key else None

# note that the actual model name specified after llamafile: below is irrelevant,
# but we left it to show what we used to generate the output saved in the README file
agent = AnyAgent.create(
    "tinyagent",
    AgentConfig(
        model_id="llamafile:Qwen3.5-9B-Q5_K_S",
        api_base="http://localhost:8080",
        instructions="""You must use the available tools to find an answer.""",
        tools=[
            MCPStreamableHttp(
                url="https://mcp.exa.ai/mcp",
                headers=exa_headers,
                tools=["web_search_exa", "web_fetch_exa"],
            ),
        ],
    ),
)

prompt = sys.argv[1] if len(sys.argv) > 1 else """
What are 5 tv shows that are trending in September 2026? Please provide the name of the show, the platform, the exact release date, the genre,
the rating (better using a uniform metric, eg. tomatometer), and a brief description of each. Conclude with a References section with a list
of URLs you have used to prepare your answer.
"""
agent_trace = agent.run(prompt)
print(agent_trace.final_output)
