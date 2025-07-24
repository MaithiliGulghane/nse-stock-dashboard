import yfinance as yf
import json
import os
import time
import datetime
from azure.storage.blob import BlobServiceClient

def fetch_and_upload():
    # ✅ Step 1: Define tickers
    tickers = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]
    stock_data = {}

    # ✅ Step 2: Fetch latest close prices
    for ticker in tickers:
        data = yf.Ticker(ticker)
        hist = data.history(period="1d")
        if not hist.empty:
            price = hist["Close"].iloc[-1]
            stock_data[ticker] = float(price)

    # ✅ Step 3: Connect to Azure Blob Storage
    connection_string = os.environ['AZURE_STORAGE_KEY']
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_name = "raw"
    container_client = blob_service_client.get_container_client(container_name)

    # ✅ Step 4: Create container if it doesn’t exist
    try:
        container_client.create_container()
    except Exception:
        pass  # Ignore error if it already exists

    # ✅ Step 5: Upload JSON with timestamped filename
    now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    blob_name = f"stockdata-{now}.json"
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(json.dumps(stock_data), overwrite=True)

    print(f"✅ Uploaded {blob_name} → {stock_data}")

# ✅ Step 6: Run in loop every X minutes
INTERVAL_MINUTES = 10

try:
    while True:
        fetch_and_upload()
        print(f"⏳ Waiting {INTERVAL_MINUTES} minutes...\n")
        time.sleep(INTERVAL_MINUTES * 60)
except KeyboardInterrupt:
    print("🔁 Auto-fetching stopped by user.")
