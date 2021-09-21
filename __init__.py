# https://github.com/thiswillbeyourgithub/i3_search_anki_collection
# Work under GPL v3 license
import urllib.request
import json
import argparse


def ankiconnect(action, **params):
    def request_wrapper(action, **params):
        return {'action': action, 'params': params, 'version': 6}

    requestJson = json.dumps(request_wrapper(action, **params)
                             ).encode('utf-8')
    try:
        response = json.load(urllib.request.urlopen(
                                urllib.request.Request(
                                    'http://localhost:8765',
                                    requestJson)))
    except (ConnectionRefusedError, urllib.error.URLError) as e:
        print(f"{e}: is Anki open and ankiconnect enabled?")
        raise SystemExit()

    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']


parser = argparse.ArgumentParser()
parser.add_argument("--query",
                    nargs=1,
                    metavar="QUERY",
                    dest='query',
                    type=str,
                    required=True,
                    help="Query to ask to anki")
args = parser.parse_args().__dict__

ankiconnect(action="guiBrowse", query=args["query"][0])
