import streamlit as st
from googletrans import Translator, LANGUAGES

# Translator object
translator = Translator()

# Streamlit App
st.set_page_config(page_title="Language Translation Tool", page_icon="🌐")

st.title("🌐 Language Translation Tool")

# Input text
text = st.text_area("Enter text to translate:", "")

# Language selectors
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("Source Language", 
                               ["auto"] + list(LANGUAGES.keys()), 
                               format_func=lambda x: "Auto Detect" if x=="auto" else LANGUAGES[x].title())
with col2:
    target_lang = st.selectbox("Target Language", 
                               list(LANGUAGES.keys()), 
                               index=list(LANGUAGES.keys()).index("en"), 
                               format_func=lambda x: LANGUAGES[x].title())

# Translate Button
if st.button("Translate"):
    if text.strip():
        try:
            result = translator.translate(text, src=source_lang, dest=target_lang)
            st.success("✅ Translation successful!")
            st.subheader("Translated Text:")
            st.text_area("Output", result.text, height=120)
            
            # Copy functionality
            st.code(result.text)
        except Exception as e:
            st.error(f"⚠ Error: {str(e)}")
    else:
        st.warning("⚠ Please enter some text to translate.")
