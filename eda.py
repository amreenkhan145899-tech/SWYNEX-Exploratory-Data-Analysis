# SWYNEX - Task 2: Exploratory Data Analysis (EDA)
# Dataset: Titanic

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Dataset Load karna
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# 2. Pehli 5 rows dekhna
print("First 5 Rows:")
print(df.head())

# 3. Dataset ki basic jaankari
print("\nDataset Info:")
print(df.info())
print("\nShape (Rows, Columns):", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

# 4. Statistics
print("\nDescriptive Statistics:")
print(df.describe())

# 5. Missing Values ko handle karna
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df = df.drop(columns=['Cabin'])

# 6. Survival Rate
print("\nSurvival Rate:")
print(df['Survived'].value_counts(normalize=True))

# 7. Graph 1 - Survival Count
plt.figure(figsize=(6,4))
sns.countplot(x='Survived', data=df)
plt.title('Survival Count (0 = Died, 1 = Survived)')
plt.savefig('survival_count.png')
plt.show()

# 8. Graph 2 - Survival by Gender
plt.figure(figsize=(6,4))
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title('Survival by Gender')
plt.savefig('survival_by_gender.png')
plt.show()

# 9. Graph 3 - Age Distribution
plt.figure(figsize=(6,4))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.savefig('age_distribution.png')
plt.show()

# 10. Graph 4 - Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('correlation.png')
plt.show()

print("\nEDA Complete!")
