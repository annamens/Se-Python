from selenium import webdriver


driver = webdriver.chrome

main_window = driver.current_window_handle
child_windows = driver.window_handles

window = driver.switch_to.window(child_windows[-1])