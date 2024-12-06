import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import folium

# Load the dataset
@st.cache
def load_data():
    return pd.read_csv('employee_data.csv')

# Data Cleaning Function
def clean_data(df):
    df.dropna(inplace=True)  # Drop missing values
    return df

# Data Exploration Function
def explore_data(df):
    st.subheader("Data Exploration")
    st.write(df.describe())
    st.write("Access Location Counts:")
    st.bar_chart(df['access_location'].value_counts())

# Predictive Modeling Function
def predict_movement(df):
    st.subheader("Predictive Modeling")
    df['label'] = np.where(df['access_location'] == 'Restricted Area', 1, 0)  # Label for classification
    X = df[['employee_id', 'project']]
    y = df['label']
    
    # Convert categorical variables to numeric
    X = pd.get_dummies(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    
    accuracy = model.score(X_test, y_test)
    st.write(f"Model Accuracy: {accuracy:.2f}")

# Geolocation Visualization Function
def visualize_geolocation(df):
    st.subheader("Geolocation Visualization")
    map_center = [df['geolocation'].apply(lambda x: eval(x)[0]).mean(), df['geolocation'].apply(lambda x: eval(x)[1]).mean()]
    m = folium.Map(location=map_center, zoom_start=2)
    
    for loc in df['geolocation']:
        folium.Marker(location=eval(loc)).add_to(m)
    
    st.write(m)

# Main Game Logic
def main():
    st.title("The Case of the Missing Code")
    st.write("Welcome, Data Detective! Your mission is to uncover the mystery of Dr. Ada Bytes' disappearance.")
    
    df = load_data()
    cleaned_df = clean_data(df)
    
    if st.button("Explore Data"):
        explore_data(cleaned_df)
    
    if st.button("Predict Movement"):
        predict_movement(cleaned_df)
    
    if st.button("Visualize Geolocation"):
        visualize_geolocation(cleaned_df)

if __name__ == "__main__":
    main()
