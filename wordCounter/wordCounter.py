import re
from collections import Counter
import string
import docx
import pandas as pd
from PyPDF2 import PdfReader
import streamlit as st

def count_word_frequency(text):
    """Counts word frequencies using a custom tokenizer."""
    # Normalize text: convert to lowercase and remove punctuation
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize text using regular expressions
    words = re.findall(r'\b\w+\b', text)  # Matches words only (ignores spaces, punctuation)
    
    # Count word frequencies
    word_counts = Counter(words)
    return word_counts

def read_file(file):
    """Reads content from supported file types."""
    if file.name.endswith('.txt'):
        return file.read().decode('utf-8')
    elif file.name.endswith('.docx'):
        doc = docx.Document(file)
        return "\n".join([paragraph.text for paragraph in doc.paragraphs])
    elif file.name.endswith('.pdf'):
        pdf_reader = PdfReader(file)
        return "\n".join([page.extract_text() for page in pdf_reader.pages])
    elif file.name.endswith('.csv'):
        df = pd.read_csv(file)
        return df.to_string()
    else:
        st.error("Unsupported file format. Please upload a .txt, .docx, .csv, or .pdf file.")
        return None

# Streamlit Interface
st.title("Word Frequency Counter")

# User Input Options
option = st.radio(
    "Choose an input method:",
    ("Type a paragraph", "Upload a file")
)

text = ""

if option == "Type a paragraph":
    text = st.text_area("Enter your paragraph here:")
elif option == "Upload a file":
    uploaded_file = st.file_uploader(
        "Upload a .txt, .docx, .csv, or .pdf file:", type=['txt', 'docx', 'csv', 'pdf']
    )
    if uploaded_file is not None:
        text = read_file(uploaded_file)

# Button to trigger word frequency calculation
if st.button("Get Frequency"):
    if text:
        st.write("### Word Frequencies (Sorted by Frequency):")
        word_counts = count_word_frequency(text)
        
        # Convert to DataFrame and sort by frequency in descending order
        word_freq_table = pd.DataFrame(word_counts.items(), columns=["Word", "Frequency"])
        word_freq_table = word_freq_table.sort_values(by="Frequency", ascending=False)
        
        # Adjust column width using Pandas Styler
        styled_table = word_freq_table.style.set_table_styles(
            [
                {"selector": "th", "props": [("text-align", "center"), ("width", "100px")]},
                {"selector": "td", "props": [("text-align", "center"), ("width", "100px")]},
            ]
        )
        
        # Display the styled table
        st.dataframe(styled_table, use_container_width=True)
    else:
        st.warning("Please provide input text or upload a file.")

# Main function to run the app
def main():
    if __name__ == "__main__":
        main()