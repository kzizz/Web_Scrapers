import requests
from bs4 import BeautifulSoup
import shutil

URL = 'https://www.si.edu/search/collection-images?edan_q=portraits&edan_fq%5B0%5D=%28date%3A%221790s%22%20AND%20date%3A%221850s%22%29%20OR%20%28date%3A%221800s%22%20AND%20date%3A%221850s%22%29%20OR%20%28date%3A%221820s%22%20AND%20date%3A%221850s%22%29%20OR%20%28date%3A%221830s%22%20AND%20date%3A%221850s%22%29%20OR%20%28date%3A%221840s%22%20AND%20date%3A%221850s%22%29%20OR%20%28date%3A%221860s%22%20AND%20date%3A%221850s%22%29%20OR%20%28date%3A%221870s%22%20AND%20date%3A%221850s%22%29%20OR%20%28date%3A%221880s%22%20AND%20date%3A%221850s%22%29%20OR%20%28date%3A%221900s%22%20AND%20date%3A%221850s%22%29&edan_fq%5B1%5D=media_usage%3A%22CC0%22'
# URL = 'https://www.si.edu/'
results = requests.get(URL)

soup= BeautifulSoup(results.text, 'html.parser')
# print(soup.prettify())

imgs = []

image_div = soup.find_all('div',class_='node node--teaser node--teaser-long')

for container in image_div:
    image = container.a.find('span', class_='b-media-wrapper field--type-image').img['src'] #span.image
    imgs.append(image)

print(imgs)

#Now download the images locally

for i, img_url in enumerate(imgs):
    r = requests.get(img_url, stream=True) #Get request on full_url
    imagename = 'images' + '/' + 'portraits' + str(i+1) + '.jpg'
    if r.status_code == 200:                     #200 status code = OK
        with open(imagename, 'wb') as f: 
            f.write(r.content)
print("done")