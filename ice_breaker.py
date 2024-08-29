from langchain_core.prompts.prompt import PromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
import os
if __name__ == "__main__":
    print("hello lanchain")
    print(os.environ["OPENAI_API_KEY"])
    
summary_message = """ Learning a langchain course and want to more {information} given the 
above information and context do give me output"""

summary_prompt_template = PromptTemplate(input_variables = summary_message, template = summary_message)

llm = ChatOpenAI(temperature=0, model = "gpt-3.5-turbo")

llm_o = ChatOllama(model="llama3.1")
# chaining to the llm 
chain = summary_prompt_template | llm 
chain_2  = summary_prompt_template | llm_o | StrOutputParser()
# result= chain.invoke(input = {"information": "what are chain and how do we use that "})
# print(result)
result= chain_2.invoke(input = {"information": "what are chain and how do we use that "})
print(result)