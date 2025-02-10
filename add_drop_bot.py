from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time


from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager

options = Options()
options.add_experimental_option("detach", True)

# Automatically downloads and uses the correct Edge WebDriver
service = Service(EdgeChromiumDriverManager().install())

driver = webdriver.Edge(service=service, options=options)
driver.get("https://kepler-beta.itu.edu.tr")

CRNS = ["11111", "22222"] #Almak istediğiniz CRN'leri yazın.

mail = "babapro@itu.edu.tr"
password = "babapro"

# service_object = Service(r"C:\Users\yagiz\Desktop\ITU_ADD_DROP_BOTU-main\msedgedriver.exe")
# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Edge(service=service_object, options=options)

# driver.get("https://kepler-beta.itu.edu.tr")
# time.sleep(1)
driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$tbUserName").send_keys(mail)
driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$tbPassword").send_keys(password)

login_btn = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$btnLogin").click()
time.sleep(2)

#driver.find_element(By.CLASS_NAME, "stretched-link").click() ##eğer yatay geçiş yapmadıysanız bu satırı silin.

time.sleep(1)

driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[1]/div[2]/div[1]/ul/li[5]/a").click()
driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[1]/div[2]/div[4]/ul/li/div/ul/li[2]/a").click()

time.sleep(5)
counter = 1

while True:

    for i, crn in enumerate(CRNS):
        driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[2]/div/div/div[4]/div/form/div[1]/div/div[{}]/div/input'.format(i+1)).send_keys(crn)


    print("Attempt: {}".format(counter))

    driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[2]/div/div/div[4]/div/form/button[2]').click()
    driver.find_element(By.XPATH, "//*[@id='modals-container']/div/div[2]/div/div[3]/button[2]").click()
    counter += 1
    time.sleep(5)




