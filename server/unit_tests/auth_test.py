import unittest
from configparser import ConfigParser
import os
import requests
from time import sleep


path = os.getcwd()
path = path.split(os.sep)
parent_path = os.sep.join(path[:-1])
config_path = parent_path + os.sep + 'app_config.ini'

config = ConfigParser()
config.read(config_path)
api_uri = f"http://{config['SERVER_INFO']['host']}:{config['SERVER_INFO']['port']}/api"

token = None


class AuthTestCase(unittest.TestCase):
    def test_1_health(self):
        uri = api_uri + '/health'
        response = requests.get(uri)

        self.assertEqual(response.status_code, 200)

    def test_2_protected_before_login(self):
        uri = api_uri + '/protected'
        response = requests.get(uri)

        self.assertEqual(response.status_code, 401)

    def test_3_login(self):
        uri = api_uri + '/login'
        body = {
            'email': 'test@tbd.com',
            'password': 'test123'
        }
        response = requests.post(uri, data=body)

        self.assertEqual(response.status_code, 200)
        global token
        token = response.json()['access_token']
        self.assertIsNotNone(token)

    def test_4_protected_after_login(self):
        uri = api_uri + '/protected'
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

        response = requests.get(uri, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_5_logout(self):
        uri = api_uri + '/logout'
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

        response = requests.delete(uri, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_protected_after_logout(self):
        uri = api_uri + '/protected'
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

        response = requests.get(uri, headers=headers)
        self.assertEqual(response.status_code, 401)
