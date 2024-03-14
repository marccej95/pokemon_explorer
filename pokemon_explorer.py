import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import requests
import numpy as np

st.title("Pokemon Explorer!")

def get_details(poke_number):
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{poke_number}/"
        response = requests.get(url)
        pokemon = response.json()
        return pokemon["name"], pokemon["height"], pokemon["weight"], len(pokemon["moves"]), pokemon["types"][0]["type"]["name"], pokemon["sprites"]["front_default"], pokemon["sprites"]["front_shiny"], pokemon["cries"]["latest"]
    except Exception as error:
        return error, np.NAN, np.NAN, np.NAN, np.NaN, np.NaN, np.NaN, np.NaN


## Input number to get pokemon
pokemon_number = st.number_input("Pick a pokemon", min_value=1, max_value=1025)

colour_mapper = {"normal":"#00b3b3",
                 "fire":"#ffa64d", 
                 "water":"#6699ff", 
                 "grass":"#00cc66", 
                 "flying":"#66ccff", 
                 "fighting":"#ff0066", 
                 "poison":"#cc00ff", 
                 "electric":"#ffff00", 
                 "ground":"#996633", 
                 "rock":"#b8b894", 
                 "psychic":"#ff6666", 
                 "ice":"#66ffff", 
                 "bug":"#33cc33", 
                 "ghost":"#0099ff", 
                 "steel":"#79a6d2", 
                 "dragon":"#3366cc", 
                 "dark":"#006666", 
                 "fairy":"#cc99ff"}


name, height, weight, moves, type, img_url, shiny_url, cry_url = get_details(pokemon_number)
height = height/10
weight = weight/100

height_data = pd.DataFrame(data={"Pokemon": ["Weedle", name, "Dragonair"], "Heights": [0.3,height,4]})

colors = ["gray",colour_mapper[type],"gray"]

graph = sns.barplot(data=height_data, x="Pokemon", y="Heights", palette=colors)

left_co, cent_co, right_co = st.columns(3)

with cent_co:
    st.image(img_url, width=200)
    st.write("Normal Sprite")
    st.image(shiny_url, width=200)
    st.write("Shiny Sprite")
st.audio(cry_url)
st.write(f"Name: {name.capitalize()}")
st.write(f"Type: {type.capitalize()}")
st.write(f"Height: {height}m")
st.write(f"Weight: {weight}kg")
st.write(f"Move Count: {moves}")


st.pyplot(graph.figure)
