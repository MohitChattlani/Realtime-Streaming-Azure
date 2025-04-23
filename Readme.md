# Azure Event hubs Pipeline:

This project demonstrates an end-to-end event-driven architecture using **Azure Event Grid**, **Azure Event Hub**, **Apache Spark Structured Streaming** in **Azure Databricks** and **Azure Cosmos DB for MongoDB**.

Here is the flow of data:

![Data Pipeline Diagram](images/azure_event_grid_arch_2.PNG)

## Overview

Following steps were performed:

1. Created an **Azure Event Grid** Topic
2. Subscribed the topic to **Azure Event Hub**
3. Send sample events to **Event Grid**
4. Read and processed these events from **Azure event hub** in real-time using **Spark Streaming** inside **Azure Databricks**
5. Pushed the events in realtime to **Azure Cosmos DB for MongoDB**
