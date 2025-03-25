"""Prompt templates for the React LangChain Agent."""
from langchain.prompts import PromptTemplate
from langchain.tools import Tool
from langchain.tools.render import render_text_description


def create_react_prompt(tools: list[Tool]) -> PromptTemplate:
    """Create a ReAct prompt template for the agent.
    
    Args:
        tools: List of tools available to the agent.
        
    Returns:
        PromptTemplate: The configured prompt template.
    """
    template = """
    Answer the following questions as best you can. You have access to the following tools:

    {tools}
    
    Use the following format:
    
    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question
    
    Begin!
    
    Question: {input}
    Thought: {agent_scratchpad}
    """
    
    return PromptTemplate.from_template(template=template).partial(
        tools=render_text_description(tools),
        tool_names=", ".join([t.name for t in tools]),
    ) 