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


Detailed Functional Steps:

1. The Ingestion Source (Producer Service): A multi-threaded simulation engine mimicking distinct retail distribution nodes. It continuously generates transaction payloads structured with Store IDs, Material IDs, Item Quantities, Transaction Values, and IDoc Status signals.

2. The Event Broker (Redpanda Layer): Acts as a low-latency event-streaming message bus. It ingests the multi-threaded JSON streams into dedicated, partitioned retail-operations topics, completely decoupling data production from downstream consumers.

3. The Analytics & Inference Hub (Consumer Engine): A continuous Python streaming consumer that pulls messages from the broker, applies explicit data type transformations via Pandas, and extracts structural attributes for analysis.

4. Predictive Analytics Stage: The processed payload is piped into a pre-compiled Scikit-Learn unsupervised model to classify transactional risks and evaluate material consumption limits concurrently.

5. Persistence Layer: Structured records, accompanying anomaly classifications, and stockout alert matrices are written directly into a PostgreSQL target system.

6. The User Layer (Observability Dashboard): A client-facing Streamlit application that monitors the database. It utilizes auto-refreshing polling threads to display transaction variations, live metric feeds, operational SLA statuses, and high-priority system anomaly reports.

💻 Technologies & Frameworks Used

* Programming Language: Python 3.10+ (Core backend execution environment)

* Message Broker Infrastructure: Redpanda / Apache Kafka (High-throughput, event-driven streaming architecture)

* Storage Engines: PostgreSQL (Time-series analytical storage and system health logging)

* Containerization & Deployment: Docker & Docker Compose (Microservice orchestration and local replication stability)

* Hosting Platforms: Neon.tech (Serverless managed cloud database infrastructure), Streamlit Community Cloud (Public front-end hosting)

🤖 Machine Learning Model: Isolation Forest

Working Principle:The predictive anomaly architecture uses an Isolation Forest classifier, an unsupervised machine learning algorithm optimized for high-dimensional data spaces and streaming outlier detection.Unlike typical classification models that attempt to map and profile what a "normal" transaction looks like, the Isolation Forest isolates anomalies explicitly. It builds an ensemble of completely randomized Decision Trees over the input features:
      
         $$\text{Input Features} = [\text{Quantity}, \text{Amount}, \text{Is\_Status\_51}]$$

Because anomalies structurally possess distinct characteristics (e.g., abnormally massive order amounts, extreme batch volumes, or critical error flags like IDoc Status 51), they require significantly fewer random splits to become completely isolated from the rest of the dataset.

🌍 Real-World Business Value

1. Minimizing Operational Downtime (MTTR Reduction): By detecting faulty backend communication lines and IDoc Status 51 errors the split-second they appear in the queue, operations teams can respond before entire retail point-of-sale (POS) systems experience data sync delays.

2. Autonomous Risk Mitigation: Rather than performing manual audit checks at the end of a fiscal month, enterprise operators get instant notification of erratic volume spikes, irregular store purchases, or data transmission failures.

3. Inventory Stockout Prevention: The rule engine monitors immediate order velocities against current stock limits, enabling automated, proactive procurement triggers before items completely clear out from physical retail floors.

4. Preserving a "Clean Core" Strategy: By running heavy data science operations and dashboard applications entirely outside the primary ERP instance, companies maintain standard upgrade paths and reduce performance strain on their central transactional system.