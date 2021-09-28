from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re

# link = input('Give your link to download podcasts: ')
link = 'https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5zb3VuZGNsb3VkLmNvbS91c2Vycy9zb3VuZGNsb3VkOnVzZXJzOjQ3MzQ4NjczOS9zb3VuZHMucnNz'
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
                print(jsdata)
                match = re.search("https://[^;]+\.mp3|http://www\.podtrac\.com/pts/redirect\.mp3/[^;]+\.mp3", jsdata)
                episodes[title] = match.group()
                print('added: ' + episodes[title])
finally:
    driver.quit()
    print(episodes)


