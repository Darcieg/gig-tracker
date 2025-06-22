import streamlit as st
from datetime import datetime, date, time
from logic.calculations import calculate_duration, calculate_total_pay, calculate_mileage
from logic.storage import save_gig_to_csv

def build_gig_dict(
    name, vendor, date, start, end, pay, tip, miles, duration, notes
):
    """Assemble gig metadata into a structured dictionary for CSV export."""


    return {
        "Gig Name": name,
        "Vendor": vendor,
        "Date": date,
        "Start Time": start,
        "End Time": end,
        "Base Pay": pay,
        "Tip": tip,
        "Miles": miles,
        "Duration (min)": duration,
        "Notes": notes,
    }

st.title("Gig Tracker")


st.header("Add a new gig")

# Collect input from user form
# If form is submitted, calculate metrics and display
# Save gig details to CSV

with st.form("gig_form"):
    gig_name = st.text_input("Gig Name")
    gig_vendor = st.text_input("Gig Vendor")
    start_time = st.time_input("Start Time")
    end_time = st.time_input("End Time")
    start_mile = st.number_input("Starting Mile")
    end_mile = st.number_input("Ending Mile")
    gig_date = st.date_input("Date", value = date.today())
    base_pay = st.number_input("Base Pay ($)")
    tip = st.number_input("Tip ($)")
    notes = st.text_area("Notes")

    submitted = st.form_submit_button("Add Gig")

if submitted:
    duration = calculate_duration(start_time, end_time)
    total_pay = calculate_total_pay(base_pay, tip)
    miles = calculate_mileage(start_mile, end_mile)
    st.success(f"✅ Gig {gig_name} added!")
    st.write(f"**Date:** {gig_date}")
    st.write(f"**Time Spent:** {duration} minutes")
    st.write(f"**Pay:** ${total_pay}")
    st.write(f"**Notes:** {notes}")
    st.write(f"**Miles:** {miles}")
    gig_data = build_gig_dict(
        name=gig_name,
        vendor=gig_vendor,
        date=gig_date,
        start=start_time,
        end=end_time,
        pay=base_pay,
        tip=tip,
        miles=miles,
        duration=duration,
        notes=notes
    )
    save_gig_to_csv(gig_data)


