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
import gspread
import streamlit
from google.oauth2.service_account import Credentials
import pandas as pd
from datetime import datetime



# ---------- Connect to Google Sheet ----------
def connect_sheet(sheet_name):
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_info(
        streamlit.secrets["gspread"],
        scopes=scopes
    )
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1
    return sheet



# ---------- Append mood ----------
def append_mood(sheet, mood, note):
    """Append a new mood entry to the sheet with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([timestamp, mood, note])



# ---------- Retrieve today's mood data ----------
def get_today_data(sheet):
    """Fetch data for the current day from the sheet."""
    df = pd.DataFrame(sheet.get_all_records())
    if df.empty:
        return df
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    today = pd.Timestamp.today().normalize()
    return df[df['timestamp'] >= today]