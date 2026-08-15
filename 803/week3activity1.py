"""week3activity1.py
Refactored: Read, clean and run simple analysis on Sample_dataset.csv with a main() entrypoint
Adds robust CSV discovery and CLI argument for CSV path.
"""
import re
import sys
import argparse
from pathlib import Path
import pandas as pd

CSV_FILENAME = "Sample_dataset.csv"
DEFAULT_SEARCH_ROOTS = [Path("/mnt/d/MSE"), Path(__file__).resolve().parent, Path(__file__).resolve().parent.parent, Path.cwd()]

# --- helpers ---------------------------------------------------------------

def text_to_number(s):
    """Parse common textual numbers like 'thirty-eight' or 'sixty five thousand'."""
    if pd.isna(s):
        return None
    s = str(s).lower().replace("-", " ").replace(",", " ").strip()
    m = re.search(r"(-?\d[\d,\.]*)", s)
    if m:
        num = m.group(1).replace(",", "")
        try:
            return float(num)
        except:
            pass
    words = {
        "zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,
        "eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19,
        "twenty":20,"thirty":30,"forty":40,"fifty":50,"sixty":60,"seventy":70,"eighty":80,"ninety":90,
    }
    tokens = s.split()
    total = 0
    current = 0
    for t in tokens:
        if t in words:
            current += words[t]
        elif t == "hundred":
            current *= 100
        elif t == "thousand":
            current = (current if current else 1) * 1000
            total += current
            current = 0
        else:
            pass
    total += current
    return float(total) if total != 0 else None


def clean_currency(x):
    if pd.isna(x):
        return None
    s = str(x).replace(",", "").strip()
    s = re.sub(r"[^\d\.\-]", " ", s).strip()
    m = re.search(r"-?\d+(\.\d+)?", s)
    if m:
        return float(m.group(0))
    return text_to_number(x)


# --- core functionality ---------------------------------------------------

def find_csv(path_hint: str = None) -> Path:
    """Return Path to CSV. If path_hint provided and exists, use it. Otherwise search DEFAULT_SEARCH_ROOTS for CSV_FILENAME."""
    if path_hint:
        p = Path(path_hint)
        if p.is_file():
            return p.resolve()
        # try relative to script dir
        p2 = Path(__file__).resolve().parent.joinpath(path_hint)
        if p2.is_file():
            return p2.resolve()
    # search predefined roots
    found = []
    for root in DEFAULT_SEARCH_ROOTS:
        try:
            for p in root.rglob(CSV_FILENAME):
                found.append(p.resolve())
        except PermissionError:
            continue
    if found:
        return found[0]
    raise FileNotFoundError(f"Could not find {CSV_FILENAME}. Searched: {[str(p) for p in DEFAULT_SEARCH_ROOTS]}")


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, dtype=str).apply(lambda col: col.str.strip() if col.dtype == "object" else col)
    df.columns = [c.strip() for c in df.columns]
    return df


def parse_date(s):
    if pd.isna(s) or str(s).strip() == "":
        return pd.NaT
    s2 = str(s).strip()
    for fmt in ("%d/%m/%Y","%d/%m/%y","%Y-%m-%d","%Y-%d-%m","%d-%m-%Y"):
        try:
            return pd.to_datetime(s2, format=fmt, dayfirst=True)
        except:
            pass
    try:
        return pd.to_datetime(s2, dayfirst=True, errors="coerce")
    except:
        return pd.NaT


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["ID"] = pd.to_numeric(df.get("ID"), errors="coerce")
    df["Name"] = df.get("Name").fillna("Unknown").replace("", "Unknown")

    df["Age_clean"] = pd.to_numeric(df.get("Age"), errors="coerce")
    mask_age_missing = df["Age_clean"].isna()
    df.loc[mask_age_missing, "Age_clean"] = df.loc[mask_age_missing, "Age"].apply(text_to_number)

    df["Net_worth_clean"] = df.get("Net worth").apply(clean_currency)
    df["Salary_clean"] = df.get("Salary").apply(clean_currency)

    df["Country"] = df.get("Country").replace({"AU":"AUS", "Aus":"AUS"}).fillna("Unknown")

    df["JoinDate_clean"] = df.get("Join Date").apply(parse_date)

    no_id = df[df["ID"].isna()].copy()
    has_id = df[~df["ID"].isna()].copy()

    agg_funcs = {}
    for col in ["Name","Age_clean","Net_worth_clean","Country","Salary_clean","JoinDate_clean"]:
        agg_funcs[col] = lambda s: s.dropna().iloc[0] if s.dropna().shape[0] > 0 else pd.NA

    if not has_id.empty:
        grouped = has_id.groupby("ID").agg(agg_funcs).reset_index()
    else:
        grouped = pd.DataFrame(columns=["ID","Name","Age_clean","Net_worth_clean","Country","Salary_clean","JoinDate_clean"])

    cleaned = pd.concat([grouped,
                         no_id.assign(
                             ID=no_id["ID"],
                             Name=no_id["Name"],
                             Age_clean=no_id["Age_clean"],
                             Net_worth_clean=no_id["Net_worth_clean"],
                             Country=no_id["Country"],
                             Salary_clean=no_id["Salary_clean"],
                             JoinDate_clean=no_id["JoinDate_clean"]
                         )[["ID","Name","Age_clean","Net_worth_clean","Country","Salary_clean","JoinDate_clean"]]
                        ], ignore_index=True, sort=False)

    cleaned["Age_clean"] = pd.to_numeric(cleaned["Age_clean"], errors="coerce")
    cleaned["Net_worth_clean"] = pd.to_numeric(cleaned["Net_worth_clean"], errors="coerce")
    cleaned["Salary_clean"] = pd.to_numeric(cleaned["Salary_clean"], errors="coerce")
    cleaned["JoinDate_clean"] = pd.to_datetime(cleaned["JoinDate_clean"], errors="coerce")

    return cleaned


