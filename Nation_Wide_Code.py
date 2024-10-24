import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('/content/760k-Car-Owners-Nationwide-China-csv-2020.csv')

# Define a dictionary to map Chinese headers to English headers
header_translation = {
    '车架号': 'VIN',  # Vehicle Identification Number
    '姓名': 'Name',
    '身份证': 'ID Number',
    '性别': 'Gender',
    '手机': 'Phone',
    '邮箱': 'Email',
    '省': 'Province',
    '城市': 'City',
    '地址': 'Address',
    '邮编': 'Postal Code',
    '生日': 'Birthday',
    '行业': 'Industry',
    '月薪': 'Monthly Salary',
    '婚姻': 'Marital Status',
    '教育': 'Education',
    '车系': 'Car Series',
    '车型': 'Car Model',
    '配置': 'Configuration',
    '发动机号': 'Engine Number',
    'BRAND': 'Brand',
    '颜色': 'Color',
}

# Rename the columns using the header_translation dictionary
df.rename(columns=header_translation, inplace=True)

# Define the file path where you want to save the updated CSV file
file_path = '/content/760k-Car-Owners-Nationwide-China-csv-2020.csv' # Updated file name to avoid overwriting
df.to_csv(file_path, index=False)

print("Headers have been translated to English, and the main file has been updated.")


import pandas as pd

# Load the CSV file into a pandas DataFrame
file_path = '/content/760k-Car-Owners-Nationwide-China-csv-2020.csv'
df = pd.read_csv(file_path)

# List of columns to drop
columns_to_drop = ['gender', 'monthly salary', 'marriage', 'educate', 'configuration', 'color', 'industry','Unnamed: 21']

# Drop the specified columns from the DataFrame
df.drop(columns=columns_to_drop, inplace=True, errors='ignore')

# Overwrite the original CSV file with the updated DataFrame
file_path = '/content/760k-Car-Owners-Nationwide-China-csv-2020.csv' # Updated file name to avoid overwriting
df.to_csv(file_path, index=False)

print("Specified columns have been dropped, and the main file has been updated.")


import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('/content/760k-Car-Owners-Nationwide-China-csv-2020.csv')

# Function to check for missing values
def check_missing_values(df):
    missing_values = df.isnull().sum()
    missing_summary = missing_values[missing_values > 0].sort_values(ascending=False)

    if missing_summary.empty:
        print("No missing values found in the dataset.")
    else:
        print("Missing values found in the following columns:")
        print(missing_summary)

# Function to check for duplicate rows
def check_duplicates(df):
    duplicate_rows = df[df.duplicated()]

    if duplicate_rows.empty:
        print("No duplicate rows found.")
    else:
        print(f"Number of duplicate rows: {len(duplicate_rows)}")
        print(duplicate_rows.head())  # Display the first few duplicate rows

# Function to check for outliers using IQR method
def check_outliers(df):
    outliers_info = {}

    # Checking for numerical columns only
    numerical_columns = df.select_dtypes(include=['number']).columns

    for column in numerical_columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # Find outliers
        outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]

        if not outliers.empty:
            outliers_info[column] = len(outliers)

    if outliers_info:
        print("Outliers found in the following columns:")
        for col, count in outliers_info.items():
            print(f"{col}: {count} outliers")
    else:
        print("No outliers found.")

# Run checks
check_missing_values(df)
check_duplicates(df)
check_outliers(df)


import pandas as pd
import re
import os

# Define a regular expression pattern to validate emails
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Function to validate email addresses
def is_valid_email(email):
    # Check if the email is a non-empty string
    if isinstance(email, str) and email:
        # Validate against the corrected regex pattern
        return bool(re.fullmatch(email_pattern, email))
    return False  # Return False for non-string or empty values

# Identify invalid emails
invalid_emails_df = df[~df['Email'].apply(is_valid_email)]

# Save invalid emails to 'garbage2.csv', creating the file if it doesn't exist
invalid_emails_file = '/content/garbage2.csv'
if not os.path.exists(invalid_emails_file):
    with open(invalid_emails_file, 'w') as file:
        pass  # This will create an empty file if it doesn't exist

# Write invalid emails to 'garbage2.csv'
invalid_emails_df.to_csv(invalid_emails_file, index=False)

