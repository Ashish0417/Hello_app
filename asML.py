import streamlit as st
import pickle
import pandas as pd
import requests

def poster_path(id):
    response =requests.get("https://api.themoviedb.org/3/movie/{}?api_key=17b13ec2b44d89b27d0c2879137ae47e".format(id))
    data=response.json()
    if(data["poster_path"]!=None):
        return "https://image.tmdb.org/t/p/w185/"+data["poster_path"]
    # st.text(data["poster_path"])streamlit

st.title("Movie recommending system")
movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies_ls=pd.DataFrame(movies_dict)
same=pickle.load(open('same.pkl','rb'))

def recmmend(select):
    suggest=[]
    poster=[]
    indx=movies_ls[movies_ls['title']==select].index[0]
    listi=sorted(list(enumerate(same[indx])),reverse=True,key=lambda x:x[1])[1:6]


    for i in listi:
        movid=movies_ls.iloc[i[0]].movie_id
        suggest.append(movies_ls.iloc[i[0]].title)
        # st.text(movies_ls.iloc[i[0]].title)
        poster.append(poster_path(movid))
    return suggest,poster


option = st.selectbox(
    'How would you like to be contacted?',
    movies_ls['title'].values

    )
# st.button("Reset", type="primary")
recmmend((option))
if st.button('Recommend'):
    suggest,poster=recmmend(option)
    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.text(suggest[0])
        st.image(poster[0])

    with col2:
        st.text(suggest[1])
        st.image(poster[1])

    with col3:
        st.text(suggest[2])
        st.image(poster[2])

    with col4:
        st.text(suggest[3])
        st.image(poster[3])

    with col5:
        st.text(suggest[4])
        st.image(poster[4])