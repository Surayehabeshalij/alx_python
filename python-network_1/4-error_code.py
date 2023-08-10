import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    # Example: status code 401
    response_200 = requests.get(url)
    print('Correct output - case: request {} with status code {}'.format(url, response_200.status_code))
    response_401 = requests.get(url)
    print('Correct output - case: request {} with status code {}'.format(url, response_401.status_code))

    # Example: status code 500
    response_500 = requests.get(url)
    print('Correct output - case: request {} with status code {}'.format(url, response_500.status_code))