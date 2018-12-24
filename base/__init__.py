
from selenium.webdriver.common.by import By

app_package = "com.android.settings"
app_activity = ".Settings"

"""
1.搜索
"""
setting_scearvh_id = (By.ID,"com.android.settings:id/search")
setting_text = (By.ID,"android:id/search_src_text")
setting_back = (By.CLASS_NAME,"android.widget.ImageButton")



