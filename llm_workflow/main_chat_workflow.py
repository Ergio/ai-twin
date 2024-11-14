from typing import Any, Optional, Dict, List
from langgraph.checkpoint.base import CheckpointTuple
from llm_workflow.agents.personal_info_agent import PersonalInfoAgent
from llm_workflow.agents.python_agent import PythonAgent
from llm_workflow.agents.web_researcher_agent import WebResearcherAgent
from llm_workflow.core.core import MultiAgentChatbot
from langchain_core.messages import AnyMessage
from langgraph.checkpoint.memory import MemorySaver
from typing import List

class MainChatWorkflow:
    def __init__(self):
        self.memory = MemorySaver()
        
    def chat_to_ai(
        self,
        user_message: str,
        thread_id: str,
        ) -> Dict[str, str]:


        agents_team = [
            PersonalInfoAgent(),
            WebResearcherAgent(),
            PythonAgent(),
        ]

        self.mac = MultiAgentChatbot(team = agents_team, memory = self.memory)

        return self.mac.invoke(user_message, thread_id)

    def get_chat_messages(self, thread_id: str) -> Optional[List[CheckpointTuple]]:
        memory_tuple = self.memory.get_tuple({"configurable": {"thread_id": thread_id}, "stream_options": {"include_usage": True}})
        messages = memory_tuple.checkpoint['channel_values']['messages']

        def format_messages(msg: AnyMessage) -> Dict[str, Any]:
            return {
                "role": msg.type,
                "content": msg.content,
                "id": msg.id,
            }

        formatted_messages = [format_messages(msg) for msg in messages if msg.type in ['human', 'ai']]

        filtered_messages = []
        last_role = None
        for msg in formatted_messages:
            if msg['role'] == 'ai' and last_role == 'ai':
                filtered_messages.pop()  # Remove the previous AI message
            filtered_messages.append(msg)
            last_role = msg['role']

        return filtered_messages
