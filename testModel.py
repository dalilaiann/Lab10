from model.country import Country
from model.modello import Model

myModel=Model()
myModel.buildGraph(2000)

print(len(myModel.compConnessa2(Country("AFG",700,"Afghanistan"))))

