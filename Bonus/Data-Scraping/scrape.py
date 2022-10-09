from selenium import webdriver
from selenium.webdriver.common.by import By

DRIVER_PATH = './chromedriver_win32/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
# driver.get('https://google.com')

url = 'https://www.practo.com/noida/doctor/dentalsquarenoida-gmail-com-dentist?practice_id=918714&specialization=Implantologist&referrer=doctor_listing'
driver.get(url)
feedbacks = driver.find_elements(By.CSS_SELECTOR, "[data-qa-id='feedback_item'")

print(feedbacks[0].text)