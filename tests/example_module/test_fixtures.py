# pytest -s tests/example_module/test_fixtures.py
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page):
    
    print("before the test runs")

    # Go to the starting url before each test.
    page.goto("https://playwright.dev/")
    yield
    
    print("after the test runs")

def test_main_navigation(page):
    # Assertions use the expect API.
    expect(page).to_have_url("https://playwright.dev/")