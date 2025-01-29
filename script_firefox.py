from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

import itertools
import pandas as pd


driver = webdriver.Firefox(executable_path='geckodriver-v0.33.0-win64/geckodriver.exe')

print("Firefox opened successfully!")

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")
print("Accessing WhatsApp Web")

df = pd.read_excel("contacts281224.xlsx", engine='openpyxl')


Number = df["Number"].tolist()
Name = df['Name'].tolist()
Variable = df['Something variable'].tolist()

print("excel read successfully!")

# print(Number, Name, Variable)

# Adjusting the script with updated XPaths and additional checks for element readiness
for i, j, k in zip(Number, Name, Variable):
    try:
        # Wait for the search box to be clickable and then click it
        xpath_search = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]'
        Search = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, xpath_search)))
        driver.execute_script("arguments[0].scrollIntoView();", Search)
        Search.click()
        time.sleep(2)
        for char in str(i):
            Search.send_keys(char)
            time.sleep(0.1)  # Adjust the sleep time as necessary
        # Search.send_keys("94576219")
        time.sleep(1)
        Search.send_keys(Keys.ENTER)
        time.sleep(3)

        # Wait for the message box to be clickable and then click it
        xpath_message = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]'
        Message = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, xpath_message)))
        driver.execute_script("arguments[0].scrollIntoView();", Message)
        time.sleep(2)

        # Send 'Hello ' + j + ',' with a delay between each keystroke
        greeting = 'Hello ' + str(j) + ','
        for char in greeting:
            Message.send_keys(char)
            time.sleep(0.05)

        time.sleep(1)
        Message.send_keys(Keys.SHIFT, Keys.ENTER)

        # Send the value of 'k' with a delay between each keystroke
        for char in str(k):
            Message.send_keys(char)
            time.sleep(0.1)

        # List of emoji shortcuts
        emoji_shortcuts = [':snake', ':tada', ':clinking', ':heart']

        # Iterate through each emoji shortcut in the list
        for emoji in emoji_shortcuts:
            # Send each character of the emoji shortcut with a delay
            for char in emoji:
                Message.send_keys(char)
                time.sleep(0.1)  # Adjust the sleep time as necessary

            # Confirm the selection of the emoji
            Message.send_keys(Keys.ENTER)
            time.sleep(0.1)  # Short pause after confirming the emoji selection


        time.sleep(1)
        Message.send_keys(Keys.ENTER)
        time.sleep(2)
        print('Sent to ' + str(j))

    except Exception as e:
        print(f"An error occurred: {e}")



driver.quit()


