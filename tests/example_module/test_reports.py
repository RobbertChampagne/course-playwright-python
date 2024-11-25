# pytest tests/example_module/test_reports.py --html=report.html
# pytest tests/example_module/test_reports.py --json-report --json-report-file=report.json
# pytest tests/example_module/test_reports.py

import re
from playwright.sync_api import Page, expect

def test_locating_elements(page):
    page.goto("https://playwright.dev/")
    get_started_button = page.get_by_role("link", name="Get started")
    
    get_started_button.hover()
    get_started_button.click()
    