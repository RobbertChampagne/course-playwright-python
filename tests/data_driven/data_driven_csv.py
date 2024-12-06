# pytest tests/data_driven/data_driven_csv.py
import csv
import pytest
from playwright.sync_api import Page, expect
from pathlib import Path

# Construct the absolute path to the data.csv file
data_file_path = Path(__file__).parent / "data.csv"

def load_csv_data(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

@pytest.mark.parametrize("data", load_csv_data(data_file_path))
def test_data_driven_csv(page, data):
    page.goto("https://playwright.dev/")
    element = page.locator("h1")
    expect(element).to_have_text(data["text"])