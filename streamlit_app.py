import numpy as np
import pandas as pd
import yfinance as yf
from keras.models import load_model
import streamlit as st
import matplotlib.pyplot as plt

st.header('Stock Market Predictor')

stock =st.text_input('Enter Stock Symnbol', 'GOOG')
start = '2012-01-01'
end = '2022-12-31'

st.subheader('Stock Data')
