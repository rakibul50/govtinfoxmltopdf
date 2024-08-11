import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def download_file(url, folder):
    """Downloads a file from a URL and saves it to a specified folder."""
    if not os.path.exists(folder):
        os.makedirs(folder)

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        file_name = os.path.join(folder, url.split('/')[-1])
        with open(file_name, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        print(f"Downloaded {file_name}")
        return file_name
    else:
        raise Exception(f"Failed to download file from {url}, status code: {response.status_code}")


def scrape_and_download_latest_xml(base_url, page_url, folder):
    """Scrapes the webpage for the latest XML file and downloads it."""
    # Setup Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Load the webpage
        driver.get(page_url)
        time.sleep(5)  # Wait for the page to load completely

        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        links = soup.find_all('a', href=True)

        # Extract XML file links
        xml_files = [urljoin(base_url, link['href']) for link in links if link['href'].lower().endswith('.xml')]

        # Handle the case where no XML files are found
        if not xml_files:
            raise Exception("No XML files found on the page.")

        # Download the latest XML file
        latest_file_url = sorted(xml_files)[-1]
        xml_file_path = download_file(url=latest_file_url, folder=folder)
        return xml_file_path

    finally:
        # Ensure that the browser is closed even if an error occurs
        driver.quit()

