from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_openai import OpenAIEmbeddings

# # 创建模型对象 不传model默认用的是 text-embeddings-v1
# model = DashScopeEmbeddings()
# 阿里云平台

vector_store = InMemoryVectorStore(
    embedding=OpenAIEmbeddings(
        model="GLM-Embedding-2",
        base_url="https://llmapi.paratera.com"
    )
)

loader = CSVLoader(
    file_path="./data/info.csv",
    encoding="utf-8",
    source_column="source",    # 指定本条数据的来源是哪里
)

documents = loader.load()
# id1 id2 id3 id4...
# 向量存储的 新增、删除、检索
vector_store.add_documents(
    documents=documents,    # 被添加的文档，类型：list[Document]
    ids=["id"+str(i) for i in range(1,len(documents)+1)]
)

# 删除 传入[id,id...]
vector_store.delete(["id1","id2"])

# 检索 返回类型list[Document]
result = vector_store.similarity_search(
    "Python是不是简单易学呀",
    3  #检索的结果要几个
)
print(result)