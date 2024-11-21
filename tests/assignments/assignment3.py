# pytest -s tests/assignments/assignment3.py::test_filter_and_locator_solution

# Assignment 3 (Filtering Locators with the same text)

from playwright.sync_api import Page, expect

def test_add_multiple_todo_items(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").fill("Todo")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Todo")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Todo")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    # Do NOT select the item first
    page.get_by_role("button", name="Delete").click()  # Will fail

# Use .filter() & .locator() to find the delete button from the second item.
def test_filter_and_locator_solution(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").fill("Todo")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Todo")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("Todo")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    
    # Find the list item containing "Todo"
    todo_items = page.locator("li").filter(has_text="Todo")

    # Hover over the second list item to make the delete button visible
    todo_items.nth(1).hover()

    # Click the delete button
    todo_items.nth(1).locator("button.destroy").click()
