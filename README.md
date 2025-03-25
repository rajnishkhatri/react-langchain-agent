# React LangChain Agent

A Python project that demonstrates the implementation of a LangChain agent using the ReAct (Reasoning + Acting) pattern. The agent can perform various tasks using tools, with the current implementation focusing on text analysis.

## Quick Demo 🚀

Try the interactive demo:

```bash
# Install the package
pipenv install

# Run the Gradio interface
pipenv run python -m react_langchain_agent.interface.app
```

This will launch a web interface where you can:
- Input text queries
- See the agent's thought process
- Get instant results
- Try pre-defined examples

## Project Overview for Different Audiences

### For High School Students 🎓
Think of this project as a smart assistant that can:
- Count the number of letters in words or sentences
- Show you exactly how it thinks about solving problems
- Explain its reasoning step by step
- Use tools to help it solve problems

It's like having a helpful friend who:
1. Listens to your questions
2. Thinks about how to solve them
3. Uses available tools to find answers
4. Explains their thinking process

### For AI Engineers 👨‍💻
This implementation demonstrates:
- ReAct pattern integration with LangChain's agent framework
- Custom tool development and registration using `@tool` decorator
- Prompt engineering with structured output parsing
- State management through agent scratchpad
- Custom callback implementation for LLM interaction monitoring
- Environment configuration and dependency management
- Type hints and proper error handling

Key technical features:
```python
agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_log_to_str(x["agent_scratchpad"]),
    }
    | prompt
    | llm
    | ReActSingleInputOutputParser()
)
```

### For AI Solution Architects 🏗️
This project serves as a foundation for:
- **Modular AI System Design**: 
  ```
  react_langchain_agent/
  ├── src/
  │   └── react_langchain_agent/
  │       ├── config/        # Configuration management
  │       ├── core/         # Core agent functionality
  │       ├── tools/        # Tool implementations
  │       └── utils/        # Utility functions
  ├── tests/               # Test files
  └── setup.py            # Package installation
  ```
- **Scalable Architecture**: 
  - Tool registration pattern for easy extension
  - Callback system for monitoring and logging
  - Environment-based configuration
- **Integration Patterns**:
  - LLM integration via OpenAI
  - Tool integration via LangChain
  - State management via agent scratchpad
- **Best Practices**:
  - Security (environment variables)
  - Dependency management (Pipenv)
  - Code organization
  - Error handling

### For AI Scientists 🔬
This implementation provides a framework for:
- **Cognitive Architecture Research**:
  - ReAct pattern implementation for studying reasoning and action loops
  - Observable thought process through structured prompting
  - Tool utilization patterns in LLM-based agents
- **Agent Behavior Analysis**:
  - Step-by-step reasoning transparency
  - Decision-making process monitoring
  - Tool selection and utilization patterns
- **Research Extensions**:
  - Memory mechanisms integration
  - Multi-tool reasoning
  - Meta-learning capabilities
  - Prompt optimization studies

## Features

### Core Components
1. **Configuration Management** (`config/settings.py`):
   ```python
   class Settings:
       OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
       TEMPERATURE: float = 0.0
       STOP_SEQUENCES: list[str] = ["\nObservation", "Observation"]
   ```

2. **Agent Implementation** (`core/agent.py`):
   - ReAct pattern implementation
   - Tool management
   - State handling
   - Error management

3. **Tools** (`tools/text_tools.py`):
   ```python
   @tool
   def get_text_length(text: str) -> int:
       """Returns the length of a text by characters."""
       return len(text.strip())
   ```

4. **Monitoring** (`utils/callbacks.py`):
   - LLM interaction tracking
   - Error logging
   - Performance monitoring

## Setup

1. Clone the repository:
```bash
git clone git@github.com:rajnishkhatri/react-langchain-agent.git
cd react-langchain-agent
```

2. Install dependencies:
```bash
pipenv install
```

