import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================================================
# TASK 3 - DATA VISUALIZATION
# =========================================================

# Load cleaned dataset
df = pd.read_csv(
    r"C:\Users\KRUPA PATIL\Desktop\CODSOFT_DATA_ANALYTICS\TASK3_DATA_VISUALIZATION\cleaned_student_data.csv"
)

print("=" * 60)
print("             DATA VISUALIZATION")
print("=" * 60)

print("\nDATASET")
print(df)

print("\nDATASET INFORMATION")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nSUMMARY STATISTICS")
print(df.describe())

print("\nAVERAGE MARKS")
print("Overall Average Marks:", round(df["Marks"].mean(), 2))

# =========================================================
# 1. STUDENT DISTRIBUTION BY GENDER
# Pie Chart
# =========================================================

gender_count = df["Gender"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(
    gender_count.values,
    labels=gender_count.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Student Distribution by Gender")
plt.tight_layout()
plt.show()


# =========================================================
# 2. MARKS DISTRIBUTION
# Histogram
# =========================================================

plt.figure(figsize=(8, 5))
plt.hist(
    df["Marks"],
    bins=5,
    edgecolor="black"
)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()


# =========================================================
# 3. MARKS BY CITY
# Bar Chart
# =========================================================

city_marks = df.groupby("City")["Marks"].mean()

plt.figure(figsize=(8, 5))
plt.bar(
    city_marks.index,
    city_marks.values
)
plt.title("Average Marks by City")
plt.xlabel("City")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()


# =========================================================
# 4. MARKS CORRELATION HEATMAP
# Heatmap
# =========================================================

numeric_data = df[["Age", "Marks"]]

plt.figure(figsize=(7, 5))
sns.heatmap(
    numeric_data.corr(),
    annot=True,
    cmap="coolwarm",
    linewidths=0.5
)
plt.title("Marks Correlation Heatmap")
plt.tight_layout()
plt.show()


# =========================================================
# 5. AVERAGE MARKS BY GENDER
# Bar Chart
# =========================================================

gender_marks = df.groupby("Gender")["Marks"].mean()

plt.figure(figsize=(8, 5))
plt.bar(
    gender_marks.index,
    gender_marks.values
)
plt.title("Average Marks by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()


# =========================================================
# 6. AGE VS MARKS
# Scatter Plot
# =========================================================

plt.figure(figsize=(8, 5))
plt.scatter(
    df["Age"],
    df["Marks"],
    s=80
)
plt.title("Age vs Marks")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.grid(True)
plt.tight_layout()
plt.show()


# =========================================================
# 7. MARKS SPREAD
# Box Plot
# =========================================================

plt.figure(figsize=(8, 5))
plt.boxplot(
    df["Marks"],
    orientation="vertical"
)
plt.title("Marks Spread")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()


# =========================================================
# 8. STUDENT MARKS COMPARISON
# Line Chart
# =========================================================

plt.figure(figsize=(10, 5))
plt.plot(
    df["Student_ID"],
    df["Marks"],
    marker="o",
    linewidth=2
)
plt.title("Student Marks Comparison")
plt.xlabel("Student ID")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


print("\n" + "=" * 60)
print("Data Visualization completed successfully!")
print("=" * 60)