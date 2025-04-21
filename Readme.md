# Azure Event hubs Pipeline:

This project demonstrates an end-to-end event-driven architecture using **Azure Event Grid**, **Azure Event Hub**, and **Apache Spark Structured Streaming** in **Azure Databricks**.

Here is the flow of data:

Azure Event Grid -> Event Hub -> Spark Streaming in Databricks

## Overview

Following steps were performed:

1. Created an Azure Event Grid Topic
2. Subscribed the topic to Azure Event Hub
3. Send sample events to Event Grid
4. Read and processed these events from Azure event hub in real-time using Spark Streaming inside Azure Databricks