%matplotlib notebook

import pandas as pd
import io
import requests
import numpy as np
from matplotlib import pyplot as plt

#IMPORTO DATOS
url="https://raw.githubusercontent.com/facumruiz/DA-COVID-ARG/main/covid_total_diario.csv"
data = pd.read_csv(url)

# FILTRO DATOS POR MES
DICIEMBRE = data.iloc[:3]
ENERO = data.iloc[3:34]
FEBRERO = data.iloc[34:62]


# DICIEMBRE
FECHA = DICIEMBRE['fecha']
DOSIS = DICIEMBRE['total_1ra_y_2da_dosis_aplicadas']
fig = plt.figure()
plot = fig.add_axes([0.1,0.1,0.9,0.9])
plot.bar(FECHA, DOSIS)
#print(DICIEMBRE)

# ENERO
FECHA = ENERO['fecha']
DOSIS = ENERO['total_1ra_y_2da_dosis_aplicadas']
fig = plt.figure()
plot = fig.add_axes([0.1,0.1,0.9,0.9])
plot.bar(FECHA, DOSIS)
#print(ENERO)

# FEBRERO
FECHA = FEBRERO['fecha']
DOSIS = FEBRERO['total_1ra_y_2da_dosis_aplicadas']
fig = plt.figure()
plot = fig.add_axes([0.1,0.1,0.9,0.9])
plot.bar(FECHA, DOSIS)


# CONSOLA
print("-------------------------2020-------------------------")
print("----------------DATOS MES DE DICIEMBRE----------------")
print("------------------------------------------------------")
print(DICIEMBRE)
print("------------------------------------------------------")
print("-------------------------2021-------------------------")
print("------------------DATOS MES DE ENERO------------------")
print("------------------------------------------------------")
print(ENERO)
print("------------------------------------------------------")
print("----------------DATOS MES DE FEBRERO------------------")
print("------------------------------------------------------")
print(FEBRERO)
