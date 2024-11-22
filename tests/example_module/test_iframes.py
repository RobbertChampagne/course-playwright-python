# pytest -s tests/example_module/test_iframes.py::test_frame

from playwright.sync_api import Page, expect
import time
# time.sleep(1)
 
def test_frame(page):
    page.goto("https://www.w3schools.com/howto/tryit.asp?filename=tryhow_html_file_upload_button")
    
    # Accept cookies
    page.get_by_text("Accept all & visit the site").click()
    
    frame = page.locator("iframe[name=\"iframeResult\"]").content_frame
    
    expect(frame.get_by_role("button", name="Submit")).to_be_visible()
    expect(frame.locator("#myFile")).to_be_visible()
    frame.locator("#myFile").click()
    