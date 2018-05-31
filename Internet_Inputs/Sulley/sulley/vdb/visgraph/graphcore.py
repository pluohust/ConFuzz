'''
Graphcore contains all the base graph manipulation objects.
'''
import itertools

from exc import *
import visgraph.pathcore as vg_pathcore

class Graph:

    '''
    The base Graph object implements a simple nodes and edges graph.

    Nodes -
        Nodes consist of a dicionary of properties about that node and
        a unique id which identifies the node in the current graph.  From
        API perspective a node is a tuple of (nodeid, nodeprops).

    Edges -
        Edges are directional sets of a from node-id and to node-id and
        a piece of arbitrary edge information.
    '''

    def __init__(self):
        self.wipeGraph()
        self.nidgen = itertools.count()
        self.eidgen = itertools.count()
        self.metadata = {}

    def setMeta(self, mprop, mval):
        self.metadata[mprop] = mval

    def getMeta(self, mprop, default=None):
        return self.metadata.get(mprop, default)

    def wipeGraph(self):
        '''
        Re-initialize the graph structures and start clean again.
        '''
        self.edges = {}
        self.nodes = {}
        self.edge_by_from = {}
        self.edge_by_to = {}

    def getEdges(self):
        '''
        Get the list of edges in the graph.  Edges are defined
        as (eid, fromid, toid, einfo) tuples.

        Example: for eid, fromid, toid, einfo in g.getEdges():
        '''
        return list(self.edges.values())

    def getEdge(self, eid):
        '''
        Get the (eid, fromid, toid, einfo) tuple for the specified
        edge.

        Example: e = g.getEdge(eid)
        '''
        return self.edges.get(eid, None)

    def getEdgeInfo(self, eid, key, default=None):
        '''
        Get a property about an edge specified by from/to id.

        Example: n = g.getEdgeInfo(eid 'name', 'Default Name')
        '''
        edge = self.edges.get(eid)
        if edge == None:
            raise EdgeNonExistant(eid)
        eid, fromid, toid, einfo = edge
        return einfo.get(key, default)

    def setEdgeInfo(self, eid, key, value):
        '''
        Set a key/value pair about a given edge by
        it's from/to id.

        Example: g.setEdgeInfo(eid, 'awesomeness', 99)
        '''
        edge = self.edges.get(eid)
        if edge == None:
            raise EdgeNonExistant(eid)
        eid, fromid, toid, einfo = edge
        einfo[key] = value

    def setNodeInfo(self, nodeid, key, value):
        '''
        Store a piece of information (by key:value) about a given node.

        Example g.setNodeInfo(nid, 'Description', 'My Node Is Awesome!')
        '''
        d = self.nodes.get(nodeid)
        if d == None:
            raise NodeNonExistant(nodeid)
        d[key] = value

    def getNodeInfo(self, nodeid, key, default=None):
        '''
        Retrieve a piece of information about a given node by key.

        Example: descr = g.getNodeInfo(nid, 'Description', default='OH HAI')
        '''
        d = self.nodes.get(nodeid)
        if d == None:
            raise NodeNonExistant(nodeid)
        return d.get(key, default)

    def getNodeProps(self, nodeid):
        '''
        Get the node info dictionary for the specified node.

        Example: d = g.getNodeProps(nid)
        '''
        return self.nodes.get(nodeid)

    def addNode(self, nodeid=None, ninfo=None, **kwargs):
        '''
        Add a Node object to the graph.  Returns the nodeid.

        Example: nid = g.addNode()
                 g.addNode('woot', {'height':20, 'width':20})

        NOTE: If nodeid is unspecified, it is considered an 'anonymous'
              node and will have an ID automagically assigned.
        '''
        if nodeid == None:
            nodeid = self.nidgen.next()
        p = self.nodes.get(nodeid)
        if p != None:
            raise DuplicateNode(nodeid)
        if ninfo == None:
            ninfo = {}
        ninfo.update(kwargs)
        ninfo['nodeid'] = nodeid
        self.nodes[nodeid] = ninfo
        return nodeid

    def delNode(self, nid):
        for eid,nfrom,nto,einfo in self.getRefsFrom(nid):
            self.delEdge(eid)
        for eid,nfrom,nto,einfo in self.getRefsTo(nid):
            self.delEdge(eid)
        return self.nodes.pop(nid)

    def getNode(self, nodeid):
        '''
        Return the dictionary of properties for the specified node id.
        '''
        return self.nodes.get(nodeid)

    def getNodes(self):
        '''
        Return a list of (nodeid, nodeinfo) tuples.
        '''
        return self.nodes.items()

    def hasNode(self, nodeid):
        '''
        Check if a given node is present within the graph.

        Example: if g.hasNode('yermom'): print 'woot'
        '''
        return self.getNode(nodeid) != None

    def addEdge(self, fromid, toid, eid=None, einfo=None, **kwargs):
        '''
        Add an edge to the graph.  Edges are directional.

        Example: g.addEdge(node_1, node_2, einfo={'name':'Woot Edge'})
        '''
        if einfo == None:
            einfo = {}
        einfo.update(kwargs)
        if eid == None:
            eid = self.eidgen.next()
        e = (eid, fromid, toid, einfo)
        self.edges[eid] = e
        xlist = self.edge_by_from.get(fromid)
        if xlist == None:
            xlist = []
            self.edge_by_from[fromid] = xlist
        ylist = self.edge_by_to.get(toid)
        if ylist == None:
            ylist = []
            self.edge_by_to[toid] = ylist
        xlist.append(e)
        ylist.append(e)
        return eid

    def delEdge(self, eid):
        '''
        Delete an edge from the graph (by eid).

        Example: g.delEdge(eid)
        '''
        e = self.edges.pop(eid, None)
        if e == None:
            raise EdgeNonExistant(eid)

        eid, fromid, toid, einfo = e
        self.edge_by_to[toid] = [ x for x in self.edge_by_to[toid] if x[0] != eid ]
        self.edge_by_from[fromid] = [ x for x in self.edge_by_from[fromid] if x[0] != eid ]

    def getRefsFrom(self, nodeid):
        '''
        Return a list of edges which originate with us.

        Example: for eid, fromid, toid, einfo in g.getRefsFrom(id)
        '''
        ret = self.edge_by_from.get(nodeid)
        if ret == None:
            ret = []
        return ret

    def getRefsTo(self, nodeid):
        '''
        Return a list of edges which terminate at us.

        Example: for eid, fromid, toid, einfo in g.getRefsFrom(id)
        '''
        ret = self.edge_by_to.get(nodeid)
        if ret == None:
            ret = []
        return ret

    def getClusterGraphs(self):
        '''
        Return a list of the subgraph clusters (as graphs) contained
        within this graph.  A subgraph "cluster" is defined as a
        group of interconnected nodes.  This can be used to split
        out grouped subgraphs from within a larger graph.
        '''
        ret = []
        nodes = self.getNodes()
        done = {}
        while len(nodes):
            nid, ninfo = nodes.pop()
            if done.get(nid):
                continue

            # Generate the cluster subgraph
            todo = [ (nid, ninfo), ]
            g = Graph()

            while len(todo):
                gnid, gninfo = todo.pop()

                done[gnid] = True

                if not g.getNode(gnid):
                    g.addNode(nodeid=gnid, ninfo=gninfo)

                for eid,n1,n2,einfo in self.getRefsFrom(gnid):

                    if not g.getNode(n2):
                        n2info = self.getNodeProps(n2)
                        g.addNode(nodeid=n2, ninfo=n2info)
                        todo.append((n2, n2info))

                    if not g.getEdge(eid):
                        g.addEdge(n1, n2, eid=eid, einfo=einfo)

                for eid,n1,n2,einfo in self.getRefsTo(gnid):

                    if not g.getNode(n1):
                        n1info = self.getNodeProps(n1)
                        g.addNode(nodeid=n1, ninfo=n1info)
                        todo.append((n1, n1info))

                    if not g.getEdge(eid):
                        g.addEdge(n1, n2, eid=eid, einfo=einfo)

            ret.append(g)

        return ret
                

    def pathSearchOne(self, *args, **kwargs):
        for p in self.pathSearch(*args, **kwargs):
            return p

    def pathSearch(self, fromid, toid=None, edgecb=None, tocb=None):
        '''
        Search for the shortest path from one node to another
        with the option to filter based on edges using
        edgecb.  edgecb should be a function:

        def myedgecb(graph, eid, fromid, toid, depth)

        which returns True if it's OK to traverse this node
        in the search.

        Additionally, toid may be None and the caller may specify
        tocb with a function such as:

        def mytocb(graph, nid)

        which must return True on finding the target node

        Returns a list of edge ids...
        '''

        if toid == None and tocb == None:
            raise Exception('You must use either toid or tocb!')

        root = vg_pathcore.newPathNode(nid=fromid, eid=None)

        todo = [(root, 0),]

        # FIXME make this a deque so it can be FIFO
        while len(todo):

            pnode,depth = todo.pop() # popleft()
            ppnode, pkids, pprops = pnode

            nid = pprops.get('nid')
            for edge in self.getRefsFrom(nid):

                eid, srcid, dstid, einfo = edge

                if vg_pathcore.isPathLoop(pnode, 'nid', dstid):
                    continue

                # Check if the callback is present and likes us...
                if edgecb != None:
                    if not edgecb(self, edge, depth):
                        continue

                # Are we the match?
                match = False
                if dstid == toid:
                    match = True

                if tocb and tocb(self, dstid):
                    match = True

                if match:

                    m = vg_pathcore.newPathNode(pnode, nid=dstid, eid=eid)
                    path = vg_pathcore.getPathToNode(m)

                    ret = []
                    for ppnode, pkids, pprops in path:
                        eid = pprops.get('eid')
                        if eid != None:
                            ret.append(eid)

                    yield ret

                # Add the next set of choices to evaluate.
                branch = vg_pathcore.newPathNode(pnode, nid=dstid, eid=eid)
                todo.append((branch, depth+1))

        #return []

    def pathSearchFrom(self, fromid, nodecb, edgecb=None):
        '''
        Search from the specified node (breadth first) until you
        find a node where nodecb(graph, nid) == True.  See
        pathSearchFromTo for docs on edgecb...
        '''

