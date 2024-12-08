# pytest tests/assignments/assignment8_fixtures_pom/assignment8_fixtures_pom.py
import pytest
from playwright.sync_api import Page, expect
from pom import TodoList

# Assignment 8 (Fixture + POM)

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page):
    item = "Buy milk"
    todo_list = TodoList(page)

    # Go to the starting url before each test.
    ...
    
    # Add a the first item to the todo list
    ...
    
    # Run the tests.
    yield
    
    # Clean up.
    ...
    
def test_pom(page):
    item_two = "Buy cookies"
    item_three = "Buy water"
    todo_list = TodoList(page)
    
    # Navigate to the Todo page
    ...
    
    # Add items to the todo list
    ...
    
    # Verify that the new items are added to the list
    ...
    
    # Remove a item from the list
    ...
  