# from langchain_community.chat_models import ChatZhipuAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.callbacks import StreamingStdOutCallbackHandler

from dotenv import load_dotenv
import os
load_dotenv()

llm = ChatOpenAI(
    model="GLM-5-Turbo",
    openai_api_key=os.getenv("ZHIPUAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_API_URL"),
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)
print("Welcome to the blog creator! Enter 'exit' to end the conversation.")
chat_prompt_template = ChatPromptTemplate(
    messages=[
        ("system", "You are a helpful professional blog writer that writes blog posts about {topic}. The blog post should be 300 words long and should be in the MD format: # Topic # and ## Subtopic ##. The blog post should be written in a way that is easy to understand and follow."),
        ("user", "Write a blog post about {topic}.")
    ]
)
chat_history = []
while True:
    user_input = input("Enter a topic for the blog: ")
    if user_input.lower() == "exit":
        break
    chat_prompt = chat_prompt_template.invoke({"topic": user_input})
    for chunk in llm.stream(chat_prompt):
        print(chunk.content, end="", flush=True)
        chat_history.append(AIMessage(content=chunk.content))