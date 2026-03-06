from controlador import SimulacionController

if __name__ == "__main__":

    controller = SimulacionController()
    procesos = [25, 50, 100, 150, 200]

    # --- ESCENARIOS BASE ---
    controller.correr_simulacion(
        procesos,
        titulo="Intervalo 10",
        nombre_archivo="intervalo_10",
        ram_capacity=100,
        cpu_speed=3,
        cpu_count=1,
        interval=10
    )

    controller.correr_simulacion(
        procesos,
        titulo="Intervalo 5",
        nombre_archivo="intervalo_5",
        ram_capacity=100,
        cpu_speed=3,
        cpu_count=1,
        interval=5
    )

    controller.correr_simulacion(
        procesos,
        titulo="Intervalo 1",
        nombre_archivo="intervalo_1",
        ram_capacity=100,
        cpu_speed=3,
        cpu_count=1,
        interval=1
    )

    # --- ESTRATEGIAS (usando intervalo 1 porque es el más crítico) ---

    # Más RAM
    controller.correr_simulacion(
        procesos,
        titulo="RAM 200 - Intervalo 1",
        nombre_archivo="ram_200",
        ram_capacity=200,
        cpu_speed=3,
        cpu_count=1,
        interval=1
    )

    # CPU más rápido
    controller.correr_simulacion(
        procesos,
        titulo="CPU 6 instrucciones - Intervalo 1",
        nombre_archivo="cpu_rapido",
        ram_capacity=100,
        cpu_speed=6,
        cpu_count=1,
        interval=1
    )

    # 2 CPUs
    controller.correr_simulacion(
        procesos,
        titulo="2 CPUs - Intervalo 1",
        nombre_archivo="dos_cpus",
        ram_capacity=100,
        cpu_speed=3,
        cpu_count=2,
        interval=1
    )

    print("\nSimulación completa. Revisa la carpeta 'graficas'.")