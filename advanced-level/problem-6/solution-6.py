from operator import index

import pandas as pd

# Step 1: Read the CSV file
data = pd.read_excel(r'/home/wsl-ubuntu/Python_task/python-practice-problems/advanced-level/problem-6/mydata.xlsx')

# Step 2: Sort by 'score' in descending order (highest first)
sorted_data = data.sort_values(by='marks', ascending=False)

# Step 3: Get top 5 records
top_5 = sorted_data.head(5)

# Step 4: Display result
print(top_5)
