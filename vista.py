import matplotlib.pyplot as plt
import os

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