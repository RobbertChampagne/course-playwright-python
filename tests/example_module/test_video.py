# pytest tests/example_module/test_video.py
from playwright.sync_api import Page, expect
import logging
import os
import shutil

# ? Video logic inside the test file not in conftest.py because the implementation is to complex.
# ? Recording always will slow down the test execution.
# ? Use trace viewer to debug the test cases.

# Setup logging configuration
logger = logging.getLogger("Examples that need a conftest")

def test_video(page: Page):
    video_path = None
    context = None
    test_failed = False
    try:
        # Use the existing browser instance from the page fixture
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
        logger.error(f"Test failed: {e}")
        test_failed = True
        raise
    finally:
        if context:
            context.close()
            # Retrieve the video path after closing the context
            try:
                if page and page.video:
                    video_path = page.video.path()
                    logger.info(f"Video saved at: {video_path}")
                    # Rename the video file
                    new_video_path = os.path.join(os.path.dirname(video_path), "test_video_fail.webm")
                    shutil.move(video_path, new_video_path)
                    video_path = new_video_path
                    logger.info(f"Video renamed to: {new_video_path}")
            except AttributeError:
                logger.warning("No video recorded.")
            
            # Clean up video if the test passes
            if not test_failed and video_path and os.path.exists(video_path):
                os.remove(video_path)
                logger.info(f"Video removed: {video_path}")
            




    