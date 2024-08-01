import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import gzip

# Load the preprocessed data and similarity matrix
try:
    movies = pickle.load(open('movies.pkl', 'rb'))
    with gzip.open('similarity.pkl.gz', 'rb') as f:
        similarity = pickle.load(f)
except FileNotFoundError:
    st.error('Preprocessed data files not found. Please ensure `movies.pkl` and `similarity.pkl` are present in the directory.')
    st.stop()



def recommend(movie_title):
    try:
        # Ensure the movie title exists in the dataset
        if movie_title not in movies['title'].values:
            return []

        # Get the index of the movie
        index = movies[movies['title'] == movie_title].index[0]
        
        # Get the similarity scores for the movie
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        
        # Get the titles of the top 6 most similar movies (excluding the input movie)
        recommended_movies = [movies.iloc[i[0]].title for i in distances[1:7]]
        return recommended_movies
    except Exception as e:
        st.error(f'Error during recommendation: {e}')
        return []

# Streamlit app
st.title('Movie Recommendation System')

st.write('### Enter a movie title to get recommendations')

movie_title = st.text_input('Movie Title', placeholder='The Avengers')

if st.button('Get Recommendations'):
    if movie_title:
        recommendations = recommend(movie_title)
        if recommendations:
            st.write('### Recommended Movies:')
            for movie in recommendations:
                st.write(f'- {movie}')
        else:
            st.write('Movie not found in the database. Please try another title.')
    else:
        st.write('Please enter a movie title.')
