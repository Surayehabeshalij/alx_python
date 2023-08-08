#!/usr/bin/python3
"""
Python script that fetches an URL with requests package
"""
import requests

url = "https://alu-intranet.hbtn.io/status"

response = requests.get(url)

print("Body response:")
print(f"\t- type: {str(type(response.text))}")
print(f"\t- content: {response.text}")
print(f"\t- length: {len(response.text)}")