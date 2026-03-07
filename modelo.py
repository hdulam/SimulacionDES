import simpy
import random
import statistics

"""
Aca se simulan los diferentes métodos para correr la simulación.
"""

class SimulacionModel:
    
    #inicializar
    def __init__(self, ram_capacity=100, cpu_speed=3, cpu_count=1, interval=10, seed=42):
        self.ram_capacity = ram_capacity
        self.cpu_speed = cpu_speed
        self.cpu_count = cpu_count
        self.interval = interval
        self.seed = seed

    #proceso individual
    def proceso(self, env, RAM, CPU, tiempos):
        llegada = env.now
        
        memoria = random.randint(1, 10)
        instrucciones = random.randint(1, 10)

        yield RAM.get(memoria)

        while instrucciones > 0:
            with CPU.request() as req:
                yield req
                yield env.timeout(1)

                ejecutadas = min(self.cpu_speed, instrucciones)
                instrucciones -= ejecutadas

            if instrucciones <= 0:
                break

            decision = random.randint(1, 21)
            if decision == 1:
                yield env.timeout(1)

        yield RAM.put(memoria)

        tiempos.append(env.now - llegada)

    def generador(self, env, total_procesos, RAM, CPU, tiempos):
        for _ in range(total_procesos):
            env.process(self.proceso(env, RAM, CPU, tiempos))
            yield env.timeout(random.expovariate(1.0 / self.interval))

    #aca se hace que se ejecute la simulación y se calculen los resultados
    def ejecutar(self, total_procesos):
        random.seed(self.seed)

        env = simpy.Environment()
        RAM = simpy.Container(env, init=self.ram_capacity, capacity=self.ram_capacity)
        CPU = simpy.Resource(env, capacity=self.cpu_count)

        tiempos = []

        env.process(self.generador(env, total_procesos, RAM, CPU, tiempos))
        env.run()

        promedio = statistics.mean(tiempos)
        desviacion = statistics.stdev(tiempos)

        return promedio, desviacion