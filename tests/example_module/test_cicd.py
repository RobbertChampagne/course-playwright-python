# pytest tests/example_module/test_cicd.py
from playwright.sync_api import Page, expect
from core.utils import save_trace

def test_main_navigation(page):
    context = page.context
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    try:    
        page.goto("https://playwright.dev/python/")
       
        # Pass:
        #expect(page.get_by_label("Switch between dark and light")).to_be_visible()

        # Fail:
        expect(page.get_by_label("Switch between dark and light123")).to_be_visible()
    
    finally:
        save_trace(context, 'cicd', 'cicd_example.zip')