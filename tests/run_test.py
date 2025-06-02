# pip install selenium webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from ui.test_menu import *
from ui.test_contact import *
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url_local = "http://127.0.0.1:5000"

def run_tests():
    test_navegacao(driver, url_local, time)
    test_envia_formulario_contact(driver, url_local, time)

if __name__ == "__main__":
    run_tests()