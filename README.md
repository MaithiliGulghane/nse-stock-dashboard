# NSE Stock Tracker Dashboard 📈

## Overview
This project tracks stock prices from NSE (e.g., RELIANCE, TCS, INFY), stores them in Azure Blob Storage, transforms the data in Databricks, and visualizes trends in Power BI.

## Components
- **Colab Script**: Fetch and upload stock prices
- **Databricks Notebook**: Load + add timestamp
- **Power BI**: Visual dashboard

## Azure Setup
- Blob Storage container: `raw`
- Secrets stored as environment variables

## Sample Output
- File in Blob: `stockdata-2025-07-24-06-48.json`
- JSON format: `{ "RELIANCE.NS": 1400.90, ... }`

## Dashboard Features
- 📊 Price trend by stock
- 📋 Table of latest prices
- 🕒 Timestamp from filename

## How to Run
1. Upload and run `fetch_and_upload.py` on Colab (with `AZURE_STORAGE_KEY`)
2. Run Databricks notebook
3. Open Power BI dashboard
