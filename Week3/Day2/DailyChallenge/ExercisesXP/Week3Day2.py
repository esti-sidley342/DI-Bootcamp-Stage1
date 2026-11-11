import sklearn
import scipy as sp
import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder


#Exercise 1: Load the Titanic dataset and check for duplicates

#import file
# Read the Titanic CSV file into a pandas DataFrame
df = pd.read_csv(
    r"C:\Users\USER1\Bootcamp-files\DI_Bootcamp-Stage1\Week3\Day2\train\train.csv"
)


# Count the number of duplicate rows across all columns
num_duplicates = df.duplicated().sum()

print(f"Number of duplicates before removal: {num_duplicates}")

# Display any duplicate rows
duplicate_rows = df[df.duplicated(keep=False)]

print("\nDuplicate rows:")
print(duplicate_rows)

# Remove duplicate rows
df_clean = df.drop_duplicates()

# Verify that duplicates have been removed
remaining_duplicates = df_clean.duplicated().sum()

print(f"\nNumber of duplicates after removal: {remaining_duplicates}")

# Compare row counts before and after
print(f"\nOriginal number of rows: {len(df)}")
print(f"Number of rows after removing duplicates: {len(df_clean)}")

#Exercise 2: Check for missing values in the Titanic dataset
# Count missing values in each column
missing_values = df.isnull().sum()

print("Missing values by column:")
print(missing_values)

# Display only columns that contain missing values
print("\nColumns with missing values:")
print(missing_values[missing_values > 0])

# Remove rows with missing values
df = df.dropna()

# Create a copy so the original dataset remains unchanged
df_dropna = df.copy()

# Remove rows containing ANY missing values
df_dropna = df_dropna.dropna()

print(
    f"\nNumber of rows after dropna(): {len(df_dropna)}"
)

# Create another copy
df_fillna = df.copy()

# Replace missing Cabin values with a constant string
df_fillna["Cabin"] = df_fillna["Cabin"].fillna("Unknown")

# Replace missing Embarked values with a constant value
df_fillna["Embarked"] = df_fillna["Embarked"].fillna("Missing")

print("\nMissing values after fillna():")
print(df_fillna[["Cabin", "Embarked"]].isnull().sum())

# Note:
# This approach is useful for categorical columns where
# "Unknown" or "Missing" is meaningful.

# Create another copy
df_imputed = df.copy()
from sklearn.impute import SimpleImputer

# Create an imputer that replaces missing values
# with the median of the column
age_imputer = SimpleImputer(strategy="median")

# Fit the imputer and replace missing Age values
df_imputed["Age"] = age_imputer.fit_transform(
    df_imputed[["Age"]]
)

print("\nMissing Age values after imputation:")
print(df_imputed["Age"].isnull().sum())

# Median is often preferred for Age because it is less affected by extreme values than the mean.

# Create a final cleaned dataset
df_clean = df.copy()

# Fill missing Cabin values with a constant
df_clean["Cabin"] = df_clean["Cabin"].fillna("Unknown")

# Impute Age with the median value
age_imputer = SimpleImputer(strategy="median")
df_clean["Age"] = age_imputer.fit_transform(
    df_clean[["Age"]]
)

# Remove rows where Embarked is missing
df_clean = df_clean.dropna(subset=["Embarked"])

print("\nRemaining missing values in cleaned dataset:")
print(df_clean.isnull().sum())

print(f"\nNumber of rows in cleaned dataset: {len(df_clean)}")

#Exercise 3: Feature engineering

# Create a new feature called FamilySize.
# SibSp = number of siblings/spouses aboard
# Parch = number of parents/children aboard
#
# Adding 1 includes the passenger themselves in the family size count

df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# Verify the new feature was created
print("\nFamilySize feature:")
print(df[["SibSp", "Parch", "FamilySize"]].head())

# EXTRACT TITLES FROM NAMES

# Extract the title (Mr, Mrs, Miss, etc.)
df["Title"] = df["Name"].str.extract(r",\s*([^\.]+)\.")

# Display a sample of extracted titles
print("\nExtracted Titles:")
print(df[["Name", "Title"]].head())


# Count the number of each title
print("\nTitle Counts:")
print(df["Title"].value_counts())

#Convert categorical variables to numbers

# Convert the Sex column into multiple binary columns.
sex_encoded = pd.get_dummies(
    df["Sex"],
    prefix="Sex"
)

# Add encoded columns to the dataset
df = pd.concat([df, sex_encoded], axis=1)

print("\nOne-Hot Encoded Sex columns:")
print(df[["Sex", "Sex_female", "Sex_male"]].head())

#encode the new title feature

# LabelEncoder converts categories into integers.
# Mr -> 0
# Mrs -> 1
# Miss -> 2

title_encoder = LabelEncoder()

df["TitleEncoded"] = title_encoder.fit_transform(df["Title"])
title_encoder = LabelEncoder()

df["TitleEncoded"] = title_encoder.fit_transform(
    df["Title"]
)

print("\nEncoded Titles:")
print(df[["Title", "TitleEncoded"]].head())


# Display the mapping used by LabelEncoder
print("\nTitle Mapping:")

for title, code in zip(
    title_encoder.classes_,
    range(len(title_encoder.classes_))
):
    print(f"{title} -> {code}")

#Review new features

print("\nDataset Columns:")
print(df.columns)

print("\nPreview of Engineered Dataset:")
print(
    df[
        [
            "Name",
            "FamilySize",
            "Title",
            "TitleEncoded"
        ]
    ].head()
)