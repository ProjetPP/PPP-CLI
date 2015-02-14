import sys

import ppp_datamodel
from ppp_datamodel.nodes import *
from ppp_datamodel.communication import *

PRETTYPRINTERS = []

def print_(indent, s, newline=True):
    if newline:
        sys.stdout.write('\n')
        sys.stdout.write('    '*indent)
    else:
        sys.stdout.write(' ')
    sys.stdout.write(s)

def register(cls):
    def decorator(f):
        global PRETTYPRINTERS
        PRETTYPRINTERS.append((cls, f))
        return f
    return decorator

@register(int)
@register(str)
def base(node, indent):
    print_(indent, str(node), False)

@register(list)
def list_(node, indent):
    for item in node:
        print_(indent, '*')
        prettyprint(item, indent)

@register(dict)
def dict(node, indent):
    for (key, value) in sorted(node.items()):
        print_(indent, '%s:' % key)
        prettyprint(value, indent)

@register(Request)
def request(node, indent):
    print_(indent, 'Request:')
    prettyprint(node.tree, indent)
    sys.stdout.write('\n')

@register(Response)
def response(node, indent):
    print_(indent, 'Response (%s):' % (' -> '.join(x.module for x in node.trace)))
    prettyprint(node.tree, indent)
    sys.stdout.write('\n')

@register(Sentence)
def sentence(node, indent):
    print_(indent, node.value, False)

@register(Triple)
def triple(node, indent):
    print_(indent, 'Subject:')
    prettyprint(node.subject, indent)
    print_(indent, 'Predicate:')
    prettyprint(node.predicate, indent)
    print_(indent, 'Object:')
    prettyprint(node.object, indent)

@register(List)
def list(node, indent):
    print_(indent, 'List:')
    for item in node.list:
        print_(indent, '*')
        prettyprint(item, indent)

@register(Intersection)
def list(node, indent):
    print_(indent, 'Intersection:')
    for item in node.list:
        print_(indent, '*')
        prettyprint(item, indent)

@register(Union)
def list(node, indent):
    print_(indent, 'Union:')
    for item in node.list:
        print_(indent, '*')
        prettyprint(item, indent)

@register(Missing)
def missing(node, indent):
    print_(indent, '?', False)

@register(Resource)
def resource(node, indent):
    prettyprint(node.value, indent)

@register(MathLatexResource)
def mathlatexresource(node, indent):
    print_(indent, 'value:')
    prettyprint(node.value, indent)
    try:
        latex = node.latex
    except ppp_datamodel.exceptions.AttributeNotProvided:
        pass
    else:
        print_(indent, 'latex:')
        prettyprint(node.latex, indent)

@register(JsonldResource)
def jsonldresource(node, indent):
    print_(indent, node.value)
    prettyprint(node.graph, indent)

@register(Sort)
def sort(node, indent):
    print_(indent, 'Sort (%s):' % node.predicate)
    prettyprint(node.list, indent)

@register(Last)
def last(node, indent):
    print_(indent, 'Last:')
    prettyprint(node.list, indent)

@register(First)
def first(node, indent):
    print_(indent, 'First:')
    prettyprint(node.list, indent)

PRETTYPRINTERS.reverse()
def prettyprint(node, indent=-1):
    for (cls, prettyprinter) in PRETTYPRINTERS:
        if isinstance(node, cls):
            return prettyprinter(node, indent+1)
    print_(indent+1, repr(node))
    sys.stdout.write('\n')
