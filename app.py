import streamlit as st
from recipe_tools import EnhancedRecipeTools
import os

# Set up your tools
recipe_tools = EnhancedRecipeTools('processed_indian_recipes.csv')

st.title("🍛 AI Rasoi - Your Kitchen Assistant")
ingredients = st.text_input("What ingredients do you have?")
if ingredients:
    recipes = recipe_tools.find_recipes([ingredients])
    st.write(recipes)
