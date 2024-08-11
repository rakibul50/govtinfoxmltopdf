# gov_info XML to PDF Converter

## Description

This project fetches the latest XML file from a dynamically changing URL and converts it into a PDF.

## Project Structure

- `src/`: Contains the source code.
  - `fetch_latest_xml.py`: Fetches the latest XML file.
  - `xml_to_pdf.py`: Converts XML content to a PDF.
  - `main.py`: Main script to run the project.

## Requirements

- Python 3.x
- `requests`, `bs4`, `reportlab`, `webdriver_manager`, `selenium`


### 1. Navigate to Your Project Directory

Open a terminal and navigate to the directory where your project is located:
```bash
   cd /path/to/your/project
```  
### 2. Create the Virtual Environment
Create a virtual environment using the venv module. Replace myenv with your preferred environment name:
```bash 
python3 -m venv myenv
```
### 3. Activate the Virtual Environment
Activate the virtual environment so that any Python packages you install will be isolated to this environment.

On macOS/Linux:

```bash
 source myenv/bin/activate
```

On Windows:

```bash 
myenv\Scripts\activate
```

### 4. Deactivate the Virtual Environment

When you're done working, you can deactivate the virtual environment by running:
```bash 
deactivate
```

## Usages

1. Install dependencies:
   ```bash
   pip3 install -r requirements.txt

2. Run the project:
   ```bash
   python3 src/main.py

Note: xml file created under files directory and pdf files also stored in same directory.