import requests

base_url = 'http://127.0.0.1:8000/'

def create_user():
    url = base_url + 'user/'

    data = {
        'name': 'Divyam Shah',
        'password':'divyam',
        'contact_number': '9054413199',
        'email': 'divyamshah1234@gmail.com',
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
    url = base_url + 'login-api/'

    email = 'divyamshah1234@gmail.com'
    password = 'divyam'

    data = {
        'email':email,
        'password':password,
    }

    response = requests.post(url, data=data)

    return response


if __name__ == '__main__':
    # create_user_respone = create_user()
    # print(create_user_respone.text)

    get_user_respone = get_user()
    print(get_user_respone.text)

    # login_user_respone = login_user()
    # print(login_user_respone.text)

