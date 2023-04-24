import requests

url = 'https://freemidi.org/getter-27603'
response = requests.get(url)

with open('myfile.txt', 'wb') as f:
    f.write(response.content)