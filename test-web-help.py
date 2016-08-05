
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from testrail import *
import sys




password = sys.argv[1]
# Gui Map
url = "https://test001.vortex.shared-dev.xmatters.com/xmatters/signOn.do"
username = "test001"        
elemUsername = "(//input)[2]"
password = "88888888"
elemPassword = "(//input)[3]"
elemClick = "//button"
webdriverPathChrom = "/Users/yangao/MyProject/on-call-reminder/chromedriver"
webdriverPathPhantomJS = "/Users/yangao/MyProject/ahch-to-test/phantomjs/bin/phantomjs"





driver = webdriver.PhantomJS(webdriverPathPhantomJS)

# login
print 'Login...'
driver.get(url)
driver.find_element_by_xpath(elemUsername).send_keys(username)
driver.find_element_by_xpath(elemPassword).send_keys(password)
driver.find_element_by_xpath(elemClick).click()
sleep(2)

print 'Step1. click Profile and question icon'
driver.find_element_by_xpath("(//div[text()='test001'])[1]").click()
sleep(2)
driver.find_element_by_xpath("(//div[text()='Profile'])[1]").click()
sleep(2)
driver.find_element_by_xpath("//a[@class='icon-question']").click()
sleep(2)
driver.switch_to_window(driver.window_handles[1])

Title = driver.title
Url = driver.current_url
H1Text = driver.find_element_by_xpath("//h1").text



comment1 = 'Step1: \nTitle: ' + Title + '\nUrl: ' + Url + '\nH1: ' + H1Text
print comment1
driver.close()


print 'verify test result -- Page Title, H1 Text and Url...'
if Title == 'Profile' and H1Text == 'Profile' and Url == 'https://help.xmatters.com/ondemand/user/details.htm?cshid=UserDetailsPlace':
    status_id = 1
else:
    status_id = 5
print status_id


print "Step2.click Messaging and question icon"

driver.switch_to_window(driver.window_handles[0])
sleep(2)

driver.find_element_by_xpath("//a[text()='Messaging']").click()
sleep(2)
driver.find_element_by_xpath("//a[@class='icon-question']").click()
sleep(2)
driver.switch_to_window(driver.window_handles[1])
sleep(2)


Title = driver.title
Url = driver.current_url
H1Text = driver.find_element_by_xpath("//h1").text


comment2 = '\nStep2: \nTitle: ' + Title + '\nUrl: ' + Url + '\nH1: ' + H1Text
print comment2



print 'verify test result -- Page Title, H1 Text and Url...'
if Title == 'Send a communication plan message' and H1Text == 'Send a communication plan message' and Url == 'https://help.xmatters.com/ondemand/xmodwelcome/communicationplanbuilder/send-message-using-form.htm?cshid=PanelSectionsPlace':
	status_id = 1
else:
	status_id = 5
print status_id

print 'Close driver...'
driver.switch_to_window(driver.window_handles[0])
driver.close()


client = APIClient('https://vic-qa-testrail.xmatters.com/testrail/')
client.user='ygao'
client.password = password

print 'input test result to testrail'

result = client.send_post('add_result_for_case/4228/260449',{ 'status_id': status_id, 'comment': comment1 +'\n' + comment2 })
print (result)

sleep(60)






