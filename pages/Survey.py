# This creates the page for users to input data.
# The collected data should be appended to the 'data.csv' file.

import streamlit as st
import pandas as pd
import os.path
import os # The 'os' module is used for file system operations (e.g. checking if a file exists).

if "inititalWaterAmnt" not in st.session_state:
    st.session_state["initialWaterAmount"] = 0
if "initialDaySelect" not in st.session_state:
    st.session_state["initialDaySelect"] = "Monday"

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Water Survey",
    page_icon="💦",
)

# PAGE TITLE AND USER DIRECTIONS
st.title("Data Collection Survey 💦")
st.write("Please fill out the form below to add how much water you drink to the dataset.")

# DATA INPUT FORM
# 'st.form' creates a container that groups input widgets.
# The form is submitted only when the user clicks the 'st.form_submit_button'.
# This is useful for preventing the app from re-running every time a widget is changed.
with st.form(key = "survey_form", clear_on_submit=True):
    # Create text input widgets for the user to enter data.
    # The first argument is the label that appears above the input box.
    st.subheader("Choose the day of the week!")
    category_input = st.radio(
        "Select the Day of the Week",
        ("Monday", "Tuesday", "Wednesday", "Friday", "Saturday", "Sunday"),
                                  key = "dayRadio", horizontal=True)
    value_input = st.number_input( "How many ounces of water did you drink today?",
                                  min_value = 0, max_value=500, step = 1,
                                  key = "Amount of Water" )

    # The submit button for the form.
    submitted = st.form_submit_button("Submit Data")

    # This block of code runs ONLY when the submit button is clicked.
    if submitted:
        # --- YOUR LOGIC GOES HERE ---
        # TO DO:
        # 1. Create a new row of data from 'category_input' and 'value_input'.
        categoryInput = st.session_state["dayRadio"]
        valueInput = st.session_state["Amount of Water"]

        newRow = f"{categoryInput}, {valueInput}\n"
        csv_file = "data.csv"

        try:
            with open(csv_file, "a") as k:
                k.write(newRow)
            st.success("Your data has been submitted!")
        except Exception:
            st.error(f"An error occurred: {Exception}")
        
        #    - You can use pandas or Python's built-in 'csv' module.
        #    - Make sure to open the file in 'append' mode ('a').
        #    - Don't forget to add a newline character '\n' at the end.
        
        st.write(f"You entered: **Category:** {category_input}, **Value:** {value_input}")
        st.write("After you input all your values, look to the sidebar on the left. Go to the Visualization page to see the graphs!")


# DATA DISPLAY
# This section shows the current contents of the CSV file, which helps in debugging.
#st.divider() # Adds a horizontal line for visual separation.
#st.header("Current Data in CSV")

# Check if the CSV file exists and is not empty before trying to read it.
#if os.path.exists('data.csv') and os.path.getsize('data.csv') > 0:
    # Read the CSV file into a pandas DataFrame.
    #current_data_df = pd.read_csv('data.csv')
    # Display the DataFrame as a table.
    #st.dataframe(current_data_df)
#else:
    #st.warning("The 'data.csv' file is empty or does not exist yet.")

