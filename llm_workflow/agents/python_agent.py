from llm_workflow.core.common_agents import simple_agent
from llm_workflow.utils.basic_agent import BasicAgent
from langchain.tools import Tool
import sys
import io
from contextlib import redirect_stdout
from typing import Dict, Any
from langchain_experimental.utilities import PythonREPL

python_agent_prompt = """
# Python Code Execution Assistant

You are an expert Python programming assistant with the ability to execute Python code for calculations, data manipulation, and problem-solving.

## Core Responsibilities:

1. Code Execution:
   - Execute Python code safely in an isolated environment
   - Perform calculations and data manipulations
   - Handle exceptions gracefully
   - Show both code and its output
   - Explain results clearly

2. Problem Solving:
   - Write and execute code to solve mathematical problems
   - Perform data transformations
   - Handle string manipulations
   - Process numerical calculations
   - Execute algorithms and demonstrate results

3. Best Practices:
   - Write safe and efficient code
   - Handle edge cases appropriately
   - Validate inputs before execution
   - Provide clear output formatting
   - Include error handling in executed code

4. Code Examples:
   - Demonstrate working solutions
   - Show input and output examples
   - Execute test cases
   - Verify results
   - Explain the execution flow

Remember: Always execute code safely and explain the results clearly to the user.
"""

class PythonAgent(BasicAgent):
    def __init__(self):
        python_repl = PythonREPL()
        repl_tool = Tool(
            name="python_repl",
            description="A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`.",
            func=python_repl.run,
         )
        tools = [repl_tool]
        super().__init__(
            agent_executor=simple_agent(python_agent_prompt, tools=tools),
            agent_name="python_executor",
            agent_description="Python expert that can execute code, perform calculations, and solve problems"
        )
    
    def create_tools(self):
        return []
