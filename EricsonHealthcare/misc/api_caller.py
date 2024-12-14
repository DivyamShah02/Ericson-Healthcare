import requests

base_url = 'http://127.0.0.1:8000/'

def create_user():
    url = base_url + 'user/user/'

    data = {
        'name': 'Divyam Investigator',
        'password':'divyam',
        'contact_number': '9054413199',
        'email': 'investigator@gmail.com',
        'city': 'Ahmedabad',
        'state': 'Gujarat',
        'role': 'investigator',
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
    url = base_url + 'login-api/'

    email = 'admin@admin.com'
    password = 'admin'

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


if __name__ == '__main__':
    create_user_respone = create_user()
    print(create_user_respone.text)

    # get_user_respone = get_user()
    # print(get_user_respone.text)

    # login_user_respone = login_user()
    # print(login_user_respone.text)

    # get_visit_details_by_case_id_and_investigator_id()

