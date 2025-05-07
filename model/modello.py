import copy

import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph=nx.Graph()
        self._idMap={}
        self._solConnessa=[]

    def buildGraph(self, year):
        """Costruisce il grafo"""
        self._graph=nx.Graph()
        self._nodes=DAO.getAllNodes(year)
        self._graph.add_nodes_from(self._nodes)
        for c in self._nodes:
            self._idMap[c.CCode]=c
        self.addEdges(year)

    def addEdges(self,year):
        """Aggiunge gli archi al grafo"""
        edges=DAO.getEdges(year, self._idMap)
        for e in edges:
            self._graph.add_edge(e[0],e[1])

    def getSizeCompConnessa(self):
        """Calcola il numero di componenti connesse nel grafo"""
        print(nx.connected_components(self._graph))
        return len(list(nx.connected_components(self._graph)))

    def getNumNodes(self):
        return len(self._graph.nodes)

    def getNumEdges(self):
        return len(self._graph.edges)

    def getDegree(self, node):
        """Restituisce il grado del nodo passato come input"""
        return self._graph.degree(node)

    #ricerca con BFS
    def compConnessa1(self, node):
        """Calcola componente connessa associato al nodo di input con algoritmo BFS"""
        tree=list(nx.bfs_tree(self._graph, node))
        return tree[1:]

    #ricerca con DFS
    def compConnessa2(self, node):
        """Calcola componente connessa associato al nodo di input con algoritmo DFS"""
        tree = list(nx.dfs_tree(self._graph, node))
        return tree[1:]

    #ricerca con algoritmo ricorsivo
    def compConnessa3(self, nodo):
        """Calcola componente connessa associato al nodo di input con algoritmo ricorsivo"""
        self._solConnessa = []
        parziale=[nodo]
        rimanenti=self.calcola_successori(parziale,nodo)
        self._ricorsione(parziale, rimanenti)
        return self._solConnessa[1:]


    def _ricorsione(self, parziale, rimanenti):
        """Calcola componente connessa"""
        if len(rimanenti)==0:
            if len(parziale)>len(self._solConnessa):
                self._solConnessa=copy.deepcopy(parziale)
        else:
            for i in range(len(rimanenti)):
                 if rimanenti[i] not in parziale:
                    parziale.append(rimanenti[i])
                    nuovi_rimanenti=self.calcola_successori(parziale, rimanenti[i])
                    self._ricorsione(parziale, nuovi_rimanenti)
                    parziale.pop()


    def calcola_successori(self, parziale,nodo):
        """Calcola i nodi successori di un nodo"""
        successori=list(self._graph.neighbors(nodo))
        rimanenti=[]
        for n in successori:
            if n not in parziale:
                rimanenti.append(n)
        return rimanenti


    #ricerca con metodo iterativo
    def compConnessa4(self, nodo):
        """Calcola componente connessa associato al nodo di input con algoritmo iterativo"""
        nodi_visitati=[]
        nodi_davisitare=[nodo]

        while len(nodi_davisitare)!=0:
            for nodo in nodi_davisitare:
                if nodo not in nodi_visitati:
                    nodi_visitati.append(nodo)
                    nodi_davisitare.extend(list(self._graph.neighbors(nodo)))
                nodi_davisitare.remove(nodo)

        return nodi_visitati[1:]


