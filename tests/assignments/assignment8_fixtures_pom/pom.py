from playwright.sync_api import expect

# Define a class
class TodoList:

    # Constructor method that initializes the class object
    def __init__(self, page):
        self.page = page
        self.input_new_item = page.locator('input.new-todo')
        self.list_items = page.get_by_test_id("todo-title") # can be multiple
        self.delete_button = page.get_by_role("button", name="Delete")
        
    def navigate(self):
        self.page.goto("https://demo.playwright.dev/todomvc/")

    def add_item(self, text):
        self.input_new_item.fill(text)
        self.input_new_item.press("Enter")
        
    def remove_item(self, text):
        self.list_items.get_by_text(text).hover()
        self.delete_button.click()
    
    def remove_all(self):
        while self.list_items.count() > 0:
            self.list_items.nth(0).hover()
            self.delete_button.click()
        
    def check_list(self, text):
        item = self.list_items.filter(has_text= text)
        expect(item).to_be_visible()
        expect(item).to_contain_text(text)