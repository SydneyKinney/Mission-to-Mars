{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "71e6189e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2022-08-12 07:59:32.812951\n",
      "\n",
      "Platform            : 12.4 | Darwin | 21.5.0 | x86_64\n",
      "\n",
      "Python              : 3.10.5 | packaged by conda-forge | (main, Jun 14 2022, 07:03:09) [Clang 13.0.1 ]\n",
      "                    : sys.version_info(major=3, minor=10, micro=5, releaselevel='final', serial=0)\n",
      "                    : CPython\n",
      "\n",
      "Beautiful Soup      : 4.11.1\n",
      "NumPy               : 1.23.1\n",
      "Pandas              : 1.4.3\n",
      "Selenium            : 4.2.0\n",
      "Splinter            : 0.18.1\n",
      "webdriver-manager   : 3.8.3\n"
     ]
    }
   ],
   "source": [
    "import numpy  as np\n",
    "import pandas as pd\n",
    "\n",
    "import bs4\n",
    "from   bs4 import BeautifulSoup as soup\n",
    "\n",
    "import webdriver_manager\n",
    "from   webdriver_manager.chrome import ChromeDriverManager\n",
    "\n",
    "import splinter\n",
    "from   splinter import Browser\n",
    "# This Splinter code will be used in the assignment below.\n",
    "#executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "#browser         = Browser(driver_name='chrome',\n",
    "#                           retry_count=1,\n",
    "#                           **executable_path,\n",
    "#                           headless   =True) # set to False if you would like to see the web page\n",
    "\n",
    "# Selenium 4\n",
    "#   Selenium 4 code should not be required to run Splinter code.\n",
    "#   Selenium 4 code is included here for the purposes of explication.\n",
    "import selenium\n",
    "from   selenium                          import webdriver\n",
    "from   selenium.webdriver.chrome.service import Service as ChromeService\n",
    "from   selenium.webdriver.common.by      import By\n",
    "\n",
    "from datetime import datetime\n",
    "print(datetime.now())\n",
    "print()\n",
    "import platform\n",
    "print(f\"{'Platform':<20}: \"\n",
    "      f\"{platform.mac_ver()[0]} | \"\n",
    "      f\"{platform.system()} | \"\n",
    "      f\"{platform.release()} | \"\n",
    "      f\"{platform.machine()}\")\n",
    "print()\n",
    "import sys\n",
    "print(f\"{'Python':<20}: {sys.version}\")\n",
    "print(f\"{'':<20}: {sys.version_info}\")\n",
    "print(f\"{'':<20}: {platform.python_implementation()}\")\n",
    "print()\n",
    "print(f\"{'Beautiful Soup':<20}: {bs4.__version__}\")\n",
    "print(f\"{'NumPy':<20}: {np.__version__}\")\n",
    "print(f\"{'Pandas':<20}: {pd.__version__}\")\n",
    "print(f\"{'Selenium':<20}: {selenium.__version__}\")\n",
    "print(f\"{'Splinter':<20}: {splinter.__version__}\")\n",
    "print(f\"{'webdriver-manager':<20}: {webdriver_manager.__version__}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0f1271e8",
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "752eb5a4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Visit the mars nasa news site\n",
    "url = 'https://redplanetscience.com'\n",
    "browser.visit(url)\n",
    "# Optional delay for loading the page\n",
    "browser.is_element_present_by_css('div.list_text', wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "40495124",
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "news_soup = soup(html, 'html.parser')\n",
    "slide_elem = news_soup.select_one('div.list_text')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7678e160",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<div class=\"content_title\">A New Video Captures the Science of NASA's Perseverance Mars Rover</div>"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "slide_elem.find('div', class_='content_title')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b07dfe43",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"A New Video Captures the Science of NASA's Perseverance Mars Rover\""
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the parent element to find the first `a` tag and save it as `news_title`\n",
    "news_title = slide_elem.find('div', class_='content_title').get_text()\n",
    "news_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "513612e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'With a targeted launch date of July 30, the next robotic scientist NASA is sending to the to the Red Planet has big ambitions.'"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the parent element to find the paragraph text\n",
    "news_p = slide_elem.find('div', class_='article_teaser_body').get_text()\n",
    "news_p"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c43999e9",
   "metadata": {},
   "source": [
    "### Featured Images"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "364e91bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit URL\n",
    "url = 'https://spaceimages-mars.com'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "43585c79",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find and click the full image button\n",
    "full_image_elem = browser.find_by_tag('button')[1]\n",
    "full_image_elem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "8f64fdb9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse the resulting html with soup\n",
    "html = browser.html\n",
    "img_soup = soup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "72e3c961",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'image/featured/mars1.jpg'"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Find the relative image url\n",
    "img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')\n",
    "img_url_rel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "926a5018",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://spaceimages-mars.com/image/featured/mars1.jpg'"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the base url to create an absolute url\n",
    "img_url = f'https://spaceimages-mars.com/{img_url_rel}'\n",
    "img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "650131d6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>description</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Mars - Earth Comparison</th>\n",
       "      <td>Mars</td>\n",
       "      <td>Earth</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Diameter:</th>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Distance from Sun:</th>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Length of Year:</th>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Temperature:</th>\n",
       "      <td>-87 to -5 °C</td>\n",
       "      <td>-88 to 58°C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                    Mars            Earth\n",
       "description                                              \n",
       "Mars - Earth Comparison             Mars            Earth\n",
       "Diameter:                       6,779 km        12,742 km\n",
       "Mass:                    6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "Moons:                                 2                1\n",
       "Distance from Sun:        227,943,824 km   149,598,262 km\n",
       "Length of Year:           687 Earth days      365.24 days\n",
       "Temperature:                -87 to -5 °C      -88 to 58°C"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_html('https://galaxyfacts-mars.com')[0]\n",
    "df.columns=['description', 'Mars', 'Earth']\n",
    "df.set_index('description', inplace=True)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "8dd87468",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>Mars</th>\\n      <th>Earth</th>\\n    </tr>\\n    <tr>\\n      <th>description</th>\\n      <th></th>\\n      <th></th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>Mars - Earth Comparison</th>\\n      <td>Mars</td>\\n      <td>Earth</td>\\n    </tr>\\n    <tr>\\n      <th>Diameter:</th>\\n      <td>6,779 km</td>\\n      <td>12,742 km</td>\\n    </tr>\\n    <tr>\\n      <th>Mass:</th>\\n      <td>6.39 × 10^23 kg</td>\\n      <td>5.97 × 10^24 kg</td>\\n    </tr>\\n    <tr>\\n      <th>Moons:</th>\\n      <td>2</td>\\n      <td>1</td>\\n    </tr>\\n    <tr>\\n      <th>Distance from Sun:</th>\\n      <td>227,943,824 km</td>\\n      <td>149,598,262 km</td>\\n    </tr>\\n    <tr>\\n      <th>Length of Year:</th>\\n      <td>687 Earth days</td>\\n      <td>365.24 days</td>\\n    </tr>\\n    <tr>\\n      <th>Temperature:</th>\\n      <td>-87 to -5 °C</td>\\n      <td>-88 to 58°C</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.to_html()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "439211eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. Use browser to visit the URL \n",
    "url = 'https://marshemispheres.com/'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "3daffb6f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. Create a list to hold the images and titles.\n",
    "hemisphere_image_urls = []\n",
    "\n",
    "# 3. Write code to retrieve the image urls and titles for each hemisphere.\n",
    "links = browser.find_by_css('a.product-item img')\n",
    "\n",
    "for i in range(len(links)):\n",
    "    hemisphere = {}\n",
    "\n",
    "    # Find elements going to click link.\n",
    "    browser.find_by_css('a.product-item img')[i].click()\n",
    "\n",
    "    # Find sample image link\n",
    "    sample_element = browser.links.find_by_text('Sample').first\n",
    "\n",
    "    # Get hemisphere Title\n",
    "    hemisphere['img_url'] = sample_element['href']\n",
    "\n",
    "    # Get hemisphere Title\n",
    "    hemisphere['title'] = browser.find_by_css('h2.title').text\n",
    "\n",
    "    # Add Objects to hemisphere_image_urls list\n",
    "    hemisphere_image_urls.append(hemisphere)\n",
    "\n",
    "    # Go Back\n",
    "    browser.back()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "699f9f6f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'img_url': 'https://marshemispheres.com/images/full.jpg',\n",
       "  'title': 'Cerberus Hemisphere Enhanced'},\n",
       " {'img_url': 'https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg',\n",
       "  'title': 'Schiaparelli Hemisphere Enhanced'},\n",
       " {'img_url': 'https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg',\n",
       "  'title': 'Syrtis Major Hemisphere Enhanced'},\n",
       " {'img_url': 'https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg',\n",
       "  'title': 'Valles Marineris Hemisphere Enhanced'}]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 4. Print the list that holds the dictionary of each image url and title.\n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "5f938007",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5. Quit the browser\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ebb948e2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2bdf03f5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ccbe4c4e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "data-b-10-missiontomars",
   "language": "python",
   "name": "data-b-10-missiontomars"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
