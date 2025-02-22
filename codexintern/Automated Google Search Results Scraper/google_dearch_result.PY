from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller

#Automatic chromedriver instalation
chromedriver_autoinstaller.install()

# WebDriver setup
options = Options()
driver = webdriver.Chrome(options=options)

# open google search page
query = 'Best data science courses'
driver.get("https://www.google.com")

# search box
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)

search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)

# wait few seconds 
time.sleep(20)

# load result
results = driver.find_elements(By.CSS_SELECTOR, 'div.tF2Cxc')

# list for data store 
data = []
for result in results:
    try:
        title = result.find_element(By.CSS_SELECTOR, 'h3').text
        link = result.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        desc = result.find_element(By.CSS_SELECTOR, 'span').text
        data.append({"Title": title, "Link": link, "Description": desc})
    except Exception as e:
        print("Error:", e)

# डsave to csv
df = pd.DataFrame(data)
df.to_csv("output.csv", index=False)

print("Scraping complete... Data saved in output.csv")

driver.quit()
