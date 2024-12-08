# pytest tests/assignments/assignment7_new_pages.py

# ? TIPS: # https:#playwright.dev/python/docs/pages

# Assignment 7 (New Pages)

from playwright.sync_api import Page, expect

def test_new_pages(page):
    # Navigate the page to the Amazon Press Belgium website : 'https://fl.amazon-press.com.be/'
    ...
    
    # Start waiting for a new page to open (before clicking the Twitter button)
    ...
        
        # Click the Twitter button, triggering the opening of a new page
        #...
        
    # Wait for the new page to be available   
    ...
    
    # Expect that the 'X' logo is visible on the new page
    ...