import json
import unittest
from parameterized import parameterized

def add(x, y):
    return x + y


# data = [
#     {"x": 10, "y": 20, "except_value": 30},
#     {"x": 100, "y": 200, "except_value": 300},
#     {"x": 1000, "y": 20, "except_value": 1020}
# ]
# 需要把数据[{},{},{}]  --->[(),(),()]  模拟json转元组
def read_json_data():
    ls = []
    # 从json文件中读取[{},{}]数据
    with open('data/params_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            tmp = tuple(item.values())
            ls.append(tmp)
    return ls
'''
参数实现步骤：
1 导包
2 在通用测试方法上一行，添加@parameterized.expand(data)
3 给 expand() 传入[(),(),()]格式数据
4 修改通用测试方法形参，按数据中的key设计参数
5 在通用测试方法内，使用形参
'''
class TestParams(unittest.TestCase):
    # 给定通用测试方法
    @parameterized.expand(read_json_data)
    def test_add(self,x,y,except_value):
        res = add(x,y)
        self.assertEqual(except_value,res)

    # def test01_add(self):
    #     res = add(10,20)
    #     self.assertEqual(30,res)
    #
    # def test02_add(self):
    #     res = add(100,200)
    #     self.assertEqual(300,res)
    #
    # def test03_add(self):
    #     res = add(1000,20)
    #     self.assertEqual(1020,res)
