import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space


#sidebar contents
with st.sidebar:
    st.title(" 📒😁 Chat-with-PDF")
    st.markdown('''
        ## About
        Now you can chat with your PDF files.

        This app is Powered by: 
        - [Streamlit](https://streamlit.io/).
        - [LangChain](https://www.langchain.com/).
        - [OpenAI](https://openai.com/). LLM model

    ''')

    add_vertical_space(5)
    st.write('Made with 🥰 by [Vinit Gurjar](https://github.com/VinitGurjar)')