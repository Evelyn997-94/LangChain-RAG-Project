from langchain_openai import ChatOpenAI

model=ChatOpenAI(model="GLM-4-Air",
                 base_url="https://llmapi.paratera.com")


res = model.invoke("你是谁呀，能做什么？")
print(res)