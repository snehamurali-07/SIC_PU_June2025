import pandas as pd
import os
'''
def read_excel_file():
    #Define the path to the Excel file
    file_path ='data_analysis/student_data.csv'

    # Read the Excel file into a pandas DataFrame
    df = pd.read_csv(file_path)

	# Display the first few rows of the DataFrame
    print(df.count())
    print(df.head())
    print(df.tail())

def read_excel_file1():
    file_path = 'data_analysis/student_data.csv'
    df = pd.read_csv(file_path)
    for index, row in df.iterrows():
        print(row[0], '  ', row[1])

def read_excel_file2():
    file_path = 'data_analysis/student_data.csv'
    df = pd.read_csv(file_path)
    for row in df.iterrows():
       print(row[1][0], row[1][1])

read_excel_file()
'''


data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)  # Convert it into a Pandas DataFrame

file_path = 'student_data2.csv'  # Store the DataFrame into a CSV file
df.to_csv(file_path)

if os.path.exists(file_path):  # Read the CSV file using `os` module + built-in file handling
    with open(file_path, 'r') as file:
        content = file.read()
        print("CSV File Content:\n")
        print(content)
else:
    print("CSV file not found.")
