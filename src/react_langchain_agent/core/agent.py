"""Core agent implementation using the ReAct pattern."""
from typing import Any, Union, List

from langchain.agents.format_scratchpad import format_log_to_str
from langchain.agents.output_parsers import ReActSingleInputOutputParser
from langchain.schema import AgentAction, AgentFinish
from langchain.tools import Tool
from langchain_openai import ChatOpenAI

from react_langchain_agent.config.settings import settings
from react_langchain_agent.core.prompts import create_react_prompt
from react_langchain_agent.utils.callbacks import AgentCallbackHandler


class ReActAgent:
    """ReAct pattern agent implementation."""
    
    def __init__(self, tools: List[Tool]):
        """Initialize the agent with tools.
        
        Args:
            tools: List of tools available to the agent.
        """
        self.tools = tools
        self.llm = ChatOpenAI(
            temperature=settings.TEMPERATURE,
            stop=settings.STOP_SEQUENCES,
            callbacks=[AgentCallbackHandler()],
        )
        self.prompt = create_react_prompt(tools)
        self.agent = (
            {
                "input": lambda x: x["input"],
                "agent_scratchpad": lambda x: format_log_to_str(x["agent_scratchpad"]),
            }
            | self.prompt
            | self.llm
            | ReActSingleInputOutputParser()
        )
        
    def find_tool_by_name(self, tool_name: str) -> Tool:
        """Find a tool by its name.
        
        Args:
            tool_name: Name of the tool to find.
            
        Returns:
            Tool: The found tool.
            
        Raises:
            ValueError: If tool is not found.
        """
        for tool in self.tools:
            if tool.name == tool_name:
                return tool
        raise ValueError(f"Tool with name {tool_name} not found")
    
    def run(self, input_text: str) -> dict:
        """Run the agent on input text.
        
        Args:
            input_text: The input text to process.
            
        Returns:
            dict: The agent's response.
        """
        intermediate_steps = []
        agent_step = ""
        
        while not isinstance(agent_step, AgentFinish):
            agent_step: Union[AgentAction, AgentFinish] = self.agent.invoke(
                {
                    "input": input_text,
                    "agent_scratchpad": intermediate_steps,
                }
            )
            print(agent_step)
            
            if isinstance(agent_step, AgentAction):
                tool_name = agent_step.tool
                tool_to_use = self.find_tool_by_name(tool_name)
                tool_input = agent_step.tool_input
                
                observation = tool_to_use.func(str(tool_input))
                print(f"{observation=}")
                intermediate_steps.append((agent_step, str(observation)))
        
        return agent_step.return_values 