from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import urllib.request

link = input('Give your link to download podcasts: ')
# link = 'https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5jYXB0aXZhdGUuZm0vc2xpbW1lci1wcmVzdGVyZW4v?sa=X&ved=2ahUKEwjF6dC52tn1AhWKg_0HHcaBCzgQ9sEGegQIARAE'
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
                link = re.search("https://[^;]+\.mp3|http://www\.podtrac\.com/pts/redirect\.mp3/[^;]+\.mp3",
                                 jsdata).group()
                filename = re.search("[^/]+\.mp3", jsdata).group()
                episodes[title] = link
                filenames[filename] = link
                # print('added: ' + episodes[title])
finally:
    driver.quit()

    if len(filenames) > 0:

        print("Title -> link")
        index = 0
        for key, value in episodes.items():
            print(f"{index}: {key} -> {value}")
            index += 1

        print("\n\nFilename -> link")
        index = 0
        for key, value in filenames.items():
            print(f"{index}: {key} -> {value}")
            index += 1

        type_var = ""
        index = 0
        while type_var.lower() != "single" and type_var.lower() != "all":
            type_var = input("Input download type 'single' to downlad one file or 'all' to download all ({}) files: ".format(len(list(filenames))))
        print("### type_var:{}".format(type_var))

        if type_var == 'all':
            for listel in list(filenames):
                print ("### {} Download file with name: {}".format(index,listel))
                index += 1
                link = list(filenames.values())[int(index)]
                urllib.request.urlretrieve(link, listel)
        elif type_var == 'single':
            number = ''
            while number.lower() != "stop":
                number = input("Input number you want to download or stop to interrupt: ")
                if number.lower() == "stop":
                    break
                link = list(filenames.values())[int(number)]
                name = list(filenames)[int(number)]
                print ("### Download file #{} with name: {}".format(number,name))
                urllib.request.urlretrieve(link, name)
