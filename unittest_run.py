import time
import sys
import unittest # 单元测试
import ddt  # 数据驱动

from GUItest.data.getData import get_data
from GUItest.HTMLTestRunner_PY3 import HTMLTestRunner
from GUItest.utility.clsDriven import clsDriven
from GUItest.utility.setupWD import setupWD

# 框架结构图
# 项目总测试驱动 - 00
    # 获取数据 - 01
    # 调取webdriver驱动 - 02
    # 类反射灵活引包,调用用例,执行测试 - 03
    # 如需引用不同角色登录, 从common包.main_login 调用 - 04
    # 用例执行函数传参,自行取数据列表下标 - 05

@ddt.ddt    # 数据装饰器
class ProjectTest(unittest.TestCase):

    @classmethod    # 类装饰器
    # @ddt.data(*get_data())    无法传入参数
    # @ddt.unpack
    def setUpClass(cls):
        print("Test Start")

    # 封包函数参数
    @ddt.data(*get_data())  # 获取表格数据
    @ddt.unpack
    def test_maincase(self, tid, title, browser, mod, mtd, data, expc):
        print(tid + ',' + title + '\n') # 打印说明
        wd = setupWD().get_wd(browser)  # 调取webdriver驱动 - 02 多浏览器
        mtd = clsDriven().driven(mod, mtd)  # 调用用例方法
        data_li = eval(data)    # 传入参数列表
        # print(li)
        # 用例执行函数传参,自行取数据列表下标 - 05
        result = mtd(wd, data_li, expc)
        print(f"实际结果:{result},预期结果:{expc}")

        self.assertEqual(result, expc)
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        print("Test End")


if __name__ == '__main__':

    format_time = time.strftime("%Y-%m-%d %H-%M-%S") # 格式时间戳
    # print(format_time)

    # unittest.main()

    # 测试报告
    f = open(f'../report/项目GUI兼容测试报告 {format_time}.html', 'wb')
    r = HTMLTestRunner(stream=f, title=u'项目GUI兼容测试报告', description=u'详情')

    ts = unittest.TestSuite()
    ts.addTests(tests=unittest.TestLoader().loadTestsFromTestCase(ProjectTest))

    r.run(ts)
    f.close()