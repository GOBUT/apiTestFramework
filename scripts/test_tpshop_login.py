import unittest

from api.tpshop_login_api import TpshopLoginApi
from common.assertUitl import assertUtl

class TestTpshopLogin(unittest.TestCase):
    # 登录成功
    def test01_login_success(self):
        # 组织请求数据
        data = {"username": "13812345678", "password": "123456", "verify_code": "8888"}
        # 调用封装的接口
        resp = TpshopLoginApi.login(data)
        print("登陆成功：",resp.json())
        # 断言
        assertUtl(self,resp,200,1,"登陆成功")
        # self.assertEqual(200,resp.status_code)
        # self.assertEqual(1,resp.json().get("status"))
        # self.assertIn("登陆成功",resp.json().get("msg"))


    # 手机号为空
    def test02_mobile_none(self):
        # 组织请求数据
        data = {"username": None, "password": "123456", "verify_code": "8888"}
        # 调用封装的接口
        resp = TpshopLoginApi.login(data)
        print("手机号为空", resp.json())
        # 断言
        assertUtl(self, resp, 200, -2, "密码错误!")
        # self.assertEqual(200, resp.status_code)
        # self.assertEqual(-2, resp.json().get("status"))
        # self.assertIn("密码错误!", resp.json().get("msg"))
    # 密码错误
    def test03_pwd_err(self):
        # 组织请求数据
        data = {"username": "13812345678", "password": "222222", "verify_code": "8888"}
        # 调用封装的接口
        resp = TpshopLoginApi.login(data)
        print("密码错误", resp.json())
        # 断言
        assertUtl(self, resp, 200, -2, "密码错误!")
        # self.assertEqual(200, resp.status_code)
        # self.assertEqual(-2, resp.json().get("status"))
        # self.assertIn("密码错误!", resp.json().get("msg"))
    # 验证码错误
    def test04_verify_err(self):
        # 组织请求数据
        data = {"username": "13812345678", "password": "222222", "verify_code": "9999"}
        # 调用封装的接口
        resp = TpshopLoginApi.login(data)
        print("验证码错误", resp.json())
        # 断言
        assertUtl(self, resp, 200, 0, "验证码错误")
        # self.assertEqual(200, resp.status_code)
        # self.assertEqual(0, resp.json().get("status"))
        # self.assertIn("验证码错误", resp.json().get("msg"))