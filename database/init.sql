CREATE TABLE IF NOT EXISTS retail_events (
    id SERIAL PRIMARY KEY,
    store_id VARCHAR(50),
    material_id VARCHAR(50),
    quantity INT,
    amount NUMERIC(10, 2),
    idoc_status VARCHAR(10),
    is_anomaly INT,
    stockout_risk INT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP    
);

CREATE TABLE IF NOT EXISTS system_metrics (
    id SERIAL PRIMARY KEY,
    current_mttr_mins INT,
    sla_compliance_pct NUMERIC(5, 2),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert dummy seed operational metrics
INSERT INTO system_metrics (current_mttr_mins, sla_compliance_pct) VALUES (18, 99.4);