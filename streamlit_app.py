import appdirs as ad
ad.user_cache_dir = lambda *args: "/tmp"
import yfinance as yf
import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC1')
