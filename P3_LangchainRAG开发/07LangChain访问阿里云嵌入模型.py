from langchain_openai import OpenAIEmbeddings

# # 创建模型对象 不传model默认用的是 text-embeddings-v1
# model = DashScopeEmbeddings()
# 阿里云平台

model = OpenAIEmbeddings(
    model="GLM-Embedding-2",
    base_url="https://llmapi.paratera.com"
)

# 不用invoke stream
# embed_query、embed_documents
print(model.embed_query("我喜欢你"))
print(model.embed_documents(["我喜欢你","我稀饭你","晚上吃啥"]))


