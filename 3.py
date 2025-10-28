import streamlit as st

# Define the list of words to ignore
IGNORE_WORDS = {'of', 'and', 'the', 'in', 'on', 'at', 'for', 'with', 'a', 'an'}

def generate_acronym(phrase):
    words = phrase.split()
    # Only take the first letter of words not in IGNORE_WORDS
    acronym = ''.join(word[0].upper() for word in words if word.lower() not in IGNORE_WORDS)
    return acronym

# Streamlit UI
st.set_page_config(page_title="Acronym Generator", page_icon="🔤")

st.title("🔤 Acronym Generator")

phrase = st.text_input("Enter a phrase:")
if st.button("Generate"):
    if phrase.strip():
        acronym = generate_acronym(phrase)
        if acronym:
            st.success(f"**Acronym:** {acronym}")
        else:
            st.warning("No valid words to form an acronym.")
    else:
        st.warning("Please enter a phrase.")
