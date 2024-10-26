import requests

# URL of the Chuck Norris API endpoint
url = 'https://api.chucknorris.io/jokes/random'

# Making a GET request to the API
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    joke = response.json()  # Parse the JSON response
    print(f"Here's a Chuck Norris joke for you: {joke['value']}")
else:
    print('Failed to retrieve a joke')
