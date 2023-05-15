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

# This defines Snowflake connection settings, set in Streamlit config.toml file
if 'snowflake_connection' not in st.session_state:
    st.session_state.snowflake_connection = Session.builder.configs(st.secrets.snowflake).create()
    session = st.session_state.snowflake_connection
else:
    session = st.session_state.snowflake_connection

# Function to get existing from Snowflake
# Reruns the whole Streamlit application if you pass contestant name that 
# doesn't exists in the database -- rerun() -function
def get_current_status():
    # load messages df
    df = session.sql(f""" SELECT * FROM MM_KISAVEIKKAUS.MM_KISAVEIKKAUS_CURRENT_STATUS """)

    try: 
        df.collect()
    except:
        st.experimental_rerun()

    return df

def get_overall_status():
    # load messages df
    df = session.sql(f""" SELECT * FROM MM_KISAVEIKKAUS.MM_KISAVEIKKAUS_OVERALL_STATUS """)

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
        st.empty()
with col3:        
        st.empty()

# Let's get previous prediction from Snowflake
dataset=get_current_status()

st.experimental_data_editor(dataset, height=530, use_container_width=True, num_rows="fixed", disabled=True)

dataset_overall=get_overall_status()

st.experimental_data_editor(dataset_overall, use_container_width=False, num_rows="fixed", disabled=True)
