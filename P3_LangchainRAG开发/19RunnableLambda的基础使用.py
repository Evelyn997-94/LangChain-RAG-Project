from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

# 创建所需的解析器
str_parser = StrOutputParser()

# 模型创建
model = ChatOpenAI(model="GLM-4-Air",
                 base_url="https://llmapi.paratera.com")

# 第一个提示词模板
first_prompt = PromptTemplate.from_template(
    "我邻居姓：{lastname}，刚生了{gender}，请帮忙起名字，仅回复我名字，无需额外内容。"
    "并封装成Json格式返回给我。要求key是name，value就是你起的名字，请严格遵守格式要求。"
)

# 第二个提示词模板
second_prompt = PromptTemplate.from_template(
    "姓名：{name}，请帮我解析含义"
)
# # 函数的入参：AImessage -> dict
# my_func = RunnableLambda(lambda ai_msg:{"name":ai_msg.content})
# chain = first_prompt | model | my_func |second_prompt | model | str_parser
#
# for chunk in chain.stream({"lastname":"张","gender":"女孩"}):
#     print(chunk,end="",flush=True)

# 函数的入参：AImessage -> dict
chain = first_prompt | model | (lambda ai_msg:{"name":ai_msg.content}) |second_prompt | model | str_parser

for chunk in chain.stream({"lastname":"张","gender":"女孩"}):
    print(chunk,end="",flush=True)

