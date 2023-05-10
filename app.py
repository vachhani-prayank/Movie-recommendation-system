import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-us'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original/" + data['poster_path']

def recommend(movie1):
    movie_index1 = movies1[movies1['title'] == movie1].index[0]
    distance1 = similarity[movie_index1]
    movies_list1 = sorted(list(enumerate(distance1)),reverse=True, key = lambda x:x[1])[1:6]

    recommended_movies1 = []
    recommended_movies_posters1 = []

    for i in movies_list1:
        movie_id = movies1.iloc[i[0]].movie_id
        
        recommended_movies1.append(movies1.iloc[i[0]].title)
        # fetch poster from API TMDB
        recommended_movies_posters1.append(fetch_poster(movie_id))
    return recommended_movies1,recommended_movies_posters1

def recommend(movie2):
    movie_index2 = movies2[movies2['title'] == movie2].index[0]
    distance2 = similarity[movie_index2]
    movies_list2 = sorted(list(enumerate(distance2)),reverse=True, key = lambda x:x[1])[1:6]

    recommended_movies2 = []
    recommended_movies_posters2 = []

    for i in movies_list2:
        movie_id = movies2.iloc[i[0]].movie_id
        
        recommended_movies2.append(movies2.iloc[i[0]].title)
        # fetch poster from API TMDB
        recommended_movies_posters2.append(fetch_poster(movie_id))
    return recommended_movies2,recommended_movies_posters2


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies1 = pd.DataFrame(movies_dict)
movies2 = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name1 = st.selectbox(
    'SELECT MOVIE 1', 
    movies1['title'].values) 

selected_movie_name2 = st.selectbox(
    'SELECT MOVIE 2', 
    movies2['title'].values) 


if st.button('Recommend'):
    names,posters = recommend(selected_movie_name1)
    names2,posters2 = recommend(selected_movie_name2)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
        st.text(names2[2])
        st.image(posters2[2])
    with col2:
        st.text(names2[0])
        st.image(posters2[0])
        st.text(names[3])
        st.image(posters[3])
    with col3:
        st.text(names[1])
        st.image(posters[1])
        st.text(names2[3])
        st.image(posters2[3])
    with col4:
        st.text(names2[1])
        st.image(posters2[1])
        st.text(names[4])
        st.image(posters[4])
        
    with col5:
        st.text(names[2])
        st.image(posters[2])
        st.text(names2[4])
        st.image(posters2[4])