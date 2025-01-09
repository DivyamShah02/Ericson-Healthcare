import requests
import base64

def decrypt(b64_text):
    # Decode the Base64 string back to bytes, then to text
    return base64.b64decode(b64_text.encode()).decode()

def send_sms(number:int, template_no:int, message_data:dict):
    '''This function sends SMS to the given number using the given template number and message data.
        :param number: The mobile number to which the SMS is to be sent
        :param template_no: 1 for OTP message, 2 for case assignment message
        :param message_data: dictionary containing the data to be inserted in the message
        for template_no 1: {"otp": 111111}
        for template_no 2: {"field_office_name": "John Doe", "case_type": "Medical", "patient_name": "Jane Smith", "mobile_number": "1234567890", "hospital_name": "City Hospital", "contact_number_of_hospital": "0987654321", "TAT_time": "24 hours"}'''
    try:
        url = "http://buzzify.in/V2/http-api-post.php"

        templates = {
            1: "OTP for Login to your eMate is {}. This one time password is valid for 5 minutes. Thanks Ericson TPA",
            2: "Dear {}, {} claim of {}, contact number {} from {}, {} has been assigned to you with TAT of {}. Faithfully, you will get this case closed within TAT. Team EHPL"
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

        data = {
                "apikey": decrypt('ZjVES1piaVJxMmtiVnRTMQ=='),
                "senderid": "ERITPA",
                "number": number,
                "message": message,
                "format": "json",
            }
                    
        response = requests.post(url, json=data)
        print(response.json())
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__=='__main__':
    
    response = send_sms(number=9054413199, template_no=1, message_data={"otp": 111111})

    # response = send_sms(number=9054413199, template_no=2, message_data={
    #                             "field_office_name": "John Doe",
    #                             "case_type": "Medical",
    #                             "patient_name": "Jane Smith",
    #                             "mobile_number": "1234567890",
    #                             "hospital_name": "City Hospital",
    #                             "contact_number_of_hospital": "0987654321",
    #                             "TAT_time": "24 hours"})

    print(response)

    # http://buzzify.in/V2/http-api.php?apikey=f5DKZbiRq2kbVtS1&senderid=ERITPA&number=9054413199&message=OTP for Login to your eMate is 111111. This one time password is valid for 5 minutes. Thanks Ericson TPA&format=json
