import pandas as pd


df_origin = pd.read_csv(“txtfilename.csv”)
genre = []
df_origin[‘Genre’] genre

df_country = pd.read_csv('country.csv')
df_pop = pd.read_csv('pop.csv')
df_hipHopRap = pd.read_csv('hipHopRap.csv')
df_dance = pd.read_csv('dance.csv')

#First, we will import the pandas library for functionality to reach our program. Then we will create a data frame that reads the CSV file and saves its columns as keys. 

for index in df_origin
	for index_country in df_country
"""    
		if song isin country genre df, add ‘Country’ to ‘Genre’ column
"""        
	for index_pop in df_pop
"""    
		if song isin pop genre df, add “Pop” to “Genre” column
"""
	for index_hipHopRap in df_hipHopRap 
"""    
		if song isin hip-hop/rap genre df, add “Hip-Hop/Rap” to “Genre” column
"""

For index_dance in df_dance 
"""
	if song isin dance genre df, add “Dance” to “Genre” column
"""