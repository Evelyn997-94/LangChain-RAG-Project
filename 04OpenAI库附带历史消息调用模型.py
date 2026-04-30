from openai import OpenAI
# 1.获取client对象
client = OpenAI(
    base_url="https://llmapi.paratera.com"
)

# 2.调用模型
response=client.chat.completions.create(
    model="Qwen3-235B-A22B-Instruct-2507",
    messages = [
        {"role":"system","content":"你是AI助理，回答很简洁"},
        {"role":"user","content":"小明有2条宠物狗"},
        {"role":"assistant","content":"好的"},
        {"role": "user", "content": "小明有3条宠物狗"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "总共有几个宠物？"}
    ],
    stream=True   # 开启了流式输出的功能
)

# 3.处理结果
# print(response.choices[0].message.content)
for chunk in response:
    print(
        chunk.choices[0].delta.content,
        end=" ",     # 每一段之间以空格分隔
        flush=True   # 立刻刷新缓冲区
    )