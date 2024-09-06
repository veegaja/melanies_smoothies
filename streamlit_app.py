# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

cnx = st.connection('snowflake')
session=cnx.session



