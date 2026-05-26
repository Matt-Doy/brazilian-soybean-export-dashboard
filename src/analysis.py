import argparse
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


def load_data(path: str) -> pd.DataFrame:
    """Load synthetic Brazilian soybean export data."""
    df = pd.read_csv(path)
    df["month"] = pd.to_datetime(df["month"])
    df["freight_revenue_usd"] = df["volume_tons"] * df["freight_rate_usd_per_ton"]
    return df


def create_outputs(df: pd.DataFrame, output_dir: Path) -> dict:
    """Create summary tables and save them as CSV files."""
    output_dir.mkdir(parents=True, exist_ok=True)

    monthly_exports = (
        df.groupby("month", as_index=False)["volume_tons"]
        .sum()
        .sort_values("month")
    )

    exports_by_port = (
        df.groupby("port", as_index=False)["volume_tons"]
        .sum()
        .sort_values("volume_tons", ascending=False)
    )

    exports_by_destination = (
        df.groupby("destination_country", as_index=False)["volume_tons"]
        .sum()
        .sort_values("volume_tons", ascending=False)
    )

    route_summary = (
        df.groupby(["port", "destination_country"], as_index=False)
        .agg(
            total_volume_tons=("volume_tons", "sum"),
            avg_freight_rate_usd_per_ton=("freight_rate_usd_per_ton", "mean"),
            estimated_freight_revenue_usd=("freight_revenue_usd", "sum"),
        )
        .sort_values("estimated_freight_revenue_usd", ascending=False)
    )

    monthly_exports.to_csv(output_dir / "monthly_exports.csv", index=False)
    exports_by_port.to_csv(output_dir / "exports_by_port.csv", index=False)
    exports_by_destination.to_csv(output_dir / "exports_by_destination.csv", index=False)
    route_summary.to_csv(output_dir / "route_summary.csv", index=False)

    return {
        "monthly_exports": monthly_exports,
        "exports_by_port": exports_by_port,
        "exports_by_destination": exports_by_destination,
        "route_summary": route_summary,
    }


def create_charts(summaries: dict, chart_dir: Path) -> None:
    """Create and save charts."""
    chart_dir.mkdir(parents=True, exist_ok=True)

    monthly = summaries["monthly_exports"]
    by_port = summaries["exports_by_port"]
    by_destination = summaries["exports_by_destination"]
    routes = summaries["route_summary"].head(10).copy()
    routes["route"] = routes["port"] + " → " + routes["destination_country"]

    plt.figure(figsize=(11, 5))
    plt.plot(monthly["month"], monthly["volume_tons"], marker="o")
    plt.title("Synthetic Brazilian Soybean Exports by Month")
    plt.xlabel("Month")
    plt.ylabel("Volume (tons)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(chart_dir / "monthly_exports.png", dpi=150)
    plt.close()

    plt.figure(figsize=(9, 5))
    plt.bar(by_port["port"], by_port["volume_tons"])
    plt.title("Synthetic Soybean Export Volumes by Brazilian Port")
    plt.xlabel("Port")
    plt.ylabel("Volume (tons)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(chart_dir / "exports_by_port.png", dpi=150)
    plt.close()

    plt.figure(figsize=(9, 5))
    plt.bar(by_destination["destination_country"], by_destination["volume_tons"])
    plt.title("Synthetic Soybean Export Volumes by Destination")
    plt.xlabel("Destination country")
    plt.ylabel("Volume (tons)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(chart_dir / "exports_by_destination.png", dpi=150)
    plt.close()

    plt.figure(figsize=(11, 6))
    plt.barh(routes["route"], routes["estimated_freight_revenue_usd"])
    plt.title("Top 10 Routes by Estimated Freight Revenue")
    plt.xlabel("Estimated freight revenue (USD)")
    plt.ylabel("Route")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(chart_dir / "freight_revenue_by_route.png", dpi=150)
    plt.close()


def print_market_summary(df: pd.DataFrame, summaries: dict) -> None:
    """Print a concise market-style summary."""
    total_volume = df["volume_tons"].sum()
    top_port = summaries["exports_by_port"].iloc[0]
    top_destination = summaries["exports_by_destination"].iloc[0]
    top_route = summaries["route_summary"].iloc[0]
    peak_month = summaries["monthly_exports"].sort_values("volume_tons", ascending=False).iloc[0]

    print("\nBrazilian soybean export dashboard - synthetic dataset")
    print("-----------------------------------------------------")
    print(f"Total synthetic export volume: {total_volume:,.0f} tons")
    print(f"Top port: {top_port['port']} ({top_port['volume_tons']:,.0f} tons)")
    print(f"Top destination: {top_destination['destination_country']} ({top_destination['volume_tons']:,.0f} tons)")
    print(f"Peak export month: {peak_month['month'].strftime('%Y-%m')} ({peak_month['volume_tons']:,.0f} tons)")
    print(
        "Top route by estimated freight revenue: "
        f"{top_route['port']} → {top_route['destination_country']} "
        f"({top_route['estimated_freight_revenue_usd']:,.0f} USD)"
    )
    print("\nNote: all data is synthetic and for educational purposes only.")


def main():
    parser = argparse.ArgumentParser(description="Brazilian soybean export dashboard using synthetic data.")
    parser.add_argument("--input", default="data/synthetic_brazil_soybean_exports.csv", help="Input CSV path.")
    parser.add_argument("--outputs", default="outputs", help="Output directory for CSV summaries.")
    parser.add_argument("--charts", default="charts", help="Output directory for charts.")
    args = parser.parse_args()

    df = load_data(args.input)
    summaries = create_outputs(df, Path(args.outputs))
    create_charts(summaries, Path(args.charts))
    print_market_summary(df, summaries)

    print(f"\nCharts saved to: {Path(args.charts).resolve()}")
    print(f"Summary tables saved to: {Path(args.outputs).resolve()}")


if __name__ == "__main__":
    main()
