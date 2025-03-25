"""Text analysis tools for the React LangChain Agent."""
from typing import Any

from langchain.agents import tool


@tool
def get_text_length(text: str) -> int:
    """Returns the length of a text by characters.
    
    Args:
        text: The text to analyze.
        
    Returns:
        int: The number of characters in the text.
    """
    print(f"get_text_length enter with {text=}")
    # Strip away non-alphabetic characters just in case
    text = text.strip("'\n").strip('"')
    return len(text)


# List of all available tools
AVAILABLE_TOOLS = [get_text_length] 