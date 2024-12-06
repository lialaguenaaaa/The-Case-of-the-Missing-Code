# The Case of the Missing Code

## Overview
A detective game where players solve the mystery of a missing data scientist, Dr. Ada Bytes, using predictive analytics.

## Features ⬤
Data Detective Hunt Game: "The Case of the Missing Code"
Objective
Create an engaging interactive Python-based detective game where players solve the mystery of a missing data scientist using predictive analytics. This game incorporates data cleaning, exploration, modeling, and visualization tasks, leveraging Python libraries for interactive gameplay.

Game Overview
Theme: The Case of the Missing Code
A renowned data scientist, Dr. Ada Bytes, has vanished under mysterious circumstances. Players are hired as "data detectives" to uncover what happened by analyzing datasets, solving puzzles, and building predictive models. The players' mission is to locate Dr. Bytes and uncover the culprit behind her disappearance.

Core Components
1. Theme
Title: The Case of the Missing Code
Story: Dr. Ada Bytes was working on a revolutionary predictive analytics model when she suddenly disappeared. Her last-known dataset holds the clues to her whereabouts. Can you solve the mystery?
Player Role: Data detectives tasked with uncovering hidden patterns and anomalies.

2. Dataset
Type: Synthetic dataset (employee metadata, work logs, suspicious communications, geolocation data).
Features:
Employee activity logs (timestamps, projects, unusual patterns).
Communication patterns (frequency, sentiment analysis).
Geographic data (office access logs, map coordinates).

3. Game Flow
Introduction
Animated story intro using Python's Rich library or Streamlit for a polished UI.
"You’ve been called to investigate Dr. Bytes’ disappearance. Her last dataset might be the key!"
Challenges
Data Cleaning Task
Identify and fix missing, inconsistent, or corrupted data points in the activity logs.
Tools: Pandas and NumPy.
Goal: Prepare the dataset for exploration.
Data Exploration Task
Analyze employee activity logs for anomalies (e.g., someone accessing restricted areas).
Tools: Matplotlib, Seaborn, and Plotly.
Goal: Visualize patterns and identify potential suspects.
Predictive Modeling Task
Build a classification model to predict Dr. Bytes’ movements based on historical data.
Tools: Scikit-learn (Decision Trees, KNN).
Goal: Narrow down the location and identify the most likely culprit.
Visualization Task
Use geolocation data to map movements.
Tools: Folium or Plotly for interactive maps.
Goal: Uncover Dr. Bytes' last known location.

4. Coding Requirements
Interactive Gameplay:
Streamlit: For a web-based interface.
Rich: For terminal-based storytelling with colorful graphics.
AI Integration:
ChatGPT API: Provides clues when players struggle.
AutoML (e.g., H2O): Automatically validates player-built models and suggests improvements.
Predictive Analytics:
Regression: Predict the timeline of events.
Clustering: Analyze activity logs for outliers.

5. Delivery
GitHub Hosting:
Game repository includes:
Codebase with modular design.
Comprehensive README with setup instructions.
Sample synthetic dataset.
Hosted game demo link (via Streamlit or other platforms).
Documentation:
Markdown-based story walkthrough.
Flowchart of game mechanics.
Guide for instructors on testing.

Evaluation Criteria
Game Design and Engagement (50%)
Intuitive and immersive gameplay.
Engaging storyline with seamless task integration.
Predictive Analytics Implementation (30%)
Effective data cleaning, exploratory analysis, and modeling.
Clear, meaningful visualizations to advance the narrative.
Code Quality and Documentation (20%)
Clean, modular, and commented code.
Comprehensive README with gameplay instructions and methodology.

Example Deliverable:
Title: The Case of the Missing Code
Gameplay: Players uncover Dr. Bytes’ whereabouts by solving data puzzles.
Tasks: Clean data, find anomalies, build models, and create visualizations.
Output: Players identify the culprit and Dr. Bytes’ location.
