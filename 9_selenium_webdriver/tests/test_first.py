def test_first(browser, url):
    browser.get(url)
    assert browser.title == "Your Store", f"Wrong title: {browser.title}"
