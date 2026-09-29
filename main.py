import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

# Import the agent so ADK can initialize it
from agent import root_agent


async def main():
    print("=" * 40)
    print("Google ADK Chatbot")
    print("Type 'exit' to quit")
    print("=" * 40)

    while True:
        user = input("\nYou: ")

        if user.lower() == "exit":
            break

        # Placeholder: in ADK, conversations are normally run through
        # the ADK runner or the `adk web` interface rather than calling
        # the Agent object directly.

        print("\nAssistant:")
        print("Run this agent using the ADK runner or `adk web`.")


if __name__ == "__main__":
    asyncio.run(main())