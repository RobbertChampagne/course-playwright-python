# pytest -s tests/assignments/assignment6_multiple_pages.py

# ? TIPS: # https:#playwright.dev/python/docs/pages

# Assignment 6 (Multiple Pages)

from playwright.sync_api import Page, expect

def test_multiple_pages(page):
    # Create two new browser pages from the provided context
    # Use the existing page fixture as page_one
    ...
    
    # Create a new page for page_two
    context = page.context
    ... = context.new_page()
    
    # Navigate the first page to Sauce Labs login page: https://www.saucedemo.com/
    ...
    
    # Navigate the second page to OrangeHRM login page: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
    ...
    
    # Fill the login form on the first page (standard_user, secret_sauce)
    ...
    
    # Fill the login form on the second page (Admin, admin123)
    ...
    
    # Assertions on the first page
    # Verify the presence of the header text on Sauce Labs : 'Swag Labs'
    expect(...).to_contain_text('Swag Labs')

    # Verify the presence of a specific text within a heading element : 'Dashboard'
    expect(...).to_contain_text('Dashboard')