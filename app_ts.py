import pickle
import streamlit as st
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=0f5c0501eda1fa91be771631d724af9a&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# Load the movies and similarity data
movies_list = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_list)  # Convert the loaded list to a DataFrame
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    # getting index of movies
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])

    recommended_movies = []
    recommended_movie_posters = []
    for i in movies_list[1:6]:  # Skip the first one and get the next five
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)  
                #fetch poster from API
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movies , recommended_movie_posters

# Streamlit UI
movies_list = movies['title'].values
st.title('Movie recommendation system')

selected_movie_name = st.selectbox(
    "How would you like to be connected?",
    movies_list
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
