# pytest tests/example_module/test_pom.py
from models.pom import TodoList
from playwright.sync_api import Page, expect

def test_pom(page):
    item = "Buy milk"
    todo_list = TodoList(page)
    
    # Navigate to the TodoMVC page
    todo_list.navigate()
    
    # Add a new item to the todo list
    todo_list.add_item(item)
    
    # Verify that the new item is added to the list
    expect(page.get_by_test_id("todo-title")).to_be_visible()
    expect(page.get_by_test_id("todo-title")).to_contain_text(item)
    
    # OR
    
    todo_list.check_list(item)
  