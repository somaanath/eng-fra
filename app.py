import streamlit as st
from transformers import pipeline

classifier = pipeline("translation_en_to_fr",model="t5-base")
def main():
    st.title("English to french")

    with st.form("text_field"):
        text = st.text_area('enter some text:')
        # clicked==True only when the button is clicked
        clicked = st.form_submit_button("Submit")
        if clicked:
          results = classifier([text])
          st.json(results)

if __name__ == "__main__":
    main()