import pytest
from playwright.sync_api import sync_playwright, expect
from dotenv import load_dotenv
import os
import logging
from core.loggingSetup import setup_logging
from core.browser_utils import select_browser
from ..authentication_module.setup.auth_utils import ensure_auth_state

# Setup logging configuration
setup_logging()
logger = logging.getLogger("Authentication")

# Load environment variables from .env file
load_dotenv()
user = os.getenv('SWAGLABS_USER_ONE')
password = os.getenv('SWAGLABS_PASSWORD')
url = os.getenv('SWAGLABS_URL')

# Define the path for state.json file
state_path = os.path.join(os.path.dirname(__file__), 'setup', 'state.json')

@pytest.fixture(scope="session")
def browser_context(pytestconfig):
    # Get options from pytest configuration
    browser_name = pytestconfig.getoption("browser")
    headless = not pytestconfig.getoption("headed")
    device = pytestconfig.getoption("--device")
    
    # Use the last specified browser so that command line options take precedence over pytest.ini
    browser_name = browser_name[-1]

    # Use Playwright to launch the browser and create a new context
    with sync_playwright() as p:
        
        # Select and launch the specified browser
        browser = select_browser(p, browser_name, headless)
            
        # Ensure the authentication state is valid
        context = ensure_auth_state(p, browser_name, headless, url, user, password, state_path)
        
        # Yield the context to the test functions
        yield context
        
        # Close the browser context and browser after the test is done
        context.close()
        browser.close()
        
@pytest.fixture(scope="function")
def page_context(browser_context):
    # Create a new page in the browser context
    page = browser_context.new_page()
    
    # Navigate to the specified URL
    page.goto(url)
    
    # Yield the page to the test function
    yield page
    
    # Close the page after the test function is done
    page.close()


