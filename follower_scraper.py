from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
USERNAME = "maralthesage"

driver = webdriver.Chrome()


driver.get(f"https://{USERNAME}.medium.com/followers")
number_of_followers = int(driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[2]/div/div/div/div/div/div[1]/div[1]/div[2]/span').text.split()[0])

for i in range(int(number_of_followers/10)+1):
    sleep(1)
    html = driver.find_element(By.TAG_NAME, 'html')
    html.send_keys(Keys.END)

names = driver.find_elements(By.TAG_NAME, "h2")
# names = driver.find_elements(By.XPATH, '/html/body/div/div/div[3]/div[3]/div/main/div/div/div/div[3]/ul/div[1]/div/div[1]/div/a/h2')

with open("followers.txt", "w") as file:
    for item in names[1:-1]:
        print(item.text)
        file.write(item.text+"\n")
