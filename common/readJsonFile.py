# # 定义函数，读取json文件
# import json
#
#
# def read_json_data():
#     ls = []
#     with open('../data/tpshop_login.json') as f:
#         data = json.load(f)
#         for item in data:
#             tmp = tuple(item.values())
#             ls.append(tmp)
#     return ls
#
import os
import json

def read_json_data():
    # 获取当前文件所在目录
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # 拼接 JSON 文件路径
    json_file = os.path.join(base_dir, '..', 'data', 'tpshop_login.json')

    # 确保文件存在
    if not os.path.exists(json_file):
        raise FileNotFoundError(f"JSON 文件 {json_file} 不存在")

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            yield tuple(item.values())