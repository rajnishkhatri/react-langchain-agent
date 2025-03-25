# React LangChain Agent

A Python project that demonstrates the implementation of a LangChain agent using the ReAct (Reasoning + Acting) pattern. The agent can perform various tasks using tools, with the current implementation focusing on text analysis.

## Features

- ReAct pattern implementation using LangChain
- Custom tool implementation (text length calculator)
- Environment variable management
- Custom callback handler for monitoring LLM interactions

## Setup

1. Clone the repository
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
- `callbacks.py`: Custom callback handler for monitoring LLM interactions
- `Pipfile` & `Pipfile.lock`: Dependency management files
- `requirements.txt`: Alternative dependency specification

## Dependencies

- langchain
- openai
- python-dotenv
- black (for code formatting)

## License

MIT 