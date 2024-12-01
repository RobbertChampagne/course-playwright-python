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
    todo_list.navigate()
    
    # Add a the first item to the todo list
    todo_list.add_item(item)
    
    # Run the tests.
    yield
    
    # Clean up.
    todo_list.remove_all()
    
def test_pom(page):
    item_two = "Buy cookies"
    item_three = "Buy water"
    todo_list = TodoList(page)
    
    # Navigate to the Todo page
    todo_list.navigate()
    
    # Add items to the todo list
    todo_list.add_item(item_two)
    todo_list.add_item(item_three)
    
    # Verify that the new items are added to the list
    todo_list.check_list(item_two)
    todo_list.check_list(item_three)
    
    # Remove a item from the list
    todo_list.remove_item(item_two)
  