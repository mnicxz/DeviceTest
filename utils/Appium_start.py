# coding:utf-8
# appium_start.py
from appium import webdriver
from utils.Dos_adb  import Dos_adb
from config.ConfigGet import ConfigGet
import os
path  =os.path.dirname(os.getcwd())# appium日志路径
appium_log = os.path.join(os.path.join(path,'logs'),'appium_log.txt')
class Appium_start():
    #启动appium服务
    def start(self,DUT_NAME):
        print('我进来启动appium了')
        '''
         启动appium
        '''
        adb = Dos_adb()
        devices = adb.get_device()[0]
        a = 'start /b appium -p %s'%ConfigGet.Get_Config(DUT_NAME,'port')+' --log %s'%appium_log
        adb.get_adb(a)
    #关闭appium服务
    def stop_appium(self,DUT_NAME):
        p = os.popen(f"netstat  -aon|findstr {ConfigGet.Get_Config(DUT_NAME,'port')}")
        p0 = p.read().strip()
        if p0 != '' and 'LISTENING' in p0:
            p1 = int(p0.split('LISTENING')[1].strip()[0:5])  # 获取进程号
            print(p1)
            os.system(f'taskkill /F /PID {p1}')  # 结束进程
            print('appium server已结束')

Appium_start = Appium_start()

