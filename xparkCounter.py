from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
import time
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--email")
parser.add_argument("--password")

# 配置瀏覽器選項
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-application-cache')
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(chrome_options=chrome_options)

# Facebook 登錄
def facebook_login(driver, email, password):
    driver.find_elements(By.XPATH, "//input[@name='email']")[1].send_keys(email)
    driver.find_elements(By.XPATH, "//input[@name='pass']")[1].send_keys(password)
    driver.find_element(By.XPATH, "//div[@aria-label='Accessible login button']").click()

#scroll down this page to get more comment
def scroll_down(driver):

    for i in range(1000):
        
        # Scroll to the bottom
        ele = driver.find_element(By.CLASS_NAME, "xb57i2i.x1q594ok.x5lxg6s.x78zum5.xdt5ytf.x6ikm8r.x1ja2u2z.x1pq812k.x1rohswg.xfk6m8.x1yqm8si.xjx87ck.xx8ngbg.xwo3gff.x1n2onr6.x1oyok0e.x1odjw0f.x1iyjqo2.xy5w88m")
        
        driver.execute_script("arguments[0].scrollTop=arguments[0].scrollHeight", ele)
        time.sleep(2+(i/100)*3)

        if (i%100)==0: 
            print(i)
            get_now_result()

    get_now_result()
 

def get_now_result():
    choice = ["【🅐 胖貢貢】#Xpark #企名大師就是我", "【🅑 烏梅汁】#Xpark #企名大師就是我", "【🅒 Tomorin】#Xpark #企名大師就是我", "【🅓 燈】#Xpark #企名大師就是我", "【🅔 碧天伴走】#Xpark #企名大師就是我"]
    choice_list = [set(),set(),set(),set(),set()]

    authors = driver.find_elements(By.XPATH, f"//div[contains(@aria-label, 'Comment by')]")

    for i in range(len(authors)):
        votes = authors[i].find_elements(By.XPATH, ".//div[contains(text(),'【')]")
        author = authors[i].find_elements(By.XPATH, ".//span//span//span")
        if len(votes) != 0 and len(author)!=0:
            for j in range(5):
                    if choice[j] in votes[0].text:
                        choice_list[j].add(author[0].text)

    for i in range(5):
        print(choice[i] + " : " + str(len(choice_list[i])))
        

# 主程式
if __name__ == "__main__":
    args = parser.parse_args()
    EMAIL = args.email  # 輸入你的 Facebook 帳號
    PASSWORD = args.password  # 輸入你的 Facebook 密碼
    POST_URL = "https://www.facebook.com/Xparkaquarium/posts/pfbid0dfu7trF6wmPSHd3Tzbz1eTVsmrZn6U6SYx5ad8njAP6Be78V65F9GvdcYsmwmDLyl?rdid=eySUOTdaFkXAVmNN"  # 替換為目標貼文的 URL

    try:
        # 登錄 Facebook
        driver.get(POST_URL)
        facebook_login(driver, EMAIL, PASSWORD)
   
        # 加載所有留言
        scroll_down(driver)

    finally:
        driver.quit()