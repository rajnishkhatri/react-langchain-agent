"""Main entry point for the React LangChain Agent."""
from react_langchain_agent.config.settings import settings
from react_langchain_agent.core.agent import ReActAgent
from react_langchain_agent.tools.text_tools import AVAILABLE_TOOLS


def main():
    """Main entry point for the application."""
    # Validate settings
    errors = settings.validate()
    if errors:
        print("Configuration errors:")
        for error in errors:
            print(f"- {error}")
        return

    print("Hello ReAct LangChain!")
    
    # Initialize and run agent
    agent = ReActAgent(tools=AVAILABLE_TOOLS)
    result = agent.run("What is the length of the word: rajnish khatri")
    print("Final result:", result)


if __name__ == "__main__":
    main()
