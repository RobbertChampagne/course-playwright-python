# pytest tests/cicd/tests/test_cicd_fail.py
from playwright.sync_api import Page, expect
from core.utils import save_trace

def test_cicd_fail(page_context):
    try:
        # Unpack the page and context from the fixture
        page, context = page_context
        
        page.goto("https://playwright.dev/python/")
       
        # Fail:
        expect(page.get_by_label("123")).to_be_visible()
        
    finally:
        # Stop tracing and save it to a file
        save_trace(context, 'cicd', 'test_cicd_fail.zip')