# Data Provenance and Lineage Tracking

## Overview
This project implements a complete **Data Provenance and Lineage Tracking system**
using **Python, FastAPI, Pandas, and SQLite**.

Each ETL transformation step is automatically logged into a JSON-based ledger,
capturing dataset source, operation, timestamp, and metadata.

## Tech Stack
- Python 3
- FastAPI
- SQLAlchemy
- SQLite
- Pandas

## Features
- Automatic lineage logging from ETL pipelines
- REST APIs to log and query lineage
- JSON-based metadata storage
- Swagger / OpenAPI documentation

## API Endpoints
- `POST /lineage/log` – Log lineage information
- `GET /lineage/{dataset_id}` – Fetch lineage history

## How to Run
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
python etl/etl_pipeline.py
