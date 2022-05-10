import pandas as pd
import os

# get current working directory
working_dir = os.path.dirname(__file__)

# read csv files with all 200 songs for each country and store in array
canada_songs = pd.read_csv(os.path.join(working_dir, "../database/Canada/Shazam Top 100 Dance 25-04-2022.csv"))
mexico_songs = pd.read_csv(os.path.join(working_dir, "../database/Mexico/Shazam Top 200 Mexico Chart 25-04-2022.csv"))
united_states_songs = pd.read_csv(os.path.join(working_dir, "../database/United_States/Shazam_Top_200_United_States_Chart_25-04-2022.csv"))
countries = [canada_songs, mexico_songs, united_states_songs]

# list all genres in each country with the pathname to the csv files with their songs
canada_genres = {
    "Dance": os.path.join(working_dir, "../database/Canada/Shazam Top 100 Dance 25-04-2022.csv"),
    "Hip-Hop Rap": os.path.join(working_dir, "../database/Canada/Shazam Top 100 Hip-Hop_Rap 25-04-2022.csv"),
    "Pop": os.path.join(working_dir, "../database/Canada/Shazam Top 100 Pop 25-04-2022.csv")
}

mexico_genres = {
    "Dance": os.path.join(working_dir, "../database/Mexico/Shazam Top 100 Dance 28-04-2022.csv"),
    "Hip-Hop Rap": os.path.join(working_dir, "../database/Mexico/Shazam Top 100 Hip-Hop_Rap 28-04-2022.csv"),
    "Pop": os.path.join(working_dir, "../database/Mexico/Shazam Top 100 Pop 28-04-2022.csv")
}

united_states = {
    "Dance": os.path.join(working_dir, "../database/United_States/Shazam_Top_100_Dance_25-04-2022.csv"),
    "Hip-Hop Rap": os.path.join(working_dir, "../database/United_States/Shazam_Top_100_Hip-Hop_Rap_25-04-2022.csv"),
    "Pop": os.path.join(working_dir, "../database/United_States/Shazam_Top_100_Pop_25-04-2022.csv"),
    "Country": os.path.join(working_dir, "../database/United_States/Shazam_Top_100_Country_25-04-2022.csv"),
}

# store all country genres in array
country_genres = [canada_genres, mexico_genres, united_states]

# store country name in array to find sub-folders to store results later
country_name = ["Canada", "Mexico", "United_States"]

# start iteration at Canada (index 0)
index = 0
for country in countries:
    # get only Artist and Title columns
    main_extract = country.loc[:, ["Artist", "Title"]]

    # get list of genres of that country from the genres array
    genres = country_genres[index]

    # new array with second dimension of "Artists", "Title" , "Genre" to store values
    new_array = [[], [], []]

    # iterate through all songs in "200 songs" csv file
    for song in main_extract.values:

        # iterate through all csv files in each genre
        for genre_name, file_name in genres.items():

            # extract only artist and title
            genre_extract = pd.read_csv(file_name).loc[:, ["Artist", "Title"]]

            # iterate through each song and compare with main csv file, if they match, append to 2d-array
            for x in genre_extract.values:
                if (song == x).all():
                    new_array[0].append(x[0])
                    new_array[1].append(x[1])
                    new_array[2].append(genre_name)

    # create data frame from 2d-array
    final_data_frame = pd.DataFrame({
        "Artist": new_array[0],
        "Title": new_array[1],
        "Genre": new_array[2]
    })

    # save data frame to csv file, directory depends on country name
    final_data_frame.to_csv(os.path.join(working_dir, f"../database/{country_name[index]}/{country_name[index]}Results.csv"))

    # increment the index to go to the next country
    index += 1
	