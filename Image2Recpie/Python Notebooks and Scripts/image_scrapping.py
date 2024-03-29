# -*- coding: utf-8 -*-
"""Image_Scrapping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PFnj4dRu5rZbiOOt9PzSM0351yg7rtvH
"""

import requests
import urllib.request
import bs4
from bs4 import BeautifulSoup
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request
import os

def get_Data(url,folder_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    os.makedirs(folder_name, exist_ok=True)
    image_tags = soup.find_all("img")
    for image in image_tags:
        image_url = image.get("src")
        if image_url and image_url.startswith("https://"):
            response = requests.get(image_url)
            if response.status_code == 200:
                image_filename = os.path.basename(image_url)
                image_path = os.path.join(folder_name, image_filename)
                with open(image_path, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded: {image_filename}")

def get_page_contents(url):
    page=urllib.request.urlopen(url)
    page_soup=BeautifulSoup(page,'html.parser')
    img_item=page_soup.find_all('picture')
    print(img_item)

def list_img(url):
    list_of_img = []
    for i in range(1,100):
        page = urllib.request.urlopen(url)
        page_soup = BeautifulSoup(page, 'html.parser')
        img_items = page_soup.find_all('picture')

        for item in img_items:
            sources = item.find_all('source')
            for source in sources:
                srcset = source['srcset']
                list_of_img.append(srcset)
    return list_of_img

def set_images(list_of_img,filename,end_val,str_val):
    count = str_val
    n=0
    if not os.path.exists(filename):
            os.makedirs(filename)

    for i, img_url in enumerate(list_of_img):
        i=str_val+n
        n=n+1
        if count == end_val:
            break
        try:

            response = urllib.request.urlopen(img_url)
            image_data = response.read()


            filenamePath = f"{filename}/image_{i+1}.jpg"
            with open(filenamePath, "wb") as f:
                f.write(image_data)

            print(f"Image {i+1} saved as {filename}")
            count+=1
        except urllib.error.HTTPError as e:
            print(f"Error downloading image {i+1}: {e}")

str_val=0
end_val = 60
for i in range(1,16):
    url = f"https://www.istockphoto.com/search/2/image?page={i}&phrase=Naan"
    folder_name = "Naan_img"
    filename = "Naan"
    get_Data(url,folder_name)
    get_page_contents(url)
    list_images = list_img(url)
    set_images(list_images,filename,end_val,str_val)
    str_val = end_val
    end_val=end_val+60

str_val=0
end_val = 60
for i in range(1,16):
    url = f"https://www.istockphoto.com/search/2/image?page={i}&phrase=paneer%20tikka"
    folder_name = "Paneer_Tikka_img"
    filename = "Paneer_Tikka"
    get_Data(url,folder_name)
    get_page_contents(url)
    list_images = list_img(url)
    set_images(list_images,filename,end_val,str_val)
    str_val = end_val
    end_val=end_val+60

str_val=0
end_val = 60
for i in range(1,13):
    url = f"https://www.istockphoto.com/search/2/image?page={i}&phrase=vadapav"
    folder_name = "vadapav_img"
    filename = "vadapav"
    get_Data(url,folder_name)
    get_page_contents(url)
    list_images = list_img(url)
    set_images(list_images,filename,end_val,str_val)
    str_val = end_val
    end_val=end_val+60

str_val=0
end_val = 60
for i in range(1,16):
    url = f"https://www.istockphoto.com/search/2/image?page={i}&phrase=spring%20rolls"
    folder_name = "spring_rolls_img"
    filename = "spring_rolls"
    get_Data(url,folder_name)
    get_page_contents(url)
    list_images = list_img(url)
    set_images(list_images,filename,end_val,str_val)
    str_val = end_val
    end_val=end_val+60

str_val=0
end_val = 60
for i in range(1,16):
    url = f"https://www.istockphoto.com/search/2/image?page={i}&phrase=pav%20bhaji"
    folder_name = "pav_bhaji_img"
    filename = "pav_bhaji"
    get_Data(url,folder_name)
    get_page_contents(url)
    list_images = list_img(url)
    set_images(list_images,filename,end_val,str_val)
    str_val = end_val
    end_val=end_val+60

str_val=0
end_val = 60
for i in range(1,16):
    url = f"https://www.istockphoto.com/search/2/image?page={i}&phrase=pani%20puri%20"
    folder_name = "pani_puri_img"
    filename = "pani_puri"
    get_Data(url,folder_name)
    get_page_contents(url)
    list_images = list_img(url)
    set_images(list_images,filename,end_val,str_val)
    str_val = end_val
    end_val=end_val+60

str_val=0
end_val = 60
for i in range(1,16):
    url = f"https://www.istockphoto.com/search/2/image?page={i}&phrase=pakora"
    folder_name = "pakora_img"
    filename = "pakora"
    get_Data(url,folder_name)
    get_page_contents(url)
    list_images = list_img(url)
    set_images(list_images,filename,end_val,str_val)
    str_val = end_val
    end_val=end_val+60

str_val=0
end_val = 60
for i in range(1,16):
    url = f"https://www.istockphoto.com/search/2/image?page={i}&phrase=omelette"
    folder_name = "omelette_img"
    filename = "omelette"
    get_Data(url,folder_name)
    get_page_contents(url)
    list_images = list_img(url)
    set_images(list_images,filename,end_val,str_val)
    str_val = end_val
    end_val=end_val+60

str_val=0
end_val = 60
for i in range(1,16):
    url = f"https://www.istockphoto.com/search/2/image?page={i}&phrase=kofta"
    folder_name = "kofta_img"
    filename = "kofta"
    get_Data(url,folder_name)
    get_page_contents(url)
    list_images = list_img(url)
    set_images(list_images,filename,end_val,str_val)
    str_val = end_val
    end_val=end_val+60

str_val=0
end_val = 60
for i in range(1,16):
    url = f"https://www.istockphoto.com/search/2/image?page={i}&phrase=jalebi"
    folder_name = "jalebi_img"
    filename = "jalebi"
    get_Data(url,folder_name)
    get_page_contents(url)
    list_images = list_img(url)
    set_images(list_images,filename,end_val,str_val)
    str_val = end_val
    end_val=end_val+60

str_val=0
end_val = 60
for i in range(1,16):
    url = f"https://www.istockphoto.com/search/2/image?page={i}&phrase=hot%20dog"
    folder_name = "hot_dog_img"
    filename = "hot_dog"
    get_Data(url,folder_name)
    get_page_contents(url)
    list_images = list_img(url)
    set_images(list_images,filename,end_val,str_val)
    str_val = end_val
    end_val=end_val+60

str_val=0
end_val = 60
for i in range(1,16):
    url = f"https://www.istockphoto.com/search/2/image?page={i}&phrase=ice%20cream"
    folder_name = "ice_cream_img"
    filename = "ice_cream"
    get_Data(url,folder_name)
    get_page_contents(url)
    list_images = list_img(url)
    set_images(list_images,filename,end_val,str_val)
    str_val = end_val
    end_val=end_val+60

str_val=0
end_val = 60
for i in range(1,16):
    url = f"https://www.istockphoto.com/search/2/image?page={i}&phrase=dosa"
    folder_name = "dosa_img"
    filename = "dosa"
    get_Data(url,folder_name)
    get_page_contents(url)
    list_images = list_img(url)
    set_images(list_images,filename,end_val,str_val)
    str_val = end_val
    end_val=end_val+60

str_val=0
end_val = 60
for i in range(1,16):
    url = f"https://www.istockphoto.com/search/2/image?page={i}&phrase=dhokla"
    folder_name = "dhokla_img"
    filename = "dhokla"
    get_Data(url,folder_name)
    get_page_contents(url)
    list_images = list_img(url)
    set_images(list_images,filename,end_val,str_val)
    str_val = end_val
    end_val=end_val+60

str_val=0
end_val = 60
for i in range(1,21):
    url = f"https://www.istockphoto.com/search/2/image?page={i}&phrase=dal"
    folder_name = "dal_img"
    filename = "dal"
    get_Data(url,folder_name)
    get_page_contents(url)
    list_images = list_img(url)
    set_images(list_images,filename,end_val,str_val)
    str_val = end_val
    end_val=end_val+60

str_val=0
end_val = 60
for i in range(1,10):
    url = f"https://www.istockphoto.com/search/2/image?page={i}&phrase=chole%20bhature"
    folder_name = "chole_bhature_img"
    filename = "chole_bhature"
    get_Data(url,folder_name)
    get_page_contents(url)
    list_images = list_img(url)
    set_images(list_images,filename,end_val,str_val)
    str_val = end_val
    end_val=end_val+60



# get_page_contents(url)

# list_images = list_img(url)

# len(list_images)

# set_images(list_images,filename,end_val)

