import urllib
import selenium
print("Welcome To Python scripts")
#load the url()import urllib.request;


url = "https://www.santanderbank.com/"
response = urllib.request.urlopen(url) 
webContent = response.read()
print(webContent)

driver = selenium.webdriver.Chrome()
driver.get("https://www.santanderbank.com/")   