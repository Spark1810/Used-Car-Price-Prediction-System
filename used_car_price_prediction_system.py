import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import pickle
from PIL import Image
import time

sns.set()

st.title("USED CAR PRICE PREDICTION SYSTEM") 

activities = ["Introduction", "Prediction","About Us"]
choice = st.sidebar.selectbox("Select Activities", activities)
if choice == 'Introduction':
    st.markdown("             Welcome to our Car Price Prediction System! The Used Car Price Prediction System is an application designed to estimate the price of a used car based on various factors and market trends. It utilizes a combination of historical car data, machine learning algorithms, and predictive modeling techniques to generate accurate price predictions. The system aims to assist car buyers, sellers, and enthusiasts in making informed decisions by providing them with an estimated price range for a used car. By analyzing factors such as the car's make, model, year, mileage, condition, fuel type, and other relevant parameters, the system generates predictions that take into account market demand, depreciation rates, and the impact of different variables on car values.")
    st.subheader("Usage")
    st.markdown("To run this Streamlit application, you need to have Streamlit installed.")
    st.markdown("Save the code in a Python file, e.g., car_price_prediction.py.")
    st.markdown("Open a terminal or command prompt and navigate to the directory containing the file.")
    st.markdown("Run the command 'streamlit run car_price_prediction.py'.")
    st.markdown("The application will start running, and you can interact with it in a web browser.")
    st.markdown("Select the desired activity (Introduction, Prediction, or About Us) using the sidebar.")
    st.markdown("Follow the instructions provided in each activity to input the necessary information or view the relevant content.")
    
# ==========================================================================================================================

elif choice == 'Prediction':
    import matplotlib.pyplot as plt

    st.title("Check Your Car Price...")
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # ============================================================================================================================================    PREDICTION

    age = st.selectbox(
        "YEAR ",
        ('2020 to 2023', '2017 to 2020', '2015 to 2017', '2013 to 2015', '2010 to 2013', '2007 to 2010', '2005 to 2007', '2000 to 2005', '2000 or Before')
    )
    if age == '2020 to 2023':
        age = 1
    elif age == "2017 to 2020":
        age = 2
    elif age == "2015 to 2017":
        age = 3
    elif age == "2013 to 2015":
        age = 4
    elif age == "2010 to 2013":
        age = 5
    elif age == "2007 to 2010":
        age = 6
    elif age == "2005 to 2007":
        age = 7
    elif age == "2000 to 2005":
        age = 8
    else:
        age = 9
    Price = st.number_input("Current Showroom Price (in Lakhs)")
    User = st.slider("Number of Previous Owner", max_value=5)
    km = st.number_input("Kilometers Driven")
    st.selectbox(
        "Fuel Type",
        ("Petrol", "Diesel")
    )
    st.write(" ")
    if st.button('Calculate'):
        res=Price-(5*(User+1)*Price/100)-(2*age*Price/100)-(((km+1)/100000)*Price/100)
        res2=Price-(5*(User+1)*Price/100)-(2*age*Price/100)-(Price-((User+1)*Price/100)-(age*Price/100))/80
        st.success("Predicted Prize of Car : "+str(res), icon="✅")
        st.balloons()
        time.sleep(3)
        st.warning('Minimum Expected Prize : '+str(res2), icon="⚠️")
        




# ===============================================================================

elif choice == 'Dashboard':
    import matplotlib.pyplot as plt

    st.title("DEMENTIA REPORT ")

    import mysql.connector

    con = mysql.connector.connect(host='localhost', user='root', passwd='', database='')
    mycursor = con.cursor()
    import pandas as pd
    import streamlit as st

    mycursor.execute("USE demen")
    mysql = "select*from udb2"
    mycursor.execute(mysql)
    data = mycursor.fetchall()
    df3 = pd.DataFrame({
        'PATIENT ID': [],
        'GENDER': [],
        'AGE GROUP': [],
        'YEARS OF EDUCATION': [],
        'MMSE': [],
        'SES': [],
        'ETIV': [],
        'NWBV': [],
        'ASF': [],
        'RESULT': []
    })
    # EMPTY TABLE VIEW
    # st.table(df3)
    for data2 in data:
        new_row = {"PATIENT ID": data2[0], "GENDER": data2[1], "AGE GROUP": data2[2], "YEARS OF EDUCATION": data2[3],
                   "MMSE": data2[4], "SES": data2[5], "ETIV": data2[6], "NWBV": data2[7], "ASF": data2[8],
                   "RESULT": data2[9]}
        df3 = df3.append(new_row, ignore_index=True)
    # Display the updated dataframe as a table in Streamlit
    # st.table(df3)

    import streamlit as st
    import pandas as pd
    import bamboolib as bam
    import plotly.express as px

    # Create a bamboolib dataframe
    df3
    bam.enable()

    # Streamlit components
    st.header('Data Exploration and Manipulation')
    st.subheader(' ')

    # Add data exploration and manipulation steps using bamboolib
    col1, col2 = st.columns(2)

    # Add checkboxes to the first column
    with col1:
        st.set_option('deprecation.showPyplotGlobalUse', False)
        if st.checkbox("Correlation Plot"):
            plt.matshow(df3.corr())
            st.pyplot()

    # Add the filtered DataFrame to the second column
    with col2:
        if st.checkbox("Summary"):
            st.write(df3.describe())
    st.subheader(' ')
    st.subheader('Filtering Columns ')

    selected_column = st.selectbox('Select Column', df3.columns)

    # ======================================================================

    unique_values = df3[selected_column].unique()

    # Create a multiselect dropdown with the unique values
    selected_values = st.multiselect('Select Values to Filter ', unique_values)

    # Filter the DataFrame based on the selected values
    filtered_df = df3[df3[selected_column].isin(selected_values)]

    # Display the filtered DataFrame
    st.write(filtered_df)
    st.subheader(' ')
    st.subheader('Aggregation Function ')

    selected_function = st.selectbox('Select Function', ['Mean', 'Sum', 'Max', 'Min'])

    # Display the results
    st.subheader(f'{selected_function} of {selected_column}')
    st.write(df3.groupby(selected_column).agg(selected_function.lower()))

    # ======================================================================
    st.subheader(' ')
    st.subheader('Visualizations ')
    # Add data exploration and manipulation steps using bamboolib
    col3, col4 = st.columns(2)

    # Add checkboxes to the first column
    with col3:
        st.set_option('deprecation.showPyplotGlobalUse', False)
        column = st.selectbox('Select column to plot Y axis', df3.columns)
        column2 = st.selectbox('Select column to plot X axis', df3.columns)
        chart_type = st.radio('Select Chart Type', ('Line Chart', 'Bar Chart', 'Scatter Plot', 'Pie Chart'))
        if chart_type == 'Line Chart':
            chart = px.line(df3, x=column2, y=column)
        elif chart_type == 'Bar Chart':
            chart = px.bar(df3, x=column2, y=column)
        elif chart_type == 'Scatter Plot':
            chart = px.scatter(df3, x=column2, y=column)
        elif chart_type == 'Pie Chart':
            chart = px.pie(df3, values=column2, names=column)

    # Add the filtered DataFrame to the second column
    with col4:
        st.plotly_chart(chart)

# ============================================================================================
elif choice == "About Us":
    st.header("CREATED BY _**SUDHARSHAN VIJAY SK**_")
    st.subheader("Know More @ https://github.com/Spark1810")

