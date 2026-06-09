-- Dim Tables
CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    risk_grade TEXT
);

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY,
    full_date DATE,
    day INTEGER,
    month INTEGER,
    year INTEGER,
    is_weekend BOOLEAN
);

-- Fact Tables
CREATE TABLE fact_nav (
    date DATE,
    amfi_code INTEGER,
    nav REAL,
    FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_transactions (
    transaction_date DATE,
    amfi_code INTEGER,
    amount_inr REAL,
    transaction_type TEXT,
    state TEXT
);