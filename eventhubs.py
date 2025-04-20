# Databricks notebook source

#First we need to install com.microsoft.azure:azure-eventhubs-spark_2.12:2.3.22 (Maven)

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
    .outputMode("append")
    .format("console")
    .option("failOnDataLoss", "false")
    .trigger(processingTime="10 seconds")
    .start()
)