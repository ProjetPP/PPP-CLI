import sys
from ppp_datamodel.nodes import Resource, Missing, AbstractNode, List, Triple

class DotNode(AbstractNode):
    _type = 'dotnode'
    _possible_attributes = ('name', 'label', 'original')

counter = 0
def make_fresh():
    global counter
    counter += 1
    return 'n' + str(counter)

def predicate(node):
    name = make_fresh()
    if isinstance(node, Resource) and not isinstance(node, DotNode):
        label = node.value
    elif isinstance(node, Missing):
        label = '?'
    elif isinstance(node, List):
        label = 'list'
        for item in node.list:
            print('%s [ label = "%s" ];' % (child.name, child.label))
            print('%s -> %s;' %
                (name, item.value))
    else:
        label = node.type
        for (attrname, attr) in node._attributes.items():
            if attrname in ('type', 'value_type'):
                continue
            if not isinstance(attr, (list, tuple)):
                attr = [attr]
            for child in attr:
                assert isinstance(child, DotNode), child
                if isinstance(node, Triple) and \
                        attrname == 'inverse_predicate' and \
                        isinstance(child.original, List) and \
                        len(child.original.list) == 0:
                    continue
                print('%s [ label = "%s" ];' % (child.name, child.label))
                print('%s -> %s [ label = "%s" ];' %
                    (name, child.name, attrname))
    return DotNode(name, label, node)


def print_tree(node):
    node.traverse(predicate)

def print_responses(responses):
    print('digraph G {\n')
    for response in responses:
        print_tree(response.tree)
    print('}\n')
