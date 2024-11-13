import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather Forecast for Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help ="Select the number of forecasted days.")
option = st.selectbox("Select data to view",
                      ("Temperature","Sky"))

st.subheader(f"{option} for the next {days} days in {place.title()}")

data = get_data(place, days, option)

def get_data(days):
    dates =["2024-10-10", "2024-10-11", "2024-10-12"]
    temperatures =[10, 15, 12]
    temperatures = [days * i for i in temperatures]
    return dates,temperatures

d, t = get_data(days)

figure = px.line(x=d, y=t, labels ={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)

