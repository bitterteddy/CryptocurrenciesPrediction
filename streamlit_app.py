#import yfinance as yf
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
from keras.models import load_model
import matplotlib.pyplot as plt
import time

st.title('Uber pickups in NYC1w!')
