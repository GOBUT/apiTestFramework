import unittest

from api.tpshop_login_api import TpshopLoginApi
from common.assertUitl import assertUtl
from parameterized import parameterized
from common.readJsonFile import read_json_data
'''
参数实现步骤：
1 导包
2 在通用测试方法上一行，添加@parameterized.expand(data)
3 给 expand() 传入[(),(),()]格式数据
4 修改通用测试方法形参，按数据中的key设计参数
5 在通用测试方法内，使用形参
'''
class TestTpshopLoginParame(unittest.TestCase):
    # 通用方法（参数化）
    @parameterized.expand(read_json_data)
    def test_login(self,desc,query_data,status_code,code,message):
        resp = TpshopLoginApi.login(query_data)
        print(desc,resp.json())
        # 断言
        assertUtl(self,resp,status_code,code,message)



