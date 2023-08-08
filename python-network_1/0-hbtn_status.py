import requests

url = "https://alu-intranet.hbtn.io/status"

response = requests.get(url)

expected_response = {
    "type": "<class 'str'>",
    "content": "OK",
    "length": 2
}

actual_response = {
    "type": str(type(response.text)),
    "content": response.text,
    "length": len(response.text)
}

print("[Expected]")
print("Body response:")
print(f"\t- type: {expected_response['type']}")
print(f"\t- content: {expected_response['content']}")
print(f"\t- length: {expected_response['length']}\n")

print("[Got]")
print("Body response:")
print(f"\t- type: {actual_response['type']}")
print(f"\t- content: {actual_response['content']}")
print(f"\t- length: {actual_response['length']}")