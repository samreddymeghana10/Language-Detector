import streamlit as st
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Make results consistent
DetectorFactory.seed = 0

st.set_page_config(
    page_title="Language Detector",
    page_icon="🌍"
)

st.title("🌍 Language Detector")
st.write("Enter text below and detect its language.")

text = st.text_area(
    "Enter text:",
    height=150,
    placeholder="Example: Bonjour, comment allez-vous aujourd'hui?"
)

if st.button("Detect Language"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        try:
            language_code = detect(text)

            language_names = {
                "en": "English",
                "fr": "French",
                "es": "Spanish",
                "de": "German",
                "it": "Italian",
                "pt": "Portuguese",
                "nl": "Dutch",
                "ru": "Russian",
                "ar": "Arabic",
                "hi": "Hindi",
                "te": "Telugu",
                "ta": "Tamil",
                "kn": "Kannada",
                "ml": "Malayalam",
                "bn": "Bengali",
                "zh-cn": "Chinese",
                "ja": "Japanese",
                "ko": "Korean",
            }

            language_name = language_names.get(
                language_code,
                "Unknown language"
            )

            st.success("Language detected!")
            st.write(f"**Language:** {language_name}")
            st.write(f"**Language code:** `{language_code}`")

        except LangDetectException:
            st.error(
                "Unable to detect the language. "
                "Please enter a longer text sample."
            )
