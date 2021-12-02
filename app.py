import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import requests

coss_similarity = pickle.load(open('coss_similarity.pkl','rb'))

def find_poster(movie_id):
    reponce = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d299cebc789050a714be44b4c500456a&language=en-US'.format(movie_id))
    data = reponce.json()
    #st.text(data)
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    moive_index = movie_frame[movie_frame['title'] == movie].index[0]
    distences = coss_similarity[moive_index]
    movie_list = sorted(list(enumerate(distences)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movie = []
    movie_poster_dislay = []
    for i in movie_list:
        movie_id = movie_frame.iloc[i[0]].movie_id

        recommend_movie.append(movie_frame.iloc[i[0]].title)
        # fetch movie poster from tmdb
        movie_poster_dislay.append(find_poster(movie_id))

    return recommend_movie, movie_poster_dislay


movie_dff = pickle.load(open('movies_dict.pkl','rb'))
movie_frame = pd.DataFrame(movie_dff)
movie_frr = movie_frame['title'].values

st.title('Movie Recommender System')

option = st.selectbox(
'Selected your movie',
movie_frr)
if st.button('Submit'):
    movie_names, movie_posters = recommend(option)
    st.subheader('Your top five movie recommendation')

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_names[0])
        st.image(movie_posters[0])

    with col2:
        st.text(movie_names[1])
        st.image(movie_posters[1])

    with col3:
        st.text(movie_names[2])
        st.image(movie_posters[2])

    with col4:
        st.text(movie_names[3])
        st.image(movie_posters[3])

    with col5:
        st.text(movie_names[4])
        st.image(movie_posters[4])