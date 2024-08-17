import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from scipy.optimize import minimize
import streamlit as st

# Creando titulo
st.title("K-means Clustering con Streamlit")

#Subir Archivo
uploaded_file = st.file_uploader("Sube un archivo excel", type=["elsx"])