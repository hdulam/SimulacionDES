# SimulacionDES
Hoja de trabajo 5 para Algoritmos y Estructuras de Datos | Universidad del Valle de Guatemala

Nombre: Hector Duarte
Curso: Algoritmos y Estructura de Datos

Descripción:

En este proyecto se realizó una simulación de un sistema operativo de tiempo compartido utilizando la librería SimPy en Python.

La simulación modela cómo los procesos:

    Llegan al sistema.

    Solicitan memoria RAM.

    Esperan turno para usar el CPU.

    Ejecutan instrucciones.

    Pueden realizar operaciones de I/O.

    Finalmente terminan y liberan memoria.

El objetivo es analizar el tiempo promedio que un proceso permanece en el sistema bajo diferentes condiciones de carga.


Estructura del proyecto

    modelo.py → Contiene la lógica de la simulación.

    vista.py → Muestra los resultados y genera las gráficas.

    controlador.py → Conecta el modelo con la vista.

    main.py → Archivo principal que ejecuta los experimentos.

    venv/ → Entorno virtual con las dependencias.

    graficas/ → Carpeta donde se guardan las gráficas generadas.

    Experimentos realizados

Se probaron las siguientes cantidades de procesos:

    25
    50
    100
    150
    200

Con diferentes intervalos de llegada:


    Intervalo 10

    Intervalo 5

    Intervalo 1

También se probaron mejoras al sistema:

    Aumentar la RAM a 200.

    Hacer el CPU más rápido (6 instrucciones por unidad de tiempo).

    Usar 2 CPUs.

    Las gráficas se generan automáticamente y se guardan en la carpeta graficas.

    Cómo ejecutar el programa

    Activar el entorno virtual incluido en la carpeta:

    source venv/bin/activate

Ejecutar el programa:

    python3 main.py

    IMPORTANTE: REVISAR QUE VENV ESTÉ BIEN CONFIGURADO PARA LA MÁQUINA DONDE SE VA A CORRER, SE CREO USANDO UNA MAC M1 AUNQUE NO SE SI IMPACTA. SINO CREAR OTRO VENV E INSTALAR MATPLOTLIB Y SIMPY AHI

El programa mostrará los resultados en consola y generará las gráficas automáticamente. Las gráficas estan en la carpeta graficas.

Conclusión

Al aumentar la cantidad de procesos, el tiempo promedio en el sistema aumenta bastante. Esto indica que el sistema comienza a saturarse cuando hay demasiados procesos compitiendo por los recursos.

También se observa que la desviación estándar aumenta, lo que significa que algunos procesos tardan mucho más que otros en completarse cuando el sistema está bajo alta carga.