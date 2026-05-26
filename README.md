# Brazilian Soybean Export Dashboard

## Overview

This project analyzes a simplified dataset of Brazilian soybean exports by port, destination country and month.

The objective is to demonstrate how Python can be used to analyze agricultural commodity flows, port activity and export seasonality in a Brazil-related trade context.

## Important note on the data

The dataset used in this project is **synthetic and created for educational purposes only**.  
It does not represent official Brazilian export statistics, real customs data, real trade flows or confidential commercial information.

The goal is to demonstrate data analysis logic and business reasoning in a commodity trading and shipping context.

## Business Context

Brazil is one of the world's major soybean exporters. Soybean exports are closely linked to:

- agricultural commodity trading;
- dry bulk shipping demand;
- port logistics;
- seasonal harvest cycles;
- trade flows with China, Europe and other import regions.

For a profile interested in commodities, shipping and Brazil, this type of analysis is highly relevant.

## Tools Used

- Python
- pandas
- numpy
- matplotlib

## Key Features

The project includes:

- monthly export volume analysis;
- export volumes by Brazilian port;
- destination country analysis;
- commodity flow seasonality;
- average freight rate by route;
- estimated freight revenue;
- automated charts;
- summary tables exported to CSV.

## Project Structure

```text
brazilian-soybean-export-dashboard/
│
├── data/
│   └── synthetic_brazil_soybean_exports.csv
│
├── src/
│   └── analysis.py
│
├── charts/
│   ├── monthly_exports.png
│   ├── exports_by_port.png
│   ├── exports_by_destination.png
│   └── freight_revenue_by_route.png
│
├── outputs/
│   ├── monthly_exports.csv
│   ├── exports_by_port.csv
│   ├── exports_by_destination.csv
│   └── route_summary.csv
│
├── docs/
│   └── data_dictionary.md
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Dataset Columns

The synthetic dataset contains:

- `month`
- `port`
- `destination_country`
- `volume_tons`
- `freight_rate_usd_per_ton`
- `vessel_type`
- `incoterm`

## Main Business Questions

This project answers questions such as:

1. Which Brazilian ports handle the largest soybean export volumes?
2. Which destination countries receive the largest volumes?
3. How do exports evolve throughout the year?
4. Which routes generate the highest estimated freight revenue?
5. What is the role of seasonality in Brazilian soybean exports?

## How to Run

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

Run the analysis:

```bash
python src/analysis.py --input data/synthetic_brazil_soybean_exports.csv
```

The script generates summary CSV files in `outputs/` and charts in `charts/`.

## Recruiter-Relevant Summary

This project shows the ability to use Python for commodity flow analysis in a Brazil-related shipping and trading context. It combines market understanding, data manipulation and business-oriented visualizations.

It is especially relevant for roles related to:

- commodity trading;
- agricultural commodities;
- shipping and freight analysis;
- market analysis;
- Brazil and South American trade flows;
- data analyst roles in trading or logistics.
