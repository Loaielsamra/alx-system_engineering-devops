#!/usr/bin/python3
"""exports employee data to CSV"""

if __name__ == "__main__":

    import csv
    import requests
    import sys

    url = "https://jsonplaceholder.typicode.com/"
    resp = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    username = resp.get("username")

    with open("{}.csv".format(sys.argv[1]), "w", newline="") as cfile:
        pen = csv.writer(cfile, quoting=csv.QUOTE_ALL)

        for t in todos:
            pen.writerow([sys.argv[1], username,
                         t.get("completed"), t.get("title")])
