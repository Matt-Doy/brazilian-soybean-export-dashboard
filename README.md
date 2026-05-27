# Brazilian Soybean Export Dashboard

> **Python · pandas · plotly · Jupyter**  
> Export flow analysis · Price dynamics · Destination markets · Seasonal patterns · South American commodity markets  
> *Applied commodity data analysis focused on Brazil — the world's largest soybean exporter*

---

## Overview

This dashboard analyses **Brazilian soybean export flows**, covering volumes by destination,
price dynamics, seasonal patterns and year-on-year comparisons. Brazil accounts for
approximately **50% of global soybean exports** — understanding its export dynamics is
fundamental for anyone working in agricultural commodity trading, shipping and supply chain.

Built as a portfolio project combining **commodity market knowledge**, **Python data analysis**
and a **genuine focus on South America** — reflecting 6 months of professional and personal
experience in Brazil in 2024.

---

## Why Brazilian Soybeans Matter

Brazil's soybean export cycle drives:

- **Freight rates** on the Panamax and Supramax markets (South America → China routes)
- **Dry bulk shipping demand** out of Santos, Paranaguá and Mato Grosso logistics corridors
- **Price spreads** between CBOT soybeans and Brazilian FOB prices
- **Currency dynamics**: BRL/USD fluctuations directly affect Brazilian export competitiveness
- **China-Brazil flows**: China absorbs ~70% of Brazilian soybean exports

For a commodity trader or shipping operator, the Brazilian harvest calendar is a key
input into positioning and freight decisions.

---

## Key Features

- Export volume by destination country (China, EU, Southeast Asia, Middle East)
- Monthly and seasonal export patterns (harvest cycle: Feb-May peak)
- Year-on-year volume comparison
- FOB Santos price evolution
- Correlation between BRL/USD rate and export volume/price
- Shipping route implications: Santos → Dalian voyage economics context

---

## Key Market Dynamics Covered

| Theme | What It Shows |
|---|---|
| **Harvest seasonality** | Feb-May export surge drives Panamax rate spikes |
| **China dependency** | ~70% of exports to China — geopolitical sensitivity |
| **BRL effect** | Weak BRL boosts export competitiveness → volume surge |
| **CBOT vs FOB spread** | Arbitrage window that drives Brazilian farmer selling |
| **Santos port congestion** | Queuing times impact vessel scheduling and freight cost |

---

## Repository Structure

```
brazilian-soybean-export-dashboard/
│
├── src/
│   └── dashboard.py              ← main analysis and visualisation pipeline
│
├── notebooks/
│   └── soybean_analysis.ipynb    ← interactive exploration
│
├── data/
│   └── sample_soybean_exports.csv ← sample data (runs without API)
│
├── charts/
│   ├── export_by_destination.png
│   ├── monthly_seasonal_pattern.png
│   └── price_vs_brl.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Quickstart

```bash
git clone https://github.com/Matt-Doy/brazilian-soybean-export-dashboard.git
cd brazilian-soybean-export-dashboard

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python src/dashboard.py
```

---

## Tools

`Python` `pandas` `numpy` `plotly` `matplotlib` `Jupyter Notebook`

---

## Personal Context

This project reflects a genuine interest in South American commodity markets, built during
6 months spent living and training in **Jundiaí, São Paulo state, Brazil** in 2024.
Understanding Brazil's role in global commodity flows — from Mato Grosso soybean farms
to Santos port loading operations to Chinese crusher demand — is directly aligned with
a long-term career focus on South American energy and agricultural commodity markets.

---

## Related Projects

→ [brent-wti-market-analysis](https://github.com/Matt-Doy/brent-wti-market-analysis) — crude oil price dynamics  
→ [shipping-voyage-estimate-tool](https://github.com/Matt-Doy/shipping-voyage-estimate-tool) — voyage P&L and TCE  
→ [commodity-trading-sql-analysis](https://github.com/Matt-Doy/commodity-trading-sql-analysis) — SQL for trading operations

---

## About

Built by **Mattéo Doyen** — Shipping & Trading Graduate (M2, IAE Nantes, 2026).  
[LinkedIn](https://www.linkedin.com/in/mattéo-doyen/) · [GitHub](https://github.com/Matt-Doy)
