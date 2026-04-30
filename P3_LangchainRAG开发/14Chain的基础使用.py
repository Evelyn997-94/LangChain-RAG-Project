from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_openai import ChatOpenAI
chat_Prompt_template=ChatPromptTemplate.from_messages(
    [
        ("system","你是一个边塞诗人，可以作诗。"),
        MessagesPlaceholder("history"),
        ("human","请再来一首唐诗"),
    ]
)

history_data = [
    ("human","写一首唐诗。"),
    ("ai","床前明月光，疑是地上霜，举头望明月，低头思故乡"),
    ("human","好诗再来一首"),
    ("ai","锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦。"),
]

model=ChatOpenAI(model="GLM-4-Air",
                 base_url="https://llmapi.paratera.com")

# 组成链，要求每一个组件都是Runnable接口的子类
chain = chat_Prompt_template | model

# 通过链去调用invoke或stream
# res = chain.invoke({"history":history_data})
# print(res.content)

# 调用stream流式输出
for chunk in chain.stream({"history":history_data}):
    print(chunk.content,end="",flush=True)


