
# Word Frequency Counter with Streamlit developed by Reuben Martor

This Streamlit application allows users to analyze word frequency in a text paragraph or an uploaded file. The program supports multiple file formats, provides word frequency counts, and displays the results in a neatly formatted table with sortable and wider columns for better readability.

---

## Features

- **Input Methods**:
  - Type a paragraph directly into the application.
  - Upload a file for analysis.

- **Supported File Formats**:
  - **Text Files (`.txt`)**
  - **Word Documents (`.docx`)**
  - **CSV Files (`.csv`)**
  - **PDF Documents (`.pdf`)**

- **Word Frequency Analysis**:
  - Tokenizes text using regular expressions.
  - Normalizes text by converting to lowercase and removing punctuation.
  - Sorts word frequencies in descending order.
  - Displays results in a compact, styled table.

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/wuahmartor/word-frequency-counter.git
   cd word-frequency-counter
   ```

2. **Set up a virtual environment (optional)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   streamlit run wordCounter.py
   ```

---

## Usage

1. Launch the application with `streamlit run wordCounter.py`.
2. Choose your preferred input method:
   - **Type a Paragraph**: Enter text into the text area.
   - **Upload a File**: Select a `.txt`, `.docx`, `.csv`, or `.pdf` file to upload.
3. Click the "Get Frequency" button to calculate word frequencies.
4. View the results in a styled, sortable table.

---

## Dependencies

- `streamlit`: For building the web application interface.
- `pandas`: For handling tabular data and formatting the results.
- `PyPDF2`: For extracting text from PDF files.
- `python-docx`: For reading Word documents.
- `re` (Regular Expressions): For tokenizing the text.
- `collections.Counter`: For counting word frequencies.

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## File Structure

- `wordCounter.py`: Main application file for the Streamlit interface.
- `requirements.txt`: List of required Python libraries.

---

## Example Output

For the input text:
```
Hello world! Hello again, world.
```

The output table will display:
| Word   | Frequency |
|--------|-----------|
| hello  | 2         |
| world  | 2         |
| again  | 1         |

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements or bug fixes.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Author

Created by Reuben Martor - wuahmartor@gmail.com  If you have any questions or suggestions, feel free to contact me.
