#!/usr/bin/python3
"""A script that fetchs url"""


if __name__ == "__main__":
    from urllib.request import urlopen

    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        the_page = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(the_page)))
        print("\t- type: {}".format(the_page))
        print("\t- utf8 content: {}".format(the_page.decode('utf-8')))
