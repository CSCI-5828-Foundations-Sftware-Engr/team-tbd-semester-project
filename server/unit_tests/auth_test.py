import unittest
from configparser import ConfigParser
import os
import requests


path = os.getcwd()
path = path.split(os.sep)
parent_path = os.sep.join(path[:-2])
config_path = parent_path + os.sep + 'app_config.ini'

config = ConfigParser()
config.read(config_path)
api_uri = f"http://{config['SERVER_INFO']['host']}:{config['SERVER_INFO']['port']}/api"
access_token = None


class AuthTestCase(unittest.TestCase):
    def __init__(self, args):
        super().__init__(args)

    def test_1_health(self):
        uri = api_uri + '/health'
        response = requests.get(uri)

        self.assertEqual(200, response.status_code)

    def test_2_protected_before_login(self):
        uri = api_uri + '/protected'
        response = requests.get(uri)

        self.assertEqual(401, response.status_code)

    def test_3_login(self):
        uri = api_uri + '/login'
        body = {
            'email': 'test@tbd.com',
            'password': 'test123'
        }
        response = requests.post(uri, data=body)

        self.assertEqual(200, response.status_code)
        global access_token
        access_token = response.json()['access_token']
        self.assertIsNotNone(access_token)

    def test_4_protected_after_login(self):
        uri = api_uri + '/protected'
        cookies = {
            'access_token_cookie': access_token
        }

        response = requests.get(uri, cookies=cookies)
        self.assertEqual(200, response.status_code)

    def test_5_logout(self):
        uri = api_uri + '/logout'
        cookies = {
            'access_token_cookie': access_token
        }

        response = requests.post(uri, cookies=cookies)
        self.assertEqual(200, response.status_code)

    def test_protected_after_logout(self):
        uri = api_uri + '/protected'
        cookies = {
            'access_token_cookie': access_token
        }

        response = requests.get(uri, cookies=cookies)
        self.assertEqual(401, response.status_code)
