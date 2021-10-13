import paths as path
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# chromeOptions = Options()
# chromeOptions.set_headless(headless=True)
driver = webdriver.Chrome('C:\\SeleniumDriver\\chromedriver.exe');

def browseTwitter():
    driver.get('https://twitter.com/i/flow/login');
    driver.maximize_window();
    driver.implicitly_wait(10);

def login(emailLogin, passwordLogin):
    emailInput = driver.find_element_by_xpath(path.emailInputPath);
    emailInput.send_keys(emailLogin);
    sleep(1);

    loginButton = driver.find_element_by_xpath(path.loginButtonPath);
    loginButton.click();
    sleep(1);
        
    passwordInput = driver.find_element_by_xpath(path.passwordInputPath);
    passwordInput.send_keys(passwordLogin)
    sleep(1);

    loginPasswordButton = driver.find_element_by_xpath(path.loginPasswordPath);
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, f'{path.loginPasswordPath}'),
            'Entrar'
        )
    )
    loginPasswordButton.click();

def makeTwit(message):
    inputMessage = driver.find_element_by_xpath(path.inputMessagePath);
    inputMessage.click();
    inputMessage.send_keys(message);
    sleep(1);

    twitButton = driver.find_element_by_xpath(path.twitButtonPath);
    twitButton.click();

def closeChrome():
    driver.quit();






