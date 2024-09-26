import streamlit as st
import time
import os
import json
from datetime import datetime
import getcmts as gc

# functions
def run_javascript(js_code):
    st.markdown(f"<script>{js_code}</script>", unsafe_allow_html=True)

port = int(os.environ.get("PORT", 8501))

# main
def run():
    st.set_page_config(
        page_title="Scrape Comments!",
        page_icon="🐍"
    )
    st.title("SCRAPE INSTAGRAM COMMENTS FOR DATA-ANALYSIS AND RESEARCH!🐍")
    
    image_url = '123.png'
    st.image(image_url, width=300)  # Adjust the width to make the image smaller
    
    st.header("ENTER INSTAGRAM CREDENTIALS!!")
    st.write("**Note:** Due to Instagram's policy, you must log in before we can scrape comments.")
    st.write("Your credentials are required to access the comments on the specified post.")
    
    email = st.text_input("Enter your email:", type='default')
    password = st.text_input("Enter your password:", type='password')
    url = st.text_input("Enter a URL:", type='default')
    st.write("higher the scroll count higher the number of comments fetched and higher the execution time !")
    scrollcount = st.number_input("Scroll count:", min_value=0, max_value=100, step=1, format="%d")
    
    if st.button("Submit!"):
        time.sleep(1)
        st.write('Processing!!!')
        time.sleep(1)
        st.write("This will take at least 5 minutes!!!")
        t = 1
        filename = None
        
        while t <= 5:
            try:
                data = gc.cmntsget(email, password, url)
                dict_data = str(data)
                current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"file_{current_time}.json"
                with open(filename, 'w') as file:
                    json.dump(data, file)
                break
            except Exception as e:
                st.write(f"Attempt {t} failed! Error: {str(e)}")
                t += 1
        
        if filename:
            st.write("Success!")
            with open(filename, 'r') as file:
                json_data = file.read()
            st.download_button("Download", json_data, file_name=f"{filename}", mime='application/json')
        else:
            st.write("Process failed!! 😔")
            if st.button("Try again! 🔁"):
                run_javascript("location.reload();")
        
        st.header("Process Executed!! 🤖")

run()
