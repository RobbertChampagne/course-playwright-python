import html
import pytest
from playwright.sync_api import sync_playwright, expect
from dotenv import load_dotenv
import os
import logging
import sys
from pytest_html import extras
import pytest_html
from core.html_summary import pytest_html_results_summary
from core.loggingSetup import setup_logging
from core.browser_utils import select_browser

# Setup logging configuration
setup_logging()
logger = logging.getLogger("Standalone Scripts")

@pytest.fixture(scope="function")
def page_context(pytestconfig):
    # Log the start of the session
    logger.info("Starting session")
    
    # Get options from pytest configuration
    browser_name = pytestconfig.getoption("browser")
    headless = not pytestconfig.getoption("headed")
    device = pytestconfig.getoption("--device")
    
    # Use the last specified browser so that command line options take precedence over pytest.ini
    browser_name = browser_name[-1]
    
    logger.info(f"Browser specified: {browser_name}")
    logger.info(f"Headless mode: {headless}")
    logger.info(f"Device specified: {device}")
    
    # Use Playwright to launch the browser and create a new context
    with sync_playwright() as p:
        
        # Check if a device is specified and the browser supports mobile emulation
        if device and browser_name == "firefox":
            logger.info("Firefox does not support mobile emulation. Switching to Chromium.")
            browser_name = "chromium"
            browser = p.chromium.launch(headless=headless)
        else:
            # Select and launch the specified browser
            browser = select_browser(p, browser_name, headless)
        
        # To override the browser selection from the pytest.ini file and launch a specific browser, 
        # use the following code:
        # browser = p.chromium.launch(headless=False)
        
        # Check if a device is specified and the browser supports mobile emulation
        if device and browser_name in ["chromium", "webkit"]:
            device_config = p.devices[device]
            context = browser.new_context(**device_config)
        else:
            # Create a new browser context (similar to a new incognito window)
            context = browser.new_context()
        
        logger.info(f"Launching {browser_name} browser")
        
        # Start tracing to capture screenshots, snapshots, and sources
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        
        # Create a new page (tab) in the browser context
        page = context.new_page()
        
        # Yield the page and context to the test function
        yield page, context
        
        # Close the browser context and browser after the test is done
        context.close()
        browser.close()
        
# Hook to add a title to the HTML report
@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    report.title = "Playwright Module A Tests"
    
# Hook to capture screenshots on test failure and attach to HTML report
# ------------------------------------------------------------------------------
# This decorator registers the function as a pytest hook implementation.
# The hookwrapper=True argument indicates that this hook will wrap the execution of other hooks, 
# allowing it to yield control and then continue execution after other hooks have run.
@pytest.hookimpl(hookwrapper=True)
# This defines the hook function pytest_runtest_makereport, which is called to create a test report for each test item.
# item: The test item being reported on.
# call: The call object representing the test function call.
def pytest_runtest_makereport(item, call):
    # This yields control to other hooks and waits for them to complete. 
    # After other hooks have run, control returns to this function.
    outcome = yield
    # This retrieves the test report object from the outcome of the test function call.
    report = outcome.get_result()
    # This retrieves the extras attribute from the report object, if it exists. 
    # If it doesn't exist, it initializes extras as an empty list. 
    # extras is used to store additional information to be included in the HTML report.
    extras = getattr(report, "extras", [])
    # This checks if the report is for the test function call phase (as opposed to setup or teardown).
    if report.when == "call":
        # This always adds a URL to the report. In this case, it adds "http://www.example.com/".
        extras.append(pytest_html.extras.url("http://www.example.com/"))
        # This checks if the test failed.
        if report.failed:
            # This adds additional HTML content to the report if the test failed.
            extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
            # The item object represents the test item being reported on. 
            # It contains information about the test function, including its arguments. 
            # The funcargs attribute of the item object is a dictionary that maps argument names to their values. 
            # This dictionary includes all the fixtures that were provided to the test function. 
            # This line retrieves the value of the page_context fixture from the funcargs dictionary.
            page_context = item.funcargs.get("page_context")
            # This checks if the page_context fixture is available.
            if page_context:
                page, context = page_context
                # Extract the test function name from item.nodeid
                test_function_name = item.nodeid.split("::")[-1]
                # The item.nodeid is used to create a unique filename for the screenshot, replacing :: with _.
                screenshot_path = f"data/failure_screenshots/{test_function_name}.png"
                page.screenshot(path=screenshot_path)
                # This adds the screenshot image to the extras list, which will be included in the HTML report.
                extras.append(pytest_html.extras.image(screenshot_path))
        # This assigns the extras list back to the report object, 
        # ensuring that the additional information is included in the HTML report.
        report.extras = extras

