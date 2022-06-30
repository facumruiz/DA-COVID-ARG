%matplotlib notebook

import pandas as pd
import io
import requests
import numpy as np
from matplotlib import pyplot as plt
url="https://raw.githubusercontent.com/facumruiz/DA-COVID-ARG/main/covid_total_diario.csv"

data = pd.read_csv(url)
DICIEMBRE = data.iloc[[0,1,2]]

FECHA = DICIEMBRE['fecha']
DOSIS = DICIEMBRE['total_1ra_y_2da_dosis_aplicadas']
fig = plt.figure()
plot = fig.add_axes([0.1,0.1,0.9,0.9])
plot.bar(FECHA, DOSIS)
row1

