# pytest tests/authentication_module/tests/test_one.py

from playwright.sync_api import Page, expect

def test_one(page_context):
    # Unpack the page and context from the fixture
    page = page_context
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page.locator("[data-test=\"item-0-title-link\"]")).to_be_visible()
    
def test_two(page_context):
    # Unpack the page and context from the fixture
    page = page_context
    page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page.locator("[data-test=\"item-0-title-link\"]")).to_be_visible()