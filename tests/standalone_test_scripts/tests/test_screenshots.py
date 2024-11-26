# pytest tests/standalone_test_scripts/tests/test_screenshots.py
from playwright.sync_api import Page, expect
import logging

# Setup logging configuration
logger = logging.getLogger("Standalone test scripts")

def test_screenshot_examples(page_context):   
    # Simulate a failure to capture a screenshot
    page, context = page_context
    page.set_default_timeout(5000)
    page.goto("https://playwright.dev/")
                
    # Pass:
    # expect(page.get_by_role("img", name="Browsers (Chromium, Firefox,")).to_be_visible()

    # Fail:
    expect(page.get_by_role("img", name="123")).to_be_visible()





    