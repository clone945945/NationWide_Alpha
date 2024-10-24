# NationWide_TeamAlpha


![image](https://github.com/user-attachments/assets/b085470a-a444-4c4a-aae2-629db56e7996)

# 760k Car Owners Nationwide China Data Cleaning
Overview
This repository contains Python scripts for cleaning and processing a large dataset of car owners in China. The main objectives are to:

* Rename the column headers from Chinese to English.
* Drop specific irrelevant columns.
* Validate and clean the email addresses.
* Check for missing values, duplicates, and outliers.
* Handle and remove invalid data, including rows with missing values.
  # Dataset
The dataset, `760k-Car-Owners-Nationwide-China-csv-2020.csv`, contains details of 760,000 car owners. It includes information such as names, addresses, car details, and more.

# Code Functionality

# **1. Header Translation**
The headers in the dataset are in Chinese. A dictionary has been created to translate these headers to English:

* The script renames columns like 车架号 to VIN, 姓名 to Name, etc.
* The dataset is then saved back into the original file.
# 2. Dropping Irrelevant Columns
Some columns in the dataset (e.g., `gender, monthly salary, marriage, education,` etc.) are not required for the analysis. These columns are dropped, and the changes are saved to the main file.

# 3. Email Validation and Cleaning
 * A regular expression is used to validate email addresses.
 * Invalid email addresses (such as "noemail@email.com") are extracted and saved to a separate file (garbage2.csv).
 * Rows with invalid email addresses are removed from the dataset.
 * Any missing values are filled with `'N/A'`.
   
# 4. Missing Values, Duplicate Rows, and Outliers Detection
* The script checks for any missing values, duplicate rows, and outliers.
* **Missing Values:** If missing values are found, a summary is printed.
* **Duplicates:** If duplicate rows exist, they are identified and printed.
* **Outliers:** Numerical columns are checked for outliers using the IQR (Interquartile Range) method. Outliers are detected and reported.
  
# How to Use
* Make sure your dataset file is named 760k-Car-Owners-Nationwide-China-csv-2020.csv and is placed in the /content/ directory of your project.

* Run the Code: Each script performs a different cleaning task on the dataset. You can execute these scripts in the given order to clean the data efficiently.
  
  # Code Breakdown
Header Translation:
# This code translates the headers from Chinese to English.
<!-- Python block -->

```python
header_translation = {
    '车架号': 'VIN', 
    '姓名': 'Name',
    # ... (other translations)
}
df.rename(columns=header_translation, inplace=True)
df.to_csv(file_path, index=False)
```
# Dropping Columns:
<!-- Python block -->

```python
# This script drops unnecessary columns such as 'gender', 'marriage', etc.
columns_to_drop = ['gender', 'monthly salary', 'marriage', ...]
df.drop(columns=columns_to_drop, inplace=True)
df.to_csv(file_path, index=False)
```
# Email Validation:
<!-- Python block -->

```python
# Validate emails and remove invalid ones.
invalid_emails_df = df[~df['Email'].apply(is_valid_email)]
invalid_emails_df.to_csv(invalid_emails_file, index=False)
df = df[df['Email'].apply(is_valid_email)]
df.fillna('N/A', inplace=True)
df.to_csv(file_path, index=False)
```
Checking for Missing Values, Duplicates, and Outliers:
<!-- Python block -->

```python
# Check for missing values, duplicates, and outliers.
check_missing_values(df)
check_duplicates(df)
check_outliers(df)
```
# Handling Missing Values:
<!-- Python block -->

```python
# Identify rows with missing values and save them to 'garbage2.csv'.
missing_values_df = df[df.isnull().any(axis=1)]
missing_values_df.to_csv(garbage_file, index=False)
df_cleaned = df.dropna()
df_cleaned.to_csv(file_path, index=False)
```
# How to Run Checks After Changes
Whenever changes are made to the data, it's important to re-check the dataset for issues such as missing values, duplicates, or outliers.

In the code:

* Missing values: If there are missing values, a summary of which columns contain them will be displayed.
* Duplicates: If duplicate rows are present, the count and a preview will be shown.
* Outliers: Columns with outliers will be reported.

# Requirements
Python 3.x
Libraries: `pandas, re, os`
To install the required libraries, use:
<!-- Python block -->

```python
pip install pandas
```
# Conclusion
This project ensures the dataset is clean and ready for further analysis by addressing issues like missing values, invalid data, and irrelevant columns. The code snippets above provide a structured approach for automating this data cleaning process.


  
