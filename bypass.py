from undetected_chromedriver import Chrome
import time

# create a new instance of Chrome using a context manager
with Chrome() as chrome:
    # navigate to the website
    website = input("Enter the website: ")
    chrome.get(website)

    time.sleep(10)
    # no need to explicitly close the browser, it will be closed automatically
