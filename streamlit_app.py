# Use a non-existing directory for ease of testing
import appdirs as ad

ad.user_cache_dir = lambda *args: ".cache"

# If the ad.user_cache_dir directory doesn't exist, this fails
import yfinance as yf
import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')
