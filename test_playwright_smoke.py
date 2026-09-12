from playwright.sync_api import expect
from login_page import LoginPage
from inventory_page import InventoryPage
from checkout_page import CheckoutPage

def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_login_with_wrong_password(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "wrong_password")

    expect(login_page.get_error_message()).to_be_visible()

# def test_intentional_fail(page):
#     page.goto("https://www.saucedemo.com")
#     expect(page.get_by_text("Текст якого точно нема")).to_be_visible()

# pipa


def test_sort_products_low_to_high(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.sort_by("lohi")

    prices = page.locator(".inventory_item_price").all_inner_texts()
    prices_float = [float(p.replace("$", "")) for p in prices]

    assert prices_float == sorted(prices_float)

def test_full_checkout_flow(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()

    checkout_page = CheckoutPage(page)
    checkout_page.start_checkout()
    checkout_page.fill_info("John", "Doe", "12345")
    checkout_page.finish_order()

    expect(checkout_page.complete_header).to_have_text("Thank you for your order!")