# pytest tests/assignments/assignment10_network.py --headed

# Assignment 10 (Network) .fulfill()

from playwright.sync_api import Page, expect

def test_assignment_10(page):
    # Create a custom response
    test_data = '{ "id": 2, "email": "janet.weaver@reqres.in", "first_name": "James", "last_name": "Bond" }'
    
    # Enable request interception + Fulfill the intercepted request with a custom response
    ...
    
    # Navigate to a page that triggers network requests
    ...
    
    # Wait for the response to the intercepted request
    expect(page.locator("pre")).to_contain_text('{ "id": 2, "email": "janet.weaver@reqres.in", "first_name": "James", "last_name": "Bond" }')
    
