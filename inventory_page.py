class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.sort_dropdown = page.locator(".product_sort_container")
        self.item_names = page.locator(".inventory_item_name")
        self.add_to_cart_buttons = page.locator("button[class*='btn_inventory']")
        self.cart_icon = page.locator(".shopping_cart_link")

    def sort_by(self, value):
        self.sort_dropdown.select_option(value)

    def add_first_item_to_cart(self):
        self.add_to_cart_buttons.first.click()

    def go_to_cart(self):
        self.cart_icon.click()
