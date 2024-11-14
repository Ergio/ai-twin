from langchain_core.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from llm_workflow.utils.basic_agent import BasicAgent


def supervisor_agent(team: list[BasicAgent]):
    members = [agent.agent_name for agent in team]
    descriptions = [agent.agent_description for agent in team]
    member_descriptions = ", ".join([f"{name} - {desc}\n" for name, desc in zip(members, descriptions)])

    system_prompt = """You are a supervisor tasked with managing a conversation between the following workers:  {members}.
Descriptions of the workers are as follows:
{member_descriptions}
Given the following user request, respond with the best (most suitable) worker to act next.
Try to use all possible agents to have more context for the correct answer!
Use Ukrainian language in explanation.
Selected worker will perform a task and respond with result and status. When finished, respond with FINISH."""

    # Our team supervisor is an LLM node. It just picks the next agent to process
    # and decides when the work is completed
    options = ["FINISH"] + members
    # Using openai function calling can make output parsing easier for us
    function_def = {
        "name": "route",
        "description": "Select the next role.",
        "parameters": {
            "title": "routeSchema",
            "type": "object",
            "properties": {
                "explanation": {
                    "title": "Explanation",
                    "type": "string",
                },
                "next": {
                    "title": "Next",
                    "anyOf": [
                        {"enum": options},
                    ],
                }
            },
            "required": ["next"],
        },
    }
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
            (
                "system",
                "Given the conversation above, who should act next?"
                " Or should we FINISH? Select one of: {options}",
            ),
        ]
    ).partial(options=str(options), members=", ".join(members), member_descriptions=member_descriptions)
    llm = ChatOpenAI(model="gpt-4o-2024-08-06")

    supervisor_chain = (
        prompt
        | llm.bind_functions(functions=[function_def], function_call="route")
        | JsonOutputFunctionsParser()
    )
    return supervisor_chain