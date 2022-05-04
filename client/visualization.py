import seaborn as sns #Unsure if we need to import matplotlib as well?
import dataAnalysis
import pandas as pd

# testing df:
data = [['artist1', 'song1', 'Country'], ['artist2', 'song2', 'Hip-Hop Rap'], ['artist3', 'song3', 'Pop'], ['artist4', 'song4', 'Dance'], ['artist5', 'song5', 'Hip-Hop Rap'], ['artist6', 'song6', 'Country']]
testing_df = pd.DataFrame(data, columns = ['Artist', 'Title', 'Genre'])

# print(testing_df)

# This file will be for seaborn implementation. We will create different plots to create visualizations based on the data that dataAnalysis.py generates.
# Plan: import the 2 dataframe object variables to compare from the dataAnalysis.py file (from file.py import variableName), and create two pie charts
# to compare genre listening habits by city/state/country.



# Graph types to consider: pie chart, bar graph, or box plot? Pie chart seems most effective.
# link for seaborn pie chart tutorial: https://www.statology.org/seaborn-pie-chart/