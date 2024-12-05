# pytest tests/cicd/tests/test_cicd_pass.py
from playwright.sync_api import Page, expect
from core.utils import save_trace

def test_cicd_pass(page_context):
    try:
        # Unpack the page and context from the fixture
        page, context = page_context
        
        page.goto("https://playwright.dev/python/")
         
        # Pass:
        expect(page.get_by_label("Switch between dark and light")).to_be_visible()
        
    finally:
        # Stop tracing and save it to a file
        save_trace(context, 'cicd', 'test_cicd_fail.zip')