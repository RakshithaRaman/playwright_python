import time
from os import name

from playwright.sync_api import Page, Playwright, expect


## hide/display placeholder
def test_chrome_browser(playwright:Playwright):
    chrome = playwright.chromium.launch(headless=False)
    page =chrome.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()


# Alerts handling
    page.on("dialog", lambda dialog : dialog.accept())
    page.get_by_role("button",name="Confirm").click()
    time.sleep(5)

#frame handling

    frame_page = page.frame_locator("#courses-iframe")
    frame_page.get_by_role("link",name="All Access plan").click()
    expect(frame_page.locator("body")).to_contain_text("Happy Subscibers!")


#table handling
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            priceColValue=index
            print(f"the coulumn value is {priceColValue}")
            break

    rice_row = page.locator("tr").filter(has_text="Rice")
    expect(rice_row.locator("td").nth(priceColValue)).to_have_text("37")
    print(rice_row.locator("td").nth(priceColValue).inner_text())


##Mouse Hover
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    page.get_by_role("Link",name="Top").click()