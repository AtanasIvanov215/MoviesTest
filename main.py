import pandas as pd
import numpy as np
import ast
import json


# read the csv and get to know the df structure
df = pd.read_csv('movies_metadata.csv',low_memory=False, delimiter=',')
columns = list(df.columns)
print(columns)

# view the unique movies
movie_count = df['imdb_id'].nunique()
print(movie_count)

# average rating for all movies
avr_rating_all = df['vote_average'].mean()
print(avr_rating_all)

# top 5 highest rated movies

top_5 = df.nlargest(5, columns=['vote_average'])
names = top_5['original_title']
names = names.to_string(index = False)
print(names)

# Number of movies release each year

# List of columns containing datetime values
datetime_columns = ['release_date']

# Define the desired datetime format
desired_format = '%Y-%m-%d'

# Loop through the datetime columns and convert them to the desired format
for column in datetime_columns:
    df['release_date'] = pd.to_datetime(df['release_date'], format=desired_format, errors='coerce')

dates = pd.to_datetime(df['release_date'])
df['year'] = dates.dt.year
movies_by_year = df['year'].value_counts()
print(movies_by_year)

# Movies by Genre

# Transforming the Column in to an iterable list
multi = []
genres = df['genres']
for g in genres:
    res = ast.literal_eval(g)
    multi.append(res)
# Creating new dict to iterate over the values and count them
counts_genres={}
for m in multi:
    for m1 in m:
        for key, value in m1.items():
            if key == 'name':
                if value not in counts_genres:
                    counts_genres[value] = 0
                counts_genres[value] +=1
print(counts_genres)

# Save as JSON

json_df = df.to_json()






















