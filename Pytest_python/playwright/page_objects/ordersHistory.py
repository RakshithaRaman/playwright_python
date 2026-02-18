from .orderDetails import OrderDetailsPage


class OrdersHistoryPage:

    def __init__(self, page):
        self.page = page

    def selectOrder(self,order_ID):
        row_data = self.page.locator("tr").filter(has_text=order_ID)
        row_data.get_by_role("button", name="View").click()
        orderDetailsPage = OrderDetailsPage(self.page)
        return orderDetailsPage


