from __future__ import annotations

from datetime import datetime

import pandas as pd
import streamlit as st

from rx_dashboard_codex import build_dashboard, dashboard_kpis, load_df, model


st.set_page_config(page_title="MedSync2", layout="wide")


def calculate_sync_quantities(current_meds, sync_date):
    results = []
    sync_datetime = datetime.strptime(sync_date, "%Y-%m-%d")
    today = datetime.today()
    days_until_sync = (sync_datetime - today).days

    if days_until_sync < 0:
        st.error("Sync date must be in the future")
        return []

    for med in current_meds:
        days_left = med["remaining"] // med["daily_dose"]
        additional_days_needed = days_until_sync - days_left
        units_needed = max(additional_days_needed * med["daily_dose"], 0)
        results.append(
            {
                "name": med["name"],
                "days_left": days_left,
                "units_needed": units_needed,
            }
        )

    return results


def render_medication_sync_calculator() -> None:
    st.title("Medication Sync Calculator")
    st.write("Calculate how many units of each medication are needed to sync refill dates.")

    with st.form("med_form"):
        num_meds = st.number_input("Number of medications", min_value=1, max_value=10, step=1)
        meds = []
        for i in range(num_meds):
            name = st.text_input(f"Medication {i + 1} Name", key=f"name_{i}")
            daily_dose = st.number_input(f"{name or f'Medication {i + 1}'} Daily Dose", min_value=1, key=f"dose_{i}")
            remaining = st.number_input(f"{name or f'Medication {i + 1}'} Units Remaining", min_value=0, key=f"remaining_{i}")
            meds.append({"name": name or f"Medication {i + 1}", "daily_dose": daily_dose, "remaining": remaining})

        sync_date = st.date_input("Desired Sync Date")
        submitted = st.form_submit_button("Calculate")

    if submitted:
        result = calculate_sync_quantities(meds, sync_date.strftime("%Y-%m-%d"))
        if result:
            st.subheader("Sync Plan")
            for med in result:
                st.write(f"**{med['name']}**: {med['units_needed']} units needed to sync by {sync_date}")


def _format_percent_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    formatted = df.copy()
    for column in columns:
        if column in formatted.columns:
            formatted[column] = formatted[column].map(lambda value: "" if pd.isna(value) else f"{value:.1%}")
    return formatted


def render_rx_dashboard() -> None:
    st.title("Rx Operational Dashboard")
    st.caption("Jul-Nov 2025 actuals with a scenario-modeled sixth month.")

    models = model(load_df())
    kpis = dashboard_kpis(models)
    cols = st.columns(4)
    for index, (label, value) in enumerate(kpis.items()):
        with cols[index % 4]:
            st.metric(label, value)

    st.subheader("Monthly Model")
    st.dataframe(
        _format_percent_columns(models["monthly"], ["CVS_Share", "MoM_Pct"]),
        use_container_width=True,
    )

    st.subheader("Platform Model")
    st.dataframe(
        _format_percent_columns(models["platform"], ["CVS_Share", "Volume_Share"]),
        use_container_width=True,
    )

    st.subheader("Scenario Model")
    st.dataframe(models["scenarios"], use_container_width=True)

    st.subheader("Priority Watchlist")
    st.dataframe(
        _format_percent_columns(models["watch"], ["Volume_Share", "CVS_Share", "Peak_Cap_Utilization"]),
        use_container_width=True,
    )

    st.divider()
    outdir = st.text_input("Export directory", value="build")
    if st.button("Build dashboard artifacts"):
        outputs = build_dashboard(outdir=outdir)
        st.success(f"Dashboard artifacts written to {outputs['outdir']}")
        st.write("HTML:", outputs["html"])
        st.write("XLSX:", outputs["xlsx"])
        for name, path in outputs["csvs"].items():
            st.write(f"{name} CSV:", path)


def main() -> None:
    page = st.sidebar.radio(
        "Choose workflow",
        ["Medication Sync Calculator", "Rx Operational Dashboard"],
    )
    if page == "Medication Sync Calculator":
        render_medication_sync_calculator()
    else:
        render_rx_dashboard()


if __name__ == "__main__":
    main()
