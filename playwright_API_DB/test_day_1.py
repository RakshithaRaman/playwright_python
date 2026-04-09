import time
from playwright.sync_api import Page, Playwright , expect


def test_launch_page(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.havesnacks.com/")
    expect(page).to_have_url("https://www.havesnacks.com/")
    expect(page).to_have_title("Have Snacks-Bite the Happiness")
    time.sleep(5)

def test_footer_link_check(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.havesnacks.com/")
    page.locator("a[href='/about-us']").click()
    time.sleep(5)

def test_links_footer_check(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.havesnacks.com/")

    types_of_food = page.locator("//div[@class='flex justify-center gap-4 flex-wrap']").all_text_contents()
    print(types_of_food)
    for item in types_of_food:
        print("-", item)


