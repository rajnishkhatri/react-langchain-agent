"""Gradio interface for the React LangChain Agent."""
import os
import gradio as gr
from typing import Dict, Any, Tuple
from langchain_community.callbacks import get_openai_callback

from react_langchain_agent.config.settings import settings
from react_langchain_agent.core.agent import ReActAgent
from react_langchain_agent.tools.text_tools import AVAILABLE_TOOLS


def process_input(text: str) -> Tuple[Dict[str, Any], str]:
    """Process input through the agent.
    
    Args:
        text: Input text to process.
        
    Returns:
        Tuple containing:
            - Dict containing the agent's response
            - String containing the callback logs
    """
    # Validate settings
    errors = settings.validate()
    if errors:
        return {
            "error": "Configuration error",
            "details": "\n".join(errors)
        }, "Configuration error occurred"
    
    # Initialize agent
    agent = ReActAgent(tools=AVAILABLE_TOOLS)
    
    try:
        # Run agent with callback tracking
        with get_openai_callback() as cb:
            result = agent.run(text)
            
            # Format callback logs
            logs = f"""
Agent Execution Log:
-------------------
Total Tokens Used: {cb.total_tokens}
- Prompt Tokens: {cb.prompt_tokens}
- Completion Tokens: {cb.completion_tokens}
Total Cost (USD): ${cb.total_cost:.4f}

Thought Process:
{result.get('intermediate_steps', 'No intermediate steps recorded')}
"""
            return result, logs
            
    except Exception as e:
        error_response = {
            "error": "Processing error",
            "details": str(e)
        }
        return error_response, f"Error occurred: {str(e)}"

# Create the Gradio interface
def create_interface() -> gr.Interface:
    """Create the Gradio interface for the agent.
    
    Returns:
        gr.Interface: The configured Gradio interface.
    """
    # Define examples
    examples = [
        ["What is the length of the word: hello"],
        ["What is the length of the phrase: artificial intelligence"],
        ["What is the length of: OpenAI ChatGPT"],
    ]
    
    # Create interface
    iface = gr.Interface(
        fn=process_input,
        inputs=gr.Textbox(
            lines=2,
            placeholder="Enter your question here...",
            label="Input Text",
        ),
        outputs=[
            gr.JSON(label="Agent Response"),
            gr.Textbox(label="Execution Log", lines=10)
        ],
        title="ReAct LangChain Agent Demo",
        description="""
        This demo showcases a LangChain agent using the ReAct (Reasoning + Acting) pattern.
        Currently, it can analyze text length, but more tools can be added.
        
        The interface shows both the agent's response and a detailed execution log including:
        - Token usage statistics
        - Cost information
        - Agent's thought process
        
        Example questions:
        - What is the length of the word: hello
        - What is the length of the phrase: artificial intelligence
        """,
        examples=examples,
        theme=gr.themes.Soft(),
    )
    
    return iface

def main():
    """Run the Gradio interface."""
    # Create and launch the interface
    iface = create_interface()
    iface.launch(
        server_name="0.0.0.0",  # Make accessible from outside
        share=True,             # Create a public link
    )

if __name__ == "__main__":
    main() 