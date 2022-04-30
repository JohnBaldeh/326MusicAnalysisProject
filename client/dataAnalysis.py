import pandas as pd

def genreCheck(df_origin, df_country, df_pop, df_hipHopRap, df_dance) :

	for row in df_origin.iterrows() :
		if (df_origin.loc[row, {"Artist", "Title"}].isin(df_country)) :
			# add 'Country' to df column: Genre. delete pass when implemented
			df_origin.loc[row, "Genre"] = "Country"

		elif (df_origin.loc[row, {"Artist", "Title"}].isin(df_pop)) :
			# add 'Pop' to df column: Genre. delete pass when implemented
			df_origin.loc[row, "Genre"] = 'Pop'

		elif (df_origin.loc[row, {"Artist", "Title"}].isin(df_hipHopRap)) :
			# add 'Hip-Hop Rap' to df column: Genre. delete pass when implemented
			df_origin.loc[row, "Genre"] = 'Hip-Hop Rap'

		elif(df_origin.loc[row, {"Artist", "Title"}].isin(df_dance)) :
			# add 'Dance' to df column: Genre. delete pass when implemented
			df_origin.loc[row, "Genre"] = 'Dance'

		else :
			pass


	# FOR FIRST: use current row's songname for rowIndex, and "Title" as colIndex
	# FOR DF_ORIGIN: use current row's songname for rowIndex, and "Title" as colIndex
	# if(( df_origin.iloc[rowIndex, colIndex].isin( ) and df_origin.iloc[rowIndex, colIndex] ))



	print(df_origin)

	# pass

# FOR TESTING. REPLACE FUNCTIONALITY WITH if __name__ == "__main__" FUNCTION

def main() :
	df_origin = pd.read_csv('database/United_States/Shazam_Top_200_United_States_Chart_25-04-2022.csv')

	df_country = pd.read_csv('database/United_States/Shazam_Top_100_Country_25-04-2022.csv')
	df_pop = pd.read_csv('database/United_States/Shazam_Top_100_Pop_25-04-2022.csv')
	df_hipHopRap = pd.read_csv('database/United_States/Shazam_Top_100_Hip-Hop_Rap_25-04-2022.csv')
	df_dance = pd.read_csv('database/United_States/Shazam_Top_100_Dance_25-04-2022.csv')

	# print(df_origin)

	# print(df_origin.loc[:, {"Artist", "Title"}])

	genreCheck(df_origin, df_country, df_pop, df_hipHopRap, df_dance)

main()