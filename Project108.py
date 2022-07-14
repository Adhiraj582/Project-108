import csv
import pandas as pd
import plotly.figure_factory as ff

reader = pd.read_csv('datapro108.csv')

fig = ff.create_distplot([reader["Avg Rating"].tolist()], [
                         "Avg Rating"])
fig.show()
