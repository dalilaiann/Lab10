import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph=nx.Graph()
        self._idMap={}



    def buildGraph(self, year):
        self._graph=nx.Graph()
        self._nodes=DAO.getAllNodes(year)
        self._graph.add_nodes_from(self._nodes)
        for c in self._nodes:
            self._idMap[c.CCode]=c
        self.addEdges(year)
    def addEdges(self,year):
        edges=DAO.getEdges(year, self._idMap)
        for e in edges:
            self._graph.add_edge(e[0],e[1])

    def getSizeCompConnessa(self):
        print(nx.connected_components(self._graph))
        return len(list(nx.connected_components(self._graph)))


    def getNumNodes(self):
        return len(self._graph.nodes)

    def getNumEdges(self):
        return len(self._graph.edges)

    def getDegree(self, node):
        return self._graph.degree(node)

    #ricerca con BFS
    def compConnessa1(self, node):
        tree=nx.bfs_tree(self._graph, node)
        return tree

    #ricerca con DFS
    def compConnessa2(self, node):
        tree = nx.dfs_tree(self._graph, node)
        return tree

