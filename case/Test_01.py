# coding=utf-8
"""
    #[通话记录]_基本功能_进入/退出 通话记录
    #用例名：查看通话记录列表
    #用例ID：TC_Call_001
    #预制条件：
    #   01.手表内存在通话记录
    #测试步骤:
    #   01.联系人中查看通话记录
    #预期结果:
    #   01.显示通话记录列表
"""
import unittest
import time
from page import Oxygen
from config import ConfigGet
from Comment.Comment import Comment
from utils.log import Logger

class TC_Call_001(unittest.TestCase):

    #前置条件
    def setUp(self) -> None:
        self.SUBDUT_Device = ConfigGet.ConfigGet.Get_Device_Config('SUBDUT')
        print(Oxygen.PageActivity.settingActivity.win_name)
        time.sleep(2)

    #测试步骤
    def test_01(self):
        Comment.xpath_click(self.SUBDUT_Device,xpath='//android.widget.TextView[@content-desc="全部应用程序"]')
        Comment.xpath_click(self.SUBDUT_Device,xpath='//android.widget.TextView[@content-desc="设置"]')
        time.sleep(5)
        Comment.text_name_click(self.SUBDUT_Device,text_name='网络和互联网')
        print(Comment.GetClassText_Text(self.SUBDUT_Device, 'WLAN'))
        Comment.text_name_click(self.SUBDUT_Device,text_name='WLAN')
        list = Comment.GetDeviceSize(self.SUBDUT_Device)
        width = list[0]
        height = list[1]
        print(width)
        print(height)
        Comment.swipe(self.SUBDUT_Device,x1=width*0.2,y1=height/10,x2=width*0.2,y2=height/3)
        Comment.xpath_click(self.SUBDUT_Device,xpath='//android.widget.ImageButton[@content-desc="向上导航"]')
        time.sleep(2)

    #收尾
    def tearDown(self) -> None:
        self.SUBDUT_Device.press_keycode(3)
        print('测试结束')

if __name__ == '__main__':
    unittest.main()
    # Logger.logger.getLogger(TC_Call_001).addHandler(Logger.logger.NullHandler())
    # Logger('error.log', level='info').logger.error('error', unittest.main())