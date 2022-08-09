#!/usr/bin/env python
# coding: utf-8
# In[9]:

import numpy  as np
import pandas as pd
import bs4
from   bs4 import BeautifulSoup as soup
import webdriver_manager
from   webdriver_manager.chrome import ChromeDriverManager
import splinter
from   splinter import Browser
# This Splinter code will be used in the assignment below.
#executable_path = {'executable_path': ChromeDriverManager().install()}
#browser         = Browser(driver_name='chrome',
#                           retry_count=1,
#                           **executable_path,
#                           headless   =True) # set to False if you would like to see the web page

# Selenium 4
#   Selenium 4 code should not be required to run Splinter code.
#   Selenium 4 code is included here for the purposes of explication.
import selenium
from   selenium                          import webdriver
from   selenium.webdriver.chrome.service import Service as ChromeService
from   selenium.webdriver.common.by      import By

from datetime import datetime
print(datetime.now())
print()
import platform
print(f"{'Platform':<20}: "
      f"{platform.mac_ver()[0]} | "
      f"{platform.system()} | "
      f"{platform.release()} | "
      f"{platform.machine()}")
print()
import sys
print(f"{'Python':<20}: {sys.version}")
print(f"{'':<20}: {sys.version_info}")
print(f"{'':<20}: {platform.python_implementation()}")
print()
print(f"{'Beautiful Soup':<20}: {bs4.__version__}")
print(f"{'NumPy':<20}: {np.__version__}")
print(f"{'Pandas':<20}: {pd.__version__}")
print(f"{'Selenium':<20}: {selenium.__version__}")
print(f"{'Splinter':<20}: {splinter.__version__}")
print(f"{'webdriver-manager':<20}: {webdriver_manager.__version__}")


# In[10]:
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# In[11]:
# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# In[12]:
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

# In[13]:
slide_elem.find('div', class_='content_title')

# In[14]:
# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# In[15]:
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# ### Featured Images

# In[16]:
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# In[17]:
# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# In[18]:
# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# In[19]:
# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# In[20]:
# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# In[21]:
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# In[22]:
df.to_html()

# In[23]:
browser.quit()




