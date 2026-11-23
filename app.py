import streamlit as st
import pandas as pd
from datetime import date
import os

st.set_page_config(page_title="School Attendance", page_icon="✅")
st.title("✅ School Attendance Register")
st.write(f"Date: {date.today()}")

my_class = st.selectbox("Select Class", ["P.1","P.2","P.3","P.4","P.5","P.6","P.7","S.1","S.2","S.3","S.4"])

students_by_class = {
    "P.1": ["Amina Nakato", "John Mukasa", "Grace Atim", "Peter Ssemwanga"],
    "P.2": ["Sarah Nansubuga", "David Okello", "Faith Namirembe", "Moses Kizito"],
    "P.3": ["Esther Akello", "Paul Mugisha", "Ruth Nakitto", "Samuel Kato"],
    "P.4": ["Mary Achieng", "James Ochieng", "Joyce Nabukenya", "Daniel Ssebuliba"],
    "P.5": ["Rebecca Nanyonjo", "Isaac Muwanga", "Hannah Babirye", "Emmanuel Wasswa"],
    "P.6": ["Deborah Nakimuli", "Joshua Tumusiime", "Priscilla Namatovu", "Brian Ssenyonjo"],
    "P.7": ["Winnie Nalwanga", "Kevin Mubiru", "Catherine Ndagire", "Andrew Kaggwa"],
    "S.1": ["Brian Okot", "Mercy Atuhaire", "Collins Ssebunya", "Sharon Kemigisha"],
    "S.2": ["Ivan Ssempala", "Joan Nankya", "Patrick Lule", "Diana Nalubega"],
    "S.3": ["Alex Mugerwa", "Lilian Nassozi", "Henry Kintu", "Phiona Akite"],
    "S.4": ["Ronald Ssemanda", "Brenda Namugerwa", "Felix Okello", "Natasha Nakandi"],
}

st.subheader(f"Class {my_class}")
present_list = []
for name in students_by_class[my_class]:
    if st.checkbox(name, value=True):
        present_list.append(name)

st.success(f"Present: {len(present_list)} / {len(students_by_class[my_class])}")

if st.button("Save Attendance"):
    file_name = "attendance.csv"
    file_exists = os.path.exists(file_name)
    df = pd.DataFrame([{"Date": str(date.today()), "Class": my_class, "Student Name": n, "Status": "Present"} for n in present_list])
    df.to_csv(file_name, mode="a", header=not file_exists, index=False)
    st.success("Saved!")
    st.table(df)
