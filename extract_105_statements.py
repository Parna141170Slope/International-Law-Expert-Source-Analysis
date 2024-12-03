
import pandas as pd

# Load the Excel file
data = pd.ExcelFile('InternationalLawNarrativeAnalysisNSeemanandJBallabon20241124.xlsx')

# Load the 'Must Should Statements' tab
must_should_tab = data.parse(sheet_name='Must Should Statements')

# Define keywords and organizations
hostage_keywords = ['hostage', 'hostages']
indomitable_organizations = ['PCHR Gaza', 'Al Mezan', 'Al-Haq', 'Addameer', 'DCI Palestine']

# Filter for statements mentioning hostages
hostage_statements = must_should_tab[must_should_tab['Statement'].str.contains('|'.join(hostage_keywords), case=False, na=False)]

# Further filter for the five indomitable organizations
hostage_statements_filtered = hostage_statements[hostage_statements['Source'].str.contains('|'.join(indomitable_organizations), na=False)]

# Save the filtered data to an Excel file
if not hostage_statements_filtered.empty:
    hostage_statements_filtered.to_excel('Hostage_Statements_105.xlsx', index=False)
    print("Hostage-related statements saved to: Hostage_Statements_105.xlsx")
else:
    print("No hostage-related statements found for the five indomitable organizations.")
