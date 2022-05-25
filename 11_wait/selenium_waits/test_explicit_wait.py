from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_header(browser):
    browser.get("https://konfic.github.io/front_example/pages/slowlyloading.html")
    
    wait = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "header")),
        message=f"The element is not present in the page."
    )
