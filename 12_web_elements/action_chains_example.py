from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import time

URL = "https://www.w3schools.com/html/tryit.asp?filename=tryhtml5_draganddrop2"


def browser_factory(browser: str) -> webdriver:
    driver: webdriver = None
    
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(GeckoDriverManager().install())
    else:
        return f"Got unexpected browser - {browser}"
    
    return driver


def drag_and_drop_element(browser_name: str = "chrome") -> None:
    browser = browser_factory(browser_name)
    browser.get(URL)
    
    action = ActionChains(browser)
    
    time.sleep(5)
    
    img = browser.find_element(By.CSS_SELECTOR, "img#drag1")
    div_1 = browser.find_element(By.CSS_SELECTOR, "div#div1")
    div_2 = browser.find_element(By.CSS_SELECTOR, "div#div2")
    
    for _ in range(1, 11):
        action.click_and_hold(img).pause(0.3).move_to_element(div_1).release()
        action.click_and_hold(img).pause(0.3).move_to_element(div_2).release()
        action.perform()


if __name__ == "__main__":
    drag_and_drop_element()
