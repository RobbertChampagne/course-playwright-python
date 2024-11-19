# pytest -s tests/example_module/test_locators.py::test_locate_by_title

import re
from playwright.sync_api import Page, expect

def test_locating_elements(page):
    page.goto("https://playwright.dev/")
    get_started_button = page.get_by_role("link", name="Get started")
    
    get_started_button.hover()
    get_started_button.click()
    
def test_locate_by_role(page):
    page.goto("https://playwright.dev/")
    
    # <a role="button" class="navbar__link">Python</a>
    page.get_by_role("button", name="Python").click()
    page.get_by_role("banner").click()
    page.get_by_role("link", name="Get started").click()
    
def test_locate_by_label(page):
    page.goto("https://playwright.dev/")
    
    # <a ... aria-label="GitHub repository"></a>
    page.get_by_label("GitHub repository").click()

def test_locate_by_placeholder(page):
    page.goto("https://playwright.dev/")
    
    # <input ... placeholder="Search docs" >
    page.get_by_label("Search").click()
    page.get_by_placeholder("Search docs").click()
    
def test_locate_by_text(page):
    page.goto("https://playwright.dev/")
    
    # <span>Playwright</span>
    page.get_by_text("Playwright", exact=True).click()
    
def test_locate_by_alt_text(page):
    page.goto("https://playwright.dev/")
    
    # <img src="img/logos/Browsers.png" alt="Browsers (Chromium, Firefox, WebKit)"> 
    expect(page.get_by_alt_text("Browsers (Chromium, Firefox,")).to_be_visible()
    





