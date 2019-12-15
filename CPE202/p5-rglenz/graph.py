from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.color=None
        self.visited=False

class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        self.vertlst={}
        f=open(filename,'r')
        lines=f.readlines()
        for line in lines:
            line=line.split()
            self.add_vertex(line[0])
            self.add_vertex(line[1])
            self.add_edge(self.get_vertex(line[0]),self.get_vertex(line[1])) 
        f.close()

    def add_vertex(self,key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        try:
            self.vertlst[key]
        except KeyError:
            self.vertlst[key]=Vertex(key)
        

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        try:
            return self.vertlst[key]
        except Exception:
            return None

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        #adds both vertexs to eachothers adjacent list
        self.vertlst[v1.id].adjacent_to.append(v2)
        self.vertlst[v2.id].adjacent_to.append(v1)

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        return list(self.vertlst.keys())

    def conn_components(self): 
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        keys=self.get_vertices()
        s=Stack(len(self.vertlst))
        visited=[]
        visitedtmp=[]
        for item in keys:
            if not self.vertlst[item].visited:
                s.push(self.vertlst[item])
                while not s.is_empty():
                    vert=s.pop()
                    for item in vert.adjacent_to:
                        if not self.vertlst[item.id].visited:
                            s.push(self.vertlst[item.id])
                            self.vertlst[item.id].visited=True
                            visitedtmp.append(item.id)
                visitedtmp.sort()
                visited.append(visitedtmp)
                visitedtmp=[]
        visited.sort()
        for item in self.vertlst:
            self.vertlst[item].visited=False
        return visited

    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''
        q=Queue(len(self.vertlst))
        keys=self.conn_components()
        for lst in keys:
            for item in lst:        
                if not self.vertlst[item].visited:
                    self.vertlst[item].visited=True
                    self.vertlst[item].color=True
                    q.enqueue(self.vertlst[item])
                while not q.is_empty():
                    vert=q.dequeue()
                    color=vert.color
                    for item in vert.adjacent_to:
                        if item.visited:
                            if item.id == vert.id:
                                continue
                            if item.color is color:
                                return False
                        else:
                            item.color=not color
                            item.visited=True
                            q.enqueue(item)
        return True
        


