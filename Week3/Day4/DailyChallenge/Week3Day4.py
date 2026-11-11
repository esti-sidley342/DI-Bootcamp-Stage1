import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\USER1\Bootcamp-files\DI_Bootcamp-Stage1\Week3\Day4\Airplane_Crashes_and_Fatalities_Since_1908_t0_2023.csv",
    encoding="latin1")

print(df.head())# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe(include="all"))

# Create a copy for cleaning
df_clean = df.copy()

# Fill missing categorical values with "Unknown"
categorical_cols = df_clean.select_dtypes(include="object").columns

for col in categorical_cols:
    df_clean[col] = df_clean[col].fillna("Unknown")

# Fill missing numerical values with median
numerical_cols = df_clean.select_dtypes(include=["int64", "float64"]).columns

for col in numerical_cols:
    df_clean[col] = df_clean[col].fillna(df_clean[col].median())

print("\nMissing values after cleaning:")
print(df_clean.isnull().sum())

# Convert Date column to datetime
df_clean["Date"] = pd.to_datetime(
    df_clean["Date"],
    errors="coerce"
)

print(df_clean["Date"].head())

# Create new date-based features
df_clean["Year"] = df_clean["Date"].dt.year
df_clean["Month"] = df_clean["Date"].dt.month
df_clean["Day"] = df_clean["Date"].dt.day

print(df_clean[["Date", "Year", "Month", "Day"]].head())

# Categorise crashes by number of fatalities

fatality_bins = [-1, 0, 10, 50, 100, 1000]

fatality_labels = [
    "No Fatalities",
    "Low",
    "Moderate",
    "High",
    "Mass Casualty"
]

df_clean["FatalityCategory"] = pd.cut(
    df_clean["Fatalities"],
    bins=fatality_bins,
    labels=fatality_labels
)

print(df_clean["FatalityCategory"].value_counts())

# Group crashes into decades

df_clean["Decade"] = (
    (df_clean["Year"] // 10) * 10
)

print(df_clean["Decade"].head())

# One-hot encode FatalityCategory

fatality_encoded = pd.get_dummies(
    df_clean["FatalityCategory"],
    prefix="Fatality",
    dtype=int
)

# Merge back into dataset
df_clean = pd.concat(
    [df_clean, fatality_encoded],
    axis=1
)

print(df_clean.head())

print("\nDataset Shape:")
print(df_clean.shape)

print("\nColumn Types:")
print(df_clean.dtypes)

print("\nPreview of Cleaned Dataset:")
print(df_clean.head())

# basic dataset information

# Total number of recorded crashes
total_crashes = len(df_clean)

print(f"Total number of crashes: {total_crashes}")

# Total fatalities

# Sum all fatalities across the dataset
total_fatalities = df_clean["Fatalities"].sum()

print(f"Total fatalities: {total_fatalities}")

# Total passengers aboard

# Calculate total people aboard
total_Aboard = df_clean["Aboard"].sum()

print(f"Total passengers aboard: {total_Aboard}")

# Survival statistics

# Calculate total survivors
# Survivors = Aboard - Fatalities

df_clean["Survivors"] = (
    df_clean["Aboard"] - df_clean["Fatalities"]
)

total_survivors = df_clean["Survivors"].sum()

print(f"Total survivors: {total_survivors}")

# Overall survival rate

# Calculate percentage survival rate

survival_rate = (
    total_survivors / total_Aboard
) * 100

print(f"Overall survival rate: {survival_rate:.2f}%")

# Average fatalities per crash

average_fatalities = (
    df_clean["Fatalities"].mean()
)

print(
    f"Average fatalities per crash: "
    f"{average_fatalities:.2f}"
)

# Highest fatality crash

max_fatalities = (
    df_clean["Fatalities"].max()
)

print(
    f"Highest fatalities in a single crash: "
    f"{max_fatalities}"
)

# crashes over time
# Count crashes by year

crashes_per_year = (
    df_clean.groupby("Year")
    .size()
)

print("\nCrashes Per Year:")
print(crashes_per_year.head())

# -----------------------------------------------------
# VISUALISE CRASH FREQUENCY
# -----------------------------------------------------

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))

plt.plot(
    crashes_per_year.index,
    crashes_per_year.values,
    color="navy"
)

