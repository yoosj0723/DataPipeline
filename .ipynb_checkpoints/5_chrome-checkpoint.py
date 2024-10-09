from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# WebDriver 설정
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Daum 웹페이지 열기
url = 'https://www.daum.net/'
driver.get(url)

# 5초간 대기 후 브라우저 종료
time.sleep(5)
driver.quit()
