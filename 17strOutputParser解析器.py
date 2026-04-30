from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage
parser = StrOutputParser()
model = ChatOpenAI(model="GLM-4-Air",
                 base_url="https://llmapi.paratera.com")
prompt = PromptTemplate.from_template(
    "我邻居姓：{lastname}，刚生了{gender}，请起名，仅告知我名字无需其它内容。"
)

chain = prompt | model | parser | model | parser
res : str = chain.invoke({"lastname":"张","gender":"女儿"})
print(res)
print(type(res))