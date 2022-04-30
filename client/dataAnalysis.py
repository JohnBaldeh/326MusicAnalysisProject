import pandas as pd


# df_origin = pd.read_csv("database/United_States/Shazam_Top_200_United_States_Chart_25-04-2022.csv")
# genre = []
# df_origin['Genre'] = genre

# df_country = pd.read_csv("database/United_States/Shazam_Top_100_Country_25-04-2022.csv")
# df_pop = pd.read_csv("database/United_States/Shazam_Top_100_Pop_25-04-2022.csv")
# df_hipHopRap = pd.read_csv("database/United_States/Shazam_Top_100_Hip-Hop_Rap_25-04-2022.csv")
# df_dance = pd.read_csv("database/United_States/Shazam_Top_100_Dance_25-04-2022.csv")

#First, we will import the pandas library for functionality to reach our program. Then we will create a data frame that reads the CSV file and saves its columns as keys. 


def genreCheck(countryTopSongs, genreCountry, genrePop, genreHipHopRap, genreDance) :

	# for row in df_origin :
	# 	if (row['Artist'].isin(df_country['Artist'])) and row['Title'].isin(df_country['Title']) :
	# 		# add 'Country' to df column: Genre. delete pass when implemented
	# 		df_origin['Genre'][row.index] = 'Country'

	# 	elif (row['Artist'].isin(df_pop['Artist'])) and row['Title'].isin(df_pop['Title']) :
	# 		# add 'Pop' to df column: Genre. delete pass when implemented
	# 		df_origin['Genre'][row.index] = 'Pop'

	# 	elif (row['Artist'].isin(df_hipHopRap['Artist'])) and row['Title'].isin(df_hipHopRap['Title']) :
	# 		# add 'Hip-Hop Rap' to df column: Genre. delete pass when implemented
	# 		df_origin['Genre'][row.index] = 'Hip-Hop Rap'

	# 	elif(row['Artist'].isin(df_dance['Artist'])) and row['Title'].isin(df_dance['Title']) :
	# 		# add 'Dance' to df column: Genre. delete pass when implemented
	# 		df_origin['Genre'][row.index] = 'Dance'

	# 	else :
	# 		pass


	# FOR FIRST: use current row's songname for rowIndex, and "Title" as colIndex
	# FOR DF_ORIGIN: use current row's songname for rowIndex, and "Title" as colIndex
	# if(( df_origin.iloc[rowIndex, colIndex].isin( ) and df_origin.iloc[rowIndex, colIndex] ))



	# print(df_origin)

	pass

# FOR TESTING. REPLACE FUNCTIONALITY WITH if __name__ == "__main__" FUNCTION

def main() :

	df_origin = pd.read_csv(r'database/United_States/Shazam_Top_200_United_States_Chart_25-04-2022.csv')

	# df_country = pd.read_csv('database/United_States/Shazam_Top_100_Country_25-04-2022.csv')
	# df_pop = pd.read_csv("database/United_States/Shazam_Top_100_Pop_25-04-2022.csv")
	# df_hipHopRap = pd.read_csv("database/United_States/Shazam_Top_100_Hip-Hop_Rap_25-04-2022.csv")
	# df_dance = pd.read_csv("database/United_States/Shazam_Top_100_Dance_25-04-2022.csv")

	print(df_origin)

	# genreCheck(df_origin, df_country, df_pop, df_hipHopRap, df_dance)