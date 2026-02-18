import time

from playwright.sync_api import Playwright, expect

from Utils.apiBase import APIUtils



def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page =context.new_page()

    api_utils = APIUtils()
    order_ID = api_utils.createOrder(playwright)


    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    time.sleep(10)
    page.get_by_role("button", name="ORDERS").wait_for(state="visible", timeout=10000)
    page.get_by_role("button", name="ORDERS").click()
    time.sleep(10)
    row_data = page.locator("tr").filter(has_text=order_ID)
    row_data.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()



