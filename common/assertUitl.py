# 定义一个通用断言工具
def assertUtl(self,resp,status_code,code,message):
    self.assertEqual(status_code, resp.status_code)
    self.assertEqual(code, resp.json().get("status"))
    self.assertIn(message, resp.json().get("msg"))