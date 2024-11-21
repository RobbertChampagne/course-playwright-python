# pytest -s tests/assignments/assignment2.py::test_filter_and_locator_solution

# Assignment 2 (Filtering Locators)

from playwright.sync_api import Page, expect

# Follow these steps in codegen
def test_add_multiple_todo_items(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").fill("Todo 1")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Todo 2")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Todo 3")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    # Do NOT select the item first
    page.get_by_role("button", name="Delete").click()  # Will fail

# Use .filter() & .locator() to find the right button you want to click on.
def test_filter_and_locator_solution(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").fill("Todo 1")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Todo 2")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Todo 3")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    
    # Find the list item containing "Todo 1"
    todo_item = page.locator("li").filter(has_text="Todo 1")

    # Hover over the list item to make the delete button visible
    todo_item.hover()

    # Click the delete button
    todo_item.locator("button.destroy").click()
    
    