plt.title("Number of Airplane Crashes per Year")
plt.xlabel("Year")
plt.ylabel("Number of Crashes")

plt.grid(True)

plt.show()

# fatalities over time
fatalities_per_year = (
    df_clean.groupby("Year")["Fatalities"]
    .sum()
)

print("\nFatalities Per Year:")
print(fatalities_per_year.head())

# Plot fatalities by year

plt.figure(figsize=(12, 6))

plt.plot(
    fatalities_per_year.index,
    fatalities_per_year.values,
    color="red"
)

plt.title("Total Fatalities per Year")
plt.xlabel("Year")
plt.ylabel("Fatalities")

plt.grid(True)

plt.show()

#crashes by decade
crashes_by_decade = (
    df_clean.groupby("Decade")
    .size()
)

print("\nCrashes by Decade:")
print(crashes_by_decade)

# Bar chart

plt.figure(figsize=(10, 5))

crashes_by_decade.plot(
    kind="bar",
    color="steelblue"
)

plt.title("Airplane Crashes by Decade")
plt.xlabel("Decade")
plt.ylabel("Number of Crashes")

plt.show()

#survival rate by year
# Calculate yearly survival rate

yearly_stats = (
    df_clean.groupby("Year")
    .agg({
        "Aboard": "sum",
        "Fatalities": "sum"
    })
)

yearly_stats["SurvivalRate"] = (
    (
        yearly_stats["Aboard"]
        - yearly_stats["Fatalities"]
    )
    / yearly_stats["Aboard"]
) * 100

print("\nYearly Survival Rates:")
print(yearly_stats.head())

# Plot survival rates

plt.figure(figsize=(12, 6))

plt.plot(
    yearly_stats.index,
    yearly_stats["SurvivalRate"],
    color="green"
)

plt.title("Yearly Survival Rate (%)")
plt.xlabel("Year")
plt.ylabel("Survival Rate (%)")

plt.grid(True)

plt.show()

# Calculate survivors for each crash
df_clean["Survivors"] = (
    df_clean["Aboard"] - df_clean["Fatalities"]
)

# Calculate survival rate as a percentage
df_clean["SurvivalRate"] = (
    df_clean["Survivors"] / df_clean["Aboard"]
) * 100

print(df_clean[
    ["Aboard", "Fatalities", "Survivors", "SurvivalRate"]
].head())

# fatalities statistic
fatalities = df_clean["Fatalities"]

print("\nFatalities Statistics")
print("---------------------")
print("Mean:", np.mean(fatalities))
print("Median:", np.median(fatalities))
print("Standard Deviation:", np.std(fatalities))

# =====================================================
# SURVIVAL RATE STATISTICS
# =====================================================

survival_rates = df_clean["SurvivalRate"]

print("\nSurvival Rate Statistics")
print("------------------------")
print("Mean:", np.mean(survival_rates))
print("Median:", np.median(survival_rates))
print("Standard Deviation:", np.std(survival_rates))

# Distribution of fatalities

plt.figure(figsize=(8,5))
plt.hist(
    fatalities,
    bins=30,
    edgecolor="black"
)

plt.title("Distribution of Fatalities")
plt.xlabel("Fatalities")
plt.ylabel("Frequency")
plt.show()

from scipy.stats import skew, kurtosis

print("\nDistribution Shape")
print("------------------")

print(
    "Fatalities Skewness:",
    skew(fatalities)
)

print(
    "Fatalities Kurtosis:",
    kurtosis(fatalities)
)


# Extract decade from year

