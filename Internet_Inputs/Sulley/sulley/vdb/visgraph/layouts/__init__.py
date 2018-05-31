'''
A package for each of the different layout managers.
'''


# Some helper utils...
def exit_pos(ninfo):
    x,y = ninfo.get('position')
    xsize, ysize = ninfo.get('size', (0,0))
    return (x + xsize/2, y + ysize)

def entry_pos(ninfo):
    x,y = ninfo.get('position')
    xsize, ysize = ninfo.get('size', (0,0))
    return (x + xsize/2, y)

def center_pos(ninfo):
    x,y = ninfo.get('position')
    xsize, ysize = ninfo.get('size', (0,0))
    return (x + (xsize/2), y + (ysize/2))

class GraphLayout:

    def __init__(self, graph):
        self.graph = graph

    def layoutGraph(self):
        '''
        Layout the graph nodes and edges
        '''
        raise Exception('%s must implement layoutGraph()!' % self.__class__.__name__)

    def getLayoutSize(self):
        raise Exception('%s must implement getLayoutSize()!' % self.__class__.__name__)

    def renderGraph(self, rend):
        '''
        Render the graph to the given renderer.
        '''
        rend.setNodeSizes(self.graph)
        self.layoutGraph()

        width, height = self.getLayoutSize()
        rend.beginRender(width, height)

        # Render each of the nodes (except ghost nodes...)
        for nid,ninfo in self.graph.getNodes():
            if ninfo.get('ghost'):
                continue
            xpos, ypos = ninfo.get('position')
            rend.renderNode(nid, ninfo, xpos, ypos)

        # Render the edges
        for eid, fromid, toid, einfo in self.graph.getEdges():
            points = einfo.get('edge_points')
            if points != None:
                rend.renderEdge(eid, einfo, points)

        rend.endRender()

