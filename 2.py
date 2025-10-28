import streamlit as st

def generate_acronym(phrase):
    words = phrase.split()
    acronym = ''.join(word[0].upper() for word in words if word)
    return acronym

st.title("Acronym Generator")

phrase = st.text_input("Enter a phrase:")
if st.button("Generate"):
    if phrase:
        acronym = generate_acronym(phrase)
        st.success(f"Acronym: {acronym}")
    else:
        st.warning("Please enter a phrase.")
