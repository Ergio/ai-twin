from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def simple_agent(sys_prompt: str, model="gpt-4o-2024-08-06", tools = None):
    llm = ChatOpenAI(model=model)  # Changed this line
    def create_agent(llm: ChatOpenAI, tools: list, system_prompt: str):
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    system_prompt,
                ),
                MessagesPlaceholder(variable_name="messages"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),
            ]
        )
        agent = create_openai_tools_agent(llm, tools, prompt)
        executor = AgentExecutor(agent=agent, tools=tools, handle_parsing_errors=True, max_iterations = 5)# verbose=True
        return executor
    from langchain_community.tools import WikipediaQueryRun
    from langchain_community.utilities import WikipediaAPIWrapper
    
    if tools is None:
        api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
        tools = [WikipediaQueryRun(api_wrapper=api_wrapper)]
    research_agent = create_agent(llm, tools=tools, system_prompt=sys_prompt)  # Added empty list for tools
    return research_agent
