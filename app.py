import streamlit as st
from PIL import Image

st.title("Mi Primera App!!")

st.title("HOLA !!! MI NOMBRE xxx")
st.header("En este espacio comienzo a desarrollar un arma que destruirá el planeta.")
st.write("bienvenidos a mi web!!")
image = Image.open('Interfaces Mult2.jpg')
st.image(image, caption = 'Interface multimodales')
