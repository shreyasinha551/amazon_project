from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains, Keys
import time
driver= webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.amazon.com/")
welcome= driver.find_element(By.XPATH,"//span[text()='Hello, sign in']")
act= ActionChains(driver)
act.move_to_element(welcome).perform()
sign= driver.find_element(By.XPATH,"(//span[text()='Sign in'])[1]").click()
driver.back()
search= driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
search.send_keys("lakme kajal")
find= driver.find_element(By.XPATH,"(//div[text()='lakme kajal'])[1]").click()
featured= driver.find_element(By.XPATH,"//span[text()='Featured']").click()
time.sleep(3)
customer_revi= driver.find_element(By.XPATH,"(//a[text()='Avg. Customer Review'])[1]").click()
time.sleep(3)
driver.execute_script("window.scrollTo(0,500)")
time.sleep(3)
driver.find_element(By.XPATH,"//span[text()='Maybelline Unstoppable Eyeliner - Pewter - 2 Pack']").click()
time.sleep(3)

