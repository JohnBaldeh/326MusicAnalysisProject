import csv
import pandas as pd
import seaborn as sns # imports db that you will be using
from database import Canada, Mexico, United_States


#df_origin = sns.load_dataset("tips") # requests dataset "tips" from the library

#change directory
df_origin = pd.read_csv('database/United_States/Shazam_Top_200_United_States_Chart_25-04-2022.csv')


df_origin.head(10) 

#print(df_origin)

"""
# 10 indicates that data fetched is in the first 10 rows 
# head() is used to indicate the headings of the columns' output
"""

df_origin.loc[[0,2,8], :] 
#print(df_origin)


"""
This shows the  labels rows that you want to select
.loc() compares selected rows against selected columns, 
rows on the left, columns on the right

colon is used to separate the rows and the columns being fetched.

Run code - it should bring an output of only the rows that you have chosen.
"""

df_origin.loc[0:4, :]
#print(df_origin)

"""
selects all rows continuously. the last colon is used to fetch and populate all the data in the data frames
Run code: it should output data in rows continuously from row 0 to row 4
"""

df_origin.loc[:4, :] # this instructs the code to fetch data from the first row to row 4
#print(df_origin)


df_origin.loc[200:, :] 
#print(df_origin)


"""
this instructs the code to fetch data from row 200 all the way to the last row of the data 
can also work with columns
"""
df_origin.loc[:, "Artist"] #this will return the values of the artist ranking(row) against their respective name(column)
#print(df_origin)


df_origin.loc[:, {"Artists", "Title"}] 
"""
this code when run will produce an output of all rows against the artists name and the title 
this is for columns that do not immediately follow each other
"""
print(df_origin)

df_origin.loc[:, "artists" : "age"]
print(df_origin)
