import yagmail
import base64

def decrypt(b64_text):
    # Decode the Base64 string back to bytes, then to text
    return base64.b64decode(b64_text.encode()).decode()


def send_email(recipient_email, template_no, message_data):
    '''This function sends an email to the recipient email address.
        :param recipient_email: Recipient's email address
        :param template_no: Template number for the email
        :param message_data: Data for the email template
        for template_no 1: {"otp": 111111}
        for template_no 2: {"field_office_name": "John Doe", "case_type": "Medical", "patient_name": "Jane Smith", "mobile_number": "1234567890", "hospital_name": "City Hospital", "contact_number_of_hospital": "0987654321", "TAT_time": "24 hours"}
    '''
    try:
        sender_email = "autoresponse@ericsonhealthcare.com"
        sender_password = decrypt('QUVyaWNzb25oZWFsdGhjYXJlQDEyMw==')
        
        formatted_sender = f"Ericson Healthcare <{sender_email}>"
        
        templates = {
            1: "OTP for Login to your eMate is {}. This one time password is valid for 5 minutes. Thanks Ericson TPA",
            2: "Dear {}, \n\n{} claim of {}, contact number {} from {}, {} has been assigned to you with TAT of {}. Faithfully, you will get this case closed within TAT. \n\nTeam EHPL"
        }

        subjects = {
            1: "OTP for eMate Login",
            2: "New Claim Assignment"
        }

        if template_no not in templates:
            print("Invalid template number")
            return False
        
        message = ''
        if template_no == 1:
            message = templates[template_no].format(message_data.get("otp"))
        
        elif template_no == 2:
            message = templates[template_no].format(
            message_data.get("field_office_name"),
            message_data.get("case_type"),
            message_data.get("patient_name"),
            message_data.get("mobile_number"),
            message_data.get("hospital_name"),
            message_data.get("contact_number_of_hospital"),
            message_data.get("TAT_time")
            )

        yag = yagmail.SMTP(user=sender_email, password=sender_password, host="smtp.rediffmailpro.com", port=465)
        yag.send(to=recipient_email, subject=subjects[template_no], contents=message)
        yag.close()

        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # send_email(recipient_email="divyamshah1234@gmail.com", template_no=1, message_data={"otp": 111111})
    send_email(recipient_email="divyamshah1234@gmail.com", template_no=2, message_data={"field_office_name": "John Doe", "case_type": "Medical", "patient_name": "Jane Smith", "mobile_number": "1234567890", "hospital_name": "City Hospital", "contact_number_of_hospital": "0987654321", "TAT_time": "24 hours"})
