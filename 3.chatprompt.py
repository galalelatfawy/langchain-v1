from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import os

load_dotenv()

prompt_template = ChatPromptTemplate(
    messages=[
        ("system", "You are a helpful assistant that can answer questions and help with tasks."),
        ("user", "{input}")
    ]
)
prompt = prompt_template.invoke({"input": "What is the capital of Italy?"})
llm = ChatOpenAI(
    model="GLM-5-Turbo",
    openai_api_key=os.getenv("ZHIPUAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_API_URL")
)
response = llm.invoke(prompt)
print(response.content)