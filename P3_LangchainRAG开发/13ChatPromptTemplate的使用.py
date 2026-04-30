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
# StringPromptValue  to_string
prompt_text = chat_Prompt_template.invoke({"history":history_data}).to_string()
model=ChatOpenAI(model="GLM-4-Air",
                 base_url="https://llmapi.paratera.com")
res=model.invoke(prompt_text)
print(res.content,type(res))