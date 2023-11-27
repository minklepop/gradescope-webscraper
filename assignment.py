import requests
import urllib
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth

class Assignment:
    def __init__(self, name, date, time):
        self.name = name
        self.date = date
        self.time = time

    def find_assignment(self, url, web_browser):
        names = list()
        dates = list()
        times = list()
        date_and_times = list()
        assignment_list = list()
        assignment=web_browser.get(url)
        assignment_check=BeautifulSoup(assignment.text, 'html.parser')
        """for name in assignment_check.find_all('th', class_="table--primaryLink"):
            #print(name)
            if (name.has_attr('aria-label'))==False:
                names.append(name.text.strip())
        for time in assignment_check.find_all('time', class_="submissionTimeChart--dueDate"):
            print(time)
            if time.has_attr('datetime') and time['aria-label'][0:3]=="Due":
                date_and_times.append(time['datetime'][0:len(time['datetime'])-6])"""
        
        for name in assignment_check.find('tbody'):
            for NAME in name.find_all('th', class_="table--primaryLink"):
                print(name.text.strip())
                NAME.append(NAME.text.strip())
            for time in name.find_all('time', class_="submissionTimeChart--dueDate"):
                if time.has_attr('datetime') and time['aria-label'][0:3]=="Due":
                    date_and_times.append(time['datetime'][0:len(time['datetime'])-6])

        for data in date_and_times:
            dates.append(data[0:9])
            times.append(data[11:len(data)-3])
        print(len(names),len(dates),len(times))
        #for i in range(0,len(times)):
        #    assignment_list.append(Assignment(names[i],dates[i],times[i]))
        #print(assignment_list[0].name,assignment_list[0].date,assignment_list[0].time)
        return assignment_list