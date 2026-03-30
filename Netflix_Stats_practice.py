import pandas as pd

#Load the dataset

netflix_data = pd.read_csv('/Users/hakunamatata/Documents/Nivi/netflix_titles.csv')

"""
#Shape & Size

print("Dataset shape:",netflix_data.shape)
print("Total number of elements in the dataset:",netflix_data.size)
print("Length of the dataset:",len(netflix_data))

print("Columns in the dataset:",netflix_data.columns)
print("Rows in the dataset:",netflix_data.index)

#Preview the dataset

print("First 5 rows of the dataset:",netflix_data.head())
print("Last 5 rows of the dataset:",netflix_data.tail())
print("Random 5 rows of the dataset:",netflix_data.sample(5))

#Data types of each column

print("Data types of each column:",netflix_data.dtypes)
print("Summary of the dataset:",netflix_data.info())
print("Statistical summary of the dataset:",netflix_data.describe())
print("List of column names:",netflix_data.columns.tolist())

#Check for missing values

print("Number of missing values in each column:",netflix_data.isnull().sum())
print("% of missing values in each column:",netflix_data.isnull().mean()*100)
print("Numer of non-missing values in each column:",netflix_data.notnull().sum())

#Numeric columns analysis

print("Summary statistics for numeric columns:",netflix_data.describe())
print("Mean of numeric columns:",netflix_data.mean(numeric_only=True))
print("Median of numeric columns:",netflix_data.median(numeric_only=True))
print("Standard deviation of numeric columns:",netflix_data.std(numeric_only=True))
print("Minimum values of numeric columns:",netflix_data.min(numeric_only=True))
print("Maximum values of numeric columns:",netflix_data.max(numeric_only=True))

#Unique values in categorical columns

print("Unique values in 'type' column:",netflix_data['type'].unique())
print("Unique values in 'type' column:",netflix_data['type'].nunique())
print("Unique values in 'director' column:",netflix_data['director'].nunique())
print("Unique values in 'director' column:",netflix_data['director'].nunique())

#Grouping and aggregation

print("Number of movies and TV shows by type:",netflix_data.groupby('type').size())
print("Count of movies and TV shows by year:",netflix_data.groupby(['type','release_year']).size().sort_values())
print("Count director year by release:",netflix_data.groupby('release_year')['director'].count())


#Filering data

print("Movies release after 2010:",netflix_data[netflix_data['release_year']>2010])
print("Total number of movies:",len(netflix_data[netflix_data['type']=='Movie']))
print("Total number of TV shows:",len(netflix_data[netflix_data['type']=='TV Show']))

#Sorting data
print("Top 5 most recent movies:",netflix_data[netflix_data['type']=='Movie'].sort_values(by='release_year',ascending=False).head())
print("Top 5 oldest TV shows:",netflix_data[netflix_data['type']=='TV Show'].sort_values(by='release_year',ascending=True).head())
"""

print(netflix_data[netflix_data['type']=='Movie'].sort_values())