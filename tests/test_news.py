import pytest
from paginas.home import Home
from paginas.login import Login
import time

@pytest.mark.usefixtures('setup')
class TestNews(object):
    def test_login_empty(self, setup):
        home = Home(setup)
        home.access_login()

        login = Login(setup)
        login.click_login_bt()
        assert "Catch you, anonymous!" == login.check_message(), "Mensagem errada!"


    def test_login_with_wrong_username_and_without_passwd(self, setup):
        home = Home(setup)
        home.access_login()

        login = Login(setup)
        login.filling_in_field("username", "userTest")
        login.click_login_bt()
        assert "You got a short…password" == login.check_message(), "Mensagem errada!"

    def test_login_without_username(self, setup):
        home = Home(setup)
        home.access_login()

        login = Login(setup)
        login.filling_in_field("password", "qwertyuiop")
        login.click_login_bt()
        assert "Catch you, anonymous!" == login.check_message(), "Mensagem errada!"

    def test_login_with_wrong_username_and_passwd(self, setup):
        home = Home(setup)
        home.access_login()

        login = Login(setup)
        login.filling_in_field("username", "userTest")
        login.filling_in_field("password", "qwertyuiop")
        login.click_login_bt()
        login.wait_element_username()
        assert "Arrr…wrong username/password" == login.check_message(), "Mensagem errada!"

    def test_login_click_cancel(self, setup):
        home = Home(setup)
        home.access_login()

        login = Login(setup)
        login.click_cancel_bt()

        assert login.toolbar_found(), "Não esta na tela principal!"



