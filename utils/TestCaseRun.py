import unittest
import os
from case import Test_01
from utils.HTMLTestRunner import HTMLTestRunner
from utils.Appium_start import Appium_start
import threading
import time

current_path = os.path.abspath(os.path.join(os.getcwd(), "../"))  # 获取当前上级路径
#获取报告文档路径
report_path = os.path.join(current_path, 'Report')
report_title = 'Report.html'
result_path = os.path.join(report_path, report_title)

class TestCaseRun():
    def GetCase(self):
        """
            获取测试集合
        :return:返回一个添加入测试模型的测试套件
        """
        #设定测试模型
        loader = unittest.TestLoader()
        #设定测试类型
        suite = unittest.TestSuite()
        #将测试模型放入测试套件内
        suite.addTest(loader.loadTestsFromModule(Test_01))
        return suite

    def Start_Test(self):
        print('111111')
        suite = TestCaseRun.GetCase()
        run = unittest.TextTestRunner(verbosity=2)
        with open(result_path, 'wb') as report:
            run = HTMLTestRunner(report, verbosity=2, title='BU3基本功能自动化测试', description='测试报告')
            run.run(suite)
        Appium_start.stop_appium(DUT_NAME='SUBDUT')

if __name__ == '__main__':
    t1 = threading.Thread(target=Appium_start.start('SUBDUT'))
    t1.start()
    time.sleep(10)
    TestCaseRun = TestCaseRun()
    t2 = threading.Thread(target=TestCaseRun.Start_Test())
    t2.start()
    os.popen(result_path)