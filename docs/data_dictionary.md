# Data Dictionary

## Important Note

All data in this project is synthetic and created for educational purposes only.

## synthetic_brazil_soybean_exports.csv

| Column | Description |
|---|---|
| month | Month of export flow |
| port | Brazilian loading port |
| destination_country | Destination country |
| volume_tons | Synthetic exported soybean volume in metric tons |
| freight_rate_usd_per_ton | Synthetic freight rate in USD per ton |
| vessel_type | Simplified vessel type |
| incoterm | Incoterm used in the fictional trade flow |

## Business Notes

- Higher volumes are concentrated around the Brazilian soybean export season.
- Ports such as Santos and Paranaguá are intentionally given larger synthetic flows because they are major Brazilian export gateways.
- China is given a large share of synthetic destination flows because it is a key soybean import market.
- Freight revenue is estimated as `volume_tons * freight_rate_usd_per_ton`.
