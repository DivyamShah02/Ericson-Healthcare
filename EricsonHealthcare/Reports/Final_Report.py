from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf_from_dict_old(data_dict, case_type, case_id):
    """
    Creates a PDF formatted like a Word document using the provided dictionary.
    
    Args:
        data_dict (dict): Dictionary containing the data to be included in the PDF.

    Returns:
        BytesIO: Buffer containing the generated PDF.
    """
    # Create a buffer for the PDF
    buffer = BytesIO()

    # Initialize the PDF document
    pdf = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    # Prepare data for the table
    head_table_data = [[f"{case_type}"]]

    # Create the table
    head_table = Table(head_table_data, colWidths=[500])

    head_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 16),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 11),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    head_table.setStyle(head_style)

    # Add the table to the elements
    elements.append(head_table)


    # Prepare data for the table
    table_data = [["Case Number", f"{case_id}"]]
    for key, value in data_dict.items():
        if key == 'case_id' or key == 'id':
            pass
        else:
            table_data.append([key.replace("_", " ").capitalize(), str(value)])

    # Create the table
    table = Table(table_data, colWidths=[200, 300])

    # Add styles to the table
    style = TableStyle([
        # ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        # ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 0), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    table.setStyle(style)

    # Add the table to the elements
    elements.append(table)

    # Build the PDF
    pdf.build(elements)

    # Reset the buffer position
    buffer.seek(0)

    return buffer

def create_pdf_from_dict(data_dict, case_type, case_id):
    """
    Creates a PDF formatted like a Word document using the provided dictionary.
    
    Args:
        data_dict (dict): Dictionary containing the data to be included in the PDF.
        case_type (str): Type of the case.
        case_id (str): Unique identifier for the case.

    Returns:
        BytesIO: Buffer containing the generated PDF.
    """
    # Create a buffer for the PDF
    buffer = BytesIO()

    # Initialize the PDF document
    pdf = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    # Get predefined styles
    styles = getSampleStyleSheet()

    # Header Table
    head_table_data = [[f"{case_type}"]]
    head_table = Table(head_table_data, colWidths=[500])

    head_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 16),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 11),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    head_table.setStyle(head_style)
    elements.append(head_table)

    # Prepare data for the table
    table_data = [["Case Number", f"{case_id}"]]
    
    for key, value in data_dict.items():
        if key in ['case_id', 'id']:
            continue  # Skip these fields
        
        # Convert long text into a Paragraph to ensure wrapping
        if isinstance(value, str) and len(value) > 50:  # Arbitrary length to check if it's a paragraph
            formatted_value = Paragraph(value, styles["Normal"])
        else:
            formatted_value = str(value)

        table_data.append([key.replace("_", " ").capitalize(), formatted_value])

    # Create the table
    table = Table(table_data, colWidths=[200, 300])

    # Add styles to the table
    style = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 0), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    table.setStyle(style)

    # Add the table to the elements
    elements.append(table)

    # Build the PDF
    pdf.build(elements)

    # Reset the buffer position
    buffer.seek(0)

    return buffer


if __name__ == '__main__':
    # Example Usage
    data = {
        "advance_paid_details": "fsrn323",
        "case_id": 1241,
        "claim_number": "1233423",
        "date_of_admission": "2024-12-12",
        "date_of_intimation": "2023-11-30",
        "date_of_joining": "2023-02-12",
        "date_of_visit": "2024-05-23",
        "evidences_attached_uploaded_in_ft": True,
        "final_recommendation": "sdaerfg",
        "home_visit_if_plan_admission": "rega",
        "hospital_name": "rege",
        "id": 1,
        "ilhc_trigger": "reaghrt",
        "insured_statement": "rgae",
        "ipd_details_finding": "reag",
        "other_findings": "egar",
        "pt_admitted": "2023-06-23",
        "room_category": "deas",
        "treating_dr_statement": "erga"
    }

    pdf_buffer = create_pdf_from_dict(data, "Cashless Claim Report", "1241")

    # Save PDF to file for verification
    with open("output.pdf", "wb") as f:
        f.write(pdf_buffer.read())
