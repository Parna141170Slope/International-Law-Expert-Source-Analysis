
import pandas as pd

# Load the dataset of law review and other sources
# Assuming the dataset is in a CSV file named 'law_review_sources.csv'
data = pd.read_csv('law_review_sources.csv')

# Define keywords and categories for classification
keywords = {
    'Hostages': ['hostage', 'hostages'],
    'International Law': ['ICC', 'international law', 'jurisdiction'],
    'Human Rights': ['human rights', 'UN', 'Geneva Convention']
}

# Create a function to classify sources based on keywords
def classify_source(text):
    for category, words in keywords.items():
        if any(word in text.lower() for word in words):
            return category
    return 'Other'

# Apply the classification function to the dataset
data['Category'] = data['Content'].apply(classify_source)

# Save the classified data to a new file
classified_file = 'classified_law_review_sources.csv'
data.to_csv(classified_file, index=False)

print("Classified law review sources saved to:", classified_file)
