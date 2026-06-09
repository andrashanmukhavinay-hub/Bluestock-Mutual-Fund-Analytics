# Data Dictionary: Mutual Fund Analytics Capstone

This document provides a technical overview of the datasets utilized in the Mutual Fund Analytics project.

## 1. Dimensional Tables (Reference Data)
| Table | Column | Type | Description |
| :--- | :--- | :--- | :--- |
| `dim_fund` | `amfi_code` | Integer | Unique identifier for each mutual fund scheme. |
| `dim_fund` | `scheme_name` | String | Full name of the mutual fund scheme. |
| `dim_fund` | `fund_house` | String | The Asset Management Company. |
| `dim_date` | `full_date` | Date | The calendar date. |
| `dim_date` | `is_weekend` | Boolean | Flag indicating if the date falls on a weekend. |

## 2. Fact Tables (Transactional & Performance Data)
| Table | Column | Type | Description |
| :--- | :--- | :--- | :--- |
| `fact_nav` | `nav` | Float | The Net Asset Value per unit. |
| `fact_transactions`| `amount_inr`| Float | Transaction value in INR. |
| `fact_transactions`| `transaction_type` | String | SIP, Lumpsum, or Redemption. |
| `fact_performance` | `expense_ratio_pct` | Float | Annual fund management fee percentage. |
| `fact_performance` | `alpha` | Float | Excess return over the benchmark. |

## 3. Data Lineage & Sources
* **API Source:** `mfapi.in` (Real-time NAV data).
* **CSV Sources:** Provided datasets (`01_fund_master.csv` through `10_benchmark_indices.csv`).
* **Database Engine:** SQLite 3 via SQLAlchemy.

---