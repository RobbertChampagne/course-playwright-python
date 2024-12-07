# pytest -s tests/assignments/assignment1.py::test_locating_elements

# Assignment 1 (Locators)

from playwright.sync_api import Page, expect

def test_locating_elements(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").fill("Todo 1")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_label("Toggle Todo").check()
    page.get_by_label("Delete").click()
    

# Now use only the .locator() function to recreate the previous flow.
# Open a normal browser navigate to the todo app and open the inspector so you can find the css selectors.

def test_locating_elements_locator(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.locator('').fill('Todo 1')
    page.locator('').press('Enter')
    page.locator('').check()
    page.locator('').click()
    
# Explanation:
# Most of the time it will be possible to use the recommended built -in locators,
# but as the situation becomes more complex you may need to use the .locator() function from time to time.