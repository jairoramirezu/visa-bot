from datetime import datetime, timedelta


def clicks(driver, element):
    driver.execute_script("arguments[0].click();", element)


def canSetValues(driver, element):
    driver.execute_script("arguments[0].removeAttribute('readonly')", element)


def enter(driver, element):
    driver.execute_script("""
    var event = new KeyboardEvent('keydown', {
        bubbles: true, cancelable: true, keyCode: 13
    });
    arguments[0].dispatchEvent(event);
    """, element)


def is_after_5_days(date_str):
    today = datetime.now().date()
    five_days_from_today = today + timedelta(days=5)
    date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    return date_obj > five_days_from_today