def analyze(cleaned: pd.DataFrame, report_date: pd.Timestamp):
    results = {}
    results["n_rows_cleaned"] = len(cleaned)

    results["missing_by_column"] = cleaned.isna().sum().to_dict()

    numeric_cols = ["Age_clean","Salary_clean","Net_worth_clean"]
    for c in numeric_cols:
        ser = cleaned[c].dropna()
        results[f"{c}_count"] = int(ser.count())
        results[f"{c}_mean"] = float(ser.mean()) if ser.size else None
        results[f"{c}_median"] = float(ser.median()) if ser.size else None
        results[f"{c}_std"] = float(ser.std(ddof=0)) if ser.size else None

    cleaned["Tenure_years"] = ((report_date - cleaned["JoinDate_clean"]).dt.days / 365.25).round(2)
    ser = cleaned["Tenure_years"].dropna()
    results["tenure_count"] = int(ser.count())
    results["tenure_mean"] = float(ser.mean()) if ser.size else None

    results["country_counts"] = cleaned["Country"].fillna("Unknown").value_counts().to_dict()

    corr_df = cleaned[["Age_clean","Salary_clean","Net_worth_clean"]].astype(float)
    results["correlations"] = corr_df.corr().to_dict()

    top = cleaned.sort_values("Salary_clean", ascending=False).head(3)[["ID","Name","Salary_clean"]]
    results["top_earners"] = top.to_dict(orient="records")

    return results


def print_report(results: dict):
    def section(title):
        print("\n" + title)
        print("-" * len(title))

    print("CLEANING & ANALYSIS REPORT")
    section("Overview")
    print(f"Rows (after de-dup/clean): {results.get('n_rows_cleaned')}")

    section("Missing values (per column, after cleaning)")
    for k,v in results["missing_by_column"].items():
        print(f"{k}: {v}")

    section("Numeric summaries (count, mean, median, std)")
    for c in ["Age_clean","Salary_clean","Net_worth_clean"]:
        print(f"{c}: count={results.get(f'{c}_count')}, mean={results.get(f'{c}_mean')}, median={results.get(f'{c}_median')}, std={results.get(f'{c}_std')}")

    section("Country distribution")
    for k,v in results["country_counts"].items():
        print(f"{k}: {v}")

    section("Correlations (pearson)")
    for rowk,rowv in results["correlations"].items():
        print(rowk, {k: round(v,3) if pd.notna(v) else None for k,v in rowv.items()})

    section("Top earners")
    for rec in results["top_earners"]:
        print(rec)

    section("Metric explanations (what they measure & interpretation)")
    explanations = {
        "row counts": "Counts of rows before/after cleaning (shows data loss or deduping).",
        "missing_by_column": "Number of missing values per column after cleaning.",
        "mean": "Average value; sensitive to outliers. Use with median for robustness check.",
        "median": "Middle value; robust to outliers.",
        "std": "Standard deviation; indicates spread around the mean.",
        "country_counts": "Frequency distribution of Country.",
        "correlation": "Pearson correlation (-1..1) between numeric variables. Correlation ≠ causation.",
        "top_earners": "Top records by Salary — useful to identify outliers or high-value entities.",
        "tenure_years": "Years since join date; indicates record age."
    }
    for k,v in explanations.items():
        print(f"- {k}: {v}")


