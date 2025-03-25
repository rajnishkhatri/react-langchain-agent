# React LangChain Agent

A Python project that demonstrates the implementation of a LangChain agent using the ReAct (Reasoning + Acting) pattern. The agent can perform various tasks using tools, with the current implementation focusing on text analysis.

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
- **Modular AI System Design**: Demonstrates separation of concerns between agent logic, tools, and monitoring
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

- ReAct pattern implementation using LangChain
- Custom tool implementation (text length calculator)
- Environment variable management
- Custom callback handler for monitoring LLM interactions

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

- `main.py`: Main application file implementing the LangChain agent
  - ReAct pattern implementation
  - Tool registration and management
  - Agent configuration and execution
- `callbacks.py`: Custom callback handler for monitoring LLM interactions
  - Tracks prompts and responses
  - Provides debugging information
- `Pipfile` & `Pipfile.lock`: Dependency management files
- `requirements.txt`: Alternative dependency specification

## Dependencies

- langchain: Framework for developing LLM applications
- openai: OpenAI API client library
- python-dotenv: Environment variable management
- black: Code formatting

## Example Usage

```python
# Input: "What is the length of the word: rajnish khatri"
# Output:
Thought: I should use the get_text_length function to find the length of the given text.
Action: get_text_length
Action Input: "rajnish khatri"
Observation: 14
Final Answer: The text "rajnish khatri" has 14 characters
```

## Future Extensions

1. **Additional Tools**:
   - Text analysis tools
   - Mathematical operations
   - External API integrations

2. **Enhanced Capabilities**:
   - Memory management
   - Multi-step reasoning
   - Tool composition

3. **Monitoring & Analysis**:
   - Performance metrics
   - Decision analysis
   - Behavior patterns

## Contributing

Feel free to contribute by:
1. Forking the repository
2. Creating a feature branch
3. Submitting a pull request

## License

MIT 