import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import sys
#from streamlit.web import cli as stcli

import streamlit
from streamlit import runtime
from streamlit_toggle import toggle
from streamlit.web import cli as stcli
import streamlit as st
from datetime import datetime, timedelta
import os
import glob
import requests

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import streamlit as st
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager




def main():

    import re
    from bs4 import BeautifulSoup
    from selenium import webdriver
    import pandas as pd
    
    # Set up the Chrome driver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    
    def daraz(url):
        # Create Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
    
        # Create the driver with the options
        driver = webdriver.Chrome(options=chrome_options)
    
        # Load the page with Selenium
        driver.get(url)
    
        # Wait up to 10 seconds for the page to load
        # Wait for the page to finish loading all JavaScript
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//body[not(@class='loading')]")))
    
        # Get the HTML of the page and pass it to BeautifulSoup
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
    
        # Use a regular expression to match classes that have a similar pattern
        pattern = re.compile(r'gridItem--\w+')
    
        # Find all tags that have classes matching the pattern
        matching_tags = soup.find_all(class_=pattern)
    
        driver.close()
    
        # Append the matching classes to a list
        matching_classes = []
        for tag in matching_tags:
            for class_name in tag['class']:
                if pattern.match(class_name):
                    matching_class = str(tag)
                    matching_classes.append(matching_class)
    
        # Extract the price for each class content
        prices = []
        names = []
        img_links = []
        for class_content in matching_classes:
            soup = BeautifulSoup(class_content, 'html.parser')
            price_tag = soup.find(class_=re.compile('currency--\w+'))
            if price_tag:
                price = price_tag.text.strip()
                prices.append(price)
            else:
                prices.append(None)
    
            image = soup.find(class_=re.compile('image--\w+'))
            if image:
                image_link = image['src']
                alt_text = image['alt']
                names.append(alt_text)
                img_links.append(image_link)
            else:
                names.append(None)
                img_links.append(None)
    
        x = "https://icms-image.slatic.net/images/ims-web/217b267f-b12e-4693-9d1d-7a77d2265b91.png"
        df = pd.DataFrame(
            {'Site': '<img src="' + x + '" width="60" >', 'Product Name': names, 'Price': prices, 'Image Link': img_links})
        os.chdir("/mount/src/edomenico/area1")
        df.to_csv("metar.csv", header=True)
        return df.iloc[[0]]
    
    
    def kapruka(url):
        # Create Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
    
        # Create the driver with the options
        driver = webdriver.Chrome(options=chrome_options)
    
        # Load the page with Selenium
        driver.get(url)
    
        # Wait up to 10 seconds for the page to load
        # Wait for the page to finish loading all JavaScript
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//body[not(@class='loading')]")))
    
        # Get the HTML of the page and pass it to BeautifulSoup
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
    
        # Use a regular expression to match classes that have a similar pattern
        pattern = re.compile(r'catalogueV2Repeater')
    
        # Find all tags that have classes matching the pattern
        matching_tags = soup.find_all(class_='catalogueV2Repeater')
    
        driver.close()
    
        # Append the matching classes to a list
        matching_classes = []
        for tag in matching_tags:
            for class_name in tag['class']:
                if pattern.match(class_name):
                    matching_class = str(tag)
                    matching_classes.append(matching_class)
    
        # Extract the price for each class content
        prices = []
        names = []
        img_links = []
        for class_content in matching_classes:
            soup = BeautifulSoup(class_content, 'html.parser')
            price_tag = soup.find(class_='catalogueV2Local')
            if price_tag:
                price = price_tag.text.strip()
                prices.append(price)
            else:
                prices.append(None)
    
            image = soup.find(class_='CatalogueV2ImageWrapper')
            if image:
                # Use regular expression to extract the src attribute value
                match = re.search(r'src="([^"]+)"', str(image))
                if match:
                    image_link = match.group(1)
                else:
                    image_link = None
    
                # Use regular expression to extract the alt attribute value
                match = re.search(r'alt="([^"]+)"', str(image))
                if match:
                    alt_text = match.group(1)
                else:
                    alt_text = None
    
                names.append(alt_text)
                img_links.append("https://www.kapruka.com" + image_link)
    
        x = "https://www.kapruka.com/images/kapruka_logo_square.png"
        df = pd.DataFrame(
            {'Site': '<img src="' + x + '" width="60" >', 'Product Name': names, 'Price': prices, 'Image Link': img_links})
        os.chdir("/mount/src/edomenico/area1")
        df.to_csv("metar.csv", header=True)
        
        return df.iloc[[0]]
    
    
    def wasi(url):
        # Create Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
    
        # Create the driver with the options
        driver = webdriver.Chrome(options=chrome_options)
    
        # Load the page with Selenium
        driver.get(url)
    
        # Wait up to 10 seconds for the page to load
        # Wait for the page to finish loading all JavaScript
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//body[not(@class='loading')]")))
    
        # Get the HTML of the page and pass it to BeautifulSoup
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
    
        # Use a regular expression to match classes that have a similar pattern
        pattern = re.compile(r'product-inner')
    
        # Find all tags that have classes matching the pattern
        matching_tags = soup.find_all(class_='product-inner')
    
        driver.close()
    
        # Append the matching classes to a list
        matching_classes = []
        for tag in matching_tags:
            for class_name in tag['class']:
                if pattern.match(class_name):
                    matching_class = str(tag)
                    matching_classes.append(matching_class)
    
        # Extract the price for each class content
        prices = []
        names = []
        img_links = []
        for class_content in matching_classes:
            soup = BeautifulSoup(class_content, 'html.parser')
            price_tag = soup.find(class_='woocommerce-Price-amount amount')
            if price_tag:
                # Use regular expression to extract the number
                match = re.search(r'[0-9,]+(?:\.[0-9]+)?', str(price_tag))
                if match:
                    price = match.group()
                    prices.append("Rs " + price)
                else:
                    prices.append(None)
    
            image = soup.find(class_='mf-product-thumbnail')
            if image:
                # Use regular expression to extract the src attribute value
                match = re.search(r'src="([^"]+)"', str(image))
                if match:
                    image_link = match.group(1)
                    print(image_link)
                else:
                    image_link = None
    
                # Use regular expression to extract the alt attribute value
                match = re.search(r'alt="([^"]+)"', str(image))
                if match:
                    alt_text = match.group(1)
                else:
                    alt_text = None
    
                names.append(alt_text)
                img_links.append(image_link)
    
        x = "https://www.wasi.lk/wp-content/uploads/2019/11/wasilk-header-logo-250x66.png"
        df = pd.DataFrame(
            {'Site': '<img src="' + x + '" width="60" >', 'Product Name': names, 'Price': prices, 'Image Link': img_links})
        os.chdir("/mount/src/edomenico/area1")
        df.to_csv("metar.csv", header=True)
        return df.iloc[[0]]
    import streamlit as st
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    from streamlit import components
    
    from sites import *
    
    # Create a dictionary of valid username and password
    VALID_USERNAME_PASSWORD_PAIRS = {
        "admin": "password"
    }
    
    
    # Define a function to create the search page
    def create_search_page():
        # Create a search page with a title and a search bar
        st.title("Product Price Comparison")
        search_term = st.text_input("Enter a product name:")
    
        # Add a button to start scraping the prices
        if st.button("Search"):
            with st.spinner('Fetching data. Please wait...'):
                # Define the URLs for Amazon, Best Buy, and Walmart
                daraz_df = daraz("https://www.daraz.lk/catalog/?q=" + search_term.replace(" ", "+"))
                kapruka_df = kapruka("https://www.kapruka.com/srilanka_online_shopping.jsp?d=" + search_term.replace(" ", "%20"))
                # wasi_df = wasi("https://www.wasi.lk/?s=" + search_term.replace(" ", "+") + "&post_type=product")
    
                # Convert the "Image Link" column to HTML with image tags
                def convert_images():
                    daraz_df["Image Link"] = daraz_df["Image Link"].apply(
                        lambda x: '<img src="' + x + '" width="60" >')
                    kapruka_df["Image Link"] = kapruka_df["Image Link"].apply(
                       lambda x: '<img src="' + x + '" width="60" >')
                    # wasi_df["Image Link"] = wasi_df["Image Link"].apply(
                    #    lambda x: '<img src="' + x + '" width="60" >')
    
                def merge_dataframes():
                    # Merge the dataframes vertically
                    merged_df = pd.concat([daraz_df, kapruka_df], axis=0)
                    return merged_df
    
                convert_images()
                merged_df = merge_dataframes()
    
                html = merged_df.to_html(escape=False)
                # Display the prices in a table
    
                st.markdown(
                    html,
                    unsafe_allow_html=True
                )
    
    
    # Get the session state for the login status
    session_state = st.session_state
    if "logged_in" not in session_state:
        session_state["logged_in"] = False
    
    # Create a sidebar for the login page
    st.sidebar.title("Login")
    
    # Add a text input for the username
    username = st.sidebar.text_input("Username")
    
    # Add a text input for the password
    password = st.sidebar.text_input("Password", type="password")
    
    # Add a login button
    if st.sidebar.button("Login"):
        # Check if the username and password are valid
        if (username in VALID_USERNAME_PASSWORD_PAIRS) and (password == VALID_USERNAME_PASSWORD_PAIRS[username]):
            session_state["logged_in"] = True
            st.sidebar.success("Logged in!")
        else:
            st.sidebar.error("Invalid username or password")
    
    # Only create the search page if the user is logged in
    if session_state["logged_in"]:
        create_search_page()
    else:
        st.warning("Please login to use the search feature")

if __name__ == '__main__':
    #if streamlit._is_running_with_streamlit:
    main()
    #else:
    #    sys.argv = ["streamlit", "run", sys.argv[0]]
    #    #app.run_server(debug=True, port=8881)
      #  sys.exit(stcli.main())
