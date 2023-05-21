import streamlit as st
import PyPDF2
import os
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader


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
    folder_path = "./data"  # Specify the folder path where you want to save the file
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

# Example usage
text = "This is some sample text."
filename = "output.txt"
save_text_file(text, filename)

def ask_llama():
    documents = SimpleDirectoryReader('data').load_data()
    index = GPTVectorStoreIndex.from_documents(documents)

    query_engine = index.as_query_engine()
    questions = [["About the contract", "Summarize this vendor contract"],
             ["Negotiate better terms", "5 Bullet points for better terms"],
             ["Highlight any red flags", "5 Bullet points for red flags"],
             ]

    for question in questions:
        print(question, "Debug!")
        st.write('# {}'.format(question[0]))
        response = query_engine.query(question[1])
        st.write(response)

    answer = st.text_area(label='Any Questions?', placeholder='Ask any questions you may have about the contract', key='qa_prompt')
    if answer:
        response = query_engine.query(answer)
        st.write(response)

def main():
    st.set_page_config(page_title="Afterwork: Vendor Negotiation Tool", page_icon=":robot:")
    st.header("Afterwork: Vendor Negotiation Tool")

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
        ask_llama()
if __name__ == '__main__':
    main()
