# Mood of the Queue

A lightweight tool to **log and visualize the mood** of a support ticket queue, built with Python, Streamlit, and Google Sheets.

---

## Features

- Log moods using emojis: 😊 😠 😕 🎉
- Add optional context notes
- Store entries in Google Sheets via Service Account
- Auto-generated bar chart of today's mood trends
- Streamlit Cloud deployment

---

## Live Demo

| Resource           | Link |
|--------------------|------|
| Mood Logger     | [mood-logger-serene.streamlit.app](https://mood-logger-serene.streamlit.app) |
| Google Sheet    | [Log Sheet](https://docs.google.com/spreadsheets/d/1hneRLFSMkyw-WptpHRdCpA05sws-P5XgU4zy_dYMUGY/edit?usp=sharing) |

---

## Project Structure

```
mood_logger/
├── app.py # Main Streamlit app
├── gsheet_utils.py # Google Sheets API logic
├── requirements.txt
├── .gitignore
└── .streamlit/
      └── secrets.toml
