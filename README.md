# 🚀 Real-Time Crypto Streaming Pipeline

An end-to-end real-time data engineering pipeline built using **Apache Kafka**, **PySpark Streaming**, and **Streamlit**, fully runnable in **GitHub Codespaces**.

## 🏗️ Architecture

1. **Producer (`producer.py`):** Fetches live Bitcoin market data via REST API every 5 seconds and streams JSON payloads into Kafka.
2. **Message Broker (Apache Kafka):** Manages real-time data streams using Docker containers.
3. **Stream Processing (`spark_consumer.py`):** PySpark Streaming consumes, parses, and cleans data from Kafka topics.
4. **Dashboard (`dashboard.py`):** Streamlit renders real-time price changes and metrics dynamically.

---

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Stream Processing:** PySpark Streaming
* **Ingestion/Messaging:** Apache Kafka, Zookeeper
* **Containerization:** Docker & Docker Compose
* **Visualization:** Streamlit

---

## 🚀 Quickstart Guide (GitHub Codespaces)

1. Launch this repository directly in **GitHub Codespaces**.
2. Start Kafka:
   ```bash
   docker compose up -d# realtime-crypto-pipeline

   ---
