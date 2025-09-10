from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.python.org/")

print(driver.title)

search_field = driver.find_element(By.ID, "id-search-field")
search_field.click()
search_field.send_keys("itertools")

search_button = driver.find_element(By.ID, "submit")
search_button.click()

result = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".list-recent-events"))
)
items = driver.find_elements(By.CSS_SELECTOR, ".list-recent-events li")
print(items[0].text)
