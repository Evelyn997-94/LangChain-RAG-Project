# from langchain_openai import ChatOpenAI
# model=(ChatOpenAI(model="GLM-4-Air",
#                  base_url="https://llmapi.paratera.com"))
#
# # 通过stream方法获得流式输出
# res = model.stream(input="你是谁呀能做什么")
#
# for chunk in res:
#     print(chunk,end="",flush=True)

from langchain_ollama import OllamaLLM
model = OllamaLLM(model ="qwen3-vl:4b")
res = model.invoke(input="你是谁呀能做什么？")
for chunk in res:
    print(chunk,end="",flush=True)