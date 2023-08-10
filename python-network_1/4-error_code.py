import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code == 200:
        print('Correct output - case: request {} with status code 200'.format(url))
    else:
        print('Correct output - case: request {} with status code {}'.format(url, response.status_code))