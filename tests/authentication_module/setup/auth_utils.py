import os
import logging
from playwright.sync_api import Browser, BrowserContext, Page, Playwright, expect
from core.browser_utils import select_browser

def ensure_auth_state(playwright: Playwright, browser_name: str, headless: bool, url: str, username: str, password: str, state_path: str):
   
    # Create a headless browser for the authentication check (set to True)
    headless_browser = select_browser(playwright, browser_name, True)
    
    try:
        # Use the saved state.json for the browser context
        context = headless_browser.new_context(storage_state=state_path)
        page = context.new_page()
        
        page.goto(url)
        
        # Perform a simple check to ensure the state is valid
        try:
            expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products", timeout=5000)
            # Close the initial page after the check
            page.close()  
            # Close the headless context
            context.close()  
            # Close the headless browser
            headless_browser.close()  
            # Create a new context for the actual test
            browser = select_browser(playwright, browser_name, headless)
            # Return the context immediately if the state is valid
            return browser.new_context(storage_state=state_path)  
        except TimeoutError:
            logging.warning("State is invalid or expired. Recreating state.json.")
            raise Exception("State is invalid or expired.")
        
    except Exception as e:
        logging.warning(f"State is invalid or expired: {e}. Recreating state.json.")
        # If an exception occurs, delete the state.json file and perform login steps
        if os.path.exists(state_path):
            os.remove(state_path)
            
        # Reuse the initially created headless browser
        context = headless_browser.new_context()
        page = context.new_page()
        
        page.goto(url)
        page.locator("[data-test=\"username\"]").fill(username)
        page.locator("[data-test=\"password\"]").fill(password)
        page.locator("[data-test=\"login-button\"]").click()
        
        # Navigate to the inventory page after login
        page.goto(f"{url}/inventory.html")

        # Save the logged-in state to state.json
        context.storage_state(path=state_path)
        page.close()  # Close the initial page after the check
    
    #return context
    # Close the headless browser after recreating the state
    headless_browser.close()
    
    # Create a new context for the actual test
    browser = select_browser(playwright, browser_name, headless)
    return browser.new_context(storage_state=state_path)