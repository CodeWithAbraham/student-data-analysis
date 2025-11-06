import pandas as pd  
# Load dataset
df=pd.read_csv('Student_performance_data _.csv') 

print("First 5 rows:\n", df.head())  
print("\nData Summary:\n")
print(df.info())
print("\nStatistical Description:\n", df.describe())

# Create and insert EngagementLevel column
engagement_values = ['High', 'Medium', 'Low', 'Medium', 'High', 'Low', 'High', 'Medium', 'Low', 'High'] * ((len(df)//10)+1) 
engagement_values=engagement_values[:len(df)]
df.insert(5, column='EngagementLevel', value=engagement_values)  

# Create and insert AttendanceLevel based on Absences
attendance_pattern = ['High', 'Medium', 'Low', 'Medium', 'High', 'Medium', 'Low', 'High', 'Low', 'Medium']* ((len(df)//10)+1) 
attendance_pattern = attendance_pattern[:len(df)]
df.insert(7, column='AttendanceLevel', value=attendance_pattern) 

# Drop unwanted column
df.drop(columns='Ethnicity',inplace=True) 

# Sort by GPA descending
df.sort_values(by='GPA', ascending=False, inplace=True) 

# Calculate mean GPA by EngagementLevel and print 
mean_gpa_engagement = df.groupby('EngagementLevel')['GPA'].mean()
print("\nMean GPA by Engagement Level:")
print(mean_gpa_engagement)

# Print count of missing values per column
print("\nMissing values count per column:")
print(df.isnull().sum())

# Save the final DataFrame to Excel file
df.to_excel('output.xlsx', index=False)
