import unittest
import os
from case import Test_01
from utils.HTMLTestRunner import HTMLTestRunner

class TestCaseRun():
    def GetCase(self):
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        suite.addTest(loader.loadTestsFromModule(Test_01))
        return suite

if __name__ == '__main__':
    current_path = os.path.abspath(os.path.join(os.getcwd(), "../"))  # 获取当前上级路径
    report_path = os.path.join(current_path, 'Report')
    report_title = 'Report.html'
    result_path = os.path.join(report_path, report_title)
    TestCaseRun = TestCaseRun()
    suite = TestCaseRun.GetCase()
    run = unittest.TextTestRunner(verbosity=2)
    with open(result_path,'wb') as report:
        run = HTMLTestRunner(report, verbosity=2, title='BU3基本功能自动化测试', description='测试报告')
        run.run(suite)
    os.popen(result_path)