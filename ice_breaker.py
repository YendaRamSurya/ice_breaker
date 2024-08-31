from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import scrape_linkedin_profile

from agents.linkedin_lookup_agent import lookup

def ice_break_with(name: str):
    linkedin_username = lookup(name = name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username, mock = True)
    
    summary_template = """
    given the Linkedin information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template |llm
    res = chain.invoke(input={"information": linkedin_data})
    print(res)
if __name__ == "__main__":
    load_dotenv()
    print("ICE Breaker add")
    
    ice_break_with(name = "eden marco udemy")