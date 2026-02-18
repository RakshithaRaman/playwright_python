from playwright.sync_api import Page, Playwright

orders_payload = {"orders": [{"country": "India", "productOrderedId": "68a961959320a140fe1ca57e"}]}

class APIUtils:

    def get_token(self, playwright: Playwright, user_credentials):
        user_email = user_credentials['userEmail']
        user_Password = user_credentials['userPassword']
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                            data={"userEmail": user_email, "userPassword": user_Password})

        assert response.ok
        print(response.json())
        response_body = response.json()
        return response_body["token"]

    def createOrder(self,playwright:Playwright,user_credentials):
        token = self.get_token(playwright,user_credentials)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data=orders_payload,
                                 headers={"Authorization":token,
                                          "Content-Type":"application/json",
                                          })
        print(response.json())

        response_body = response.json()
        order_Id = response_body["orders"][0]
        return  order_Id