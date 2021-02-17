from paginas.base import Base
from paginas.locators.elem_news import Elements

class Home(Base):
    def access_login(self):
        btn_menu = Base.elem_found(self.driver, Elements.menu)
        btn_menu.click()

        ic_exp = Base.elem_found(self.driver, Elements.expander)
        ic_exp.click()

        ic_login = Base.elem_found(self.driver, Elements.login)
        ic_login.click()

