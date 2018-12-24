import sys,os
import pytest
import yaml

sys.path.append(os.getcwd())
from base.base_driver import init_driver
import base
from page.sttings_page import TestPage


def read_setting_data():
    with open(".\data\setting_data.yaml") as f:
        read_data = yaml.load(f)
        data_list = read_data.get("data")
        return data_list


class TestSetting:
    def setup(self):
        self.driver = init_driver(base.app_package,base.app_activity)
        self.settin_page = TestPage(self.driver)




    def teardown(self):
        self.driver.quit()
    @pytest.mark.parametrize('content',read_setting_data())
    def test_setting(self,content):
        self.settin_page.click_search()
        self.settin_page.input_setting_text(content)
        self.settin_page.click_back()