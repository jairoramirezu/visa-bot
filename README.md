
# Visa Appointment Bot

This repository contains a Python-based bot that automates the process of checking and registering visa appointment slots on a specified web page. The bot navigates through a web page in Google Chrome, continuously monitors for available appointment slots, and registers them when found.

## Overview

The Visa Appointment Bot is designed to interact with web pages using Google Chrome to automate the process of checking and booking visa appointment slots. It can be customized to work with different web pages where visa appointments are managed. The bot is built using Python and utilizes Selenium for browser automation.

## Libraries Used

- **seleniumwire**: Extends Selenium's capabilities by adding the ability to inspect requests made by the browser.
- **selenium.webdriver.common.by**: Used to locate elements on a web page.
- **selenium.webdriver.common.keys**: Provides access to keyboard keys for interaction.
- **selenium.webdriver.support.ui.WebDriverWait**: Waits for conditions to be met before proceeding.
- **selenium.webdriver.support.expected_conditions**: Contains common conditions used with WebDriverWait.
- **selenium.webdriver.support.ui.Select**: Used for interacting with dropdown menus.
- **asyncio**: Handles asynchronous operations in Python.
- **time**: Provides time-related functions.

Custom utility functions located in the `utils` directory:

- **set_new_values**:
  - `get_appointment_first`, `get_hour_first`: Functions to retrieve the first available appointment and time.
  - `get_appointment_second`, `get_hour_second`: Functions to retrieve the second available appointment and time.

- **general_utils**:
  - `clicks`, `enter`, `canSetValues`, `is_after_5_days`: Utility functions for interacting with the page and checking conditions.

- **send_new_message**: Sends a notification or message when a new appointment is found.

## Functionality

- **Web Navigation**: The bot automatically opens Chrome and navigates to the specified web page.
- **Appointment Checking**: The bot continuously checks for available visa appointments.
- **Appointment Booking**: When a slot is found, the bot registers it automatically.
- **Notifications**: The bot can send messages or notifications when it successfully books an appointment.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
