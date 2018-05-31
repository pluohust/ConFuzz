'''
A module for path related unit tests.
'''

import visgraph.pathcore as vg_pcore
import visgraph.graphcore as vg_gcore

def buildPathGraph():
    g = vg_gcore.Graph()
    n0 = g.addNode()
    n1 = g.addNode()
    n2 = g.addNode()
    n3 = g.addNode()
    n4 = g.addNode()

    g.addEdge(n0, n1)
    g.addEdge(n0, n2)
    g.addEdge(n1, n3)
    g.addEdge(n1, n4)

    return g,n0,n4

def vgtest_basic_path_search():
    g,begin_node,end_node = buildPathGraph()
    res = g.pathSearchFromTo(begin_node, end_node)
    for eid in res:
        eid, fromid, toid, einfo = g.getEdge(eid)
        print '%d --(%d)--> %d'  % (fromid, eid, toid)

def test_callback_false(graph, edge, depth):
    print 'DENY EDGE: %s' % repr(edge)

def test_callback_true(graph, edge, depth):
    print 'ALLOW EDGE: %s' % repr(edge)
    return True

def vgtest_path_callback_false_test():
    g,begin_node,end_node = buildPathGraph()
    res = g.pathSearchFromTo(begin_node, end_node, edgecb=test_callback_false)
    if len(res) != 0:
        raise Exception('Should Not Have Answers!')

def vgtest_path_callback_true_test():
    g,begin_node,end_node = buildPathGraph()
    res = g.pathSearchFromTo(begin_node, end_node, edgecb=test_callback_true)
    if len(res) == 0:
        raise Exception('Should Have Answers!')
    print repr(res)
