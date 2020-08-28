from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time

driver = webdriver.Chrome('C:/Users/min/Desktop/auto/chromedriver.exe')
url = 'https://www.rockgarden.kr:8444/'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)

#login 클릭
driver.find_element_by_xpath('//*[@id="gnb_wrap"]/div[1]/a[1]').click()

#login id/pw입력
driver.find_element_by_css_selector('#userid').send_keys('rlaalspk')
driver.find_element_by_name('userpw').send_keys('08423346Aa!')

#login 버튼클릭
driver.find_element_by_css_selector('.type-buttom').click()
time.sleep(0.5)
pyautogui.hotkey('enter')



#예약신청(파란버튼)
time.sleep(0.2)
driver.find_element_by_css_selector('.button').click()

time.sleep(0.2)
#날짜에맞는 깃발클릭(토요일)
pyautogui.click(x=954, y=869)

time.sleep(0.2)
#7:30
pyautogui.click(x=1399, y=1017)
pyautogui.hotkey('enter')
#7:22

#7:00

# time.sleep(0.2)
# #인원수 콤보박스
# driver.find_element_by_xpath('//*[@id="dvConfirm"]/div/fieldset/dl[2]/dd/select').click()
# pyautogui.hotkey('down')
# pyautogui.hotkey('down')
# pyautogui.hotkey('enter')