def main1(argv=None):
    p = argparse.ArgumentParser(description="Clean and analyze Sample_dataset.csv")
    p.add_argument("--csv", help="Path to CSV file (optional)")
    args = p.parse_args(argv)

    try:
        csv_path = find_csv(args.csv)
    except FileNotFoundError as e:
        print("ERROR:", e)
        print("Search tips: place Sample_dataset.csv in the same folder as this script or provide --csv path.")
        sys.exit(2)

    df = load_data(str(csv_path))
    cleaned = clean_data(df)
    report_date = pd.Timestamp.now().normalize()
    results = analyze(cleaned, report_date)
    results["n_rows_raw"] = len(df)
    print_report(results)

CSV_PATH = r"/mnt/d/MSE/PythonProject/MSE/803/Sample_dataset.csv"

# --- helpers ---------------------------------------------------------------

def text_to_number(s):
    """Parse common textual numbers like 'thirty-eight' or 'sixty five thousand'."""
    if pd.isna(s):
        return None
    s = str(s).lower().replace("-", " ").replace(",", " ").strip()
    m = re.search(r"(-?\d[\d,\.]*)", s)
    if m:
        num = m.group(1).replace(",", "")
        try:
            return float(num)
        except:
            pass
    words = {
        "zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,
        "eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19,
        "twenty":20,"thirty":30,"forty":40,"fifty":50,"sixty":60,"seventy":70,"eighty":80,"ninety":90,
    }
    tokens = s.split()
    total = 0
    current = 0
    for t in tokens:
        if t in words:
            current += words[t]
        elif t == "hundred":
            current *= 100
        elif t == "thousand":
            current = (current if current else 1) * 1000
            total += current
            current = 0
        else:
            pass
    total += current
    return float(total) if total != 0 else None


def clean_currency(x):
    if pd.isna(x):
        return None
    s = str(x).replace(",", "").strip()
    s = re.sub(r"[^\d\.\-]", " ", s).strip()
    m = re.search(r"-?\d+(\.\d+)?", s)
    if m:
        return float(m.group(0))
    return text_to_number(x)


# --- core functionality ---------------------------------------------------

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, dtype=str).apply(lambda col: col.str.strip() if col.dtype == "object" else col)
    df.columns = [c.strip() for c in df.columns]
    return df


def parse_date(s):
    if pd.isna(s) or str(s).strip() == "":
        return pd.NaT
    s2 = str(s).strip()
    for fmt in ("%d/%m/%Y","%d/%m/%y","%Y-%m-%d","%Y-%d-%m","%d-%m-%Y"):
        try:
            return pd.to_datetime(s2, format=fmt, dayfirst=True)
        except:
            pass
    try:
        return pd.to_datetime(s2, dayfirst=True, errors="coerce")
    except:
        return pd.NaT


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["ID"] = pd.to_numeric(df.get("ID"), errors="coerce")
    df["Name"] = df.get("Name").fillna("Unknown").replace("", "Unknown")

    df["Age_clean"] = pd.to_numeric(df.get("Age"), errors="coerce")
    mask_age_missing = df["Age_clean"].isna()
    df.loc[mask_age_missing, "Age_clean"] = df.loc[mask_age_missing, "Age"].apply(text_to_number)

    df["Net_worth_clean"] = df.get("Net worth").apply(clean_currency)
    df["Salary_clean"] = df.get("Salary").apply(clean_currency)

    df["Country"] = df.get("Country").replace({"AU":"AUS", "Aus":"AUS"}).fillna("Unknown")

    df["JoinDate_clean"] = df.get("Join Date").apply(parse_date)

    no_id = df[df["ID"].isna()].copy()
    has_id = df[~df["ID"].isna()].copy()

    agg_funcs = {}
    for col in ["Name","Age_clean","Net_worth_clean","Country","Salary_clean","JoinDate_clean"]:
        agg_funcs[col] = lambda s: s.dropna().iloc[0] if s.dropna().shape[0] > 0 else pd.NA

    if not has_id.empty:
        grouped = has_id.groupby("ID").agg(agg_funcs).reset_index()
    else:
        grouped = pd.DataFrame(columns=["ID","Name","Age_clean","Net_worth_clean","Country","Salary_clean","JoinDate_clean"])

    cleaned = pd.concat([grouped,
                         no_id.assign(
                             ID=no_id["ID"],
                             Name=no_id["Name"],
                             Age_clean=no_id["Age_clean"],
                             Net_worth_clean=no_id["Net_worth_clean"],
                             Country=no_id["Country"],
                             Salary_clean=no_id["Salary_clean"],
                             JoinDate_clean=no_id["JoinDate_clean"]
                         )[["ID","Name","Age_clean","Net_worth_clean","Country","Salary_clean","JoinDate_clean"]]
                        ], ignore_index=True, sort=False)

    cleaned["Age_clean"] = pd.to_numeric(cleaned["Age_clean"], errors="coerce")
    cleaned["Net_worth_clean"] = pd.to_numeric(cleaned["Net_worth_clean"], errors="coerce")
    cleaned["Salary_clean"] = pd.to_numeric(cleaned["Salary_clean"], errors="coerce")
    cleaned["JoinDate_clean"] = pd.to_datetime(cleaned["JoinDate_clean"], errors="coerce")

    return cleaned


