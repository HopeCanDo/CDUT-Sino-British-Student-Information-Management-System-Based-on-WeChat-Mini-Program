#!/usr/bin/python3

import requests
import getpass
import json

# base_url = "https://student.zy.cdut.edu.cn"
base_url = "https://student.zycdut.net:888"


def login(username, password):
    print("Attempting to login")
    data = {'username': username, 'password': password}
    r = requests.post(base_url + '/api/rest/user/login.json', data=data)
    if r.ok:
        cookies = dict(r.cookies)
        return cookies
    else:
        print("HTTP %i - %s, Message %s" % (r.status_code, r.reason, r.text))


def main():
    username = input("Username: ")
    password = input("Password: ")
    cookies = login(username, password)
    if not cookies:
        print("Unable to login")
        return

    r = requests.get(base_url + '/sis/api/v1/timetable/cards', cookies=cookies)
    cards = json.loads(r.text)

    print(json.dumps(cards, indent=2))


main()