#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import requests

ur1 = "https://alx-intranet.hbtn.io/status"
response= requests.get(ur1)
if response.status_code == 200:
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: ", type(response.text))
    print("\t- content: " , response.text)
else:
    print("Error:" ,response.status_code )