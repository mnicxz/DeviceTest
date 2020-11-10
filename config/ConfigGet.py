import configparser
from appium import webdriver
"""
    #此模块用于获取各配置文件内容并返回至case使用
"""

class ConfigGet():
    #获取设备config
    def Get_Device_Config(self,DUT_name:str):
        config = configparser.ConfigParser()
        config.read(r'E:\LongcheerBU3Test\config\DevicesConfig.ini')
        cops = {}
        cops["platformName"] = config.get(DUT_name, 'platformName')
        cops["platformVersion"] = config.get(DUT_name, 'platformVersion')
        cops["deviceName"] = config.get(DUT_name, 'deviceName')
        cops["appPackage"] = config.get(DUT_name, 'appPackage')
        cops["appActivity"] = config.get(DUT_name, 'appActivity')
        cops["autoAcceptAlerts"] = config.get(DUT_name, 'autoAcceptAlerts')
        cops["noReset"] = config.get(DUT_name, 'noReset')
        cops["automationName"] = config.get(DUT_name, 'automationName')
        url = config.get(DUT_name,'url')
        Device = webdriver.Remote(url, cops)
        return Device

ConfigGet = ConfigGet()