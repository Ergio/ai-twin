from llm_workflow.core.common_agents import simple_agent
from llm_workflow.utils.basic_agent import BasicAgent

support_agent_prompt = """
# Support Agent

You are an AI agent working as a support representative.

1. Customer Interaction:
   - Greet clients professionally and warmly.
   - Use the client's name when appropriate to personalize the interaction.
   - Maintain a helpful and patient demeanor throughout the conversation.

Remember, your role is crucial in maintaining client satisfaction and loyalty. 
"""

class SupportAgent(BasicAgent):
    def __init__(self):

        super().__init__(
            agent_executor=simple_agent(support_agent_prompt),
            agent_name="support_agent",
            agent_description="Provides client support"
        )
        
    def create_tools(self):

        return []
