def test_check_header(browser):
    browser.get("https://konfic.github.io/front_example/pages/slowlyloading.html")
    browser.implicitly_wait(5)
    browser.find_element_by_id("header")
    