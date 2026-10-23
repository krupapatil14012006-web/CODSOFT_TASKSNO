import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# TASK 2 - EXPLORATORY DATA ANALYSIS (EDA)
# =========================================================

# Load cleaned dataset
df = pd.read_csv("C:\\Users\\KRUPA PATIL\\Desktop\\CODSOFT_DATA_ANALYTICS\\TASK2_EDA\\cleaned_student_data.csv")

print("=" * 60)
print("        EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 60)

# Dataset
print("\nDATASET")
print(df)

# Dataset information
print("\nDATASET INFORMATION")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn Data Types:")
print(df.dtypes)

# Descriptive statistics
print("\nDESCRIPTIVE STATISTICS")
print(df.describe())

# Average marks
print("\nAVERAGE MARKS")
print("Average Marks:", round(df["Marks"].mean(), 2))

# Average marks by gender
gender_marks = df.groupby("Gender")["Marks"].mean()

print("\nAVERAGE MARKS BY GENDER")
print(gender_marks.round(2))

# Average marks by city
city_marks = df.groupby("City")["Marks"].mean()

print("\nAVERAGE MARKS BY CITY")
print(city_marks.round(2))

# Number of students by gender
gender_count = df["Gender"].value_counts()

print("\nNUMBER OF STUDENTS BY GENDER")
print(gender_count)

# Number of students by city
city_count = df["City"].value_counts()

print("\nNUMBER OF STUDENTS BY CITY")
print(city_count)

# Correlation between age and marks
correlation = df["Age"].corr(df["Marks"])

print("\nCORRELATION BETWEEN AGE AND MARKS")
print("Correlation:", round(correlation, 2))

# Outlier detection
Q1 = df["Marks"].quantile(0.25)
Q3 = df["Marks"].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["Marks"] < lower_limit) |
    (df["Marks"] > upper_limit)
]

print("\nOUTLIER DETECTION")
print("Q1:", round(Q1, 2))
print("Q3:", round(Q3, 2))
print("IQR:", round(IQR, 2))
print("Lower Limit:", round(lower_limit, 2))
print("Upper Limit:", round(upper_limit, 2))

if len(outliers) == 0:
    print("No outliers found.")
else:
    print("Outliers found:")
    print(outliers)


# =========================================================
# MARKS DISTRIBUTION
# =========================================================
plt.figure(figsize=(8, 5))
plt.hist(df["Marks"], bins=5, edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()


# =========================================================
# AVERAGE MARKS BY GEND
# =========================================================
plt.figure(figsize=(8, 5))
gender_marks.plot(kind="bar")
plt.title("Average Marks by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# =========================================================
# AVERAGE MARKS BY CITY
# =========================================================
plt.figure(figsize=(8, 5))
city_marks.plot(kind="bar")
plt.title("Average Marks by City")
plt.xlabel("City")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# =========================================================
# STUDENT DISTRIBUTION BY GENDER
# =========================================================
plt.figure(figsize=(7, 7))
plt.pie(
    gender_count,
    labels=gender_count.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Student Distribution by Gender")
plt.tight_layout()
plt.show()


# =========================================================
# STUDENT DISTRIBUTION BY CITY
# =========================================================
plt.figure(figsize=(8, 5))
city_count.plot(kind="bar")
plt.title("Student Distribution by City")
plt.xlabel("City")
plt.ylabel("Number of Students")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# =========================================================
# AGE DISTRIBUTION
# =========================================================
plt.figure(figsize=(8, 5))
plt.hist(df["Age"], bins=5, edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()


# =========================================================
# RELATIONSHIP BETWEEN AGE AND MARKS
# =========================================================
plt.figure(figsize=(8, 5))
plt.scatter(df["Age"], df["Marks"])
plt.title("Relationship Between Age and Marks")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()


# =========================================================
# MARKS COMPARISON BY STUDENT
# =========================================================
plt.figure(figsize=(10, 5))
plt.bar(df["Student_ID"], df["Marks"])
plt.title("Marks Comparison by Student")
plt.xlabel("Student ID")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


print("\nEDA completed successfully!")