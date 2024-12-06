# pytest -s tests/example_module/test_network.py 

from playwright.sync_api import Page, expect

def test_all_events(page):
    # Subscribe to "request" and "response" events.
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    page.goto("https://reqres.in/api/users?page=2")
    
