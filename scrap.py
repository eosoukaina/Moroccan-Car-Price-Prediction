
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import re

def scrape_vehicle_data(vehicle_name_url):
    # Set up Selenium WebDriver (headless mode)
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    links = []
    n_p = 6  # Number of pages to scrape
    
    try:
        for i in range(1, n_p + 1):
            driver.get(f'https://www.avito.ma/fr/maroc/voitures_d_occasion/{vehicle_name_url}--%C3%A0_vendre?o={i}')
            WebDriverWait(driver, 10).until(
                lambda driver: driver.execute_script('return document.readyState') == 'complete'
            )
            html_content = driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')
            table = soup.find_all("a", class_='sc-1jge648-0 jZXrfL')
            for element in table:
                links.append(element.get('href'))
    finally:
        driver.quit()

    # Scrape the individual vehicle details
    dictionaries = []
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        for url in links:
            list1, list2, list3, list4 = [], [], [], []
            pattern = r"^/vi/\d+\.htm$"  # Matches URLs in the format "/vi/number.htm"
            print(url)
            # Check if the URL matches the pattern
            if re.match(pattern, url):
                print(f"Skipping URL: {url}")
                continue 
            driver.get(url)
            WebDriverWait(driver, 10).until(
                lambda driver: driver.execute_script('return document.readyState') == 'complete'
            )
            WebDriverWait(driver, 60).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.sc-1x0vz2r-0.gSLYtF'))
            )
            html_content = driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')
            price = soup.find("div", class_="sc-1g3sn3w-10 leGvyq")
            elements = soup.find_all("span", class_="sc-1x0vz2r-0 gSLYtF")
            elements1 = soup.find_all("span", class_="sc-1x0vz2r-0 jZyObG")

            for element, element1 in zip(elements, elements1):
                list1.append(element1.text)
                list2.append(element.text)

            elem1 = soup.find_all("div", class_="sc-6p5md9-2 bxrxrn")
            element1_1 = []
            for i in elem1:
                element1_1.append(i.find("div", class_="sc-wdregf-0 esVxwv"))
            elem = soup.find_all("span", "sc-1x0vz2r-0 kQHNss")
            for e, f in zip(element1_1, elem):
                list3.append(e.text)
                list4.append(f.text)
            list2.extend(list4)
            list1.extend(list3)
            list1.append('price')
            list2.append(price.text)
            dictionary = dict(zip(list1, list2))
            dictionaries.append(dictionary)
    finally:
        driver.quit()

    df = pd.DataFrame(dictionaries)
    df.to_csv('data.csv', index=False)
    return df  