df_clean["Decade"] = (
    (df_clean["Year"] // 10) * 10
)

fatalities_1950s = df_clean[
    df_clean["Decade"] == 1950
]["Fatalities"]

fatalities_2000s = df_clean[
    df_clean["Decade"] == 2000
]["Fatalities"]

# T-test
from scipy.stats import ttest_ind

usa = df_clean[
    df_clean["Location"].str.contains(
        "USA",
        case=False,
        na=False
    )
]["Fatalities"]

europe = df_clean[
    df_clean["Location"].str.contains(
        "France|Germany|Italy|Spain|UK",
        case=False,
        na=False
    )
]["Fatalities"]

t_stat, p_value = ttest_ind(
    fatalities_1950s,
    fatalities_2000s,
    nan_policy="omit"
)

print("\nT-Test Results")
print("--------------")
print("T-statistic:", t_stat)
print("P-value:", p_value)


alpha = 0.05

if p_value < alpha:
    print(
        "Reject the null hypothesis."
    )
    print(
        "Average fatalities are significantly different."
    )
else:
    print(
        "Fail to reject the null hypothesis."
    )
    print(
        "No significant difference detected."
    )

    usa = df_clean[
    df_clean["Location"].str.contains(
        "USA",
        case=False,
        na=False
    )
]["Fatalities"]

europe = df_clean[
    df_clean["Location"].str.contains(
        "France|Germany|Italy|Spain|UK",
        case=False,
        na=False
    )
]["Fatalities"]


print(type(usa))
print(type(europe))

print(len(usa))
print(len(europe))

t_stat, p_value = stats.ttest_ind(
    usa,
    europe,
    nan_policy="omit"
)

print("P-value:", p_value)

#Visualisation

import matplotlib.pyplot as plt
import seaborn as sns

# Optional styling
sns.set_style("whitegrid")

# Count crashes per year
crashes_per_year = df_clean.groupby("Year").size()

# Create line chart
plt.figure(figsize=(12, 6))

plt.plot(
    crashes_per_year.index,
    crashes_per_year.values,
    color="navy",
    linewidth=2
)

plt.title("Number of Airplane Crashes per Year")
plt.xlabel("Year")
plt.ylabel("Number of Crashes")

plt.grid(True)

plt.show()

fatalities_per_year = (
    df_clean.groupby("Year")["Fatalities"]
    .sum()
)

plt.figure(figsize=(12, 6))

plt.plot(
    fatalities_per_year.index,
    fatalities_per_year.values,
    color="red"
)

plt.title("Total Fatalities per Year")
plt.xlabel("Year")
plt.ylabel("Fatalities")

plt.grid(True)

plt.show()

plt.figure(figsize=(10, 6))

sns.histplot(
    df_clean["Fatalities"],
    bins=30,
    kde=True,
    color="darkred"
)

plt.title("Distribution of Fatalities")
plt.xlabel("Fatalities")
plt.ylabel("Frequency")

plt.show()

plt.figure(figsize=(10, 3))

sns.boxplot(
    x=df_clean["Fatalities"],
    color="lightcoral"
)

plt.title("Fatalities Boxplot")

plt.show()

crashes_by_decade = (
    df_clean.groupby("Decade")
    .size()
)

plt.figure(figsize=(12, 6))

sns.barplot(
    x=crashes_by_decade.index,
    y=crashes_by_decade.values,
    color="steelblue"
)

plt.title("Number of Crashes by Decade")
plt.xlabel("Decade")
plt.ylabel("Crashes")

plt.xticks(rotation=45)

plt.show()

#Survival rate distribution

plt.figure(figsize=(10, 6))

sns.histplot(
    df_clean["SurvivalRate"],
    bins=25,
    kde=True,
    color="green"
)

plt.title("Distribution of Survival Rates")
plt.xlabel("Survival Rate (%)")
plt.ylabel("Frequency")

plt.show()

#scatterplot of aboard vs fatalities
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df_clean,
    x="Aboard",
    y="Fatalities",
    alpha=0.6
)

plt.title("Passengers Aboard vs Fatalities")
plt.xlabel("Passengers Aboard")
plt.ylabel("Fatalities")

plt.show()

#Top 10 locations with most crashes
top_locations = (
    df_clean["Location"]
    .value_counts()
    .head(10)
)

plt.figure(figsize=(12, 6))

sns.barplot(
    x=top_locations.values,
    y=top_locations.index,
    palette="Blues_r"
)

plt.title("Top 10 Locations by Number of Crashes")
plt.xlabel("Number of Crashes")
plt.ylabel("Location")

plt.show()

#correlation heatmap

numeric_cols = [
    "Aboard",
    "Fatalities",
    "Ground",
    "Survivors",
    "SurvivalRate"
]

correlation_matrix = (
    df_clean[numeric_cols]
    .corr()
)

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.show()

#boxplot comparing fatalities across decades
plt.figure(figsize=(12, 6))

sns.boxplot(
    data=df_clean,
    x="Decade",
    y="Fatalities"
)

plt.title("Fatalities per Crash by Decade")
plt.xlabel("Decade")
plt.ylabel("Fatalities")

plt.xticks(rotation=45)

plt.show()

