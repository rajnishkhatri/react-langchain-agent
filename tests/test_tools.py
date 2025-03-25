"""Tests for text analysis tools."""
from react_langchain_agent.tools.text_tools import get_text_length


def test_get_text_length():
    """Test the get_text_length tool."""
    # Test basic string
    assert get_text_length("hello") == 5
    
    # Test string with spaces
    assert get_text_length("hello world") == 11
    
    # Test string with quotes and newlines
    assert get_text_length("'hello'\n") == 5 