#  Import Virtual Environment for API Key
from dotenv import load_dotenv
load_dotenv()

# Import Important Libraries
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

#Load Model & Gemini Model
model=genai.GenerativeModel("gemini-pro")

# Define a data structure to store poem elements (e.g., a list of verses):
poem=[]


#Use Streamlit for initial Structure of Poem
st.title('Interactive Poetry Teller')
# Provide clear instructions for the user
st.info("Please choose a verse structure and enter the initial verse to start the interactive poetry experience.")
topic=st.text_input("Enter Poetry Topic:")
verse_structure=st.selectbox('Select Verse Structure:',["Couplet","Quatrain", "Free Verse"])
initial_verse=st.text_input("Enter the first Verse:")

#Create a function to generate the next verse using Gemini:
def generate_next_verse(poem):
    prompt=" ".join(poem) + " Continue the poem in similar style "
    response=model.generate_content(prompt)
    response=response.text

     # Extract verses based on selected structure
    if verse_structure=="Couplet":
        verses=response.split("\n")[:2] # Spilt into two verses
    elif verse_structure=="Quatrain":
        verses=response.split("\n")[:4] # Split into four verses
    else:
        verses=[response] # Free Verses

    poem.extend(verses)
    return verses

#Allow users to choose different poem directions (e.g., tone, imagery):
next_verses=generate_next_verse(poem)
st.subheader('Generated Poem')
st.markdown(" ".join(next_verses))

st.subheader('Mood of Poetry')
choice1=st.button('Continue with a hopeful and optimistic tone')
choice2=st.button('Shift the poem towards a more reflective and melancholic tone')

if choice1:
     st.write(next_verses)
elif choice2:
     st.write(next_verses)

#Provide an option to save the poem as a text file:

if st.button('Copy Poem from above Clipboard'):
    with open('Poem.txt',"w") as f:
        f.write("\n".join(poem))
    
    




    