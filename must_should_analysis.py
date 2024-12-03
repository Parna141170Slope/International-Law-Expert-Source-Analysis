
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_must_should_statements(file_path):
    # Load the data
    data = pd.ExcelFile(file_path)
    df = data.parse('Must Should Statements')
    
    # Basic analysis of statement types
    type_counts = df['Type'].value_counts()
    
    # Analysis of hostage references
    hostage_refs = df['Contains_Hostage_Reference'].value_counts()
    
    # Analysis by actor groups
    actor_counts = df['Actor_Grouped'].value_counts()
    
    # Create visualizations
    plt.figure(figsize=(15, 5))
    
    # Statement Types
    plt.subplot(131)
    sns.barplot(x=type_counts.index, y=type_counts.values)
    plt.title('Distribution of Statement Types')
    plt.xticks(rotation=45)
    
    # Hostage References
    plt.subplot(132)
    sns.barplot(x=hostage_refs.index, y=hostage_refs.values)
    plt.title('Distribution of Hostage References')
    
    # Top Actor Groups
    plt.subplot(133)
    top_actors = actor_counts.head(5)
    sns.barplot(x=top_actors.index, y=top_actors.values)
    plt.title('Top 5 Actor Groups')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()
    
    # Calculate percentages
    total_statements = len(df)
    must_statements = len(df[df['Type'] == 'Must statement'])
    should_statements = len(df[df['Type'] == 'Should statement'])
    hostage_references = len(df[df['Contains_Hostage_Reference'] == True])
    
    print('Summary Statistics:')
    print(f'Total Statements: {total_statements}')
    print(f'Must Statements: {must_statements} ({(must_statements/total_statements)*100:.1f}%)')
    print(f'Should Statements: {should_statements} ({(should_statements/total_statements)*100:.1f}%)')
    print(f'Statements with Hostage References: {hostage_references} ({(hostage_references/total_statements)*100:.1f}%)')
    
    return df

# Save this code to a file
