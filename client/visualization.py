# This file will be for seaborn implementation. We will create different plots to create visualizations based on the data that dataAnalysis.py generates.


from re import L
import matplotlib.pyplot as plt
from pyparsing import col
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


class PiePlot:

    def __init__(self, instance_data, countryName, colName, figSize=(5, 5)):
        """ Initializes the attributes of a plot.
        """
        self.country_name = countryName
        self.colName = colName
        self.figsize = figSize
        self.instance_data = instance_data

    def instanceCount(self):
        """ Tracks the instances of each genre within the genre column (allows for "easier" pie plot creation, since it wasn't working with strings)
        """
    # canada_occurences = canada_results['Genre'].value_counts()
    # mexico_occurences = mexico_results['Genre'].value_counts()
    # us_occurences = united_states_results['Genre'].value_counts()
        instances = (working_dir, f"/database/{self.country_name}/{self.country_name}Results.csv")
        colName = self.colName
        allvalues = getattr(pd.read_csv("".join(instances)), colName)
        counts = allvalues.value_counts()
                    
        #return series of all the genre counts
        return counts

    def makePlot(instances, figSize):
        """ Creates a pie plot with the integer instances of each genre appearing in the top 200 songs.
        """

        plot = instances.plot.pie(y='Genre', subplots = True)

        return plot


def main(colName):
    """ "Driver" for the program. Creates the plot objects by calling the PiePlot init, then uses the methods within PiePlot to further refine the dataframes into a pie plot.
    """
    canada_results = pd.read_csv(os.path.join(
        working_dir, "database/Canada/CanadaResults.csv"))
    mexico_results = pd.read_csv(os.path.join(
        working_dir, "database/Mexico/MexicoResults.csv"))
    united_states_results = pd.read_csv(os.path.join(
        working_dir, "database/United_States/United_StatesResults.csv"))

    canada_instances = PiePlot(
        canada_results, country_name[0], 'Genre', (5, 5))
    mexico_instances = PiePlot(
        mexico_results, country_name[1], 'Genre', (5, 5))
    united_states_instances = PiePlot(
        united_states_results, country_name[2], 'Genre', (5, 5))

    canada_count = canada_instances.instanceCount()
    mexico_count = mexico_instances.instanceCount()
    united_states_count = united_states_instances.instanceCount()

    # save these as pngs, or get them to display (maybe better to display using py notebook?)
    canadaPlot = PiePlot.makePlot(canada_count, (5, 5))    
    plt.savefig("canadaGenresPlot.png")
    mexicoPlot = PiePlot.makePlot(mexico_count, (5, 5))
    plt.savefig("MexicoGenresPlot.png") 
    unitedStatesPlot = PiePlot.makePlot(united_states_count, (5, 5))
    plt.savefig("unitedStatesGenresPlot.png")    


main('Genre')
