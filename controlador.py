from modelo import SimulacionModel
from vista import SimulacionView

class SimulacionController:

    def __init__(self):
        self.view = SimulacionView()

    def correr_simulacion(self, procesos_lista, titulo, nombre_archivo, **parametros):  
        model = SimulacionModel(**parametros)
        resultados = {}

        for p in procesos_lista:
            promedio, desviacion = model.ejecutar(p)
            resultados[p] = (promedio, desviacion)

        self.view.mostrar_resultados(resultados)
        self.view.graficar(resultados, titulo, nombre_archivo)

        return resultados