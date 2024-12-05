# pytest tests/parallelism/sequential
# pytest tests/parallelism/sequential/test_serial_1.py

import logging
from playwright.sync_api import Page, expect

def test_serial_1(page):
    logging.info("Running test_serial_1")
    page.goto("https://playwright.dev/python/")
    expect(page.get_by_label("Switch between dark and light")).to_be_visible()