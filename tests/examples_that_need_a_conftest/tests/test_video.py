# pytest tests/examples_that_need_a_conftest/tests/test_video.py
from playwright.sync_api import Page, expect
import logging

# Setup logging configuration
logger = logging.getLogger("Examples that need a conftest")

def test_video(page_context):
    page, context = page_context
    page.goto("https://playwright.dev/python/")
    page.get_by_role("link", name="Get started").click()
    page.get_by_role("link", name="What's next", exact=True).click()
    page.get_by_role("link", name="See a trace of your tests").click()
    page.get_by_label("Home page").click()
    
    # Pass:
    #expect(page.get_by_label("Switch between dark and light")).to_be_visible()

    # Fail:
    expect(page.get_by_label("Switch between dark and light123")).to_be_visible()






    