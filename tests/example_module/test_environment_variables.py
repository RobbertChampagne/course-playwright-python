# pytest tests/example_module/test_environment_variables.py::test_fixture
from dotenv import load_dotenv
import os
import pytest
from playwright.sync_api import Page, expect
from core.utils import save_trace

# Load environment variables from .env file
load_dotenv()

item_file = os.getenv('TODO_ITEM')

def test_env_file(page):
    page.goto("https://demo.playwright.dev/todomvc/")
    page.locator('input.new-todo').fill(item_file)
    page.locator('input.new-todo').press("Enter")
    
item_terminal = os.getenv('TODO_ITEM_TERMINAL')

def test_env_terminal(page):
    page.goto("https://demo.playwright.dev/todomvc/")
    page.locator('input.new-todo').fill(item_terminal)
    page.locator('input.new-todo').press("Enter")

item_pytest = os.getenv('TODO_ITEM_PYTEST')

def test_pytest_ini_file(page):
    page.goto("https://demo.playwright.dev/todomvc/")
    page.locator('input.new-todo').fill(item_pytest)
    page.locator('input.new-todo').press("Enter")

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page):
    # Set an environment variable inside the fixture
    os.environ['TODO_ITEM_FIXTURE'] = 'Buy bread'
    
    yield

def test_fixture(page):
    item_fixture = os.getenv('TODO_ITEM_FIXTURE')
    page.goto("https://demo.playwright.dev/todomvc/")
    page.locator('input.new-todo').fill(item_fixture)
    page.locator('input.new-todo').press("Enter")
   
