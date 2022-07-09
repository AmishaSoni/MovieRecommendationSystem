import streamlit as st
import pickle

movies_list=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
st.write("Movies Recommender")
selected_movie=st.selectbox("Select a Movie", movies_list['title'].values, index=3)

def recommend(movie):
    movie_index=movies_list[movies_list['title']==movie].index[0]
    movies_itr=sorted(list(enumerate(similarity[movie_index])),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in movies_itr:
        recommended_movies.append(i[0])
    return recommended_movies

if st.button("recommend"):
    for i in recommend(selected_movie):
       st.write(movies_list.iloc[i].title)

