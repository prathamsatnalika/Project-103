# %%

import pandas as pd
import plotly_express as px

df = pd.read_csv("D:\Project Pro-C 103\countries-aggregated_csv.csv")
fig = px.scatter(df, x="Date", y="Confirmed Cases",
                 color="Country", title="No Of Cases Of Covid-19 Every Day")

fig.show()
