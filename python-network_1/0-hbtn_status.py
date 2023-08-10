#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import requests

ur1 = "https://intranet.hbtn.io/status"
response= requests.get(ur1)
if response.status_code == 200:
    print("Body response:")
    print("\t- type: ", type(response.text))
    print("\t- content: " , response.text)
else:
    print("Error:" ,response.status_code )