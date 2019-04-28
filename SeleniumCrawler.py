from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui as pag
import sys
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://automatetheboringstuff.com')
browser.maximize_window()
elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > h1')
print('text saved to text.txt')

with open('text.txt', 'a') as out:
    out.write(elem.text)
    
pag.hotkey('ctrl', 'n')
pag.click(180, 50, button='left')
pag.typewrite('bbc\n', interval=0.1)
time.sleep(1)
pag.click(180, 450, button='left')
