import requests
import streamlit as st
import pickle
import pandas as pd

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=0b836637c368b58ce681bc7af3b32485&language=en-US'.format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_poster


movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommendation :blue[System]")

selected_movie_name = st.selectbox(
    "Explore ,,,",
    (movies['title'].values),
    index=None,
    placeholder="Select Movies Here ...",
)

if st.button('Recommend', type="primary"):
    names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(posters[0])
        st.text(names[0])

    with col2:
        st.image(posters[1])
        st.text(names[1])

    with col3:
        st.image(posters[2])
        st.text(names[2])

    with col4:
        st.image(posters[4])
        st.text(names[3])

    with col5:
        st.image(posters[4])
        st.text(names[3])

st.image("Yaseen-Photo-6.jpg", caption="Yaseen | Data Scientist")