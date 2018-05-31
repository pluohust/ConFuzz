
import visgraph.graphcore as vg_graphcore

def vgtest_basic_graph():

    g = vg_graphcore.HierarchicalGraph()

    n1 = g.addNode(ninfo={'name':'woot'})
    n2 = g.addNode(ninfo={'name':'baz'})
    n3 = g.addNode(ninfo={'name':'faz'})
    n4 = g.addNode(ninfo={'name':'foo'})

    g.setNodeInfo(n1,'hi', 'oh hai!')

    g.addEdge(n1,n2)
    g.addEdge(n1,n3)
    g.addEdge(n1,n4)
    g.addEdge(n3,n4)

    print 'ROOTS',g.getRootNodes()
    print g.getNodeInfo(n1, 'hi')

