import visgraph.dbcore as vg_dbcore

dbinfo = {
'user':'visgraph',
'password':'ohhai!',
'database':'vg_test',
}

def vgtest_basic_database():
#vg_dbcore.initGraphDb(dbinfo)

    gstore = vg_dbcore.DbGraphStore(dbinfo)

    n1 = gstore.addNode(ninfo={'name':'foo', 'size':20})
    n2 = gstore.addNode(ninfo={'name':'bar', 'size':300})
    n3 = gstore.addNode(ninfo={'name':'baz'})
    n4 = gstore.addNode(ninfo={'name':'faz'})
    n5 = gstore.addNode(ninfo={'name':'yer'})
    n6 = gstore.addNode(ninfo={'name':'mom'})

    gstore.addEdge(n3, n4)
    gstore.addEdge(n4, n5)
    gstore.addEdge(n5, n6)

    print gstore.getNodeInfo(n1, 'name')
    print gstore.getNodeInfo(n1, 'size')
    print gstore.getNodeInfo(n1, 'owoot', 20)

    eid = gstore.addEdge(n1, n2, einfo={'etype':'FooEdge'})
    print eid
    gstore.setEdgeInfo(eid, 'name', 'asdf')
    gstore.setEdgeInfo(eid, 'size', 20)
    print gstore.getEdgeInfo(eid, 'size')

    sg = gstore.buildSubGraph()

    sg.useEdges(size=20)
    #n3 = sg.addNode(ninfo={'name':'Tom Jones'})
    #sg.addEdge(n2, n3, einfo={'etype':'FBFriend'})

    #print sg.getRefsFrom(n2)

    for eid, fromid, toid, einfo in sg.getRefsFrom(n2):
        print 'NAMES: %s -> %s' % (sg.getNodeInfo(fromid, 'name', 'unknown'), sg.getNodeInfo(toid, 'name', 'unknown'))

    sg.expandNode(n3, maxdepth=1)

