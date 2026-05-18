
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()
llm = ChatOpenAI(
    model="GLM-5-Turbo",
    openai_api_key=os.getenv("ZHIPUAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_API_URL")
)
prompt_template = PromptTemplate(
    template="You are a helpful assistant that gives 3 interesting facts about {subject}.",
    input_variables=["subject"]
)
prompt = prompt_template.format(subject="egypt")
response = llm.invoke(prompt)
print(response.content)