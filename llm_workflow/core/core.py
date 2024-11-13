from llm_workflow.core.common_agents import supervisor_agent
from langchain.schema import HumanMessage
from llm_workflow.core.utils import agent_node
import uuid
from typing import Annotated
from langchain_core.messages import HumanMessage
import functools
import operator
from typing import Sequence, TypedDict
from langgraph.graph import END, StateGraph, START
from langchain_core.messages import BaseMessage, HumanMessage
from llm_workflow.utils.basic_agent import BasicAgent
from langchain.schema import AIMessage

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    next: str
from langgraph.checkpoint.memory import MemorySaver
memory = MemorySaver()

class MultiAgentChatbot:
    def __init__(self, team: list[BasicAgent], memory: MemorySaver = memory):
        members = [agent.agent_name for agent in team]
        workflow = StateGraph(AgentState)
        for agent in team:
            node = functools.partial(agent_node, agent=agent.agent_executor, name=agent.agent_name)
            workflow.add_node(agent.agent_name, node)
        workflow.add_node("supervisor", supervisor_agent(team))
        for member in members:
            workflow.add_edge(member, END)

        conditional_map = {k: k for k in members} #- from member back to supervisor
        print(conditional_map)
        workflow.add_conditional_edges("supervisor", lambda x: x["next"], conditional_map)
        workflow.add_edge(START, "supervisor")
        self.graph = workflow.compile(checkpointer=memory)

    def invoke(self, user_message: str, thread_id: str) -> str:
        result = self.graph.invoke(
            {"messages": [HumanMessage(content=user_message)]},
            {"configurable": {"thread_id": thread_id}, "recursion_limit": 100},
        )
        return result

    async def astream(self, user_message: str, thread_id: str):
        inputs = {"messages": [HumanMessage(content=user_message)]}
        config = {"configurable": {"thread_id": thread_id}, "recursion_limit": 100}
        final_result = ""
        async for chunk in self.graph.astream(inputs, config=config, stream_mode="values"):
            print(chunk["messages"][-1].content)
            # final_result += chunk
        return final_result
