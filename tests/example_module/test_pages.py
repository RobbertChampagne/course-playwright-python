# pytest tests/example_module/test_pages.py 

from playwright.sync_api import Page, expect

def test_multiple_pages(page):
    # Use the existing page fixture as page_one
    page_one = page
    
    # Create a new page for page_two
    context = page.context
    page_two = context.new_page()
    
    page_one.goto("https://www.saucedemo.com/")
    page_one.locator("[data-test=\"username\"]").fill("standard_user")
    page_one.locator("[data-test=\"password\"]").fill("secret_sauce")
    page_one.locator("[data-test=\"login-button\"]").click()
    
    page_two.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page_two.get_by_placeholder("Username").fill("Admin")
    page_two.get_by_placeholder("Password").fill("admin123")
    page_two.get_by_role("button", name="Login").click()
    
def test_handling_new_pages(page):
    page.goto("https://fl.amazon-press.com.be/")
    with page.expect_popup() as page2_info:
        page.get_by_label("Twitter").click()
    page2 = page2_info.value
    expect(page2.get_by_label("X", exact=True)).to_be_visible()