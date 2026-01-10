import pandas as pd
import requests

API_URL = "http://127.0.0.1:8000/lineage/log"

def log_lineage(dataset_id, source, operation, extra_metadata):
    payload = {
        "dataset_id": dataset_id,
        "source": source,
        "operation": operation,
        "extra_metadata": extra_metadata
    }

    response = requests.post(API_URL, json=payload)

    # SAFE PRINT (no JSON crash)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

def run_etl():
    # STEP 1: Load data
    df = pd.DataFrame({
        "sales": [100, 200, None, 400],
        "profit": [20, 50, None, 90]
    })

    log_lineage(
        dataset_id="raw_v1",
        source="in_memory",
        operation="load_data",
        extra_metadata={"rows": len(df)}
    )

    # STEP 2: Clean data
    df_clean = df.dropna()

    log_lineage(
        dataset_id="clean_v1",
        source="raw_v1",
        operation="drop_nulls",
        extra_metadata={"rows": len(df_clean)}
    )

    # STEP 3: Transform
    df_clean["profit_margin"] = df_clean["profit"] / df_clean["sales"]

    log_lineage(
        dataset_id="final_v1",
        source="clean_v1",
        operation="feature_engineering",
        extra_metadata={"columns": list(df_clean.columns)}
    )

    print("ETL completed")

if __name__ == "__main__":
    run_etl()
