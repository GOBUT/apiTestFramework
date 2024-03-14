"""
生成测试报告的步骤：
1. 创建测试套件实例。 suite
2. 添加 测试类
3. 创建 HTMLTestReport 类实例。 runner
4. runner 调用 run(), 传入 suite
"""
import logging
import unittest

from scripts.test_tpshop_login import TestTpshopLogin
from scripts.test_tpshop_login_params import TestTpshopLoginParame
from htmltestreport import HTMLTestReport

# 1. 创建测试套件实例。 suite
suite = unittest.TestSuite()
# 2. 添加 测试类, 组装测试用例
suite.addTest(unittest.makeSuite(TestTpshopLoginParame))
suite.addTest(unittest.makeSuite(TestTpshopLogin))

# 3. 创建 HTMLTestReport 类实例。 runner
runner = HTMLTestReport("./report/tpshop.html", description="这是一份tp商场的测试报告", title="tp商场测试报告")  # 相对路径

# 4. runner 调用 run(), 传入 suite
runner.run(suite)
logging.info("tpshop.html 测试报告 生成 成功！")