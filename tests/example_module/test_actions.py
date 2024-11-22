# pytest -s tests/example_module/test_actions.py::test_dialogs_with_handler

from playwright.sync_api import Page, expect
import time
# time.sleep(1)
 

def test_text_input(page):
    page.goto("http://127.0.0.1:5501/opleiding-playwright-python/tests/example_module/test.html")
    
    # TEXT INPUT
    page.get_by_role('textbox').nth(0).fill('Hello World')
    
    # DATE INPUT
    page.get_by_label('date').nth(0).fill('2020-02-02')
    
    # TIME INPUT
    page.get_by_label('time').nth(0).fill('13:15')
    
    # DATETIME INPUT
    page.get_by_label('datetime').fill('2020-02-02T13:15')
        
def test_checkboxes(page):
    page.goto("http://127.0.0.1:5501/opleiding-playwright-python/tests/example_module/test.html")
    
    # Check the checkbox
    page.get_by_label('Checkbox One').check()
    
    # Uncheck the checkbox
    page.get_by_label('Checkbox One').set_checked(False)

    # Assert the checkbox is not checked
    expect(page.get_by_label('Checkbox One')).not_to_be_checked()

    # Check the checkbox
    page.get_by_label('Checkbox One').set_checked(True)

    # Assert the checkbox is checked
    expect(page.get_by_label('Checkbox One')).to_be_checked()
    
    # Select the radio button
    page.get_by_label('Radio').check()
    
def test_clicks(page):
    page.goto("http://127.0.0.1:5501/opleiding-playwright-python/tests/example_module/test.html")
    
    # Generic click
    page.get_by_title("Subscribe").click()

    # Double click
    page.get_by_title("Subscribe").dblclick()

    # Right click
    page.get_by_title("Subscribe").click(button="right")

    # Shift + click
    page.get_by_title("Subscribe").click(modifiers=["Shift"])

    # Hover over element
    page.get_by_title("Subscribe").hover()

    # Click the top left corner
    page.get_by_title("Subscribe").click(position={ "x": 0, "y": 0})
    
def test_dialogs_auto_dismissed(page):
    page.goto("https://letcode.in/alert")
    page.get_by_role("button", name="Simple Alert").click()
    # Dialog is showing here, next click is not possible if dialog is not dismissed
    page.get_by_role("button", name="Confirm Alert").click()
       
def test_dialogs_with_handler(page):
    page.goto("https://letcode.in")
    page.get_by_role("link", name="Work-Space").click()
    page.get_by_role("link", name="Dialog").click()
    
    page.get_by_role("button", name="Simple Alert").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Confirm Alert").click()
   