class HierarchicalGraph(Graph):
    '''
    An extension to the graph base which implements the idea of hierarchy
    keeping a weight relationship based on the added edges.
    Edges are directional from X to y.

    You must add nodes with the property "rootnode" to know where the
    hierarchy begins!
    '''
    def __init__(self):
        Graph.__init__(self)

    def getRootNodes(self):
        '''
        Get all the node id's in this graph which are weight 0 (meaning
        they have no parents)...
        '''
        ret = []
        for nid, nprops in self.nodes.items():
            if nprops.get('rootnode', False):
                ret.append(nid)
        return ret

    def getNodeWeights(self):
        '''
        Calculate the node weights for the given nodes in the hierarchical
        graph based on the added "rootnode" nodes.  This will return a dict
        of { nodeid: weight, } key-pairs.

        # NOTE: This will also set the 'weight' property on the nodes
        '''
        weights = {}
        todo = [ (r, []) for r in self.getRootNodes() ]
        while len(todo):

            nid, path = todo.pop()

            cweight = weights.get(nid, 0)
            weights[nid] = max(cweight, len(path))

            path.append(nid)

            for eid, fromid, toid, einfo in self.getRefsFrom(nid):
                if weights.get(toid, -1) >= len(path):
                    continue
                if toid not in path:
                    todo.append((toid, list(path)))

        for nid,weight in weights.items():
            self.setNodeInfo(nid, 'weight', weight)

        return weights

    def getPathCount(self):
        '''
        Return the number of non-looped paths through this function.

        NOTE: one small issue, "spiral" functions where the leaf node
              has a lower weight than a block which must reach it by a
              looped path will be a few total paths short...
        '''

        nodes = []
        leafnodes = []

        # We must put all nodes into weight order
        weights = self.getNodeWeights()

        # Initialize all nodes to 0
        # (and populate leafnodes list...)
        for nid,ninfo in self.getNodes():

            nodes.append( (weights.get(nid), nid, ninfo) )
            ninfo['pathcount'] = 0

            # No refs from means leaf
            xrfcnt = len(self.getRefsFrom(nid))
            if xrfcnt == 0:
                leafnodes.append((nid,ninfo))

            # Seed root nodes with a path
            if ninfo.get('rootnode'):
                ninfo['pathcount'] = 1
                continue

        # Lets make the list of nodes *ordered* by weight
        nodes.sort()

        # Now tally ho!
        for weight, nid, ninfo in nodes:

            # Here's the magic... In *hierarchy order* each node
            # gets the sum of the paths of his parents.
            for eid, fromid, toid, einfo in self.getRefsFrom(nid):
                props = self.getNodeProps(toid)
                # A reference to somebody at our weight (probably self)
                # is considered a loop...
                if weights[toid] == weight:
                    continue
                props['pathcount'] += ninfo['pathcount']

        totcount = 0
        for nid,ninfo in leafnodes:
            totcount += ninfo['pathcount']

        return totcount

