import pandas as pd

df = pd.read_parquet("data/interim/01_loaded.parquet")

print("=" * 45)
print("STEP 1 - MISSING VALUE REPORT")
print("=" * 45)
print(df.isna().sum())
print(f"\nTotal rows before cleaning: {len(df)}")

print("\n" + "=" * 45)
print("STEP 2 - APPLYING VALIDITY RULES")
print("=" * 45)
valid = (
    df["humidity_pct"].between(50, 100)
    & df["temperature_c"].between(10, 35)
    & df["co2_ppm"].between(400, 2000)
    & df["yield_kg"].notna()
)
rows_before = len(df)
df = df[valid].copy()
print(f"Rows removed by validity rules: {rows_before - len(df)}")

print("\n" + "=" * 45)
print("STEP 3 - FORWARD FILL SHORT GAPS")
print("=" * 45)
cols = ["temperature_c", "humidity_pct", "co2_ppm"]
df[cols] = df[cols].ffill(limit=2)
print("Forward fill applied to:", cols)

print("\n" + "=" * 45)
print("STEP 4 - DROP NULL TARGET ROWS")
print("=" * 45)
before = len(df)
df = df.dropna(subset=["yield_kg"])
print(f"Rows dropped (null yield_kg): {before - len(df)}")

print("\n" + "=" * 45)
print("STEP 5 - REMOVE DUPLICATE TIMESTAMPS")
print("=" * 45)
before = len(df)
df = df.drop_duplicates(subset=["timestamp"], keep="last")
print(f"Duplicate rows removed: {before - len(df)}")

print("\n" + "=" * 45)
print("CLEANING COMPLETE")
print("=" * 45)
print(f"Final row count: {len(df)}")
print(f"Any nulls remaining: {df.isna().sum().sum()}")
print(df.head())

df.to_parquet("data/interim/02_cleaned.parquet", index=False)
print("\n02_cleaned.parquet saved!")