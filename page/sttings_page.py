import sys,os
sys.path.append(os.getcwd())

from base.base_aciton import BaseAciton
import base
class TestPage(BaseAciton):
    def __init__(self,driver):
        BaseAciton.__init__(self,driver)

    def click_search(self):
        self.click_element(base.setting_scearvh_id)

    def input_setting_text(self,content):
        self.input_element_content(base.setting_text,content)

    def click_back(self):
        self.click_element(base.setting_back)