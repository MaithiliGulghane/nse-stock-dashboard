from azure.storage.blob import BlobServiceClient
import json
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
from pyspark.sql.functions import regexp_extract, to_timestamp, col

# === Step 1: Connect to Azure Blob Storage ===
connection_string = "<your-azure-blob-connection-string>"
container_name = "raw"

blob_service = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service.get_container_client(container_name)

records = []

# === Step 2: Read all matching JSON blobs ===
blob_list = container_client.list_blobs(name_starts_with="stockdata-")

for blob in blob_list:
    if blob.name.endswith(".json"):
        blob_client = container_client.get_blob_client(blob.name)
        data = blob_client.download_blob().readall()
        json_data = json.loads(data)

        for symbol, price in json_data.items():
            records.append((symbol, float(price), blob.name))

# === Step 3: Define schema & create DataFrame ===
schema = StructType([
    StructField("symbol", StringType(), True),
    StructField("price", DoubleType(), True),
    StructField("blob", StringType(), True)
])

df = spark.createDataFrame(records, schema=schema)

# === Step 4: Extract timestamp from blob name ===
df = df.withColumn(
    "timestamp_str",
    regexp_extract(col("blob"), r"stockdata-(\d{4}-\d{2}-\d{2}-\d{2}-\d{2})", 1)
).withColumn(
    "timestamp",
    to_timestamp(col("timestamp_str"), "yyyy-MM-dd-HH-mm")
)

# === Step 5: Save as Delta Table ===
df.write.format("delta").mode("overwrite").saveAsTable("stock_prices_latest")

# === Optional: View ===
display(df)
