from model.country import Country
from model.modello import Model

myModel=Model()
myModel.buildGraph(2006)

print(f"Dimensione della componente connessa con il metodo BFS:"
      f"{len(myModel.compConnessa1(Country("ECU",130,"Ecuador")))}")

print(f"Dimensione della componente connessa con il metodo DFS:"
      f"{len(myModel.compConnessa2(Country("ECU",130,"Ecuador")))}")


print(f"Dimensione della componente connessa con il metodo ricorsivo:"
       f"{len(myModel.compConnessa3(Country("ECU",130,"Ecuador")))}")


print(f"Dimensione della componente connessa con il metodo iterativo:"
       f"{len(myModel.compConnessa4(Country("ECU",130,"Ecuador")))}")


