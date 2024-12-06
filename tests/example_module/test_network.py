# pytest -s tests/example_module/test_network.py::test_abort --headed

from playwright.sync_api import Page, expect
import time
# time.sleep(1)

def test_all_events(page):
    # Subscribe to "request" and "response" events.
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    page.goto("https://reqres.in/api/users?page=2")
    
def test_specific_event(page):
    # Use a glob url pattern
    with page.expect_response("**/users?page=2") as response_info:
        page.goto("https://reqres.in/api/users?page=2")
        expect(page.get_by_text("{\"page\":2,\"per_page\":6,\"total")).to_be_visible()
    response = response_info.value
    print(response.status, response.url)
    
test_data = "Test data"

def test_fulfill(page):
    page.route(
        "**/users?page=2",
        lambda route: route.fulfill(status=200, body=test_data))
    page.goto("https://reqres.in/api/users?page=2")
 
def test_continue(page):
    # Intercept and continue the request, and print request details
    def handle_route(route):
        request = route.request
        print(f"Intercepted request: {request.method} {request.url}")
        route.continue_()

    page.route("**/users?page=2", handle_route)
    page.goto("https://reqres.in/api/users?page=2")
    
def test_abort(page):
    page.route("**/users?page=2", lambda route: route.abort())
    page.goto("https://reqres.in/")
    page.get_by_role("link", name="List users").click()
    page.get_by_role("link", name="/api/users?page=").click()