def analyze(cleaned: pd.DataFrame, report_date: pd.Timestamp):
    results = {}
    results["n_rows_cleaned"] = len(cleaned)

    results["missing_by_column"] = cleaned.isna().sum().to_dict()

    numeric_cols = ["Age_clean","Salary_clean","Net_worth_clean"]
    for c in numeric_cols:
        ser = cleaned[c].dropna()
        results[f"{c}_count"] = int(ser.count())
        results[f"{c}_mean"] = float(ser.mean()) if ser.size else None
        results[f"{c}_median"] = float(ser.median()) if ser.size else None
        results[f"{c}_std"] = float(ser.std(ddof=0)) if ser.size else None

    cleaned["Tenure_years"] = ((report_date - cleaned["JoinDate_clean"]).dt.days / 365.25).round(2)
    ser = cleaned["Tenure_years"].dropna()
    results["tenure_count"] = int(ser.count())
    results["tenure_mean"] = float(ser.mean()) if ser.size else None

    results["country_counts"] = cleaned["Country"].fillna("Unknown").value_counts().to_dict()

    corr_df = cleaned[["Age_clean","Salary_clean","Net_worth_clean"]].astype(float)
    results["correlations"] = corr_df.corr().to_dict()

    top = cleaned.sort_values("Salary_clean", ascending=False).head(3)[["ID","Name","Salary_clean"]]
    results["top_earners"] = top.to_dict(orient="records")

    return results


def print_report(results: dict):
    def section(title):
        print("\n" + title)
        print("-" * len(title))

    print("CLEANING & ANALYSIS REPORT")
    section("Overview")
    print(f"Rows (after de-dup/clean): {results.get('n_rows_cleaned')}")

    section("Missing values (per column, after cleaning)")
    for k,v in results["missing_by_column"].items():
        print(f"{k}: {v}")

    section("Numeric summaries (count, mean, median, std)")
    for c in ["Age_clean","Salary_clean","Net_worth_clean"]:
        print(f"{c}: count={results.get(f'{c}_count')}, mean={results.get(f'{c}_mean')}, median={results.get(f'{c}_median')}, std={results.get(f'{c}_std')}")

    section("Country distribution")
    for k,v in results["country_counts"].items():
        print(f"{k}: {v}")

    section("Correlations (pearson)")
    for rowk,rowv in results["correlations"].items():
        print(rowk, {k: round(v,3) if pd.notna(v) else None for k,v in rowv.items()})

    section("Top earners")
    for rec in results["top_earners"]:
        print(rec)

    section("Metric explanations (what they measure & interpretation)")
    explanations = {
        "row counts": "Counts of rows before/after cleaning (shows data loss or deduping).",
        "missing_by_column": "Number of missing values per column after cleaning.",
        "mean": "Average value; sensitive to outliers. Use with median for robustness check.",
        "median": "Middle value; robust to outliers.",
        "std": "Standard deviation; indicates spread around the mean.",
        "country_counts": "Frequency distribution of Country.",
        "correlation": "Pearson correlation (-1..1) between numeric variables. Correlation ≠ causation.",
        "top_earners": "Top records by Salary — useful to identify outliers or high-value entities.",
        "tenure_years": "Years since join date; indicates record age."
    }
    for k,v in explanations.items():
        print(f"- {k}: {v}")


def main():
    report_date = pd.Timestamp.now().normalize()
    df = load_data(CSV_PATH)
    cleaned = clean_data(df)
    results = analyze(cleaned, report_date)
    results["n_rows_raw"] = len(df)
    print_report(results)


if __name__ == "__main__":
    main()
