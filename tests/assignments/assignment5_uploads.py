# pytest -s tests/assignments/assignment5_uploads.py::test_upload_no_click

# Assignment 5 (Uploads)

# What is Playwright doing?:
# Playwright is using the set_input_files() function and it is not using the file dialog.


from playwright.sync_api import Page, expect

def test_upload(page):
    page.goto("https://www.w3schools.com/howto/tryit.asp?filename=tryhow_html_file_upload_button")
    # Accept cookies
    page.get_by_text("Accept all & visit the site").click()
    
    page.locator("iframe[name=\"iframeResult\"]").content_frame.locator("#myFile").click()
    page.locator("iframe[name=\"iframeResult\"]").content_frame.locator("#myFile").set_input_files("./data/QA.jpg")
    page.locator("iframe[name=\"iframeResult\"]").content_frame.get_by_role("button", name="Submit").click()


# Which action(s)/lines of code are unnecessary?
# Unfortunately, Playwright cannot directly interact with the native file dialog that opens when you click on the file input element due to security reasons. 
# This limitation is common across browser automation tools.

def test_upload_no_click(page):
    page.goto("https://www.w3schools.com/howto/tryit.asp?filename=tryhow_html_file_upload_button")
    # Accept cookies
    page.get_by_text("Accept all & visit the site").click()
    
    #page.locator("iframe[name=\"iframeResult\"]").content_frame.locator("#myFile").click()
    page.locator("iframe[name=\"iframeResult\"]").content_frame.locator("#myFile").set_input_files("./data/QA.jpg")
    page.locator("iframe[name=\"iframeResult\"]").content_frame.get_by_role("button", name="Submit").click()

    expect(page.locator("iframe[name=\"iframeResult\"]").content_frame.get_by_role("button", name="Submit")).to_be_visible()
    expect(page.locator("iframe[name=\"iframeResult\"]").content_frame.locator("#myFile")).to_be_visible()
    page.locator("iframe[name=\"iframeResult\"]").content_frame.locator("#myFile").click()