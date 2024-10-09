from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# WebDriver 설정
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# url 설정
JOB_URL = "https://www.linkedin.com/jobs/search/?currentJobId=3291207294&geoId=103588929&keywords=PYTHON&location=대한민국 서울&refresh=true"

driver.get(JOB_URL)

login = driver.find_element(By.CSS_SELECTOR, ".btn-secondary-emphasis")
login.click()

username = driver.find_element(By,ID, "username")
username.send_keys("")      # ID 입력

password = driver.find_element(By.ID, "password")
password.send_keys("")      # PS 입력

login_button = driver.find_element(By.CSS_SELECTOR, ".from__button--floating")
login_button.click()

driver.implicitly_wait(5) # NoSuchElementException 발생 시 사용

apply_button = driver.find_element()
apply_button.click(By.CSS_SELECTOR, "")