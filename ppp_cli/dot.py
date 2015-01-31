import sys
from ppp_datamodel.nodes import Resource, Missing, AbstractNode

class DotName(AbstractNode):
    _type = 'dotname'
    _possible_attributes = ('name',)

counter = 0
def make_fresh():
    global counter
    counter += 1
    return 'n' + str(counter)

def predicate(node):
    name = make_fresh()
    if isinstance(node, Resource):
        print('%s [ label = "%s" ];' % (name, node.value))
    elif isinstance(node, Missing):
        print('%s [ label = "?" ];' % (name,))
    else:
        print('%s [ label = "%s" ];' % (name, node.type))
        for (attrname, childdot) in node._attributes.items():
            if attrname in ('type', 'value_type'):
                continue
            assert isinstance(childdot, DotName), childdot
            print('%s -> %s [ label = "%s" ];' %
                (name, childdot.name, attrname))
    return DotName(name)


def print_tree(node):
    node.traverse(predicate)

def print_responses(responses):
    print('digraph G {\n')
    for response in responses:
        print_tree(response.tree)
    print('}\n')
