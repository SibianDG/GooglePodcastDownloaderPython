from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re

# link = input('Give your link to download podcasts: ')
link = 'https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5jYXB0aXZhdGUuZm0vc2xpbW1lci1wcmVzdGVyZW4v?sa=X&ved=2ahUKEwjF6dC52tn1AhWKg_0HHcaBCzgQ9sEGegQIARAE'
episodes = {}
filenames = {}
options = Options()
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)
try:
    # Navigate to url
    driver.get(link)
    driver.save_screenshot('test.png')
    elements = driver.find_elements_by_class_name('oD3fme')
    for e in elements:
        title = e.find_elements_by_class_name('e3ZUqe')[0].get_attribute('innerHTML')
        tempEl = e.find_elements_by_class_name('zlb4lf')
        for t in tempEl[0].find_elements_by_tag_name('div'):
            if t.get_attribute('jsdata'):
                jsdata = t.get_attribute('jsdata')
                link = re.search("https://[^;]+\.mp3|http://www\.podtrac\.com/pts/redirect\.mp3/[^;]+\.mp3", jsdata).group()
                filename = re.search("[^/]+\.mp3", jsdata).group()
                episodes[title] = link
                filenames[filename] = link
                # print('added: ' + episodes[title])
finally:
    driver.quit()

    print("Title -> link")
    for key, value in episodes.items():
        print(f"{key} -> {value}")

    print("\n\nFilename -> link")
    for key, value in filenames.items():
        print(f"{key} -> {value}")

