from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

# Github credentials
username = "kponnu013"
password = "Leotimes@20221"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait as wait



def automate_git_pull_request():
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
	driver.get("https://www.google.com")

	# head to github login page
	driver.get("https://github.com/login")


	# find username/email field and send the username itself to the input field
	driver.find_element_by_id("login_field").send_keys(username)

	# find password input field and insert password as well
	driver.find_element_by_id("password").send_keys(password)

	time.sleep(5)

	driver.find_element_by_name("commit").click()

	time.sleep(5)

	driver.get("https://github.com/kponnu013/rdkservices")

	time.sleep(5)

	#driver.find_element_by_link_text("compare & pull request").click()
	try:
	    driver.find_element_by_partial_link_text("Compare").click()

	except:
	    print("Pull request not crewated")
	    driver.close()
	    quit()

	time.sleep(5)

	try:
	    driver.find_element_by_id("pull_request_body").send_keys("Requesting the changes to commit")
	except:
	    print("TEST")
	    driver.close()
	    quit()

	time.sleep(5)

	try:
	    driver.findElement(By.xpath("//*[@id='new_pull_request']/div/div[1]/div/div[2]/div/div[2]/div/button")).click();
	except:
	    print("NOT found ###################3")
	    driver.close()
	    quit()

	time.sleep(10)

	# close the driver
	driver.close()
