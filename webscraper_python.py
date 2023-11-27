import requests
import urllib
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
from course import Course
from assignment import Assignment

# Replace with the actual GradeScope URL
class Account:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.courses = list()
        self.urlLogin = 'https://www.gradescope.com/login'
        self.urlAccount = 'https://www.gradescope.com/account'
    
    def login(self):
        init_resp = web_browser.get(self.urlLogin)
        init_resp_parsed = BeautifulSoup(init_resp.text, "html.parser")
        for form in init_resp_parsed.find_all("form"):
            if form.get("action") == "/login":
                for inp in form.find_all("input"):
                    if inp.get("name") == "authenticity_token":
                        auth_token = inp.get("value")
        login_data = {
                "session[email]": self.email,
                "session[password]": self.password,
                "authenticity_token": auth_token,
            }
        login_resp = web_browser.post(
            self.urlLogin, params=login_data
        )
    
    def find_courses(self, web_browser):
        p=web_browser.get(urlAccount)
        soup = BeautifulSoup(p.text,'html.parser')
        for course_link in soup.find_all('a', class_='courseBox'):
            name = course_link.find('h3').text.strip()
            url = "https://www.gradescope.com/"+course_link.get('href')
            self.courses.append(Course(name, url))

url = 'https://www.gradescope.com/login'
urlAccount = 'https://www.gradescope.com/account'
urlCS = 'https://www.gradescope.com/courses/577903'
email = 'kennym1@rose-hulman.edu'
pwd = 'passw0rd12345'

personal_account = Account("kennym1@rose-hulman.edu", "passw0rd12345")
#soup = BeautifulSoup(p.text, 'html.parser')
with requests.Session() as web_browser:
    personal_account.login()
    personal_account.find_courses(web_browser)
    for course in personal_account.courses:
        course.assignment_list = Assignment.find_assignment(Assignment, course.url, web_browser)    
        for assignment in course.assignment_list:
            #print(assignment.date)
            pass

"""import requests
import urllib
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth

# Replace with the actual GradeScope URL
url = 'https://www.gradescope.com/login'
urlAccount = 'https://www.gradescope.com/account'
urlCS = 'https://www.gradescope.com/courses/577903'
email = 'kennym1@rose-hulman.edu'
pwd = 'passw0rd12345'

cookies = {
    'signed_token': 'clBKbTQxUnFsQnRtZlV3aGM0QmxhbmcrY2lJM3JoOEs0Y2N6dCtkTFRTRT0tLVV1dEQyZ3g5VW8rVVgyK1pjdkkxclE9PQ^%^3D^%^3D--26e7599cb5b42babb6e93d14cea1bcd26ee437a6',
    'remember_me': 'Q21Oa2c4eGZuNkFtUWJOOGZ6aUQzZz09LS1FNE9FaVNMNlFuYXlvbENES0g2S3F3PT0^%^3D--db83354bd8bd6982ce116e9e3ae2c414c81a2995',
    '_gradescope_session': 'cE9RNmVTNm1hRm1Pa09DWFJsa2dmMGtkZ0ptQmtlUTJ4aTY3TWwyUVhyZWw0TGZSYU81a1dnQnFISEJ0UnliTEp6K2RvYzNrRWhLVjRSYzZhSFd4b0U5WE0xMzRxa0huejVkZ1RqVjc3RVJGRVlaUVkrMkpEVFB6NXF1dFVuVUtXa2phTEt1SzJyOTFTZzQ0WERWVGNibk1sckkxNDVReTBrdlNQaC85Z3BiUVBJZFIxbU9iV1RsNENxa3VvUFY2dCtaSzBKSTcrRlJaYXNzbW1ycmI1djN6Vm1YZ1hZZWw2c1FyRTVpMUFOM3hkNUF0NExKaU1tRUxTd25zTHdyN2l3eTcyaTJxQWpRNDNpYU9LZ3hhaE9uOUQ0ek1uSGQrUmVIMWt3WWYvTWJNNGdyS0FYUmgxWS96MEVabm0wN1NHbkVqUDFHTmU0Y1F2bjNrV3FCY2FEWEUydGowT2hJK2h0UzJLT1M4VDBUZXNGWmtGcDhBZ0RuKzhRRHVndUdQbCtTVWVHVDFwaE1YZHh5WUR1VmJEdz09LS1GeGM1eUs5L3pSZDZGV2ZxSnAvcEVBPT0^%^3D--03dbe53c8abf734e897b8b4ddc8579bbc8132f7d',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^116^\\^, ^\\^Not)A;Brand^\\^;v=^\\^24^\\^, ^\\^Google',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '^\\^Windows^\\^',
}

courses = list()

with requests.Session() as s:
    init_resp = s.get("https://www.gradescope.com/")
    init_resp_parsed = BeautifulSoup(init_resp.text, "html.parser")
    # TODO: simplify this loop
    for form in init_resp_parsed.find_all("form"):
        if form.get("action") == "/login":
            for inp in form.find_all("input"):
                if inp.get("name") == "authenticity_token":
                    auth_token = inp.get("value")
    login_data = {
            "session[email]": email,
            "session[password]": pwd,
            "authenticity_token": auth_token,
        }
    login_resp = s.post(
            "https://www.gradescope.com/login", params=login_data
        )
    
    p = s.get(urlAccount)
    soup = BeautifulSoup(p.text, 'html.parser')
    for courseLink in soup.find_all('a', class_='courseBox'):
        courses.append("https://www.gradescope.com/"+courseLink.get('href'))
        
        # Find the course name
        #print(courseLink.find('h3').text.strip()) 
    
    print(courses)

    # Find the assignments

    for c in courses:
        p=s.get(c)
        soup = BeautifulSoup(p.text, 'html.parser')
        for check in soup.find_all('th', class_="table--primaryLink"):
            for name in check.find_all('a'):
                name.text.strip()"""