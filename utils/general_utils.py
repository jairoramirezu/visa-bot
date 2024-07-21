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
