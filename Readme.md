# Event-Driven Pipeline: Azure Event Grid -> Event Hub -> Spark Streaming in Databricks

This project demonstrates an end-to-end event-driven architecture using **Azure Event Grid**, **Azure Event Hub**, and **Apache Spark Structured Streaming** in **Azure Databricks**.

## Overview

I performed the following steps:

1. Created an Azure Event Grid Topic
2. Subscribed the topic to an Azure Event Hub
3. Send sample events to Event Grid
4. Read and process these events in real-time using Spark Streaming inside Azure Databricks