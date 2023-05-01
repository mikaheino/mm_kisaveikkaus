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

# This remove function is used to clean string inputs
def remove(s):
    # Pattern for matching whitespaces
    pattern=r"\s+"

    # Using re.sub() function to remove whitespaces
    s = re.sub(pattern, "", s)
    s = s.upper()

    return s

# This function injects CSS elements, in this case a custom background image from URL
# and changes the button to behave differently during hovering
def inject_css():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.cdn.yle.fi/image/upload/f_auto,c_limit,w_3840,q_auto/v1599548793/13-1-4292051-cover-1512048543525");
             background-attachment: fixed;
             background-size: cover
         }}
        div.stButton >
            button:first-child {{
            background-color: #FFFFFF;
            }}
         div.stButton > 
            button:hover {{
            background-color: #000000;
            transition: 1.0s;
            color:#DEFF16;
        }}
        [data-testid="stForm"] {{border: 0px}}
        div[data-testid="column"]:nth-of-type(1){{text-align: end;}} 
        div[data-testid="column"]:nth-of-type(2){{text-align: end;}} 
        div[data-testid="column"]:nth-of-type(3){{text-align: end;}}
         
         </style>
         """,
         unsafe_allow_html=True
     )

inject_css()


# This function defines new header style to be used with fonts
# Used to show error messages
def header(url):
     st.markdown(f'<p style="background-color: transparent;color:#FFFFFF;font-size:36px;font-weight:bold;border-radius:2%;">{url}</p>', unsafe_allow_html=True)


# This function is used in the SQL insert that sets the update time of the prediction
now = datetime.now()
date_time = now.strftime("%Y_%d_%m_%H%M%S")


# This defines Snowflake connection settings, set in Streamlit config.toml file
if 'snowflake_connection' not in st.session_state:
    st.session_state.snowflake_connection = Session.builder.configs(st.secrets.snowflake).create()
    session = st.session_state.snowflake_connection
else:
    session = st.session_state.snowflake_connection

# Function to get existing from Snowflake
# Reruns the whole Streamlit application if you pass contestant name that 
# doesn't exists in the database -- rerun() -function
def get_old_dataset():
    # load messages df
    prediction = contestant.upper() + "_MM_KISAVEIKKAUS"
    df = session.sql(f""" SELECT id, match_day, match, home_team_goals, away_team_goals FROM {prediction} """)

    try: 
        df.collect()
    except:
        st.experimental_rerun()

    return df

# Here we actually start building the Streamlit application
#
# Let's load custom banner, which contains the logos
# and place a text input after that in the middle using columns. 
# We'll use the text input later on as input for SQL injection
st.image('logo.png')

col1, col2, col3 = st.columns(3)

with col1:
        st.empty()
with col2:        
        contestant = st.text_input('Contestant Name', max_chars=20, placeholder="Contestant Name", label_visibility="hidden")
with col3:        
        st.empty()

# Clean the input
contestant = remove(contestant)

# Let's get previous prediction from Snowflake
@st.cache_data
dataset=get_old_dataset()

with st.form("data_editor_form"):
        
        edited = st.experimental_data_editor(dataset, width=1500, height=2000, use_container_width=False, num_rows="fixed")
        col1, col2 = st.columns(2)
        with col1:
                st.empty()
        with col2:
                submit_button = st.form_submit_button("Overwrite existing")   

# This add new column to show when the prediction was inputted update date
edited.insert(loc=5, column='INSERTED', value=date_time)
edited.insert(loc=6, column='POINTS', value='X')

if submit_button:
            
            try:
                prediction = contestant + "_MM_KISAVEIKKAUS"
                # Write to database
                session.write_pandas(edited, prediction, auto_create_table=True, overwrite=True)
                header('Predictions have been updated')  
                time(5)
                st.cache_data.clear()

            except:
                st.warning("Error updating table")
                #display success message for 5 seconds and update the table to reflect what is in Snowflake
                st.experimental_rerun()
