import nbformat as nbf

nb = nbf.v4.new_notebook()
cells = []

cells.append(nbf.v4.new_markdown_cell(
"""# Evidencia 3 - Primer analisis de datos con Python

En este notebook hago un primer ejercicio de analisis de datos usando Python, siguiendo el ejemplo del taller de Software Carpentry sobre datos de inflamacion de pacientes.

El archivo inflammation-01.csv tiene el numero de episodios de inflamacion por dia, para 60 pacientes, durante 40 dias. Cada fila es un paciente y cada columna es un dia."""
))

cells.append(nbf.v4.new_markdown_cell("## 1. Carga de datos"))

cells.append(nbf.v4.new_code_cell(
"""import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('inflammation-01.csv', delimiter=',')
data"""
))

cells.append(nbf.v4.new_markdown_cell("## 2. Exploracion"))

cells.append(nbf.v4.new_code_cell(
"""print("Forma de los datos (pacientes, dias):", data.shape)
print("Numero de pacientes:", data.shape[0])
print("Numero de dias registrados:", data.shape[1])
print("Valor mas alto en todo el dataset:", data.max())
print("Valor mas bajo en todo el dataset:", data.min())"""
))

cells.append(nbf.v4.new_markdown_cell("## 3. Analisis"))

cells.append(nbf.v4.new_markdown_cell(
"""Voy a hacer dos operaciones sobre los datos:

1. El promedio de inflamacion por dia, contando a todos los pacientes.
2. El promedio de inflamacion por paciente, contando todos sus dias."""
))

cells.append(nbf.v4.new_code_cell(
"""promedio_por_dia = np.mean(data, axis=0)
print("Promedio de inflamacion en los primeros 10 dias:")
print(promedio_por_dia[:10])"""
))

cells.append(nbf.v4.new_code_cell(
"""promedio_por_paciente = np.mean(data, axis=1)
print("Promedio de inflamacion de los primeros 5 pacientes:")
print(promedio_por_paciente[:5])"""
))

cells.append(nbf.v4.new_markdown_cell("## 4. Visualizacion"))

cells.append(nbf.v4.new_code_cell(
"""plt.figure(figsize=(8,5))
plt.plot(promedio_por_dia)
plt.title("Promedio de inflamacion por dia (todos los pacientes)")
plt.xlabel("Dia del ensayo")
plt.ylabel("Promedio de episodios de inflamacion")
plt.show()"""
))

cells.append(nbf.v4.new_markdown_cell("## 5. Interpretacion"))

cells.append(nbf.v4.new_markdown_cell(
"""Al graficar el promedio de inflamacion por dia se nota una subida clara al inicio del ensayo, un pico mas o menos a la mitad, y despues una bajada hacia el final. Esto tendria sentido con la idea de un medicamento que primero deja que la inflamacion suba y luego la va bajando con el tiempo.

Tambien se ve que el numero mas alto de episodios en todo el dataset es bastante mayor al promedio por paciente, lo que sugiere que algunos pacientes tuvieron dias con muchos mas episodios que el resto."""
))

nb['cells'] = cells
with open('evidencia-03-python.ipynb', 'w') as f:
    nbf.write(nb, f)
print("listo")
