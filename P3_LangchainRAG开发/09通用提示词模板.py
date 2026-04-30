from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
# zero-shot
promp_template=PromptTemplate.from_template(
    "我的邻居姓{lastname}，刚生了{gender},你帮我起个名字，简单回答。"
)
model=ChatOpenAI(model="GLM-4-Air",
                 base_url="https://llmapi.paratera.com")
#
# # 调用.format方法注入信息即可
# prompt_text = promp_template.format(lastname="张",gender="女儿")
#
# model=ChatOpenAI(model="GLM-4-Air",
#                  base_url="https://llmapi.paratera.com")
#
# res = model.invoke(input=prompt_text)
# print(res)
chain = promp_template | model
res = chain.invoke(input={"lastname":"李","gender":"女儿"})
print(res)