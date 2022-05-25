from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def wait_title(title: str, driver, timeout: int=3) -> None:
    try:
        WebDriverWait(driver, timeout).until(EC.title_is(title))
    except TimeoutException:
        raise AssertionError(f"Expected the title {title} but got {driver.title}")
    

def assert_element(selector, driver, timeout=1):
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    except TimeoutException:
        driver.save_screenshot(f"{driver.session_id}.png")
        raise AssertionError(f"Element with locator - {selector} does not contains in the page.")
    
    
def test_check_exception(browser):
    browser.get("https://konfic.github.io/front_example/pages/slowlyloading.html")
    wait_title("Example Project", browser)
    assert_element("[name='disable']", browser)
