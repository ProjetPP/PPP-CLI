#!/usr/bin/env python3
import uuid
import argparse

from . import main

parser = argparse.ArgumentParser(
        description='Command-line tool for debugging PPP modules.')
parser.add_argument('--api', type=str,
        default='http://core.frontend.askplatyp.us/',
        help='The URL of the API to query. Defaults to the core '
             'of askplatyp.us.')
parser.add_argument('--id', type=str,
        default=str(uuid.uuid4()),
        help='The request id. Defaults to a random UUID4.')
parser.add_argument('--language', type=str,
        default='en',
        help='The language code to use. Defaults to \'en\'')
parser.add_argument('--parse', action='store_true',
        default=False,
        help='Determines whether the request should be parsed according '
             'to the datamodel notation.')
parser.add_argument('request')

args = parser.parse_args()
main.main(args.api, args.id, args.language, args.parse, args.request)
