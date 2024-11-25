# pytest tests/standalone_test_scripts/tests/test_screenshots.py
from playwright.sync_api import Page, expect
from pytest_html import extras
import pytest
import logging

# Setup logging configuration
logger = logging.getLogger("Standalone test scripts")

def test_screenshot_examples(page_context):   
    # Simulate a failure to capture a screenshot
    try:
        page, context = page_context
        page.set_default_timeout(5000)
        page.goto("https://playwright.dev/")
                
        # Pass:
        expect(page.get_by_role("img", name="Browsers (Chromium, Firefox,")).to_be_visible()

        # Fail:
        #expect(page.get_by_role("img", name="123")).to_be_visible()

    except Exception as e:
        screenshot_path = f"data/failure_screenshots/example_module/test_example_failure.png"
        page.screenshot(path=screenshot_path)
        
        # Attach the screenshot path to the HTML report
        logger.info(f"See screenshot at: {screenshot_path}")
    
        pytest.fail(f"Test failed due to: {e}")




    