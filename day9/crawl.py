#!/bin/python3

from requests import get
from json import loads

base_url = 'http://10.10.169.100:3000/'
page = ''

while True:
    flag, page = loads(get(base_url + page).text).values()
    if flag == 'end' and page == 'end':
        break
    print(flag, end='', flush=True)
