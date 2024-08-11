import os
import xml.etree.ElementTree as ET
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def parse_xml(xml_file):
    """Parse the XML file and return the root element."""
    try:
        tree = ET.parse(xml_file)
        return tree.getroot()
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        return None
    except FileNotFoundError:
        print(f"File not found: {xml_file}")
        return None


def draw_text(c, text, x, y):
    """Draw text on the PDF canvas."""
    c.drawString(x, y, text)


def xml_to_pdf(xml_file):
    """Convert XML file to PDF."""
    if not xml_file.endswith('.xml'):
        print("Error: The file must be an XML file.")
        return

    pdf_name = os.path.splitext(xml_file)[0]
    pdf_file = f"{pdf_name}.pdf"

    root = parse_xml(xml_file)
    if root is None:
        return

    try:
        c = canvas.Canvas(pdf_file, pagesize=letter)
        _, height = letter
        y_position = height - 40  # Start from the top of the page
        line_height = 12

        for elem in root.iter():
            text = elem.text.strip() if elem.text else 'None'
            draw_text(c, text, 40, y_position)
            y_position -= line_height

            if y_position < 40:  # Move to a new page if out of space
                c.showPage()
                y_position = height - 40

        c.save()
        print(f"PDF created successfully: {pdf_file}")
    except Exception as e:
        print(f"An error occurred while creating the PDF: {e}")

