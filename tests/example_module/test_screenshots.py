# pytest tests/example_module/test_screenshots.py
from playwright.sync_api import Page, expect

dir = "data/example_module/screenshots/"

def test_screenshot_examples(page):
    page.goto("https://playwright.dev/")
    
    # Capture a screenshot of the current view of the page
    page.screenshot(path=f"{dir}screenshot_page.png")

    # Capture a screenshot of the entire page, including parts not visible in the viewport
    page.screenshot(path=f"{dir}screenshot_full_page.png", full_page=True)

    # Capture a screenshot of a specific image element identified by its role and name
    page.get_by_role("img", name="Browsers (Chromium, Firefox,").screenshot(path=f"{dir}screenshot_image.png")







    