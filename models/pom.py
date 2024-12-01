from playwright.sync_api import expect

# Define a class
class TodoList:

    # Constructor method that initializes the class object
    def __init__(self, page):
        self.page = page
        self.input_new_item = page.locator('input.new-todo')
        self.list_item = page.get_by_test_id("todo-title")
        
    def navigate(self):
        self.page.goto("https://demo.playwright.dev/todomvc/")

    def add_item(self, text):
        self.input_new_item.fill(text)
        self.input_new_item.press("Enter")
        
    def check_list(self, text):
        expect(self.list_item).to_be_visible()
        expect(self.list_item).to_contain_text(text)