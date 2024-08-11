import logging
from datetime import datetime
from fetch_latest_xml import scrape_and_download_latest_xml
from xml_to_pdf import xml_to_pdf

# Constants
BASE_URL = 'https://www.govinfo.gov'
DOWNLOAD_FOLDER = 'files'

def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Main function to fetch the latest XML file from a dynamically changing URL,
    convert it to PDF.
    """
    setup_logging()

    try:
        current_year = datetime.now().year
        page_url = f"{BASE_URL}/bulkdata/CFR/{current_year}/title-12/"
        
        logging.info(f"Fetching the latest XML file from {page_url}")
        xml_file = scrape_and_download_latest_xml(BASE_URL, page_url, DOWNLOAD_FOLDER)

        if xml_file:
            logging.info(f"Converting XML file {xml_file} to PDF")
            xml_to_pdf(xml_file)
        else:
            logging.warning("No XML file was downloaded. Exiting.")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
