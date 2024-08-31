import os
from dotenv import load_dotenv

load_dotenv()
from tools.tools import get_profile_url_tavily
from langchain_core.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub
from tools.tools import get_profile_url_tavily

def lookup(name: str) -> str:
    
    llm = ChatOpenAI(temperature=0, model = "gpt-3.5-turbo")
    
    template = """given the name of the person {name_of_person} I want you to get it me a link to their linkedin profile page.
    Your answer shold contain only a URL"""
    
    prompt_template= PromptTemplate(template= template, input_variables=["name_of_person"])
    
    tool_for_agent = [
        Tool(name = "crawl Google 4 linkedin profile page",
             func = get_profile_url_tavily,
             description = "useful for when you need to get the Linekdin Page URL")
    ]
    
    prompt = hub.pull("hwchase17/react")
    # definition of agent
    agent = create_react_agent(llm = llm, tools=tool_for_agent, prompt=prompt)
    # orchestrator 
    agent_executor = AgentExecutor(agent=agent, tools=tool_for_agent, verbose=True)
    
    result  = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person = name)}
    )
    
    linkedin_profile_url = result["output"]
    
    return "https://www.linkedin.com/in/eden-marco/"

