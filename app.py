# -----------------------------------------------
# Take-Home Assignment: Mood of the Queue
# Author: Serene Zan
# Date: May 22, 2024
#
# Description:
# A simple Streamlit app to log and visualize mood entries for support ticket queue.
# Data is stored in Google Sheets.
# -----------------------------------------------



# ---------- Imports ----------
import streamlit as st
import plotly.express as px
from gsheets_utils import connect_sheet, append_mood, get_today_data



# ---------- Connect to Google Sheet ----------
SHEET_NAME = "MoodLog"
sheet = connect_sheet(SHEET_NAME)



# ---------- Form to log mood ----------
st.title("Mood of the Queue")
with st.form("mood_form"):
    mood = st.selectbox("Select your mood", ["😊", "😠", "😕", "🎉"])
    note = st.text_input("Optional note")
    submitted = st.form_submit_button("Submit")
    if submitted:
        append_mood(sheet, mood, note)
        st.success("Mood logged.")



# ---------- Display mood data ----------
df = get_today_data(sheet)
if not df.empty:
    mood_counts = df['mood'].value_counts().reset_index()
    mood_counts.columns = ['Mood', 'Count']
    fig = px.bar(mood_counts, x='Mood', y='Count', title='Mood Counts Today')
    st.plotly_chart(fig)
else:
    st.write("No mood data for today yet.")