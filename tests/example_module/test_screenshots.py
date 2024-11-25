# pytest tests/example_module/test_screenshots.py
from playwright.sync_api import Page, expect

dir = "data/example_module/screenshots/"

def test_screenshot_examples(page):
    page.goto("https://playwright.dev/")
    page.screenshot(path=f"{dir}screenshot_page.png")
    page.screenshot(path=f"{dir}screenshot_full_page.png", full_page=True)
    page.get_by_role("img", name="Browsers (Chromium, Firefox,").screenshot(path=f"{dir}screenshot_image.png")







    