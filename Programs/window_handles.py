from selenium import webdriver


driver = webdriver.chrome

main_window = driver.current_window_handle
child_windows = driver.window_handles

for window in child_windows:
    if window != main_window:
        driver.switch_to_window(window)
        break