3. Create a `.env` file with your OpenAI API key:
```bash
OPENAI_API_KEY=your-api-key-here
```

4. Run the main script:
```bash
pipenv run python main.py
```

## Project Structure

```
react_langchain_agent/
├── src/
│   └── react_langchain_agent/
│       ├── config/
│       │   ├── __init__.py
│       │   └── settings.py        # Configuration management
│       ├── core/
│       │   ├── __init__.py
│       │   ├── agent.py          # Agent implementation
│       │   └── prompts.py        # Prompt templates
│       ├── interface/
│       │   ├── __init__.py
│       │   └── app.py            # Gradio web interface
│       ├── tools/
│       │   ├── __init__.py
│       │   └── text_tools.py     # Tool implementations
│       └── utils/
│           ├── __init__.py
│           └── callbacks.py      # Monitoring utilities
├── tests/
│   ├── __init__.py
│   └── test_tools.py            # Tool tests
├── main.py                      # CLI entry point
├── setup.py                     # Package configuration
├── Pipfile                      # Dependencies
└── README.md                    # Documentation
```

## Usage Examples

### Basic Text Analysis
```python
from react_langchain_agent.core.agent import ReActAgent
from react_langchain_agent.tools.text_tools import AVAILABLE_TOOLS

agent = ReActAgent(tools=AVAILABLE_TOOLS)
result = agent.run("What is the length of the word: hello world")
print(result)  # Output: {'output': '11'}
```

### Custom Tool Integration
```python
from langchain.agents import tool

@tool
def custom_tool(input: str) -> str:
    """Custom tool description"""
    return process(input)

# Add to available tools
AVAILABLE_TOOLS.append(custom_tool)
```

## Testing

The project includes comprehensive test coverage through multiple test files:

### Running Tests
```bash
# Run all tests
PYTHONPATH=$PYTHONPATH:$(pwd)/src pipenv run python test.py
PYTHONPATH=$PYTHONPATH:$(pwd)/src pipenv run python test_interface.py

# Or run individual test files:
# Core agent tests
pipenv run python test.py

# Interface tests
pipenv run python test_interface.py
```

### Test Coverage

1. **Core Agent Tests** (`test.py`):
   - Settings validation
   - Agent initialization
   - Tool registration
   - Query processing
   - Error handling

2. **Interface Tests** (`test_interface.py`):
   - Process input function
   - Gradio interface creation
   - Component configuration
   - Callback logging
   - Token usage tracking

### Test Output Examples

The tests provide detailed output including:
- Token usage statistics
- Cost information
- Agent's thought process
- Response validation
- Interface configuration

Example test output:
```
Agent Execution Log:
-------------------
Total Tokens Used: 488
- Prompt Tokens: 441
- Completion Tokens: 47
Total Cost (USD): $0.0003

Thought Process:
[Agent reasoning and steps]
```

## Monitoring and Logging

### Callback System
The project implements a comprehensive callback system that tracks:
- Token usage
- API costs
- Agent's thought process
- Execution time
- Error states

### Gradio Interface Logs
The web interface displays:
1. **Agent Response**: JSON-formatted output
2. **Execution Log**:
   - Token usage statistics
   - Cost information
   - Thought process
   - Tool usage

Example log output in the interface:
```
Agent Execution Log:
-------------------
Total Tokens Used: [count]
- Prompt Tokens: [count]
- Completion Tokens: [count]
Total Cost (USD): $[amount]

Thought Process:
[Detailed reasoning steps]
```

## Development

### Adding New Tools
1. Create tool in `tools/` directory
2. Add `@tool` decorator
3. Add to `AVAILABLE_TOOLS`
4. Add corresponding tests

### Configuration
Modify `config/settings.py` for:
- LLM parameters
- API configurations
- Environment variables

## Contributing

1. Fork the repository
2. Create a feature branch
3. Implement changes
4. Add tests
5. Submit a pull request

## License

MIT 