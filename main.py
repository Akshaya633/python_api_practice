import requests
url = "https://api.github.com/invalid"
response = requests.get(url)
if response.status_code == 200:
    print("Success!")
elif response.status_code == 404:
    print("Not Found")