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
    '/html/body/div[9]/div/div/div/section/div/div/div[2]/div[1]/form/div[2]/div/div/input').send_keys("nh!234567")
driver.find_element_by_xpath("/html/body/div[9]/div/div/div/section/div/div/div[2]/div[1]/form/div[4]/button").click()
driver.get(url='https://www.hackerrank.com/contests/14daysofcode-beginner/challenges/solve-me-first/leaderboard')

driver.implicitly_wait(20)
driver.find_element_by_xpath('//*[@id="legacy-signup"]/div[1]/p/button').click()
first='/html/body/div[2]/div[10]/div/div/section/div/div[2]/section/div[2]/div[2]/div['
second=']/div/div[2]/p/a'

for n in range(1,11):
    final=first+str(n)+second
    name = driver.find_element_by_xpath(final).text
    print(name)