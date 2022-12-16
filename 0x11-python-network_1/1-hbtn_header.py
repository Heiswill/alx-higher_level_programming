#!/usr/bin/python3
"""A script that takes a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the
header of the reponse.
"""


if __name__ == "__main__":
    from urllib.request import urlopen
    from sys import argv

    with urlopen(argv[1]) as response:
        content = response.read()
        print(response.headers.get("X-Request-Id"))
