# MedSync2

MedSync2 now includes two Streamlit workflows:

1. **Medication Sync Calculator** - estimates medication units needed to align refill dates.
2. **Rx Operational Dashboard** - models Jul-Nov 2025 Rx activity, CVS share, platform concentration, scenario projections, and a priority watchlist.

## Run the Streamlit app

```bash
pip install -r requirements.txt
streamlit run med_sync_app.py
```

Use the sidebar to switch between the medication sync calculator and the Rx operational dashboard.

## Build Rx dashboard artifacts from the CLI

From the repository root:

```bash
python -m rx_dashboard_codex --outdir build
```

Or:

```bash
python scripts/build_rx_dashboard.py --outdir build
```

Generated files are written to the selected output directory and include:

- `rx_operational_dashboard_codex.html`
- `rx_operational_dashboard_codex.xlsx`
- `rx_accounts_model_codex.csv`
- `rx_monthly_model_codex.csv`
- `rx_platform_model_codex.csv`
- `rx_scenarios_codex.csv`
- `rx_watchlist_codex.csv`

## Use the dashboard package in Python

```python
from rx_dashboard_codex import build_dashboard, load_df, model

outputs = build_dashboard(outdir="build")
print(outputs["html"])
print(outputs["xlsx"])

models = model(load_df())
print(models["monthly"])
```

## Optional custom CSV input

```bash
python -m rx_dashboard_codex --input-csv path/to/rx-data.csv --outdir build
```

The CSV must use the same schema as the embedded data in `rx_dashboard_codex/data.py`.
