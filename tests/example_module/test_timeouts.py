# pytest -s tests/example_module/test_timeouts.py::test_default_expect_timeout

from playwright.sync_api import Page, expect

def test_default_timeout(page):
    page.goto("https://example.com")
    
    # This will wait for an element that does not exist, causing a timeout
    page.get_by_text("Non-existent element").click()
 
    # Locator.click: Timeout 30000ms exceeded.
 
def test_custom_timeout(page):
    page.set_default_timeout(10000)  # Set custom timeout to 10 seconds
    page.goto("https://example.com")
    
    # This will wait for an element that does not exist, causing a timeout
    page.get_by_text("Non-existent element").click()

    # Locator.click: Timeout 10000ms exceeded.
        
# expect.set_options(timeout=1000)

def test_default_expect_timeout(page):
    page.goto("https://example.com")
    
    # This will wait for an element that does not exist, causing a timeout
    expect(page.get_by_text("Non-existent element")).to_be_visible()
    # Fails in +/- 5 seconds.
    

def test_custom_expect_timeout(page):
    page.goto("https://example.com")
    
    # This will wait for an element that does not exist, causing a timeout
    expect(page.get_by_text("Non-existent element")).to_be_visible(timeout=10000)
    # Fails in +/- 10 seconds.
