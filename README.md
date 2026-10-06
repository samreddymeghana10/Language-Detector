# Language Detector

A simple Python-based web application that detects the language of the given text using Natural Language Processing (NLP). The application is built using Streamlit and the `langdetect` library.

## Features

- Detects the language of input text
- Simple and user-friendly Streamlit interface
- Supports multiple languages
- Uses NLP techniques for language detection
- Fast and easy to use
- Can be extended with machine learning and transformer models

## Technologies Used

- Python 3.11.9
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Requests
- python-dotenv
- Langdetect
- NLTK
- spaCy
- Transformers
- PyTorch

## Requirements

```text
streamlit>=1.40,<2
pandas>=2.2,<3
numpy>=1.26,<3
scikit-learn>=1.5,<2
requests>=2.32,<3
python-dotenv>=1.0,<2
langdetect>=1.0,<2
nltk>=3.9,<4
spacy>=3.7,<4
transformers>=4.45,<6
torch>=2.4,<3
```

## Installation

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the virtual environment

For Windows:

```bash
.venv\Scripts\activate
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

Or:

```bash
python -m streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## How It Works

1. The user enters text into the Streamlit application.
2. The input text is processed.
3. The language detection model analyzes the text.
4. The detected language is displayed to the user.

## Example

Input:

```text
Hello, how are you?
```

Output:

```text
Detected Language: English
```

Another example:

```text
नमस्ते, आप कैसे हैं?
```

Output:

```text
Detected Language: Hindi
```

## Project Structure

```text
language-detector/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── data/
├── models/
└── assets/
```

## Future Improvements

- Add language confidence scores
- Support more languages
- Add text translation
- Add speech-to-text detection
- Add document language detection
- Add transformer-based language detection
- Improve the user interface
- Deploy the application online

## Troubleshooting

If Streamlit is not recognized, use:

```bash
python -m streamlit run app.py
```

If a package is missing, run:

```bash
pip install -r requirements.txt
```

Check the Python version using:

```bash
python --version
```

The recommended Python version is:

```text
Python 3.11.9
```

## License

This project is created for  learning purposes.