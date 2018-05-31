'''
Paths are enumerated threads through a particular graph.  They
are implemented as an optimized hierarchical graph using python
primitives to save memory and processing time...

Each "leaf" node may be tracked back for it's entire path by
tracking back to parents.
'''

def newPathNode(parent=None, **kwargs):
    '''
    Create a new path node with the given properties
    '''
    ret = (parent, [], kwargs)
    if parent != None:
        parent[1].append(ret)
    return ret

def getNodeParent(pnode):
    return pnode[0]

def delPathNode(pnode):
    '''
    Prune (remove) this node from the parent...
    '''
    p = getNodeParent(pnode)
    if p != None:
        p[1].remove(pnode)

def getNodeIndex(pnode):
    p = getNodeParent(pnode)
    if p != None:
        return p[1].index(pnode)
    return None

def getNodeKids(pnode):
    '''
    Return the list of children nodes for the specified
    node.

    Example: for knode in getNodeKids(pnode):
    '''
    return pnode[1]

def getRootNode(pnode):
    '''
    Get the root node for the path tree which contains
    pnode.

    Example: root = getRootNode(branchnode)
    '''
    ret = pnode
    while pnode[0] != None:
        pnode = pnode[0]
    return pnode

def getLeafNodes(pnode):
    '''
    Get all the leaf nodes for the path tree which contains
    the pnode.

    Example: for leaf in getLeafNodes(root):
    '''
    root = getRootNode(pnode)
    ret = []
    todo = [root, ]
    while len(todo):
        x = todo.pop()
        if len(x[1]) == 0:
            ret.append(x)
            continue
        for n in x[1]:
            todo.append(n)
    return ret

def getPathToNode(pnode):
    '''
    Return a list of the path nodes which lead from the
    root node to the specified path node.
    '''
    path = []
    while pnode != None:
        path.append(pnode)
        pnode = pnode[0]

    path.reverse()
    return path

def getAllPaths(pnode):
    '''
    Get a list of lists which has each path flattened out.

    Example: for path in getAllPaths(pnode):
                 print 'Found A Path:'
                 for node in path:
                    doStuff()
    '''
    leafs = getLeafNodes(pnode)
    paths = []
    for leaf in leafs:
        path = getPathToNode(leaf)
        paths.append(path)
    return paths

def getNodeProp(pnode, key, default=None):
    '''
    Get a property from the given node, returning
    default in the case that the specified property is
    not present.

    Example:
        name = getNodeProp(pnode, 'name', 'Unknown')
    '''
    return pnode[2].get(key, default)

def getPathProp(pnode, key, default=None):
    '''
    Retrieve the specified property by walking the give
    path backward until the property is found.  Returns
    the specified default if the specified key is not found
    as a property of any node in the given path.

    Example:
        name = getPathProp(pnode, 'name', 'Unknown')
    '''
    parent = pnode
    while parent != None:
        parent, kids, props = parent
        x = props.get(key)
        if x != None:
            return x
    return default

def setNodeProp(pnode, key, value):
    '''
    Set a spcified property on the given path node.

    Example:
        setNodeProp(pnode, 'name', 'woot')
    '''
    pnode[2][key] = value

def isPathLoop(pnode, key, value):
    '''
    Assuming you have some identifier property (such as graph node id)
    being set on the path nodes, you may use this API to determine if
    the current path has a node with the specified key/value property.

    Example:
        if searchPathLoop(pnode, 'nid', 5):
            continue
    '''
    parent = pnode
    while parent != None:
        parent, kids, props = parent
        if props.get(key) == value:
            return True
    return False

def getPathLoopCount(pnode, key, value):
    '''
    Assuming that the key is unique, walk the current path and see how
    many times "key" has the specified value.  This will be how many instances
    of a loop have been encountered.
    '''
    count = 0
    parent = pnode
    while parent != None:
        parent, kids, props = parent
        if props.get(key) == value:
            count += 1
    return count

