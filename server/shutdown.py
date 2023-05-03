import os
from configparser import ConfigParser
import requests

directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_file = directory + os.sep + 'app_config.ini'

config = ConfigParser()
config.read(config_file)

uri = f"http://{config['SERVER_INFO']['host']}:{config['SERVER_INFO']['port']}/api/shutdown"
try:
    requests.post(uri)
except:
    pass
