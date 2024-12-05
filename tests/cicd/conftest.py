import pytest
from playwright.sync_api import sync_playwright
from core.browser_utils import select_browser

@pytest.fixture(scope="function")
def page_context(pytestconfig, request):
    
    # Get options from pytest configuration
    browser_name = pytestconfig.getoption("browser")
    headless = not pytestconfig.getoption("headed")
    
    # Use the last specified browser so that command line options take precedence over pytest.ini
    browser_name = browser_name[-1]
    
    # Use Playwright to launch the browser and create a new context
    with sync_playwright() as p:
        # Select and launch the specified browser
        browser = select_browser(p, browser_name, headless)
        
        context = browser.new_context()
    
        # Start tracing to capture screenshots, snapshots, and sources
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
            
        # Create a new page (tab) in the browser context
        page = context.new_page()
            
        # Yield the page and context to the test function
        yield page, context
            
        # Close the browser context and browser after the test is done
        context.close()
        browser.close()