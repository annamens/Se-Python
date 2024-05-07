from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Define desired capabilities for the browser and platform
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['platform'] = 'WINDOWS'  # Change this according to your setup

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')  # You might need to add more options based on your setup

# Connect to the Selenium Grid hub
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',  # Replace <grid_hub_ip> with your hub's IP
    options=chrome_options,
    desired_capabilities=capabilities
)

# Example test
driver.get('https://www.google.com')
print(driver.title)

# Close the browser
driver.quit()
