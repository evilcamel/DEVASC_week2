#!/usr/local/bin/python3

import json
import requests

url = 'https://api.chucknorris.io/jokes/random'


def get_chuck_joke(api):
    """
    Get a random joke from the Chuck Norris API and return the serial JSON
    :param api:
    :return:serial JSON
    """
    response = requests.get(api)  # TASK 1 - use requests to get a joke.
    return response.content  # TASK 2 - return the response in JSON format


if __name__ == '__main__':
    joke = json.loads(get_chuck_joke(url))  # TASK 3 - correct the json statement
    print(joke['value'])  # TASK 4 - print just a joke without any superfluous symbols
