# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains



# feedbacks = driver.find_elements(By.CSS_SELECTOR, "[data-qa-id='feedback_item'")
# # details = driver.find_elements(By.LINK_TEXT, 'Dr. Dhruv Anand')

# print(feedbacks[0].text)

# %%
DRIVER_PATH = './chromedriver_linux64 (1)/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
# driver.get('https://google.com')

url = 'https://www.practo.com/bangalore/ophthalmologist'
# driver.get(url)

# # %%
# driver.execute_script("window.scrollTo(0, 2000);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(0, 4000);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(0, 6000);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(0, 8000);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(0, 10000);")
# time.sleep(2)


# # %%
# name = driver.find_elements(By.CSS_SELECTOR, "[data-qa-id='View Profile_button'")
# len(name)

# # %%
# name = driver.find_elements(By.CSS_SELECTOR, "[data-qa-id='View Profile_button'")
# a = ActionChains(driver)
# m = driver.find_elements(By.CSS_SELECTOR, "[data-qa-id='doctor_card'")


# # %%
# doctorname = []
# doctorQualifications = []
# doctorSpecialization = []
# doctorSummary = []
# doctorClinicAddress = []
# doctorTimingDays = []
# doctorTimingSession = []
# doctorReviewScore = []
# doctorConsulationFee = []
# currentURL = []

# # %%




# for i in range(len(name)):

#     try:
#         a.move_to_element(m[i]).perform()
#         page = name[i].click()
#         time.sleep(1)
#         window_before = driver.window_handles[0]
#         window_after = driver.window_handles[1]
#         window_after
#         driver.switch_to.window(window_after)
        
#         doctor_name = driver.find_elements(By.CSS_SELECTOR, "[data-qa-id='doctor-name'")
#         doctor_name[0].text
#         doctorname.append(doctor_name[0].text)
#         doctor_qualifications = driver.find_elements(By.CSS_SELECTOR, "[data-qa-id='doctor-qualifications'")
#         doctor_qualifications[0].text
#         doctorQualifications.append(doctor_qualifications[0].text)
#         doctor_specialization = driver.find_elements(By.CSS_SELECTOR, "[data-qa-id='doctor-specializations'")
#         doctor_specialization[0].text
#         doctorSpecialization.append(doctor_specialization[0].text)
#         # doctor_summary = driver.find_elements(By.CSS_SELECTOR, "[data-qa-id='doctor-summary'")
        
#         # # element = driver.find_element(By.CSS_SELECTOR, "[data-qa-id='summary-more")
#         # # element.click()
#         # doctor_summary[0].text
#         # doctorSummary.append(doctor_summary[0].text)
#         try:
#             doctor_clinic_address = driver.find_elements(By.CSS_SELECTOR, "[data-qa-id='clinic-address'")
#             doctor_clinic_address[0].text
#             doctorClinicAddress.append(doctor_clinic_address[0].text)
#         except:
#             doctorClinicAddress.append("")
#         try:
#             clinic_timings_days = driver.find_elements(By.CSS_SELECTOR, "[data-qa-id='clinic-timings-day'")
#             clinic_timings_days[0].text
#             doctorTimingDays.append(clinic_timings_days[0].text)
#         except:
#             doctorTimingDays.append("")
#         try:
#             clinic_timings_session = driver.find_elements(By.CSS_SELECTOR, "[data-qa-id='clinic-timings-session'")
#             clinic_timings_session[0].text
#             doctorTimingSession.append(clinic_timings_session[0].text)
#         except:
#             doctorTimingSession.append("")
#         try:
#             review_score = driver.find_elements(By.CSS_SELECTOR, "[data-qa-id='doctor-patient-experience-score'")
#             review_score[0].text
#             doctorReviewScore.append(review_score[0].text)
#         except:
#             doctorReviewScore.append("")
        
#         try:
#             consultation_fee = driver.find_elements(By.CSS_SELECTOR, "[data-qa-id='consultation_fee'")
#             consultation_fee[0].text
#             doctorConsulationFee.append(consultation_fee[0].text)
#         except:
#             doctorConsulationFee.append("")
#         currentURL.append(driver.current_url)
#         driver.close()
#         driver.switch_to.window(window_before)
#     except:
#         continue

#     # print(Exception)
#     # i+=1
        


# # %%
# print(len(doctorConsulationFee))

# # %%
# import pandas as pd

# dict = {'name': doctorname, 'qualification': doctorQualifications, 'specialization': doctorSpecialization, 'clinic_address': doctorClinicAddress, 'timing_days': doctorTimingDays, 'timing_session': doctorTimingSession, 'review_score': doctorReviewScore, 'consultation_fee': doctorConsulationFee, 'current_url': currentURL}

# df = pd.DataFrame(dict)
# df



# %%
from ast import literal_eval
import pandas as pd
import os
from tqdm import tqdm

DRIVER_PATH = './chromedriver_linux64 (1)/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)
for filename in os.listdir('../Data_final/'):
    if filename == 'with_coords':
        continue
    df = pd.read_csv(f"../Data_final/{filename}", converters={'feedbacks': literal_eval})
    addresses = []
    cnt = 0
    total = df.shape[0]
    for url in (df['current_url']):
        try:
            driver.get(url)
            coordinate = driver.find_elements(By.CSS_SELECTOR, "[data-qa-id='get-directions'")
            addresses.append(coordinate[0].get_attribute('href'))
        except:
            addresses.append("None")
        cnt += 1
        print(f'{cnt} out of {total} in {filename}')
    df['coords'] = addresses
    df.to_csv(f'../Data_final/with_coords/{filename}')
    print(df)

    

# %%
# import matplotlib.pyplot as plt
# import seaborn as sns
# plt.figure(figsize=(20, 10))
# dataplot = sns.heatmap(df.corr(), cmap="YlGnBu", annot=True)
  
# # displaying heatmap

# plt.show()

# # %%
# import pandas as pd

# df = pd.read_csv("./doctor_data/homoeopath.csv")
# df['specialization'].str.split('\n', expand=True)

# # %%



