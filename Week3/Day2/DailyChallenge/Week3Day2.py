import pandas as pd

path = r"C:\Users\USER1\Downloads\Data Science Job Salary dataset\Data Science Job Salary dataset\datascience_salaries.csv"

df = pd.read_csv(path)

print(df.head())

df['salary_normalized'] = (
    df['salary'] - df['salary'].min()
) / (
    df['salary'].max() - df['salary'].min()
)

print(df[['salary', 'salary_normalized']].head())

print(df.select_dtypes(include='number').columns)

from sklearn.preprocessing import StandardScaler

numeric_df = df.select_dtypes(include='number')

scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_df)

from sklearn.decomposition import PCA

pca = PCA(n_components=2)

principal_components = pca.fit_transform(scaled_data)

pca_df = pd.DataFrame(
    principal_components,
    columns=['PC1', 'PC2']
)

print(pca_df.head())

print(pca.explained_variance_ratio_)
print("Total variance explained:", pca.explained_variance_ratio_.sum())

# Keep only numeric columns
numeric_df = df.select_dtypes(include='number')

# Scale the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_df)

# Reduce to 2 principal components
pca = PCA(n_components=2)
principal_components = pca.fit_transform(scaled_data)

# Create a new DataFrame with the reduced features
pca_df = pd.DataFrame(
    principal_components,
    columns=['PC1', 'PC2']
)

print(pca_df.head())

# Show how much information was retained
print("Explained variance ratio:", pca.explained_variance_ratio_)
print("Total variance explained:", pca.explained_variance_ratio_.sum())