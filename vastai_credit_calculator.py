#!/usr/bin/env python3
"""
Vast.ai Promotional Credit & GPU Cost Optimization Calculator 2026.
Calculates compute hours and savings from promotional referral credits across Spot and On-Demand tiers.
"""
import argparse

def calculate_credits(credits, spot_rate, ondemand_rate):
    spot_hours = credits / spot_rate if spot_rate > 0 else 0.0
    ondemand_hours = credits / ondemand_rate if ondemand_rate > 0 else 0.0
    equivalent_ondemand_value = spot_hours * ondemand_rate
    effective_savings = equivalent_ondemand_value - credits
    return {
        "credits": credits,
        "spot_rate": spot_rate,
        "ondemand_rate": ondemand_rate,
        "spot_hours": spot_hours,
        "ondemand_hours": ondemand_hours,
        "equivalent_ondemand_value": equivalent_ondemand_value,
        "effective_savings": effective_savings
    }

def main():
    parser = argparse.ArgumentParser(description="Vast.ai Credit & Compute Hours Calculator")
    parser.add_argument("--credits", type=float, default=50.0, help="Free/Promotional credit amount in USD (default: $50.00)")
    parser.add_argument("--spot-rate", type=float, default=0.35, help="Hourly spot rate per GPU in USD (default: $0.35 for RTX 4090)")
    parser.add_argument("--ondemand-rate", type=float, default=0.75, help="Hourly on-demand rate per GPU in USD (default: $0.75)")
    args = parser.parse_args()

    res = calculate_credits(args.credits, args.spot_rate, args.ondemand_rate)
    print(f"Credit Applied:          ${res['credits']:.2f}")
    print(f"Spot GPU Hourly Rate:    ${res['spot_rate']:.2f}/hr")
    print(f"On-Demand Hourly Rate:   ${res['ondemand_rate']:.2f}/hr")
    print(f"Deliverable Spot Hours:  {res['spot_hours']:.1f} hours")
    print(f"Deliverable On-Demand:   {res['ondemand_hours']:.1f} hours")
    print(f"Equivalent Value:        ${res['equivalent_ondemand_value']:.2f}")
    print(f"Net Realized Savings:    ${res['effective_savings']:.2f}")

if __name__ == "__main__":
    main()
