import pandas as pd

# 1. Import dataset
df = pd.read_csv("C:\\Users\\KRUPA PATIL\\Desktop\\CODSOFT_DATA_ANALYTICS\\TASK1_DATA_CLEANING\\dataset\\student_data.csv")

print("\n========== DATA CLEANING & PREPROCESSING ==========")

# 2. Original dataset
print("\n1. ORIGINAL DATA")
print(df)

# 3. Dataset structure
print("\n2. DATASET STRUCTURE")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print(df.dtypes)

# 4. Missing values
print("\n3. MISSING VALUES")
print(df.isnull().sum())

# 5. Duplicate records
print("\n4. DUPLICATE RECORDS")
print("Duplicate records:", df.duplicated().sum())

# 6. Inconsistent values
print("\n5. INCONSISTENT VALUES")
print("Gender:", df["Gender"].unique())
print("City:", df["City"].unique())
print("Age:", df["Age"].unique())

# 7. Clean the data
df_clean = df.copy()

df_clean["Age"] = pd.to_numeric(df_clean["Age"], errors="coerce")
df_clean["Age"] = df_clean["Age"].fillna(df_clean["Age"].median())

df_clean["Marks"] = df_clean["Marks"].fillna(df_clean["Marks"].median())

df_clean = df_clean.drop_duplicates()

df_clean["Gender"] = df_clean["Gender"].str.strip().str.title()
df_clean["City"] = df_clean["City"].str.strip().str.title()

df_clean["Age"] = df_clean["Age"].round().astype(int)

# 8. Check after cleaning
print("\n6. AFTER CLEANING")
print("Missing values:")
print(df_clean.isnull().sum())

print("Duplicate records:", df_clean.duplicated().sum())

# 9. Final cleaned dataset
print("\n7. FINAL CLEANED DATA")
print(df_clean)

# 10. Final data types
print("\n8. FINAL DATA TYPES")
print(df_clean.dtypes)

# 11. Save cleaned dataset
df_clean.to_csv("C:\\Users\\KRUPA PATIL\\Desktop\\CODSOFT_DATA_ANALYTICS\\TASK1_DATA_CLEANING\\dataset\\cleaned_student_data.csv", index=False)

print("\nCleaned dataset saved successfully!")