import matplotlib.pyplot as plt 
import seaborn as sns #Unsure if we need to import matplotlib as well?
from dataAnalysis import *
import pandas as pd

# testing df:
data = [['artist1', 'song1', 'Country'], ['artist2', 'song2', 'Hip-Hop Rap'], ['artist3', 'song3', 'Pop'], ['artist4', 'song4', 'Dance'], ['artist5', 'song5', 'Hip-Hop Rap'], ['artist6', 'song6', 'Country']]
testing_df = pd.DataFrame(data, columns = ['Artist', 'Title', 'Genre'])


canada_results = pd.read_csv(os.path.join(working_dir, "database/Canada/CanadaResults.csv"))
mexico_results = pd.read_csv(os.path.join(working_dir, "database/Mexico/MexicoResults.csv"))
united_states_results = pd.read_csv(os.path.join(working_dir, "database/United_States/United_StatesResults.csv"))

#add country's dfs to data
canada_data = [canada_results['Genre']]
mexico_data = [mexico_results['Genre']]
us_data = [united_states_results['Genre']]
labels = ['Dance', 'Hip-Hop Rap', 'Pop', 'Country']

#define Seaborn color palette to use
palette_color = sns.color_palette('bright')

#create pie chart
canada = plt.pie(canada_data, labels = labels, colors = palette_color, autopct='%.0f%%')
mexico = plt.pie(mexico_data, labels = labels, colors = palette_color, autopct='%.0f%%')
united_states = plt.pie(us_data, labels = labels, colors = palette_color, autopct='%.0f%%')

#show the plots (add all 3 after we get one to show properly)
canada.show()



# This file will be for seaborn implementation. We will create different plots to create visualizations based on the data that dataAnalysis.py generates.
# Plan: import the 2 dataframe object variables to compare from the dataAnalysis.py file (from file.py import variableName), and create two pie charts
# to compare genre listening habits by city/state/country.



# Graph types to consider: pie chart, bar graph, or box plot? Pie chart seems most effective.
# link for seaborn pie chart tutorial: https://www.statology.org/seaborn-pie-chart/