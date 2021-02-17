from paginas.base import Base
from paginas.locators.elem_news import Elements

class Login(Base):
    def click_login_bt(self):
        bt = Base.elem_found(self.driver, Elements.bt_login)
        bt.click()

    def click_cancel_bt(self):
        bt = Base.elem_found(self.driver, Elements.bt_cancel)
        bt.click()

    def filling_in_field(self, element, text):
        a = False
        if(element == "username"):
            field = Base.elem_found(self.driver, Elements.input_username)
            a = True
        elif(element == "password"):
            field = Base.elem_found(self.driver, Elements.input_password)
            a = True

        if(a):
            field.send_keys(text)

    def check_message(self):
        message = Base.elem_found(self.driver, Elements.err_message)
        return message.text

    def wait_element_username(self):
        Base.elem_found(self.driver, Elements.input_username)

    def toolbar_found(self):
        a = Base.elem_found(self.driver, Elements.toolbar)
        if(a):
            return True
        return False
