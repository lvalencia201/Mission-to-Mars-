{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit the mars nasa news site\n",
    "url = 'https://redplanetscience.com/'\n",
    "browser.visit(url)\n",
    "\n",
    "# Optional delay for loading the page\n",
    "browser.is_element_present_by_css('div.list_text', wait_time=1)\n",
    "\n",
    "# Convert the browser html to a soup object and then quit the browser\n",
    "html = browser.html\n",
    "news_soup = soup(html, 'html.parser')\n",
    "\n",
    "slide_elem = news_soup.select_one('div.list_text')\n",
    "slide_elem.find('div', class_='content_title')\n",
    "\n",
    "# Use the parent element to find the first 'a' tag and save it as 'news_title'\n",
    "news_title = slide_elem.find('div', class_='content_title').get_text()\n",
    "news_title\n",
    "\n",
    "# Use the parent element to find the paragraph text\n",
    "news_p = slide_elem.find('div', class_='article_teaser_body').get_text()\n",
    "news_p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape_all():\n",
    "    # Initiate headless driver for deployment\n",
    "    executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "    browser = Browser('chrome', **executable_path, headless=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Run all scraping functions and store results in dictionary\n",
    "data = {\n",
    "      \"news_title\": news_title,\n",
    "      \"news_paragraph\": news_paragraph,\n",
    "      \"featured_image\": featured_image(browser),\n",
    "      \"facts\": mars_facts(),\n",
    "      \"last_modified\": dt.datetime.now()\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as soup\n",
    "import pandas as pd\n",
    "import datetime as dt\n",
    "from webdriver_manager.chrome import ChromeDriverManager"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    " # Stop webdriver and return data\n",
    "   browser.quit()\n",
    "   return data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    # If running as script, print scraped data\n",
    "    print(scrape_all())"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
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
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
