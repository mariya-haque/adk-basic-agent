from google.adk.agents import Agent

root_agent = Agent(
    name="basic_chatbot",
    model="gemini-3.5-flash",
    instruction="""
You are a helpful AI assistant.
Always answer clearly and politely.
"""
)