# pytest -s tests/assignments/assignment4_download.py::test_download

# Assignment 4 (Downloads)

# What is Playwright doing?:
# Playwright is waiting for the download to happen before it is going to click the button.

from playwright.sync_api import Page, expect

def test_download(page):
    page.goto("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download")

    # Accept cookies
    page.get_by_text("Accept all & visit the site").click()
        
    # Start waiting for the download
    with page.expect_download() as download_info:

        # Click the download link inside the iframe
        page.locator("iframe[name=\"iframeResult\"]").content_frame.get_by_role("link", name="W3Schools").click()

    # Get the download object
    download = download_info.value

    # Save the download
    download.save_as("./downloads/w3schools.html")    
