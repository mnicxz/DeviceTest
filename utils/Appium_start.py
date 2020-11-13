# coding:utf-8
# appium_start.py
from appium import webdriver
from utils.Dos_adb  import Dos_adb
from config.ConfigGet import ConfigGet
import os
path  =os.path.dirname(os.getcwd())# appium日志路径
appium_log = os.path.join(os.path.join(path,'logs'),'appium_log.txt')
class Appium_start():
    def Android_device(self,DUT_NAME):
        print('我进来启动app了')
        '''启动app'''
        driver = ConfigGet.Get_Device_Config(DUT_NAME)
        return driver
    def start(self):
        print('我进来启动appium了')
        '''
         启动appium
        '''
        adb = Dos_adb()
        devices = adb.get_device()[0]
        a = 'appium -p 4723 -U '+devices +' --log  %s' %appium_log
        adb.get_adb(a)
if __name__ == '__main__':
    Appium_start = Appium_start()
    Appium_start.start()
    Appium_start.Android_device('SUBDUT')