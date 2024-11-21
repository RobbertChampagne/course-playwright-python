# pytest -s tests/example_module/test_locators.py::test_trigger_action

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
    
def close_dropdown(page):
    page.locator("header").click()

def test_locate_by_css(page):
    page.goto("https://playwright.dev/")
    
    #<div class="navbar__item dropdown dropdown--hoverable">...</div>
    
    # Using Class Attribute
    page.locator(".navbar__item.dropdown").click()
    close_dropdown(page)
    
    # Using Attribute Selector
    page.locator("[class*='navbar__item'][class*='dropdown']").click()
    close_dropdown(page)
    
    # Using Combination of Tag and Class
    page.locator("div.navbar__item.dropdown").click()
    close_dropdown(page)
    
    # Using XPath
    page.locator("//div[contains(@class, 'navbar__item') and contains(@class, 'dropdown')]").click()
    close_dropdown(page)

def test_filter_by_text(page):
    page.goto("https://playwright.dev/python/docs/locators")
    '''
    <ul class="table-of-contents table-of-contents__left-border">
        <li><a class="table-of-contents__link toc-highlight">Locating elements</a>
            <ul>
                <li><a class="table-of-contents__link toc-highlight">Locate by role</a></li>
                <li><a class="table-of-contents__link toc-highlight">Locate by text</a></li>
            </ul>
        </li>
    </ul>
    '''
    
    # <li><a>Locating elements</a></li>
    page.get_by_role("listitem").filter(has_text="Locating elements").click()
    
def test_filter_by_not_text(page):
    page.goto("https://playwright.dev/python/docs/locators")
    '''
    <ul class="table-of-contents table-of-contents__left-border">
        <li><a class="table-of-contents__link toc-highlight">Locating elements</a>
            <ul>
                <li><a class="table-of-contents__link toc-highlight">Locate by role</a></li>
                <li><a class="table-of-contents__link toc-highlight">Locate by text</a></li>
            </ul>
        </li>
    </ul>
    '''
    
    # <li><a>Locating elements</a></li>
    print(f'Count: {page.get_by_role("listitem").filter(has_not_text="Locating elements").count()}')
    # Count: 122


def test_filter_by_child(page):
    page.goto("https://playwright.dev/python/docs/locators")
    '''
     <ul>
       <li>
           <a>Locating elements</a>
       </li>
     </ul>
    '''
    page.get_by_role("list").filter(has=page.get_by_role("listitem").filter(has_text="Locating elements")).click()
    
def test_filter_by_child_has_only_one(page):
    page.goto("https://playwright.dev/python/docs/locators")
    '''
     <ul>
       <li>
           <a>Locating elements</a>
       </li>
     </ul>
    '''
    expect(page.get_by_role("list").filter(has=page.get_by_role("listitem").filter(has_text="Locating elements"))).to_have_count(1)
    
def test_filter_by_has_not_child(page):
    page.goto("https://playwright.dev/python/docs/locators")
    '''
     <ul>
       <li>
           <a>Locating elements</a>
       </li>
     </ul>
    '''
    print(f'Count: {page.get_by_role("list").filter(has_not=page.get_by_role("listitem").filter(has_text="Locating elements")).count()}')
    # Count: 23

def test_chaining_filters(page):
    page.goto("http://127.0.0.1:5501/opleiding-playwright-python/tests/example_module/test.html")
    row_locator = page.get_by_role("listitem")
    row_locator.filter(has_text="Mary").filter(has=page.get_by_role("button", name="Say goodbye")).click()

def test_trigger_action(page):
    page.goto("http://127.0.0.1:5501/opleiding-playwright-python/tests/example_module/test.html")
    listitems = page.locator(".fruit")
    count = listitems.count()
    for i in range(count):
        print(listitems.nth(i).text_content())
        

