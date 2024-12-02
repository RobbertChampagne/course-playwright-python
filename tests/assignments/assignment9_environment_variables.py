# pytest tests/assignments/assignment9_environment_variables.py
from playwright.sync_api import Page, expect
import os
from dotenv import load_dotenv

# Assignment 9 (Environment variables)

# Load environment variables from .env file
load_dotenv()

url = ...
selector = ...
text = ...

def test_env_assignment(page):
    ...