import streamlit as st
import PyPDF2
import os

def convert_pdf_to_text(file):
    # Read the PDF file
    reader = PyPDF2.PdfReader(file)

    # Extract text from each page of the PDF
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()

    return text

def save_text_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

def main():
    st.title("PDF to Text Converter")

    # File Upload
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        # Display file details
        st.text("File Name: " + uploaded_file.name)
        st.text("File Size: " + str(uploaded_file.size) + " bytes")

        # Convert PDF to text
        text = convert_pdf_to_text(uploaded_file)

        # Save text file
        base_filename = os.path.splitext(uploaded_file.name)[0]
        text_filename = base_filename + ".txt"
        save_text_file(text, text_filename)
        st.success("Text file saved as " + text_filename)

if __name__ == '__main__':
    main()
