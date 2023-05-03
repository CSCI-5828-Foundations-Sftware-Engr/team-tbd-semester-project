import unittest
import os
from configparser import ConfigParser
import requests


path = os.getcwd()
path = path.split(os.sep)
parent_path = os.sep.join(path[:-2])
config_path = parent_path + os.sep + 'app_config.ini'
config = ConfigParser()
config.read(config_path)

api_uri = f"http://{config['SERVER_INFO']['host']}:{config['SERVER_INFO']['port']}/api"
access_token = None


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # login
        uri = api_uri + '/login'
        body = {
            'email': 'test@tbd.com',
            'password': 'test123'
        }
        response = requests.post(uri, data=body)
        global access_token
        access_token = response.json()['access_token']

    def test_add_reminder(self):
        # get user reminders first
        uri = api_uri + '/reminders/get_reminders'
        cookies = {
            'access_token_cookie': access_token
        }
        response = requests.get(uri, cookies=cookies)
        self.assertEqual(200, response.status_code)
        reminders = response.json()
        init_len = len(reminders)

        # add a reminder
        uri = api_uri + '/reminders/add_event'
        cookies = {
            'access_token_cookie': access_token
        }
        body = {
            "title": "Test",
            "description": "Test",
            "start_time": "2080/01/01 00:00",
            "end_time": "2080/01/02 00:00",
            "reminder_type": 1,
            "progress": 1
        }
        response = requests.post(uri, cookies=cookies, data=body)
        self.assertEqual(response.status_code, 200)

        # get user reminders again
        uri = api_uri + '/reminders/get_reminders'
        cookies = {
            'access_token_cookie': access_token
        }
        response = requests.get(uri, cookies=cookies)
        self.assertEqual(200, response.status_code)
        reminders = response.json()
        final_len = len(reminders)

        self.assertEqual(init_len + 1, final_len)

    def test_delete_reminders(self):
        # add a reminder
        uri = api_uri + '/reminders/add_event'
        cookies = {
            'access_token_cookie': access_token
        }
        body = {
            "title": "Test",
            "description": "Test",
            "start_time": "2080/01/01 00:00",
            "end_time": "2080/01/02 00:00",
            "reminder_type": 1,
            "progress": 1
        }
        response = requests.post(uri, cookies=cookies, data=body)
        self.assertEqual(response.status_code, 200)

        # get user reminders
        uri = api_uri + '/reminders/get_reminders'
        cookies = {
            'access_token_cookie': access_token
        }
        response = requests.get(uri, cookies=cookies)
        self.assertEqual(200, response.status_code)
        reminders = response.json()
        init_len = len(reminders)

        # delete added event
        reminder_id = reminders[-1]['reminder_id']
        uri = api_uri + '/reminders/delete_event'
        cookies = {
            'access_token_cookie': access_token
        }
        body = {
            "reminder_id": reminder_id
        }
        response = requests.post(uri, cookies=cookies, data=body)
        self.assertEqual(200, response.status_code)

        # get user reminders again
        uri = api_uri + '/reminders/get_reminders'
        cookies = {
            'access_token_cookie': access_token
        }
        response = requests.get(uri, cookies=cookies)
        self.assertEqual(200, response.status_code)
        reminders = response.json()
        final_len = len(reminders)

        self.assertEqual(init_len - 1, final_len)

    def tearDown(self):
        # logout
        uri = api_uri + '/logout'
        cookies = {
            'access_token_cookie': access_token
        }

        response = requests.post(uri, cookies=cookies)
        self.assertEqual(200, response.status_code)
