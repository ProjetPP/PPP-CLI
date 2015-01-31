import requests

from ppp_datamodel import Sentence, Request, Response
from ppp_datamodel_notation_parser.parser import parse_triples

from .dot import print_responses
from .prettyprint import prettyprint

def main(api, id_, language, parse, query, dot):
    if parse:
        query = parse_triples(query)
    else:
        query = Sentence(query)
    request = Request(id_, language, query, {}, [])
    data = requests.post(api, data=request.as_json()).json()
    responses = list(map(Response.from_dict, data))
    if dot:
        print_responses(responses)
    else:
        for response in responses:
            prettyprint(response)
