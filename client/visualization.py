# This file will be for seaborn implementation. We will create different plots to create visualizations based on the data that dataAnalysis.py generates.


from re import L
import matplotlib.pyplot as plt 
import seaborn as sns
from dataAnalysis import *
import pandas as pd

working_dir = os.path.dirname(__file__)

# Graph types to consider: pie chart, bar graph, or box plot? Pie chart seems most effective.
# link for seaborn-matplotlib pie chart tutorial: https://www.statology.org/seaborn-pie-chart/

# #add country's dfs to data
# canada_data = [canada_results["Genre"]]
# mexico_data = [mexico_results["Genre"]]
# us_data = [united_states_results["Genre"]]
# labels = ["Dance", "Hip-Hop Rap", "Pop", "Country"]

# #define Seaborn color palette to use
# palette_color = sns.color_palette('bright')

# #create pie chart
# canada = plt.pie(canada_data, labels = labels, colors = palette_color, autopct='%.0f%%')
# mexico = plt.pie(mexico_data, labels = labels, colors = palette_color, autopct='%.0f%%')
# united_states = plt.pie(us_data, labels = labels, colors = palette_color, autopct='%.0f%%')


class PiePlot :

	def __init__(self, df, countryName, colName, figSize = (5,5)) :
		""" Initializes the attributes of a plot.
		"""
		
		df = self.df
		countryName = self.countryName
		colName = self.colName
		figSize = self.figSize

	def instanceCount(countryObject) :
		""" Tracks the instances of each genre within the genre column (allows for "easier" pie plot creation, since it wasn't working with strings)
		"""
	# canada_occurences = canada_results['Genre'].value_counts()
	# mexico_occurences = mexico_results['Genre'].value_counts()
	# us_occurences = united_states_results['Genre'].value_counts()
		instances = ((working_dir, f"database/{countryObject.country_name[index]}/countryObject.{country_name[index]}Results.csv")[countryObject.colName].value_counts())
		return instances

	def makePlot(instances, figSize) :
		""" Creates a pie plot with the integer instances of each genre appearing in the top 200 songs. DOES NOT WORK YET***
		"""

		plot = instances.plot.pie(y='Genre')
		print(plot)


def main(colName) :
	""" "Driver" for the program. Creates the plot objects by calling the PiePlot init, then uses the methods within PiePlot to further refine the dataframes into a pie plot.
	"""
	canada_results = pd.read_csv(os.path.join(working_dir, "database/Canada/CanadaResults.csv"))
	mexico_results = pd.read_csv(os.path.join(working_dir, "database/Mexico/MexicoResults.csv"))
	united_states_results = pd.read_csv(os.path.join(working_dir, "database/United_States/United_StatesResults.csv"))

	canada_instances = PiePlot(canada_results, country_name[0], 'Genre', (5, 5))
	mexico_instances = PiePlot(mexico_results, country_name[1], 'Genre', (5, 5))
	united_states_instances = PiePlot(united_states_results, country_name[2], 'Genre', (5, 5))

	canada_count = PiePlot.instanceCount(canada_instances)
	mexico_count = PiePlot.instanceCount(mexico_instances)
	united_states_count = PiePlot.instanceCount(united_states_instances)

	#save these as pngs, or get them to display (maybe better to display using py notebook?)
	canadaPlot = PiePlot.makePlot(canada_count, (5, 5))
	mexicoPlot = PiePlot.makePlot(mexico_count, (5, 5))
	unitedStatesPlot = PiePlot.makePlot(united_states_count, (5, 5))


main('Genre', (5, 5))