import requests


def getCatImage() -> str:
    """
    Returns a random cat image from the internet.
    """
    response = requests.get("https://api.thecatapi.com/v1/images/search").json()
    return response[0]["url"]
