from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
USERNAME = "maralthesage"

driver = webdriver.Chrome()

driver.get(f"https://{USERNAME}.medium.com/")

# number_of_followings = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[2]/div/div/div/div/div/div[1]/div[2]/div[5]/p/button").text
# print(number_of_followings)
followings = driver.find_element(By.CSS_SELECTOR, 'div.l p.dk button.ae')
followings_number = int(followings.text.split("(")[1].split(")")[0])
followings.click()
sleep(1)


for i in range(int(followings_number/10)+1):
    more_btn = driver.find_elements(By.TAG_NAME, "button")
    for item in more_btn:
        if item.text == "Show more":
            item.click()

    sleep(1)
    html = driver.find_element(By.TAG_NAME,'html')
    html.send_keys(Keys.END)


list_of_followings = driver.find_elements(By.TAG_NAME,"h2")


with open("followings.txt", 'w') as file:
    for item in list_of_followings[23:]:
        file.write(item.text+"\n")
        print(item.text)
#
#
