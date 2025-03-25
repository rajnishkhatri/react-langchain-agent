"""Callback handlers for monitoring LLM interactions."""
from typing import Dict, Any, List

from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import LLMResult


class AgentCallbackHandler(BaseCallbackHandler):
    """Callback handler for monitoring LLM interactions."""
    
    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> None:
        """Run when LLM starts running."""
        print(f"***Prompt to LLM was:***\n{prompts[0]}")
        print("*********")

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        """Run when LLM ends running."""
        print(f"***LLM Response:***\n{response.generations[0][0].text}")
        print("*********")

    def on_llm_error(self, error: Exception, **kwargs: Any) -> None:
        """Run when LLM errors."""
        print(f"***LLM Error:***\n{str(error)}")
        print("*********") 