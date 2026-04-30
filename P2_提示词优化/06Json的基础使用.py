import json

d = {
    "name": "周杰轮",
    "age": 11,
    "gender": "男"
}

s = json.dumps(d,ensure_ascii=False)
print(s)

l = [
    {
        "name": "周杰轮",
        "age": 11,
        "gender": "男"
    },
    {
        "name": "周杰轮",
        "age": 11,
        "gender": "男"
    },
    {
        "name": "周杰轮",
        "age": 11,
        "gender": "男"
    }
]

print(json.dumps(l,ensure_ascii=False))

json_str = '{"name": "周杰轮", "age": 11, "gender": "男"}'
json_arrary_str = '[{"name": "周杰轮", "age": 11, "gender": "男"}, {"name": "周杰轮", "age": 11, "gender": "男"}, {"name": "周杰轮", "age": 11, "gender": "男"}]'

res_dict = json.loads(json_str)
print(res_dict,type(res_dict))
res_list = json.loads(json_arrary_str)
print(res_list,type(res_list))