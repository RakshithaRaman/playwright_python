import time

from playwright.sync_api import Page, Playwright, expect


#
# def test_playwright_basics(playwright):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://rahulshettyacademy.com")


# default chromium headless mode 1 single context with no memories saved
def test_pw_shortcut(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learningiiiii")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password")).to_be_visible()
    time.sleep(5)

def test_firefox_browser(playwright:Playwright):
    firefox = playwright.firefox.launch(headless=False)
    page = firefox.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learningiiiii")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password")).to_be_visible()
    time.sleep(5)



def test_handling_child_window(playwright:Playwright):
    chrome = playwright.chromium.launch(headless=False)
    page =chrome.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as new_child_page:
        page.locator(".blinkingText").click()
        child_page = new_child_page.value
        text = child_page.locator(".red").text_content()
        words = text.split("at")
        new_email = words[1].strip().split(" ")[0]
        print(new_email)
        time.sleep(5)
        assert new_email == "mentor@rahulshettyacademy.com"