# Remove rows with invalid emails from the main DataFrame
df = df[df['Email'].apply(is_valid_email)]

# Fill remaining missing values (if any) with 'N/A'
df.fillna('N/A', inplace=True)

# Save the cleaned DataFrame, updating the main file
df.to_csv('/content/760k-Car-Owners-Nationwide-China-csv-2020.csv', index=False)

print(df.head())



I used this code again to double check a change i made in the code above


import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('/content/760k-Car-Owners-Nationwide-China-csv-2020.csv')

# Function to check for missing values
def check_missing_values(df):
    missing_values = df.isnull().sum()
    missing_summary = missing_values[missing_values > 0].sort_values(ascending=False)

    if missing_summary.empty:
        print("No missing values found in the dataset.")
    else:
        print("Missing values found in the following columns:")
        print(missing_summary)

# Function to check for duplicate rows
def check_duplicates(df):
    duplicate_rows = df[df.duplicated()]

    if duplicate_rows.empty:
        print("No duplicate rows found.")
    else:
        print(f"Number of duplicate rows: {len(duplicate_rows)}")
        print(duplicate_rows.head())  # Display the first few duplicate rows

# Function to check for outliers using IQR method
def check_outliers(df):
    outliers_info = {}

    # Checking for numerical columns only
    numerical_columns = df.select_dtypes(include=['number']).columns

    for column in numerical_columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # Find outliers
        outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]

        if not outliers.empty:
            outliers_info[column] = len(outliers)

    if outliers_info:
        print("Outliers found in the following columns:")
        for col, count in outliers_info.items():
            print(f"{col}: {count} outliers")
    else:
        print("No outliers found.")

# Run checks
check_missing_values(df)
check_duplicates(df)
check_outliers(df)


import pandas as pd
import os

# Load the main CSV file into a DataFrame (replace with your file path)
df = pd.read_csv('/content/760k-Car-Owners-Nationwide-China-csv-2020.csv')

# Identify rows with missing values (NaN)
missing_values_df = df[df.isnull().any(axis=1)]  # Rows with any missing values

# Save rows with missing values to 'garbage2.csv', creating the file if it doesn't exist
garbage_file = '/content/garbage2.csv'
if not os.path.exists(garbage_file):
    with open(garbage_file, 'w') as file:
        pass  # Create an empty file if it doesn't exist

# Write rows with missing values to 'garbage2.csv'
missing_values_df.to_csv(garbage_file, index=False)

# Remove rows with missing values from the main DataFrame
df_cleaned = df.dropna()

# Save the updated DataFrame (rows without missing values) to the same file
df_cleaned.to_csv('/content/760k-Car-Owners-Nationwide-China-csv-2020.csv', index=False)

print("Rows with missing values have been saved to 'garbage2.csv'.")
print("The main file has been updated, keeping only rows without missing values.")


I used this code below to change the headers to their correct names


import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('/content/760k-Car-Owners-Nationwide-China-csv-2020.csv')

# Define a dictionary to map Chinese headers to English headers
header_translation = {
    'VIN': 'VIN',  # Vehicle Identification Number
    'Name': 'Name',
    'ID Number': 'ID_Number',
    'Gender': 'Gender',
    'Phone': 'Phone',
    'Email': 'Email',
    'Province': 'Province',
    'City': 'City',
    'Address': 'Address',
    'Postal Code': 'Postal_Code',
    'Birthday': 'Birthday',
    'Industry': 'Industry',
    'Monthly Salary': 'Monthly_Salary',
    'Marital Status': 'Marital_Status',
    'Education': 'Education',
    'Car Series': 'Car_Series',
    'Car Model': 'Car_Model',
    'Configuration': 'Configuration',
    'Engine Number': 'Engine_Number',
    'Brand': 'Brand',
    'Color': 'Color',
}

# Rename the columns using the header_translation dictionary
df.rename(columns=header_translation, inplace=True)

# Define the file path where you want to save the updated CSV file
file_path = '/content/760k-Car-Owners-Nationwide-China-csv-2020.csv' # Updated file name to avoid overwriting
df.to_csv(file_path, index=False)

print("Headers have been translated to English, and the main file has been updated.")

