from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

prompt = PromptTemplate.from_template("你是一个AI助手")
model=ChatOpenAI(model="GLM-4-Air",
                 base_url="https://llmapi.paratera.com")

chain = prompt | model | prompt | model
chain.invoke()
chain.stream()
print(type(chain))