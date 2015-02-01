import sys
from ppp_datamodel.nodes import Resource, Missing, AbstractNode, List

class DotName(Resource):
    _value_type = 'dotname'

counter = 0
def make_fresh():
    global counter
    counter += 1
    return 'n' + str(counter)

def predicate(node):
    name = make_fresh()
    if isinstance(node, Resource) and not isinstance(node, DotName):
        print('%s [ label = "%s" ];' % (name, node.value))
    elif isinstance(node, Missing):
        print('%s [ label = "?" ];' % (name,))
        print('fooooooo')
        print('%s [ label = "list" ];' % (name,))
        for item in node.list:
            print('%s -> %s;' %
                (name, item.value))
    else:
        print('%s [ label = "%s" ];' % (name, node.type))
        for (attrname, attr) in node._attributes.items():
            if attrname in ('type', 'value_type'):
                continue
            if not isinstance(attr, (list, tuple)):
                attr = [attr]
            for child in attr:
                assert isinstance(child, DotName), child
                print('%s -> %s [ label = "%s" ];' %
                    (name, child.value, attrname))
    return DotName(name)


def print_tree(node):
    node.traverse(predicate)

def print_responses(responses):
    print('digraph G {\n')
    for response in responses:
        print_tree(response.tree)
    print('}\n')
