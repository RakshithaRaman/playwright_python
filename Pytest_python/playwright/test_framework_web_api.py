import json

import pytest
from playwright.sync_api import Page, Playwright, expect

from conftest import browser_instance
from page_objects.login import LoginPage
from Utils.apiBase_Framework import APIUtils

#jsonfile-> util -> converts into python object -> access it
with open('data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']

@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(user_credentials, browser_instance, playwright: Playwright):
    userName = user_credentials['userEmail']
    password = user_credentials['userPassword']

    api_utils = APIUtils()
    order_ID = api_utils.createOrder(playwright, user_credentials)

    #login
    loginPage = LoginPage(browser_instance)
    # loginPage.navigate()
    dashboardPage = loginPage.login(userName, password)

    orderHistoryPage = dashboardPage.select_orders_nav_link()
    ordersDetailsPage =orderHistoryPage.selectOrder(order_ID)
    ordersDetailsPage.verifyOrderMessage()
