# OmniStream-Insight: Real-Time Retail Event Streaming & Predictive Observability Engine

OmniStream-Insight is a containerized, cloud-ready data engineering and MLOps ecosystem designed to ingest, process, and evaluate high-throughput enterprise retail transactions and SAP IDoc statuses in real time. Built to align with modern corporate architecture standards, it demonstrates a "Clean Core" data integration methodology by offloading complex analytics, ETL tasks, and machine learning inference to an independent, highly scalable microservices layer without putting operational overhead on core ERP environments.

---

## 📄 Executive Summary

In large-scale enterprise retail environments—such as global apparel and fast-moving consumer goods (FMCG) chains—hundreds of physical and digital stores concurrently execute sales, modify inventory accounts, and transmit intermediate documents (IDocs) to a central ERP system. Traditional auditing and operational monitoring infrastructures are heavily reactive, resulting in lagging dashboards, delayed stockout identifications, and high Mean-Time-To-Resolution (MTTR) when critical middleware data transfers crash.

**OmniStream-Insight** solves this industry problem by establishing an end-to-end event-driven infrastructure. The system continually simulates live, multi-node retail environments, injects deliberate middleware transaction errors (SAP IDoc Status 51 failures), streams events through a highly decoupled messaging broker, executes real-time feature engineering, and triggers machine learning models to predict stockout risks and flag transaction valuation anomalies instantly. The entire lifecycle is surface-exposed via a live, public-facing observability dashboard executing automatic continuous updates.

---

## 🛠️ System Architecture & Workflow

The platform utilizes a decoupled microservices architecture orchestrating five separate logical layers:

```text
[ Retail Store Nodes ] ──► ( there are Continuous Transactions & IDocs ) 
                                     │
                                     ▼
                     [ Redpanda Message Broker ] (Kafka API)
                                     │
                                     ▼
                     [ Python Streaming ETL Engine ]
                                     │
                ┌────────────────────┴────────────────────┐
                ▼                                         ▼
   [ Scikit-Learn ML Inference ]              [ Aggregation & Feature Prep ]
  (Isolation Forest Outlier Engine)           (Pandas Real-Time Structuring)
                │                                         │
                └────────────────────┬────────────────────┘
                                     ▼
                        [ PostgreSQL Database ] 
                                     │
                                     ▼
                    [ Streamlit Observability Web UI ]
               (Live Analytical Graphs & Metric Gauges)
