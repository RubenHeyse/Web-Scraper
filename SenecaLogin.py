#Log in to seneca; collect user data; write data to text file

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://app.senecalearning.com/login')
sleep(1)

browser.find_element_by_xpath('//*[@id="root"]/div[1]/div[3]/div/div/div/div/form/div[1]/input').send_keys('Your_Email')
browser.find_element_by_xpath('//*[@id="root"]/div[1]/div[3]/div/div/div/div/form/div[2]/div/input').send_keys('Your_Password')
browser.find_element_by_xpath('//*[@id="root"]/div[1]/div[3]/div/div/div/div/form/button').click()

sleep(10)
boxName = browser.find_elements_by_class_name('CourseStatsBox__labelText')
boxScore = browser.find_elements_by_class_name('CountUp')

fileName = 'Seneca_Stats.txt'
with open(fileName, 'w') as out:
    for x in range(0, 3):
        out.write(boxName[x].text + " " + boxScore[x].text + "\n")

print('Stats written to: ' + fileName)
