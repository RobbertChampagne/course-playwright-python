# pytest tests/examples_that_need_a_conftest/tests/test_example.py

from playwright.sync_api import Page, expect
import logging
import os
from core.utils import save_trace
import pytest

# Setup logging configuration
logger = logging.getLogger("Standalone test scripts")

def test_example(page_context):
    try:
        # Log the start of the test
        logger.info("Starting test")
        
        # Unpack the page and context from the fixture
        page, context = page_context
        
        page.goto("https://playwright.dev/")
        page.get_by_role("button", name="Node.js").click()
        page.get_by_label("Main", exact=True).get_by_role("link", name="Python").click()
        expect(page.get_by_label("Main", exact=True)).to_contain_text("Python")
        
    finally:
        # Stop tracing and save it to a file
        trace_name = 'example.zip'
        trace_dir_name = 'standalone_test_scripts'
        save_trace(context, trace_dir_name, trace_name)
        
        # Log the location of the trace file
        logger.info(f"Open trace: playwright show-trace traces/{trace_dir_name}/{trace_name}")
        
        
