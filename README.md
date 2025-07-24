# 📈 NSE Stock Dashboard

A complete pipeline to fetch, store, transform, and visualize NSE stock prices in near real-time using:

- 🐍 Python (Colab)
- ☁️ Azure Blob Storage
- 🔥 Databricks + Delta Lake
- 📊 Power BI

---

## 🚀 Project Overview

This project tracks selected stock prices (e.g., RELIANCE, TCS, INFY) and visualizes their latest values and trends.

### 🔁 Workflow

1. **Colab Script** fetches stock prices via `yfinance` and uploads them as `.json` files to Azure Blob Storage.
2. **Databricks Notebook** loads the blobs, extracts stock data, adds timestamps, and saves it as a Delta table.
3. **Power BI Dashboard** connects to Databricks and visualizes stock trends and latest prices.

---

## 🗂️ Folder Structure

```

nse-stock-dashboard/
│
├── colab\_scripts/
│   └── fetch\_and\_upload.py         # Fetch prices and upload to Azure Blob
│
├── databricks\_notebook/
│   └── load\_and\_transform.py       # PySpark job to load JSON, add timestamp, and save as Delta table
│
├── powerbi/
│   └── stock\_dashboard.pbix        # Power BI dashboard (connects to Databricks)
│
├── docs/
│   └── README.md                   # You're reading it 🙂



## 📁 JSON Format (Saved in Azure Blob)

Each JSON file is named like:

```

stockdata-2025-07-24-10-00.json

````

And looks like:

```json
{
  "RELIANCE.NS": 1400.90,
  "TCS.NS": 3145.60,
  "INFY.NS": 1555.10
}
````

---

## ⚙️ Components

### ✅ `colab_scripts/fetch_and_upload.py`

* Uses `yfinance` to get the latest stock prices
* Uploads them to Azure Blob Storage (`raw` container)
* Can be scheduled using a Python loop (`time.sleep()`)

### ✅ `databricks_notebook/load_and_transform.py`

* Connects to Azure Blob
* Loads all JSON blobs starting with `stockdata-`
* Extracts symbol, price, and timestamp from blob filename
* Converts to PySpark DataFrame and saves to a Delta table `stock_prices_latest`

### ✅ `powerbi/stock_dashboard.pbix`

* Visuals include:

  * 📉 Line chart or bar chart for stock trends
  * 📋 Table showing latest prices
  * 📅 Timestamp column (derived from blob filename)

---

## 🔐 Secrets & Configs

* Azure Blob `connection_string` should be stored securely (avoid hardcoding).
* In Databricks, use `dbutils.secrets.get()` or environment configs.
* Power BI connects to Databricks via Personal Access Token (PAT).

---

## 📌 Sample Delta Table Output

| symbol      | price   | timestamp           |
| ----------- | ------- | ------------------- |
| RELIANCE.NS | 1400.90 | 2025-07-24 10:00:00 |
| TCS.NS      | 3145.60 | 2025-07-24 10:00:00 |
| INFY.NS     | 1555.10 | 2025-07-24 10:00:00 |

---

## ✅ Deployment Options

* Run the fetcher via Google Colab or locally.
* Schedule with Python loop or Colab Pro background execution.
* Databricks notebook can be scheduled as a Job.
* Power BI auto-refresh using DirectQuery (Databricks connector).

---

## 🔮 Possible Enhancements

* Add email alerts for price changes
* Connect to Azure SQL or PostgreSQL
* Enable streaming for real-time updates

---

## 🙌 Author

**Your Name**
AI, Data & Cloud Enthusiast
[LinkedIn] www.linkedin.com/in/maithili-gulghane-027ab3aa

---

## ⭐ Star this repo if you find it useful!

