from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy

class Elements(object):
    # HOME
    menu = (MobileBy.ACCESSIBILITY_ID, "Navigate up")
    expander = (MobileBy.ID, "com.leavjenn.hews:id/iv_expander")
    login = (MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().textContains(\"Login\")")
    toolbar = (MobileBy.ID, "com.leavjenn.hews:id/toolbar")

    #LOGIN
    input_username = (MobileBy.ID, "com.leavjenn.hews:id/et_user_name")
    input_password = (MobileBy.ID, "com.leavjenn.hews:id/et_password")
    bt_cancel = (MobileBy.ID, "android:id/button2")
    bt_login = (MobileBy.ID, "android:id/button1")
    err_message = (MobileBy.ID, "com.leavjenn.hews:id/tv_prompt")