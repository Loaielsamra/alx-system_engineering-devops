#!/usr/bin/python3
"""Returns data for a given employee id"""

if __name__ == "__main__":

    import requests
    import sys

    url = "https://jsonplaceholder.typicode.com/"
    emp_data = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "/todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(emp_data.get("name"),
                                                          len(completed),
                                                          len(todos)))

    for t in completed:
        print("\t {}".format(t))
