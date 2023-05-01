import streamlit as st
from datetime import datetime
from snowflake.snowpark import Session
import streamlit.components.v1 as components
import pandas as pd
import base64
import json
import re

# This function defines what we see in the browser window
# Must be always the first function within Streamlit application
st.set_page_config(
    page_title="Recordly MM-kisaveikkaus",
    page_icon=":ice_hockey_stick_and_puck:",
    layout="centered",
    initial_sidebar_state="collapsed"
)
       
st.title("Instructions")
st.header("How to input your prediction")
st.write("Input your predictions by using provided forms. You can modify your existing prediction by using the\nseparate application.")
st.write("Updating your prediction will overwrite the existing and previous prediction. The system doesn't take backups.")
st.write("")
st.header("Scoring")
st.write("Let's consider a match between France and Slovakia")
st.write("You make a prediction that France will win by 3-2")
st.write("* If the game ends 3-2, you'll get three (3) points from correct score.")
st.write("* If the game ends 4-2, you'll get one (1) point for knowing the correct winner")
st.write("* In case two or more people end up in the same points, person how has added his predictions first has the upper hand.")
st.write(" ")
st.header("Participation Bet")
st.write("20 euros for each participant. Bet must be payed before first game")
st.header("Prize and share of prizes")
st.write("TBA - customized")
st.write("1. 60%")
st.write("2. 30%")
st.write("3. 10%")
