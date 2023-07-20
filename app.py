import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.title("Series Recommendation System")
# series_df=pickle.load(open("series_rec.pkl","rb"))
series_df= pd.read_pickle("series_rec.pkl")
with open("similarity_series.pkl", "rb") as file:
    similarity = pickle.load(file)
list_series=np.array(series_df['title'])

option=st.selectbox("Select Series",(list_series))

def show_description(series):
    x=[]
    index=series_df[series_df['title']==series].index[0]
    distances=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])

    for i in distances[1:6]:
        x.append("{}".format(series_df.iloc[i[0]].keywords))
    return x


def series_recommendation(series):
    index=series_df[series_df['title']==series].index[0]
    distances=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])
    l=[]
    for i in distances[1:6]:
        l.append("{}".format(series_df.iloc[i[0]].title))
    
    return l

if st.button("Recommend Me"):
    st.write("Series Recommended for you :)")

    df=pd.DataFrame({
        'Series':series_recommendation(option),
        'Keywords': show_description(option)
    })

    st.table(df)
