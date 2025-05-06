from database.DAO import DAO
from model.modello import Model

myModel=Model()
myModel.buildGraph(2000)

print(DAO.getEdges(2018, myModel._idMap))
