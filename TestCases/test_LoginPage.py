from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.Page_Login import Login_Page
from Utilities.ReadConfigFile import Read_Config

class Test_Login:
    URL = Read_Config.Get_App_URL()
    UserEmail = Read_Config.Get_Email()
    Password = Read_Config.Get_Pwd()

    def test_login(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(self.URL)
        Log = Login_Page(driver)
        Log.Set_Email(self.UserEmail)
        Log.Set_Password(self.Password)
        Log.Click_Login()
