# coding=utf-8
"""
    #此模块封装重写Appium方法作为公共方法
    #此模块内的方法禁止改动
"""

class Comment():

    def xpath_click(self,xpath):
        """
            Comment.xpath_click(xpath='***')
            通过控件的xpath属性点击
        :param xpath:控件的xpath属性
        :return:无
        """
        self.find_element_by_xpath(xpath).click()

    def id_click(self,id):
        """
            Comment.id_click(id='***')
            通过控件的id属性点击
        :param id:控件的id属性
        :return:无
        """
        self.find_element_by_id(id).click()

    def class_name(self,class_name):
        """
            Comment.class_name(class_name='***')
            通过控件的class_name属性点击
        :param class_name:控件的class_name属性
        :return:无
        """
        self.find_element_by_class_name(class_name).click()

    def text_name_click(self,text_name):
        """
            Comment.text_name_click(text_name='***')
            通过控件的text属性点击
        :param text_name:控件的text属性
        :return:无
        """
        self.find_element_by_android_uiautomator("new UiSelector().text(\"%s\")" % (text_name)).click()

    def swipe(self,x1,y1,x2,y2,duration=None):
        """
            Comment.swipe(self.SUBDUT,x1,y1,x2,y2,duration)
            从A点滑动到B点，滑动时间为毫秒
        :param x1:A点 X坐标
        :param y1:A点 Y坐标
        :param x2:B点 X坐标
        :param y2:B点 Y坐标
        :param duration:滑动时间，越低越快
        :return:无
        """
        self.swipe(x1,y1,x2,y2,duration)

    def GetDeviceSize(self):
        """
            Comment.GetDeviceSize(self.SUBDUT)
            获取设备的宽，高。注意此方法需要接收返回值
        :return:包含宽高信息的list
        """
        list = []
        list.append(self.get_window_size()['width'])
        list.append(self.get_window_size()['height'])
        return list

    def GetClassText_Text(self,text_name):
        """
            Comment.GetClassText_Text(self.SUBDUT,'wlan')
            根据Text属性获取元素文本
        :param text_name:元素Text属性
        :return:元素text文本
        """
        return self.find_element_by_android_uiautomator("new UiSelector().text(\"%s\")" % (text_name)).text

    def GetClassText_Xpath(self,xpath):
        """
            Comment.GetClassText_Xpath(self.SUBDUT,Xpath)
            根据Xpath属性获取元素文本
        :param xpath:元素Xpath属性
        :return:元素text文本
        """
        return self.find_element_by_xpath(xpath).text

    def GetClassText_Id(self,Id):
        """
            Comment.GetClassText_Id(self.SUBDUT,Id)
            根据Id属性获取元素文本
        :param Id:元素Id属性
        :return:元素text文本
        """
        return self.find_element_by_id(id).text
