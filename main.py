import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# csv file for output
df = pd.read_csv("scrapper_data.csv", index_col="SrNo")

# set count for number of rows to scrape - check the page before setting this number
count = 4

# selenium chrome webdriver setup
driver = webdriver.Chrome()
driver.get("https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787")
driver.implicitly_wait(30)

# get table
table = driver.find_element(By.CSS_SELECTOR, "#table_id")

# sort by post date descending
thead = table.find_element(By.TAG_NAME, "thead")
first_column_header = thead.find_element(By.XPATH, "./tr[1]/th[1]/a")
first_column_header.click()
time.sleep(2)
first_column_header.click()
time.sleep(2)

# click on first row item to open detailed page
rows = table.find_elements(By.XPATH, ".//tbody/tr")
cells = rows[0].find_elements(By.XPATH, ".//td/a")
cells[0].click()

# loop runs "count" times
# add required details from the page to df
for item in range(1, count+1):
	time.sleep(3)
	questno = driver.find_element(By.XPATH, "//span[contains(@class, 'text-primary-questcdn')]/b")
	df.loc[item, "Quest no"] = questno.text.split()[-1]
	df.loc[item, "Est. Value Notes"] = driver.find_element(By.XPATH, "//td[contains(text(), 'Est. Value Notes')]/following-sibling::td").text
	df.loc[item, "Description"] = driver.find_element(By.XPATH, "//td[contains(text(), 'Description')]/following-sibling::td").text
	df.loc[item, "Due Date"] = driver.find_element(By.XPATH, "//td[contains(text(), 'Closing Date')]/following-sibling::td").text
	time.sleep(3)

	# click to go to next page
	tmp = driver.find_element(By.ID, "id_prevnext_next")
	tmp.click()
	time.sleep(3)

# final output
df.to_csv('scrapper_data.csv')