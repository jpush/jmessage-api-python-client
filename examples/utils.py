from pprint import pprint

def parser(resp):
    pprint(resp.status_code)
    pprint(resp.headers)
    if resp.text:
        pprint(resp.json())
