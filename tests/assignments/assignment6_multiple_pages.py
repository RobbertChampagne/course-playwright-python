# pytest -s tests/assignments/assignment6_multiple_pages.py

# ? TIPS: # https:#playwright.dev/python/docs/pages

# Assignment 6 (Multiple Pages)

from playwright.sync_api import Page, expect

def test_multiple_pages(page):
    # Create two new browser pages from the provided context
    # Use the existing page fixture as page_one
    page_one = page
    
    # Create a new page for page_two
    context = page.context
    page_two = context.new_page()
    
    # Navigate the first page to Sauce Labs login page: https://www.saucedemo.com/
    page_one.goto("https://www.saucedemo.com/")
    
    # Navigate the second page to OrangeHRM login page: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
    page_two.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    # Fill the login form on the first page
    page_one.locator("[data-test=\"username\"]").fill("standard_user")
    page_one.locator("[data-test=\"password\"]").fill("secret_sauce")
    page_one.locator("[data-test=\"login-button\"]").click()
    
    # Fill the login form on the second page
    page_two.get_by_placeholder("Username").fill("Admin")
    page_two.get_by_placeholder("Password").fill("admin123")
    page_two.get_by_role("button", name="Login").click()
    
    # Assertions on the first page
    # Verify the presence of the header text on Sauce Labs : 'Swag Labs'
    expect(page_one.locator('[data-test="primary-header"]')).to_contain_text('Swag Labs')

    # Verify the presence of a specific text within a heading element : 'Dashboard'
    expect(page_two.get_by_role('heading')).to_contain_text('Dashboard')