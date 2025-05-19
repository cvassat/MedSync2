import streamlit as st
from datetime import datetime, timedelta

def calculate_sync_quantities(current_meds, sync_date):
    results = []
    sync_date = datetime.strptime(sync_date, "%Y-%m-%d")
    today = datetime.today()
    days_until_sync = (sync_date - today).days

    if days_until_sync < 0:
        st.error("Sync date must be in the future")
        return []

    for med in current_meds:
        days_left = med['remaining'] // med['daily_dose']
        additional_days_needed = days_until_sync - days_left
        units_needed = max(additional_days_needed * med['daily_dose'], 0)
        results.append({
            'name': med['name'],
            'days_left': days_left,
            'units_needed': units_needed
        })

    return results

st.title("Medication Sync Calculator")
st.write("Calculate how many units of each medication are needed to sync refill dates.")

with st.form("med_form"):
    num_meds = st.number_input("Number of medications", min_value=1, max_value=10, step=1)
    meds = []
    for i in range(num_meds):
        name = st.text_input(f"Medication {i+1} Name", key=f"name_{i}")
        daily_dose = st.number_input(f"{name} Daily Dose", min_value=1, key=f"dose_{i}")
        remaining = st.number_input(f"{name} Units Remaining", min_value=0, key=f"remaining_{i}")
        meds.append({'name': name, 'daily_dose': daily_dose, 'remaining': remaining})

    sync_date = st.date_input("Desired Sync Date")
    submitted = st.form_submit_button("Calculate")

if submitted:
    result = calculate_sync_quantities(meds, sync_date.strftime("%Y-%m-%d"))
    if result:
        st.subheader("Sync Plan")
        for med in result:
            st.write(f"**{med['name']}**: {med['units_needed']} units needed to sync by {sync_date}")
