#!/usr/bin/env python3
"""
Example: Violin plot of metric distributions across models.
Expects CSV files: {csv_dir}/{dataset}/{model}.csv with columns like 'Q-index', 'UIQM', etc.
"""

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src import generate_label


def main():
    p = argparse.ArgumentParser(description="Violin plot of quality metrics")
    p.add_argument("--csv-dir", default="data", help="Directory with {dataset}/{model}.csv")
    p.add_argument("--dataset", default="RUOD")
    p.add_argument("--metric", default="Q-index ↑")
    p.add_argument("--save", default="violin.png")
    args = p.parse_args()

    models = ["Original", "ACDC", "TEBCF", "BayesRet", "PCDE", "ICSP", "AutoEnh", "Semi-UIR", "USUIR", "TUDA"]
    df = pd.DataFrame()
    for m in models:
        path = Path(args.csv_dir) / args.dataset / f"{m}.csv"
        if not path.exists():
            print(f"Missing {path} – create sample data or adjust --csv-dir")
            return
        data = pd.read_csv(path)
        col = args.metric.split(" ")[0]
        df[m] = data[col]

    df_sub = df.sub(df["Original"], axis=0)
    df_sub["Original"] = df["Original"]
    df_melted = df_sub.melt()

    f, ax = plt.subplots(figsize=(12, 8))
    sns.violinplot(data=df_melted, x="variable", y="value", hue="variable", inner="box", palette="Set3", cut=2)
    ax.set_title(f"{args.dataset} – Δ {args.metric}")
    ax.set_xlabel("Models")
    ax.set_ylabel(f"Δ of {args.metric}")
    ax.set(ylim=(-0.6, 1))
    f.savefig(args.save, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {args.save}")


if __name__ == "__main__":
    main()
