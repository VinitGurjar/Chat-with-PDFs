import streamlit as st
#For pdf functionality
from PyPDF2 import PdfReader
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import RecursiveCharacterTextSplitter

#sidebar contents
with st.sidebar:
    st.title(" 📒😁 Chat-with-PDF")
    st.markdown('''
        ## About
        Now you can chat with your PDF files.

        This app is Powered by: 
        - [Streamlit](https://streamlit.io/).
        - [LangChain](https://www.langchain.com/).
        - [OpenAI](https://openai.com/).

    ''')

    add_vertical_space(5)
    st.write('Made with 🥰 by [Vinit Gurjar](https://github.com/VinitGurjar)')


def main():
    st.header("Chat with PDF 📒😁")

    # Upload a pdf file
    pdf = st.file_uploader("Upload a PDF file", type='pdf')

    #Display the pdf file if it is uploaded
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        #st.write(pdf_reader) - it will write the object name on the web
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        #st.write(text) - Will show the text of pdf on the web

        #Split the text into chunks of 1000 characters(token)
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200, 
            length_function = len
            ) 
        chunks = text_splitter.split_text(text=text)

        st.write(chunks)

if __name__ == "__main__":
    main()


