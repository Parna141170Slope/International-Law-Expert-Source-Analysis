
import pandas as pd
import matplotlib.pyplot as plt

# Define the counts and mentions for each organization
statement_data = {
    'Organization': ['PHCR Gaza', 'Al Mezan', 'Al-Haq', 'Addameer', 'DCI Palestine'],
    'Total Statements': [42, 35, 28, 0, 0],
    'Hostage Mentions': [3, 2, 1, 0, 0]
}

# Create a DataFrame
statement_df = pd.DataFrame(statement_data)

# Calculate the percentage of statements mentioning hostages
statement_df['Percentage Mentioning Hostages'] = (statement_df['Hostage Mentions'] / statement_df['Total Statements'].replace(0, 1)) * 100

# Display the DataFrame
print(statement_df)

# Plot the data for visualization
plt.figure(figsize=(10, 6))
plt.bar(statement_df['Organization'], statement_df['Percentage Mentioning Hostages'], color='skyblue')
plt.title('Percentage of Statements Mentioning Hostages by Organization')
plt.ylabel('Percentage')
plt.xlabel('Organization')
plt.ylim(0, 10)
plt.show()
