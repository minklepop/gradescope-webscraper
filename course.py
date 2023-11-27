import requests
import urllib
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
from assignment import Assignment

class Course:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.assignment_list = list()

    def get_name(self):
        return self.name
