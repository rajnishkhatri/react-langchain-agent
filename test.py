from react_langchain_agent.core.agent import ReActAgent
from react_langchain_agent.tools.text_tools import AVAILABLE_TOOLS
from react_langchain_agent.config.settings import settings

def test_agent():
    print("Testing ReAct Agent...")
    
    # Test settings
    print("\nTesting settings...")
    errors = settings.validate()
    if errors:
        print("Settings errors:", "\n".join(errors))
        return
    print("Settings validation passed!")
    
    # Test agent initialization
    print("\nTesting agent initialization...")
    try:
        agent = ReActAgent(tools=AVAILABLE_TOOLS)
        print("Agent initialized successfully!")
    except Exception as e:
        print("Error initializing agent:", str(e))
        return
    
    # Test agent execution
    print("\nTesting agent execution...")
    test_input = "What is the length of the word: hello"
    try:
        result = agent.run(test_input)
        print("Test input:", test_input)
        print("Agent response:", result)
        print("Agent test passed!")
    except Exception as e:
        print("Error running agent:", str(e))
        return

if __name__ == "__main__":
    test_agent() 