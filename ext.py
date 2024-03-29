from selenium import webdriver
from selenium.webdriver import ActionChains

path = "chromedriver"
driver = webdriver.Chrome(path)
url = "https://www.hackerrank.com/dashboard"
driver.get(url)
driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/div[1]/nav/div/div[2]/ul[2]/li[1]/button').click()
driver.find_element_by_xpath(
    '/html/body/div[9]/div/div/div/section/div/div/div[2]/div[1]/form/div[1]/div/div/input').send_keys(
    "nerdherdindore@gmail.com")
driver.find_element_by_xpath(
    '/html/body/div[9]/div/div/div/section/div/div/div[2]/div[1]/form/div[2]/div/div/input').send_keys("*******")
driver.find_element_by_xpath("/html/body/div[9]/div/div/div/section/div/div/div[2]/div[1]/form/div[4]/button").click()
# Enter the no of pages in pagination
pageno = 100

# Name the file
file = open("small-triangles-large-triangles.csv", "w")
file.write("Name,Time\n")
for page in range(1, pageno + 1):
    # Enter the link of contests leaderboard below address field
    address = 'https://www.hackerrank.com/contests/1st-year-12-days-coding-challenge/challenges/small-triangles-large-triangles/leaderboard/' \
              + str(page)

    driver.get(url=address)
    driver.implicitly_wait(8)
    # driver.implicitly_wait(40)
    # driver.find_element_by_xpath('//*[@id="legacy-signup"]/div[1]/p/button').click()

    # variables for names
    firstn = '/html/body/div[2]/div[10]/div/div/section/div/div[2]/section/div[2]/div[2]/div['
    secondn = ']/div/div[2]/p/a'

    # variables for time
    firstT = '/html/body/div[2]/div[10]/div/div/section/div/div[2]/section/div[2]/div[2]/div['
    secondT = ']/div/div[5]/p'

    for n in range(1, 11):
        finaln = firstn + str(n) + secondn
        finalT = firstT + str(n) + secondT
        name = driver.find_element_by_xpath(finaln).text
        time = driver.find_element_by_xpath(finalT).text
        Write = name + "," + time + "\n"
        file.write(Write)

file.close()
