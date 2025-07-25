import streamlit as st
import requests 

st.title("Ryhming words generator")
word=st.text_input("enter the word:")
is_clicked=st.button("click me!",type="primary")
if is_clicked:
    
    endpoint = f"https://api.datamuse.com/words?sp={word}"
 
    response = requests.get(endpoint)
 
    data = response.json()
 
    if response.status_code == 200:
        for item in data:
            st.write(item.get('word'))

 
