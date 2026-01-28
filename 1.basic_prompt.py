from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

prompt_template = PromptTemplate(
    template="What is the capital of {country}?",
    input_variables=["country"]
)
prompt = prompt_template.invoke({"country": "India"})
llm = ChatOpenAI(
    model="glm-4.7-flash",
    openai_api_key=os.getenv("ZHIPUAI_API_KEY"),
    openai_api_base="https://api.z.ai/api/coding/paas/v4"
)
response = llm.invoke(prompt)
print(response.content)