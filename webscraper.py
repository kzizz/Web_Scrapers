import requests
from bs4 import BeautifulSoup
import shutil

baseURL = 'https://www.si.edu'
keyURL = 'https://www.si.edu/search/collection-images?edan_q=portraits&edan_fq%5B0%5D=%28date%3A%221790s%22%20AND%20date%3A%221850s%22%29%20OR%20%28date%3A%221800s%22%20AND%20date%3A%221850s%22%29%20OR%20%28date%3A%221820s%22%20AND%20date%3A%221850s%22%29%20OR%20%28date%3A%221830s%22%20AND%20date%3A%221850s%22%29%20OR%20%28date%3A%221840s%22%20AND%20date%3A%221850s%22%29%20OR%20%28date%3A%221860s%22%20AND%20date%3A%221850s%22%29%20OR%20%28date%3A%221870s%22%20AND%20date%3A%221850s%22%29%20OR%20%28date%3A%221880s%22%20AND%20date%3A%221850s%22%29%20OR%20%28date%3A%221900s%22%20AND%20date%3A%221850s%22%29&edan_fq%5B1%5D=media_usage%3A%22CC0%22'
imgs = []



def parse_page(URL):
    print("Parsing a new page!")
    results = requests.get(URL)
    soup= BeautifulSoup(results.text, 'html.parser')
    image_div = soup.find_all('div',class_='node node--teaser node--teaser-long')
    
    for container in image_div:
        image = container.a.find('span', class_='b-media-wrapper field--type-image').img['src'] #span.image
        imgs.append(image)
    
    #Check if there is a next page of results
    next_page = soup.find('li', class_="pager__item pager__item--next")
    if next_page:
        next_url = baseURL + next_page.a['href']
        parse_page(next_url)
    return

#Download all scraped images locally
def download_images(img_list):
    for i, img_url in enumerate(img_list):
        r = requests.get(img_url, stream=True)
        imagename = 'images' + '/' + 'portraits' + str(i+1) + '.jpg'
        if r.status_code == 200:
            with open(imagename, 'wb') as f: 
                f.write(r.content)
    print("Done saving imgs locally")

#To be called 
def get_images(URL):
    parse_page(URL)
    print("There are ",len(imgs)," imgs scraped")
    # download_images(imgs)

get_images(keyURL)




