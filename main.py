import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm

data = pd.read_csv("Screentime-App-Details.csv")
print(data.head())

#check if we have null values
print(data.isnull().sum())

#check descriptive statistics
print(data.describe())

#amount of usage of the apps
figure = px.bar(data_frame=data,
                x = "Date",
                y= "Usage",
                color = "App",
                title = "Usage")
figure.show()

#number of notifications
figure = px.bar(data_frame=data,
                 x = "Date",
                 y = "Notifications",
                 color = "App",
                 title = "Notifications")
figure.show()

#number of times apps opened
figure = px.bar(data_frame=data,
                x = "Date",
                y = "Times opened",
                color = "App",
                title = "Times opened")
figure.show()

#relationship between number of notifications and usage
figure = px.scatter(data_frame = data,
                    x = "Notifications",
                    y = "Usage",
                    size = "Notifications",
                    trendline = "ols",
                    title = "Relationship between number of notifications and usage")
figure.show()