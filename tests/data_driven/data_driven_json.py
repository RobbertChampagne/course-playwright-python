# pytest tests/data_driven/data_driven_json.py
import json
import pytest
from playwright.sync_api import Page, expect
from pathlib import Path

# Construct the absolute path to the data.json file
data_file_path = Path(__file__).parent / "data.json"

@pytest.mark.parametrize("data", json.load(open(data_file_path)))
def test_data_driven_json(page, data):
    page.goto("https://playwright.dev/")
    element = page.locator("h1")
    expect(element).to_have_text(data)