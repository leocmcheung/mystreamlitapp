import streamlit as st
import requests
import numpy as np

st.write('This is page 2')

query = st.text_input("Enter a word")
url = 'https://api.giphy.com/v1/gifs/search'
params = {'api_key': st.secrets.giphy_api, 'q': query, "limit": 10}
response = requests.get(url, params=params).json()

while not query:
    st.stop()

gif_url = response['data'][np.random.randint(0,10)]['embed_url']
st.write(
    f'<iframe src="{gif_url}" width="800" height="600">',
    unsafe_allow_html=True
)

# st.write(st.secrets['section_1']['spell'])
