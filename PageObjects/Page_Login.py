from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By



class Login_Page:


    TextBox_Email_Id = 'input-email'
    TextBox_Password_Id = 'input-password'
    Button_Login_Xpath = "//input[@type='submit']"

    def __init__(self, driver):
        self.driver = driver


    def Set_Email(self, UserEmail):
        self.driver.find_element(By.ID, self.TextBox_Email_Id).clear()
        self.driver.find_element(By.ID, self.TextBox_Email_Id).send_keys(UserEmail)

    def Set_Password(self, Password):
        self.driver.find_element(By.ID, self.TextBox_Password_Id).clear()
        self.driver.find_element(By.ID, self.TextBox_Password_Id).send_keys(Password)

    def Click_Login(self):
        self.driver.find_element(By.XPATH, self.Button_Login_Xpath).click()
