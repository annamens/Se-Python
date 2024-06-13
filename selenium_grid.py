from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

# To run in selenium grid
#1. download selenium grid jar file and open it with the command java -jar selenium-server-4.18.1.jar standalone
# now open the URL in the browser where we can see the UI
# run the below code to execute the grid
# from selenium 4 options were introduced
GRID_URL = "http://192.168.137.1:4444/wd/hub"

chrome_options = Options()
driver = webdriver.Remote(
    command_executor=GRID_URL,
    options=chrome_options
)
driver.get("http://www.google.com")
print(driver.title)
driver.quit()
