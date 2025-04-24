# Databricks notebook source

#First we need to install these libraries by providing below maven coordinates
#1. com.microsoft.azure:azure-eventhubs-spark_2.12:2.3.22 (For Eventhub connection)
#2. org.mongodb.spark:mongo-spark-connector_2.12:10.2.0 (For Mongo DB connection)

connection_string = "Endpoint=sb://<namespace>.servicebus.windows.net/<eventhub_name>;EntityPath=<eventhub-name>;SharedAccessKeyName=<keyname>;SharedAccessKey=<key>"

event_hubs_conf = {
    'eventhubs.connectionString': sc._jvm.org.apache.spark.eventhubs.EventHubsUtils.encrypt(connection_string),
    'eventhubs.consumerGroup': '$Default'  # Replace with your actual consumer group
}

df = (
  spark.readStream
  .format("eventhubs")
  .options(**event_hubs_conf)
  .load()
)

messages = df.selectExpr("cast(body as string) as message")

# COMMAND ----------

query = (
    messages.writeStream
    .format("mongodb")
    .option("spark.mongodb.connection.uri", "your_cosmos_uri") \
    .option("spark.mongodb.database", "sample") \
    .option("spark.mongodb.collection", "events") \
    .option("checkpointLocation", "/tmp/my-data") \
    .outputMode("append") \
    .start()
)