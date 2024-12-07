# pytest -s tests/assignments/assignment12/assignment12.py --headed
import json
import pytest
from playwright.sync_api import Page, expect
from pathlib import Path
from dotenv import load_dotenv
import os

# Assignment 12

# Load environment variables from .env file
load_dotenv()

# Import the URL from the environment variables.
...

# Construct the absolute path to the todos.json file
data_file_path = Path(__file__).parent / "todos.json"

# Load the data from the todos.json file
data = json.load(open(data_file_path))['todos'] # [{'title': 'Buy groceries'}, {'title': 'Clean the house'}, ...]

def test_assignment12(page):
    # Navigate to the URL.
    ...
   
    # Loop through the todos and add them to the list.
    for item in data: # item['title']
        ...
        
    # Change the todo "Do laundry" into "Do laundry and iron".
    ...
    
    # Verify that the todo "Do laundry and iron" is present.
    ...
