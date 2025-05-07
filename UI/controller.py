import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._idMap={}

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        self._view._dd.options.clear()
        self._view._dd.value = None
        anno=self._view._txtAnno.value

        #controllo che l'anno non sia vuoto
        if anno=="":
            self._view.create_alert("Inserisci un anno!")
            return

        #controllo che l'anno sia un numero intero
        try:
            annoInt=(int)(anno)
        except ValueError:
            self._view.create_alert("Inserire un numero intero!")
            return

        #controllo che l'anno sia compreso tra il 1816 ed il 2006
        if annoInt<1816 or annoInt>2006:
            self._view.create_alert("Inserisci un numero tra il 1816 e il 2006!")
            return

        #qui il numero va bene
        self._model.buildGraph(annoInt)
        if self._model.getNumEdges==0:
            self._view._txt_result.controls.append(ft.Text("Non esistono confini mondiali con anno minore o uguale di quello inserito"))
            self._view.update_page()
        else:
            self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato"))
            self._view._dd.disabled=False
            self._view._btnRaggiungibili.disabled=False
            self.fillDD()
            self.fillIDMap()
            self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.getSizeCompConnessa()} componenti connesse"))
            self._view._txt_result.controls.append(ft.Text("Di seguito il dettaglio sui nodi:"))
            nodes=self._model._graph.nodes
            for n in nodes:
                self._view._txt_result.controls.append(
                    ft.Text(f"{str(n)}--{self._model.getDegree(n)} vicini."))
            self._view.update_page()

    def handleCalcolaRaggiungibili(self, e):
        state=self._view._dd.value


        if state is None or state=="":
            self._view.create_alert("Inserisci uno stato!")
            return
        else:
            self._view._txt_result.controls.clear()
            raggiungibili=self._model.compConnessa1(self._idMap[state])
            if len(raggiungibili)==0:
                self._view._txt_result.controls.append(
                    ft.Text(f"Non esistono stati raggiungibili da quello indicato."))
                self._view.update_page()
            else:
                self._view._txt_result.controls.append(
                    ft.Text(f"I nodi raggiungibili da {state} sono {len(raggiungibili)}:"))
                for r in raggiungibili:
                    self._view._txt_result.controls.append(ft.Text(f"{str(r)}"))
                self._view.update_page()

    def fillDD(self):
        """Riempe il DD con i nodi del grafo"""
        nodi=self._model._nodes

        for n in nodi:
            self._view._dd.options.append(ft.dropdown.Option(n))
        self._view.update_page()

    def fillIDMap(self):
        values=self._model._nodes
        for v in values:
            self._idMap[v.StateNme]=v
