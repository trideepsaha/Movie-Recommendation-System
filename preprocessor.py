# preprocess_movies.py

import pandas as pd
import ast
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer
import gzip
import pickle

# Load the dataset
movies = pd.read_csv('tmdb_5000_movies.csv')

# Print column names to check for discrepancies
print("Column names in the dataset:")
print(movies.columns)

# Columns to keep, adjusted for available columns
columns_to_keep = ['id', 'title', 'overview', 'genres', 'keywords']

# Keep only the necessary columns
movies = movies[columns_to_keep]

# Drop missing values
movies.dropna(inplace=True)

# Convert genres and keywords from string representation to list of strings
def convert(text):
    try:
        L = [i['name'] for i in ast.literal_eval(text)]
    except (ValueError, SyntaxError):
        L = []
    return L

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)

# Remove spaces from text data
def collapse(L):
    return [i.replace(" ", "") for i in L]

movies['genres'] = movies['genres'].apply(collapse)
movies['keywords'] = movies['keywords'].apply(collapse)

# Combine tags
def combine_tags(row):
    overview = row['overview'].split() if isinstance(row['overview'], str) else []
    genres = row['genres'] if isinstance(row['genres'], list) else []
    keywords = row['keywords'] if isinstance(row['keywords'], list) else []
    return overview + genres + keywords

movies['tags'] = movies.apply(combine_tags, axis=1)

# Drop original columns
new = movies.drop(columns=['overview', 'genres', 'keywords'], errors='ignore')

# Join tags into a single string
new['tags'] = new['tags'].apply(lambda x: " ".join(x))

# Stem the words in the tags
ps = PorterStemmer()

def stem(text):
    return " ".join([ps.stem(word) for word in text.split()])

new['tags'] = new['tags'].apply(stem)

# Text vectorization using Bag of Words
cv = CountVectorizer(max_features=5000, stop_words='english')
vector = cv.fit_transform(new['tags']).toarray()

# Compute similarity matrix
similarity = cosine_similarity(vector)

# Save preprocessed data and similarity matrix
pickle.dump(new, open('movies.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

# Load similarity matrix
with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

# Save the compressed file
with gzip.open('similarity.pkl.gz', 'wb') as f:
    pickle.dump(similarity, f)


print("Preprocessing complete and data saved.")

# def recommend(movie):
#     index = new[new['title'] == movie].index[0] #getting index of movies
#     distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
#     for i in distances[1:7]:
#         print(new.iloc[i[0]].title)

# recommend('The Avengers')