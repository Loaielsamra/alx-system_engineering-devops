#!/usr/bin/python3
"""Returns data for a given employee id"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    url = "https://jsonplaceholder.typicode.com/"
    emp_data = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "/todos", params={"userId": sys.argv[1]}).json()
    username = emp_data.get("username")

    with open("{}.json".format(sys.argv[1]), "w") as jfile:
        for t in todos:
            json.dump({sys.argv[1]: [{"task": t.get("title"),
                                      "completed": t.get("completed"),
                                      "username": username}]}, jfile)
