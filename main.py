from time import sleep
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from art import tprint

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument("--auto-open-devtools-for-tabs")
# options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)


def main():
    log_into_hilbib()

    # _go_to_loan_overview()

    # _reborrow_materials()

    tprint("#automatethefuckoutofeverything")


def log_into_hilbib() -> None:
    # Go to hilbib.dk
    driver.get("https://hilbib.dk/")

    # Handle cookie pop up
    handle_cookie_popup()

    sleep(100)

    # _click_login_menu_btn()

    # _click_login_btn()

    # _login_by_form()


def handle_cookie_popup():
    sleep(2)
    click_btn(By.CLASS_NAME, "coi-banner__accept")


def _click_login_menu_btn() -> None:
    sleep(1)
    click_btn(By.CLASS_NAME, "header__menu-profile")


def _click_login_btn():
    sleep(1)
    click_btn(By.CLASS_NAME, "btn-primary")


def _login_by_form():
    with open("./credentials.txt", "r") as f:
        creds = f.read().split(" ")

    _fill_form_input("userid-input", creds[0])
    _fill_form_input("pin-input", creds[1])

    click_btn(By.ID, "borchk-submit")


def _fill_form_input(id: str, text: str) -> None:
    form_field = driver.find_element(By.ID, id)
    form_field.click()
    form_field.clear()
    form_field.send_keys(text)


def click_btn(by: str, value: str) -> None:
    btn = driver.find_element(by, value)
    btn.click()


def _go_to_loan_overview() -> None:
    _click_lender_status_btn()
    _click_loan_btn()


def _click_lender_status_btn() -> None:
    sleep(1)
    btn = driver.find_element(By.CLASS_NAME, "topbar-link-user-account")
    btn.click()


def _click_loan_btn() -> None:
    sleep(1)

    # Find ul's
    uls = driver.find_element(By.CLASS_NAME, "list-links")

    # Find li's
    lis = uls.find_elements(By.TAG_NAME, "li")

    # Click loan btn
    lis[1].click()


def _reborrow_materials() -> None:
    select_all_div = driver.find_element(By.CLASS_NAME, "select-all")

    material_return_date = _get_return_date(select_all_div)
    today = datetime.today()
    delta = material_return_date - today

    if delta.days < 7:
        _renew_materials()


def _get_return_date(div) -> datetime:
    div_class_attr = div.get_attribute("class")
    extracted_return_date = div_class_attr.split(" ")[-1]
    return_date = datetime.strptime(extracted_return_date, "%Y-%m-%d")
    return return_date


def _renew_materials():
    renew_all_btn = driver.find_element(By.LINK_TEXT, "Forny alle")
    renew_all_btn.click()


if __name__ == "__main__":
    main()
