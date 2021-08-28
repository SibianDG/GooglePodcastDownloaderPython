from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re

# link = input('Give your link to download podcasts: ')
link = 'https://podcasts.google.com/feed/aHR0cHM6Ly9yc3MuYXJ0MTkuY29tL2RlLXVuaXZlcnNpdGVpdC12YW4tdmxhYW5kZXJlbi1wb2RjYXN0?sa=X&ved=2ahUKEwjen_ys_9PyAhVOh_0HHfAtDKgQ9sEGegQIARAC'
episodes = {}
options = Options()
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)
try:
    # Navigate to url
    driver.get(link)
    elements = driver.find_elements_by_class_name('oD3fme')
    for e in elements:
        title = e.find_elements_by_class_name('e3ZUqe')[0].get_attribute('innerHTML')
        tempEl = e.find_elements_by_class_name('zlb4lf')
        for t in tempEl[0].find_elements_by_tag_name('div'):
            if t.get_attribute('jsdata'):
                jsdata = t.get_attribute('jsdata')
                match = re.search("https[^?]+\.mp3", jsdata)
                episodes[title] = match.group()
                print('added')
finally:
    driver.quit()
    print(episodes)


