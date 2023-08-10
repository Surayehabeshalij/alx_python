#!/usr/bin/python3
"""takes url & email, sends a POST request and displays the response"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    pyload= {
        "email": email
    }
    response = requests.post(url, data=pyload)
    try:
        json = response.json()
        if json:
            get_email = json.get("form")["email"]    
            print("your email is:" get_email)
    except ValueError as e:
        print(e)