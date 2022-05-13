import os
from dataAnalysis import *
from visualization import *

canada_results = pd.read_csv(os.path.join(working_dir, "database/Canada/CanadaResults.csv"))
mexico_results = pd.read_csv(os.path.join(working_dir, "database/Mexico/MexicoResults.csv"))
united_states_results = pd.read_csv(os.path.join(working_dir, "database/United_States/United_StatesResults.csv"))

#country results dataframes tests
def testCanadaResults() :
	assert canada_results.iloc[0,3] == 'Dance'

def testMexicoResults() :
	assert mexico_results.iloc[7,3] == 'Pop'

def testUnitedStatesResults() :
	assert united_states_results.iloc[99,3] == 'Hip-Hop Rap'

def testCanadaResults2():
	assert canada_results.iloc[48, 3] == "Dance"

def testMexicoResults2():
	assert mexico_results.iloc[30, 3] == "Hip-Hop Rap"

def testUnitedStatesResults2():
	assert mexico_results.iloc[14, 3] == "Pop"