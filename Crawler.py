import re
import ssl

import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)


q = []
visited = []
sites_crawled = 0

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

#Starting Point

url = "https://en.wikipedia.org/wiki/Kawasaki_motorcycles"
q.append(url)


while q and sites_crawled < 50:
    sites_crawled += 1

    curr_url = q.pop(0)
    visited.append(curr_url)

    print("Crawling on", curr_url,"...")

    try:
        data_file = open("url_number_"+str(sites_crawled)+".txt", 'w', encoding='utf-8')


        driver.get(curr_url)
        visible_texts = driver.find_element_by_xpath("/html/body").text
        page_contents = visible_texts

        data_file.write(page_contents)
        data_file.close()

        elems = driver.find_elements_by_xpath("//a[@href]")
        for elem in elems:
            link_or = elem.get_attribute("href")
            link = link_or.lower()
            if(link.startswith('http') and link_or not in visited and link_or not in q and "#" not in link and 'template' not in link and 'wikimedia' not in link and 'action=edit' not in link and 'login' not in link and 'facebook' not in link and 'google' not in link and 'amazon' not in link and '.jpg' not in link and curr_url not in link):
                if('kawasaki' in link or 'motorcycle' in link or 'kawi' in link or 'moto' in link or 'bike' in link):
                    q.append(link_or)

    except:
        print("Error crawling previous site...")
        pass

driver.close()

print(visited)




