'''
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
    def addNeighbor(self,nbr,weight):
        self.connectedTo[nbr] = weight
    def __str__(self):
        return str(self.id) + 'connectTo :' \
                + str([x.id for x in self.connectedTo])
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
'''
#*****************************************************************
'''
#not used
class Graph:
    def __init__(self):
        self.verList = {}
        self.numVertices = 0
    def addVertex(self,key):
        self.numVertices += 1#num +1
        newVertex = Vertex(key)#new node
        self.verList[key] = newVertex#add node to graph
        return newVertex#tell which new node has been added
    def getVertex(self,n):
        if n in self.verList:
            return self.verList[n]
        else:
            return None
    def __contains__(self,n):
        return n in self.verList
    def addEdge(self,f,t,cost = 0):
        if f not in self.verList:
            nv = self.addVertex(f)
        if t not in self.verList:
            nv = self.addVertex(t)
        self.verList[f].addNeighbor(self.verList[t],cost)
    def getVertices(self):
        return self.verList.keys()
    def __iter__(self):
        return iter(self.verList.values())
'''
#*******************************************************************************
'''
class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0
        
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex
    
    def getVertex(self,n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertices
    
    def addEdge(self,f,t,cost=0):
            if f not in self.vertices:
                self.addVertex(f)
            if t not in self.vertices:
                self.addVertex(t)
            self.vertices[f].addNeighbor(self.vertices[t],cost)
    
    def getVertices(self):
        return list(self.vertices.keys())
        
    def __iter__(self):
        return iter(self.vertices.values())
'''
#******************************************************************************
'''
g = Graph()
for i in range(6):
    g.addVertex(i)
print(g.verList)

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)


for v in g:
    for w in v.getConnections():
        print("(%s,%s)"%(v.getId(),w.getId()))
'''
#*****************************************

from pythonds.graphs import Graph
def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')

    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]#all 4 position is dealt for every word
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g



#g = buildGraph('fourletterwords.txt')
#print(len(g.getVertices()))


#*******************************************************
'''
from pythonds.graphs import Graph,Vertex
from pythonds.basic.queue import Queue
def bfs(g,start):
    start.setDistance(0)
    start.setPred(None)#pre node
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
            currentVert.setColor('black')
    
def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())

wordgraph = buildGraph('fourletterwords.txt')
bfs(wordgraph,wordgraph.getVertex('FOOL'))
traverse(wordgraph.getVertex('SAGE'))
'''
#****************************************************
def genLegalMoves(x,y,bdSize):
    newMoves = []
    moveOffsets = [(-1,-2),(-1,2),(1,-2),(1,2),(-2,-1),(-2,1),(2,-1),(2,1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX,bdSize) and legalCoord(newY,bdSize):
            newMoves.append((newX,newY))
    return newMoves

def legalCoord(x,bdSize):
    if x >= 0 and x <bdSize:
        return True
    else:
        return False

def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row,col,bdSize)
            newPositions = genLegalMoves(row,col,bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0],e[1],bdSize)
                ktGraph.addEdge(nodeId,nid)
    return ktGraph

def posToNodeId(row,col,bdSize):
    return row*bdSize+col

def knightTour(n,path,u,limit):
    u.setColor('gray')#u:current node
    path.apend(u)#stack
    if n < limit:#limit:ending condition
        nbrList = list(u.getConnections())#list current node's nbr
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n+1,path,nbrList[i],limit)#DFS
            i += 1#next nbr
        if not done:#end this brach and not done
            path.pop()
            u.setColor('white')
        else:
            done = True
        return done

def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c += 1
            resList.append((c,v))
    resList.sort(key = lambda x:x[0])
    return [y[1] for y in resList]#y[1] is nbr node
#******************************************************
