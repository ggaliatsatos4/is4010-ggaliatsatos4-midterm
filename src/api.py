import requests

def fetch_random_joke():
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['value']
