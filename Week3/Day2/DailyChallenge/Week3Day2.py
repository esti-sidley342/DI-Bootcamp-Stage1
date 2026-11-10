import pandas as pd

# Define the file path to the CSV dataset
path = r"C:\Users\USER1\Downloads\Data Science Job Salary dataset\Data Science Job Salary dataset\datascience_salaries.csv"

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv(path)

# Display the first 5 rows of the dataset
print(df.head())

# Perform Min-Max normalisation on the salary column
# This scales salary values to a range between 0 and 1
df['salary_normalized'] = (
    df['salary'] - df['salary'].min()
) / (
    df['salary'].max() - df['salary'].min()
)

# Display the original salary and the normalised salary columns
print(df[['salary', 'salary_normalized']].head())

# Display the names of all numerical columns in the dataset
print(df.select_dtypes(include='number').columns)

# Import StandardScaler for standardising numerical data
from sklearn.preprocessing import StandardScaler

# Select only numerical columns from the dataset
numeric_df = df.select_dtypes(include='number')

# Create a scaler object
scaler = StandardScaler()

# Standardise the numerical data so each feature has mean = 0 and standard deviation = 1
scaled_data = scaler.fit_transform(numeric_df)

# Import PCA for dimensionality reduction
from sklearn.decomposition import PCA

# Create a PCA model that reduces the dataset to 2 principal components
pca = PCA(n_components=2)

# Apply PCA to the scaled data
principal_components = pca.fit_transform(scaled_data)

# Create a new DataFrame containing the two principal components
pca_df = pd.DataFrame(
    principal_components,
    columns=['PC1', 'PC2']
)

# Display the first 5 rows of the PCA-transformed data
print(pca_df.head())

# Display the percentage of variance explained by each principal component
print(pca.explained_variance_ratio_)

# Display the total variance explained by both principal components
print("Total variance explained:", pca.explained_variance_ratio_.sum())

# Salary Analysis by Experience Level

# Group data by experience level and calculate average and median salary
salary_stats = df.groupby('experience_level')['salary'].agg(
    average_salary='mean',
    median_salary='median'
)

# Display the grouped salary statistics
print(salary_stats)

# Repeat the calculation and round results to 2 decimal places
salary_stats = df.groupby('experience_level')['salary'].agg(
    average_salary='mean',
    median_salary='median'
).round(2)

# Display a title for the salary report
print("\nSalary statistics by experience level:\n")

# Loop through each experience level and print formatted salary information
for level, row in salary_stats.iterrows():
    print(
        f"Experience Level: {level} | "
        f"Average Salary: ${row['average_salary']:,.2f} | "
        f"Median Salary: ${row['median_salary']:,.2f}"
    )

# Display the complete salary statistics table
print(salary_stats)