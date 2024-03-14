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

type_mapper = {"normal":"https://archives.bulbagarden.net/media/upload/4/46/NormalIC_SM.png",
                "fire":"https://archives.bulbagarden.net/media/upload/a/a9/FireIC_SM.png", 
                "water":"https://archives.bulbagarden.net/media/upload/c/c3/WaterIC_SM.png", 
                "grass":"https://archives.bulbagarden.net/media/upload/3/33/GrassIC_SM.png", 
                "flying":"https://archives.bulbagarden.net/media/upload/b/b1/FlyingIC_SM.png", 
                "fighting":"https://archives.bulbagarden.net/media/upload/a/a5/FightingIC_SM.png", 
                "poison":"https://archives.bulbagarden.net/media/upload/8/86/PoisonIC_SM.png", 
                "electric":"https://archives.bulbagarden.net/media/upload/5/58/ElectricIC_SM.png", 
                "ground":"https://archives.bulbagarden.net/media/upload/c/c5/GroundIC_SM.png", 
                "rock":"https://archives.bulbagarden.net/media/upload/6/65/RockIC_SM.png", 
                "psychic":"https://archives.bulbagarden.net/media/upload/0/05/PsychicIC_SM.png", 
                "ice":"https://archives.bulbagarden.net/media/upload/0/00/IceIC_SM.png", 
                "bug":"https://archives.bulbagarden.net/media/upload/3/35/BugIC_SM.png", 
                "ghost":"https://archives.bulbagarden.net/media/upload/2/2a/GhostIC_SM.png", 
                "steel":"https://archives.bulbagarden.net/media/upload/b/be/SteelIC_SM.png", 
                "dragon":"https://archives.bulbagarden.net/media/upload/d/db/DragonIC_SM.png", 
                "dark":"https://archives.bulbagarden.net/media/upload/c/c8/DarkIC_SM.png", 
                "fairy":"https://archives.bulbagarden.net/media/upload/2/25/FairyIC_SM.png"}

name, height, weight, moves, type, img_url, shiny_url, cry_url = get_details(pokemon_number)
height = height/10
weight = weight/100

height_data = pd.DataFrame(data={"Pokemon": ["Weedle", name.capitalize(), "Dragonair"], "Height (m)": [0.3,height,4]})

colors = ["gray",colour_mapper[type],"gray"]

graph = sns.barplot(data=height_data, x="Pokemon", y="Height (m)", palette=colors)

col_1, col_2, col_3, col_4 = st.columns(4)

with col_1:
    st.image(img_url, width=200)
    st.write("Normal Sprite")

with col_2:
    st.image(shiny_url, width=200)
    st.write("Shiny Sprite")

with col_3:
    st.write("Name: ")
    st.write("Type: ")
    st.write("Height: ")
    st.write("Weight: ")
    st.write("Move Count: ")

with col_4:
    st.write(name.capitalize())
    st.image(type_mapper[type], width=70)
    st.write(str(height)+"m")
    st.write(str(weight)+"kg")
    st.write(str(moves))

st.audio(cry_url)

st.pyplot(graph.figure)
