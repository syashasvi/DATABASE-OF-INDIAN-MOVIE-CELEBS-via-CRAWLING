#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
from requests import get
from tqdm import tqdm
from urllib.request import urlopen
import re
import csv


# In[ ]:


url_to_scrape = 'https://www.imdb.com/list/ls068010962/'

response = get(url_to_scrape)


# In[ ]:


html_soup = BeautifulSoup(response.text, 'html.parser')


# In[ ]:





# In[ ]:




# In[ ]:


html_soup = BeautifulSoup(response.text, 'html.parser')


# In[ ]:


actors_images_containers = html_soup.find_all('div', class_ = 'lister-item mode-detail')
actors_details_containers  = html_soup.find_all('div', class_ = 'lister-item-content')



actor_names = []
actor_desc = []
actor_images = []


images2 = html_soup.find_all('img', {'src':re.compile('.jpg')})




for i, container in enumerate(actors_images_containers):

    name = container.h3.a.text
    actor_names.append(name)

    desc = container.find('p', class_ = '').text
    actor_desc.append(desc)

    image = container.a.img.get('src')
    actor_images.append(image)
    print(name)
    print(desc)
    print(image)


#for image in images2:
    #actor_images.append(image['src'])
