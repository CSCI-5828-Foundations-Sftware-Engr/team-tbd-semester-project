import unittest
import os
from configparser import ConfigParser
import requests


class MyTestCase(unittest.TestCase):
    def __init__(self):
        super().__init__()

        path = os.getcwd()
        path = path.split(os.sep)
        parent_path = os.sep.join(path[:-1])
        config_path = parent_path + os.sep + 'app_config.ini'
        config = ConfigParser()
        config.read(config_path)

        self.api_uri = f"http://{config['SERVER_INFO']['host']}:{config['SERVER_INFO']['port']}/api"

        self.token = self.login()

    def login(self):
        uri = self.api_uri + '/login'
        body = {
            'email': 'test@tbd.com',
            'password': 'test123'
        }
        response = requests.post(uri, data=body)
        return response.json()['access_token']

    def test_1_get_reminders(self):
        uri = self.api_uri + '/reminders'

        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

        response = requests.get(uri, headers=headers)

        reminders = dict(response.json()['reminders'])
        self.assertEqual(len(reminders), 0)

    def test_2_add_reminder(self):
        uri = self.api_uri + '/reminders'

        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
        body = {
            "title": "Test",
            "description": "Test",
            "start_time": "2080/01/01 00:00",
            "end_time": "2080/01/02 00:00",
            "reminder_type": 1,
            "progress": 1
        }

        response = requests.post(uri, headers=headers, data=body)

        self.assertEqual(response.status_code, 200)

    def test_3_get_reminders(self):
        uri = self.api_uri + '/reminders'

        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

        response = requests.get(uri, headers=headers)

        reminders = dict(response.json()['reminders'])
        self.assertEqual(len(reminders), 1)

if __name__ == '__main__':
    unittest.main()

