import pandas as pd
from googletrans import Translator

# Load the dataset
file_path = 'avito_train.tsv'
df = pd.read_csv('avito.csv')
df = df.drop(columns=['itemid','price','is_proved','is_blocked','phones_cnt','emails_cnt','urls_cnt','close_hours'])
# Initialize the translator
translator = Translator()

# Define the function to translate text
def translate_text(text, src='ru', dest='en'):
    try:
        return translator.translate(text, src=src, dest=dest).text
    except Exception as e:
        print(f"Error translating text: {text}. Error: {e}")
        return text
df['title'] = df['title'].astype(str)
df['description'] = df['description'].astype(str)
df['attrs'] = df['attrs'].astype(str)
df['category'] = df['category'].astype(str)
df['subcategory'] = df['subcategory'].astype(str)
# Translate the 'Title', 'Description', and 'Attributes' columns
df['title'] = df['title'].apply(lambda x: translate_text(x))
df['description'] = df['description'].apply(lambda x: translate_text(x))
df['attrs'] = df['attrs'].apply(lambda x: translate_text(x))
df['category'] = df['category'].apply(lambda x: translate_text(x))
df['subcategory'] = df['subcategory'].apply(lambda x: translate_text(x))
# Save the translated DataFrame to a new CSV file
output_path_full_translated = 'eng_avito.csv'
df.to_csv(output_path_full_translated, index=False)

# Display the path to the translated file
print(f"Translated dataset saved to {output_path_full_translated}")