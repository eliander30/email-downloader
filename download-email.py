from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://njzr-jypy.accessdomain.com/webmail/")
elem = driver.find_element(By.NAME, "email")
elem2 = driver.find_element(By.NAME, "password")
elem.clear()
elem.send_keys("david@daviddrebin.com")
elem2.send_keys("Asdonair@#2")
elem2.send_keys(Keys.RETURN)
time.sleep(15)



while True:
    list_mails = driver.find_elements(By.CSS_SELECTOR, '.mail_row.read.ui-draggable')
    for element in list_mails:
        time.sleep(3)
        hola = "messageListCompact"
        element.click()
        time.sleep(5)
        try:
            more = driver.find_element(By.ID, "nodeReplyAnchor")
            more.click()
            time.sleep(2)
            download = driver.find_element(By.ID, "download")
            download.click()
        except:
            pass

    next = driver.find_element(By.CSS_SELECTOR, '.active-next.pagingIcon.pagingIconRight')
    next.click()
    list_mails.clear()
    time.sleep(20)
    driver.refresh()
    time.sleep(15)
    
assert "No results found." not in driver.page_source
driver.close()