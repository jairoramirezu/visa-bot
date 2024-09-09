from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utils.set_new_values import get_appointment_first, get_hour_first, get_appointment_second, get_hour_second
from utils.general_utils import clicks, enter, canSetValues, is_after_5_days
from utils.send_new_message import send_message
import asyncio
import time

# initialize the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)


async def main():
    while True:
        try:
            # open the visa appointments page
            driver.get("https://ais.usvisa-info.com/es-co/niv/users/sign_in")

            # get the form to login
            email_input = driver.find_element(By.ID, "user_email")
            password_input = driver.find_element(By.ID, "user_password")
            policy_input = driver.find_element(By.NAME, "policy_confirmed")
            login_button = driver.find_element(
                By.CSS_SELECTOR, ".button.primary")

            # fill the form
            email_input.send_keys(user_email)
            password_input.send_keys(user_password)
            clicks(driver, policy_input)
            clicks(driver, login_button)

            # go to select schedule button
            WebDriverWait(driver, 10).until(EC.url_contains("groups"))
            continue_button = driver.find_element(
                By.CSS_SELECTOR, ".button.primary.small")
            clicks(driver, continue_button)

            # set want to schedule
            WebDriverWait(driver, 10).until(EC.url_contains("schedule"))
            reprogram_button = driver.find_element(
                By.XPATH, '//ul/li[@class="accordion-item"][4]//div[@class="medium-10 columns"]//a[@class="button small primary small-only-expanded"]')
            clicks(driver, reprogram_button)

            # Elements of the primary appoiment
            new_date = driver.find_element(
                By.ID, "appointments_consulate_appointment_date")
            new_time = driver.find_element(
                By.ID, "appointments_consulate_appointment_time")

            # set the PRINCIPAL date
            dates = await get_appointment_first(driver)
            months = user_months.split(',')
            matching_dates = [date for date in dates if any(
                date.startswith(f"{user_year}-{month}") for month in months)]
            valid_dates = [
                date for date in matching_dates if is_after_5_days(date)]
            if valid_dates:
                canSetValues(driver, new_date)
                thew_new_date = valid_dates[0]
                new_date.send_keys(thew_new_date)
                enter(driver, new_date)
                await send_message(f'Fecha valida: {user_email} - {thew_new_date}')
            else:
                print("")
                print('Fecha indeseada')
                continue

            # set the PRINCIPAL time
            times = await get_hour_first(driver)
            if times:
                the_new_time = times[0]
                select = Select(new_time)
                select.select_by_value(the_new_time)
                enter(driver, new_time)
            else:
                continue

            # Elements of the CAS appoiment
            new_date_as = driver.find_element(
                By.ID, "appointments_asc_appointment_date")
            new_time_as = driver.find_element(
                By.ID, "appointments_asc_appointment_time")

            # set the CAS date
            dates_as = await get_appointment_second(driver, thew_new_date, the_new_time)
            if dates_as:
                canSetValues(driver, new_date_as)
                thew_new_date_as = dates_as[-1]
                new_date_as.send_keys(thew_new_date_as)
                enter(driver, new_date_as)
            else:
                continue

            # set the CAS hour
            times_as = await get_hour_second(driver, thew_new_date, the_new_time)
            if times_as:
                the_new_time_as = times_as[0]
                select = Select(new_time_as)
                select.select_by_value(the_new_time_as)
                enter(driver, new_time_as)
            else:
                continue

            # Element to submit
            submit_appoiment = driver.find_element(
                By.ID, "appointments_submit")
            clicks(driver, submit_appoiment)

            # Element to confirm
            confirm_button = driver.find_element(
                By.CSS_SELECTOR, ".button.alert")
            clicks(driver, confirm_button)
            WebDriverWait(driver, 10)

            # Send message to telegram with email
            await send_message(f'Cita registrada: {user_email}')

            # Final all the operation
            driver.quit()
            break

        except Exception as e:
            print("")
            print(
                f"Ocurrio un error: {e} \nIntentando de nuevo en 4 minutos...")
            print("")
            time.sleep(240)

# Run the asynchronous main function
user_email = input('Email: ')
user_password = input('Contrasena: ')
user_year = input('Ano: ')
user_months = input('Mes: ')
print("")
print("¡Suerte en tu busqueda Manolo!")
print("")
asyncio.run(main())
