import time

from playwright.sync_api import Page, Playwright, expect

def test_chrome_browser(playwright:Playwright):
    chrome = playwright.chromium.launch(headless=False)
    page =chrome.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    time.sleep(5)
    Iphone_product = page.locator("app-card").filter(has_text="iphone X")
    Iphone_product.get_by_role("button").click()
    Nokia_product = page.locator("app-card").filter(has_text="Nokia Edge")
    Nokia_product.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    time.sleep(5)