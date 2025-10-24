# This creates the page for displaying data visualizations.
# It should read data from both 'data.csv' and 'data.json' to create graphs.

import streamlit as st
import pandas as pd
import json # The 'json' module is needed to work with JSON files.
import os   # The 'os' module helps with file system operations.

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",
)

# PAGE TITLE AND INFORMATION
st.title("Data Visualizations 📈")
st.write("This page displays graphs based on the collected data.")


# DATA LOADING
# A crucial step is to load the data from the files.
# It's important to add error handling to prevent the app from crashing if a file is empty or missing.

st.divider()
st.header("Load Data")

# TO DO:
# 1. Load the data from 'data.csv' into a pandas DataFrame.
#    - Use a 'try-except' block or 'os.path.exists' to handle cases where the file doesn't exist.
# 2. Load the data from 'data.json' into a Python dictionary.
#    - Use a 'try-except' block here as well.

try:
    if os.path.exists("data.csv") and os.path.getsize("data.csv") > 0:
        allData = pd.read_csv("data.csv", names = ["Category", "Value"], header = None)
        st.info(f"Successfully loaded {len(allData)} data from data.csv")
    else:
        raise FileNotFoundError("data.csv does not exist or is empty.")
    st.info(f"Completed loaded all {len(allData)} records from data.csv.")
except FileNotFoundError:
    st.error(f"Error: {FileNotFoundError} Please submit data from the Survey page first!")
    allData = pd.DataFrame({"Category":[], "Value":[]})
    st.stop()

try:
    if os.path.exists("data.json") and os.path.getsize("data.json") > 0:
        with open("data.json", "r") as o:
            jsonData = json.load(o)
        allJsonData = pd.DataFrame(jsonData["data_points"])
        st.info(f"Successfully loaded {len(allJsonData)} data from data.json.")
    else:
        raise FileNotFoundError("data.json does not exist or is empty.")
except FileNotFoundError:
    st.error(f"Error: {FilleNotFound} JSON data will be empty.")
    allJsonData = pd.DataFrame({"Label": [], "Value": []})

# GRAPH CREATION
# The lab requires you to create 3 graphs: one static and two dynamic.
# You must use both the CSV and JSON data sources at least once.

st.divider()
st.header("Graphs")

# GRAPH 1: STATIC GRAPH
st.subheader("Graph 1: Daily Water Intake Average v.s the Goal of 125 oz")
# TO DO:
# - Create a static graph (e.g., bar chart, line chart) using st.bar_chart() or st.line_chart().
# - Use data from either the CSV or JSON file.
# - Write a description explaining what the graph shows.
if allData.empty:
    st.warning("Placeholder for the first graph")
else:
    overallAvg = allData["Value"].mean()
    staticChartData = pd.DataFrame({
        "Measurement": ["Average Water Intake", "Goal"],
        "Amount": [overallAvg, 125]
        })
    st.bar_chart(staticChartData, x = "Measurement", y = "Amount")
# This graph shows the average daily water intake vs the average goal of 125 oz of water daily.


# GRAPH 2: DYNAMIC GRAPH
st.subheader("Graph 2: Daily Water Intake filtered by day") 
# TODO:
# - Create a dynamic graph that changes based on user input.
# - Use at least one interactive widget (e.g., st.slider, st.selectbox, st.multiselect).
# - Use Streamlit's Session State (st.session_state) to manage the interaction.
# - Add a '#NEW' comment next to at least 3 new Streamlit functions you use in this lab.
# - Write a description explaining the graph and how to interact with it.
if allData.empty:
    st.warning("Placeholder for your second graph.")
else:
    dayChoice = st.selectbox(
        "First Input: Filter Data by Day", # NEW
        options = ["All Days"] + list(allData["Category"].unique()), 
        key = "first_input"
        )
    if dayChoice == "All Days":
        dynamicChoice = allData.copy()
    else:
        dynamicChoice = allData[allData["Category"] == dayChoice]

    st.scatter_chart(dynamicChoice, x = "Category", y = "Value") # NEW
    st.session_state["dayChoice_filter"] = dayChoice # NEW

# This graph shows the daily water intake in a scatter chart.
# The way you interact with it is by choosing which day you would like to see the specific water intake.
# I looked up in Google on what could be efficient to access values on columns and it resulted in .unique().


# GRAPH 3: DYNAMIC GRAPH
st.subheader("Graph 3: Daily Water submitted above a threshold") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TO DO:
# - Create another dynamic graph.
# - If you used CSV data for Graph 1 & 2, you MUST use JSON data here (or vice-versa).
# - This graph must also be interactive and use Session State.
# - Remember to add a description and use '#NEW' comments.

if allJsonData.empty:
    st.warning("Placeholder for your second graph.")
else:
    min_val = int(allJsonData["value"].min())
    max_val = int(allJsonData["value"].max())
    minValueChoice = st.slider(
        "Second Input: Exercise Time correlating with Water Intake", # NEW
        min_value = min_val,
        max_value = max_val,
        value = min_val,
        step = 5,
        key = "second_input_slider"
        )
    otherDynamicChoice = allJsonData[allJsonData["value"] >= minValueChoice] # NEW
    st.line_chart(otherDynamicChoice, x = "label", y = "value") # NEW

    st.session_state["minValChoice_filter"] = minValueChoice
# This graph lets the user raise the minimum exercise time to see which water intake levels result in the longer workouts.
