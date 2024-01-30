import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("movie_dataset.csv")
#Rename columns with spaces
df.rename(columns={'Runtime (Minutes)': 'Runtime'}, inplace=True)
df.rename(columns={'Revenue (Millions)': 'Revenue'}, inplace=True)

df.dropna(subset=['Runtime', 'Metascore', 'Revenue'], inplace=True)

max_rating_index = df['Rating'].idxmax()
title_with_highest_rating = df.loc[max_rating_index, 'Title']

average_rev = df['Revenue'].mean()
subset_df = df[df['Year'].between(2015, 2017)]
average_rev_ = subset_df['Revenue'].mean()

movies_2016 = df[df['Year'] == 2016]
num_movies_2016 = len(movies_2016)

movie_director = df[df['Director'] == 'Christopher Nolan']

Rate = df[df['Rating'] >= 8.0]

median_chris = movie_director['Rating'].median()

max_rate = df.groupby('Year')['Rating'].max()
year_rate = max_rate[max_rate == max_rate.max()].index

movies_2006 = df[df['Year'] == 2006]
num_movies_2006 = len(movies_2006)             
 
all_names = df['Actors'].str.split(', ').sum()
name_counts = pd.Series(all_names).value_counts()
most_common_name = name_counts.idxmax()
    
all_names = df['Genre'].str.split(', ').sum()
unique_genre = len(set(all_names)) 

correlation_matrix = df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix of Movie Features')
plt.show()

