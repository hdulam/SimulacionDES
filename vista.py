import matplotlib.pyplot as plt
import os

"""
Aca se definen las funciones para mostrar los resultados y graficar. Es simple matplotlib, pero se usa un formato para mostrar los resultados en la grafica usando los valores de la lista.
"""

class SimulacionView:

    def mostrar_resultados(self, resultados):
        for procesos, datos in resultados.items():
            print(f"Procesos: {procesos}")
            print(f"Promedio: {datos[0]}")
            print(f"Desviación: {datos[1]}")
            print("------")

    def graficar(self, resultados, titulo, nombre_archivo):
        procesos = list(resultados.keys())
        promedios = [datos[0] for datos in resultados.values()]

        # Crear carpeta si no existe
        os.makedirs("graficas", exist_ok=True)

        plt.figure()
        plt.plot(procesos, promedios)
        plt.xlabel("Número de procesos")
        plt.ylabel("Tiempo promedio")
        plt.title(titulo)
        plt.savefig(f"graficas/{nombre_archivo}.png")
        plt.close()