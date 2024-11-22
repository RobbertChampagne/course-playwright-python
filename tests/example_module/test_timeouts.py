# pytest -s tests/example_module/test_timeouts.py::test_timeouts

from playwright.sync_api import Page, expect
import time

 
def test_timeouts(page):
    time.sleep(35)
    