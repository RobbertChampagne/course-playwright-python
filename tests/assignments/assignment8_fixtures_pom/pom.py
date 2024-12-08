from playwright.sync_api import expect

# Define a class
class TodoList:

    # Constructor method that initializes the class object
    def __init__(self, page):
        self.page = page
        self.input_new_item = ...
        self.list_items = ... # can be multiple
        self.delete_button = ...
        
    def navigate(self):
        self.page.goto("https://demo.playwright.dev/todomvc/")

    def add_item(self, text):
        ...
        
    def remove_item(self, text):
        ...
    
    def remove_all(self):
        ...
        
    def check_list(self, text):
        ...