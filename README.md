# SWYNEX - Task 2: Exploratory Data Analysis (EDA)

## Project Overview
Is project me Titanic dataset ka Exploratory Data Analysis (EDA) kiya gaya hai using Python.

## Dataset
- Dataset: Titanic Dataset
- Source: https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
- Rows: 891, Columns: 12

## Tools Used
- Python
- Pandas
- Matplotlib
- Seaborn

## Kya Kiya Gaya
1. Dataset load kiya aur pehli 5 rows dekhi
2. Missing values check ki (Age, Cabin, Embarked)
3. Age ko median se aur Embarked ko mode se fill kiya
4. Cabin column drop kiya (bahut zyada missing values thi)
5. Survival Rate nikala
6. Graphs banaye:
   - Survival Count
   - Survival by Gender
   - Age Distribution
   - Correlation Heatmap

## Key Findings
- Total me se sirf ~38% log survive hue
- Females ka survival rate males se bahut zyada tha
- 1st Class passengers ka survival rate sabse zyada tha
- Fare aur Pclass ka survival se strong relation hai

## How to Run
pip install pandas matplotlib seaborn
python eda.py

## Author
Amreen Khan
