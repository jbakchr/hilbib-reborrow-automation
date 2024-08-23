from time import sleep
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument("--headless=new") # Uncomment this for headless mode
options.add_argument("--disable-search-engine-choice-screen")

driver = webdriver.Chrome(options=options)


def main(date_today) -> None:
    log_into_hilbib()

    renew_material()

    update_last_run_date(date_today)


def log_into_hilbib() -> None:
    # Go to hilbib.dk
    driver.get("https://hilbib.dk/")

    # Handle cookie pop up
    handle_cookie_popup()

    # Click login btn
    click_main_page_login_btn()

    # Click login button on side bar
    click_side_bar_login_btn()

    # Fill out login form and login
    login_by_form()


def handle_cookie_popup() -> None:
    sleep(2)
    click_btn(By.CLASS_NAME, "coi-banner__accept")


def click_main_page_login_btn() -> None:
    sleep(1)
    click_btn(By.CLASS_NAME, "btn-ui")


def click_side_bar_login_btn() -> None:
    sleep(1)
    click_btn(By.CLASS_NAME, "btn-primary")


def login_by_form() -> None:
    sleep(1)

    with open("./credentials.txt") as f:
        creds = f.read().split(" ")

    fill_form_input("userid-input", creds[0])
    fill_form_input("pin-input", creds[1])

    click_btn(By.ID, "borchk-submit")


def fill_form_input(id: str, text: str) -> None:
    form_field = driver.find_element(By.ID, id)
    form_field.click()
    form_field.clear()
    form_field.send_keys(text)


def click_btn(by: str, value: str) -> None:
    btn = driver.find_element(by, value)
    btn.click()


def update_last_run_date(date_today) -> None:
    with open("./last_run.txt", "w") as f:
        f.write(date_today)


def renew_material() -> None:

    click_all_loans_element()

    click_group_loans_element()

    click_renewable_loans_element()

    click_renew_btn()


def click_all_loans_element() -> None:
    sleep(1)

    all_loans = driver.find_element(
        By.CSS_SELECTOR,
        "#main-content > div > div > div > div > div.status-userprofile > div:nth-child(1) > div.mt-8 > a",
    )
    all_loans.click()


def click_group_loans_element():
    sleep(1)

    group_loans_btn = driver.find_element(
        By.CSS_SELECTOR,
        "#main-content > div > div > div > div > div:nth-child(2) > div > div:nth-child(3) > button",
    )
    group_loans_btn.click()


def click_renewable_loans_element():
    sleep(2)

    renewable_loans = driver.find_element(
        By.CSS_SELECTOR,
        "#main-content > div > div > div > div > div.list-reservation-container.my-32 > ul:nth-child(2) > div",
    )
    renewable_loans.click()


def click_renew_btn():
    sleep(1)

    renew_btn = driver.find_element(By.CSS_SELECTOR, "#renew-several")
    renew_btn.click()


if __name__ == "__main__":
    today = str(datetime.now().date())

    with open("./last_run.txt") as f:
        last_run_date = f.read()

    if today != last_run_date:
        main(today)
