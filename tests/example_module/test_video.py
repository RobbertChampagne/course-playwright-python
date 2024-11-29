# pytest tests/example_module/test_video.py
from playwright.sync_api import Page, expect
import logging
import os
import shutil
from core.loggingSetup import setup_logging

# ? Video logic inside the test file not in conftest.py because the implementation is to complex.
# ? Recording always will slow down the test execution.
# ? Use trace viewer to debug the test cases.

setup_logging()
logger = logging.getLogger("Video example")

def test_video(page):
    video_path = None
    context = None
    test_failed = False
    try:
        browser = page.context.browser
        context = browser.new_context(record_video_dir="videos/")
        page = context.new_page()
        page.goto("https://playwright.dev/python/")
        page.get_by_role("link", name="Get started").click()
        page.get_by_role("link", name="What's next", exact=True).click()
        page.get_by_role("link", name="See a trace of your tests").click()
        page.get_by_label("Home page").click()
            
        # Pass:
        #expect(page.get_by_label("Switch between dark and light")).to_be_visible()

        # Fail:
        expect(page.get_by_label("Switch between dark and light123")).to_be_visible()
    except Exception as e:
        logger.info(f"Test failed: {e}")
        #  Sets the test_failed flag to True if the test fails.
        test_failed = True
        raise
    finally:
        if context:
            context.close()
            # Retrieve the video path after closing the context
            try:
                if page and page.video:
                    # Retrieves the path of the recorded video.
                    video_path = page.video.path()
                    logger.info(f"Video saved at: {video_path}")
                    # Rename the video file
                    new_video_path = os.path.join(os.path.dirname(video_path), "test_video_fail.webm")
                    # Renames the video file to the new path.
                    shutil.move(video_path, new_video_path)
                    video_path = new_video_path
                    logger.info(f"Video renamed to: {new_video_path}")
            except AttributeError:
                logger.info("No video recorded.")
            
            # - Checks if the test failed.
            # - The video_path check ensures that the video_path variable is not None.
            # - The os.path.exists(video_path) check ensures that the file actually exists on the filesystem.
            if not test_failed and video_path and os.path.exists(video_path):
                #  Removes the video file if the test passed.
                os.remove(video_path)
                logger.info(f"Video removed: {video_path}")
            




    