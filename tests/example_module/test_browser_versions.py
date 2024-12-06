# pytest -s tests/example_module/test_browser_versions.py

from playwright.sync_api import sync_playwright, expect

def test_browser_versions():
        with sync_playwright() as p:
            # Specify the path to the Chrome Beta executable
            chrome_beta_path = "C:\drivers\ChromeSetup.exe"
        
            # Launch the browser with the chrome-beta channel
            browser = p.chromium.launch(executable_path=chrome_beta_path, headless=False)
            
            # Print the browser version
            print(f"Browser version: {browser.version()}")
            
            context = browser.new_context()
            page = context.new_page()
            
            page.goto("https://reqres.in/")
            
            browser.close()

'''
Chromium Channels
chrome (Stable)
chrome-beta
chrome-dev
chrome-canary
msedge (Stable)
msedge-beta
msedge-dev
msedge-canary
Firefox Channels
firefox (Stable)
firefox-beta
firefox-nightly
WebKit Channels
webkit (Stable)
'''