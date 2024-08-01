import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import gzip
import requests

# Load the preprocessed data and similarity matrix
try:
    movies = pickle.load(open('movies.pkl', 'rb'))
    with gzip.open('similarity.pkl.gz', 'rb') as f:
        similarity = pickle.load(f)
except FileNotFoundError:
    st.error('Preprocessed data files not found. Please ensure `movies.pkl` and `similarity.pkl` are present in the directory.')
    st.stop()

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=0f5c0501eda1fa91be771631d724af9a&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data.get('poster_path', '')

def recommend(movie_title):
    try:
        # Ensure the movie title exists in the dataset
        if movie_title not in movies['title'].values:
            return [], []

        # Get the index of the movie
        index = movies[movies['title'] == movie_title].index[0]
        
        # Get the similarity scores for the movie
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        
        # Get the titles and movie IDs of the top 6 most similar movies (excluding the input movie)
        recommended_movies = []
        recommended_movie_posters = []
        for i in distances[1:6]:  # Skip the first one and get the next five
            movie_id = movies.iloc[i[0]]['id']  # Adjusted to match column name
            recommended_movies.append(movies.iloc[i[0]]['title'])  # Adjusted to match column name
            # Fetch poster from API
            recommended_movie_posters.append(fetch_poster(movie_id))
        
        return recommended_movies, recommended_movie_posters
    except Exception as e:
        st.error(f'Error during recommendation: {e}')
        return [], []

# Streamlit app
st.title('Movie Recommendation System')

st.write('### Enter a movie title to get recommendations')

movie_title = st.text_input('Movie Title', placeholder='The Avengers')

if st.button('Get Recommendations'):
    if movie_title:
        recommendations, posters = recommend(movie_title)
        if recommendations:
            st.write('### Recommended Movies:')
            cols = st.columns(5)
            for i in range(min(len(recommendations), 5)):  # Display up to 5 recommendations
                with cols[i]:
                    st.text(recommendations[i])
                    st.image(posters[i])
        else:
            st.write('Movie not found in the database. Please try another title.')
    else:
        st.write('Please enter a movie title.')
