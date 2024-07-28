from time import sleep
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument("--auto-open-devtools-for-tabs")
# options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)


def main(last_run_date) -> None:
    log_into_hilbib()

    update_last_run_date(last_run_date)


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


def update_last_run_date(last_run_date):
    print("Inside last run")
    with open("./last_run.txt", "w") as f:
        f.write(last_run_date)


if __name__ == "__main__":
    today = datetime.now().date()

    with open("./last_run.txt") as f:
        last_run_date = f.read()

    if today != last_run_date:
        main(last_run_date)
