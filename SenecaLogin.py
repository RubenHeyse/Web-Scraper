from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManage

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://app.senecalearning.com/login')
time.sleep(1)

browser.find_element_by_xpath('//*[@id="root"]/div[1]/div[3]/div/div/div/div/form/div[1]/input').send_keys('13rheyse@mgs.kent.sch.uk')
browser.find_element_by_xpath('//*[@id="root"]/div[1]/div[3]/div/div/div/div/form/div[2]/div/input').send_keys('Xm94?@8Saq6#(')
browser.find_element_by_xpath('//*[@id="root"]/div[1]/div[3]/div/div/div/div/form/button').click()
