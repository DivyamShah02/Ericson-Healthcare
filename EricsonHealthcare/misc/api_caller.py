import requests

base_url = 'http://127.0.0.1:8000/'
# base_url = 'https://ericsontpa.pythonanywhere.com/'

def create_user():
    url = base_url + 'user/user/'

    data = {
        'name': 'Admin',
        'password':'Admin@123',
        'contact_number': '1234567890',
        'email': 'admin@admin.com',
        'city': 'Ahmedabad',
        'state': 'Gujarat',
        'role': 'admin',
    }

    response = requests.post(url, data=data)

    return response

def get_user():
    url = base_url + 'user/'

    data = {
    'user_id':'IO7169754192'
    }

    response = requests.get(url, params=data)

    return response

def login_user():
    url = base_url + 'user/login-api/'

    email = 'divyamshah1234@gmail.com'
    password = 'divyam'

    data = {
        'email':email,
        'password':password,
    }

    response = requests.post(url, data=data)

    return response

def get_visit_details_by_case_id_and_investigator_id():
    url = "http://localhost:8000/visit/fetch_visits/"

    payload = {
        'case_id': '123',
        'investigator_id': 'INV123'
    }
    files=[

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)

def add_answer_of_visit():
    url = base_url + 'question/visit-question-api/'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "visit_id": 9079258494,
        "answers": {
                5: "final tetingav",
                0: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam, voluptas? Nulla maiores, numquam eos, minus veniam inventore assumenda deserunt quis amet magnam quam, ipsum eveniet. Veniam nostrum vel quod commodi!"
            }
        }

    response = requests.post(url, json=data, headers=headers)

    return response

def save_device_id():
    url = base_url + 'user/save-device-id-api/'

    data = {
        'user_id':'CO3070257634',
        'device_id':'1234567890'
    }

    response = requests.post(url, data=data)
    return response

if __name__ == '__main__':
    # print('Hello')
    # create_user_respone = create_user()
    # print(create_user_respone.text)

    sace_device_id_respone = save_device_id()
    print(sace_device_id_respone.text)

    # get_user_respone = get_user()
    # print(get_user_respone.text)

    # login_user_respone = login_user()
    # print(login_user_respone.text)

    # get_visit_details_by_case_id_and_investigator_id()

    # add_answer_of_visit_respone = add_answer_of_visit()
    # print(add_answer_of_visit_respone.text)

