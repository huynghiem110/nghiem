import tkinter as tk
from tkinter import filedialog
import os
from PyPDF2 import PdfReader
import json
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
from langchain_text_splitters import RecursiveCharacterTextSplitter


def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False,
    )
    chunks = text_splitter.create_documents([text])
    print(chunks[0])
    print(chunks[1])
    return chunks



def get_pdf_text(pdf_docs):
    # Initialize the PdfReader with the provided PDF file
    reader = PdfReader(pdf_docs)
    text = ""
    # Iterate over all the pages and extract text
    for page in reader.pages:
        text += page.extract_text()

    return text

def select_and_process_files():
    # Open file dialog to select multiple PDF files
    file_paths = filedialog.askopenfilenames(title="Select PDF Files", filetypes=[("PDF files", "*.pdf")])
    
    if file_paths:
        # Process each selected PDF file
        for file_path in file_paths:
            text = get_pdf_text(file_path)
            text_chunks = get_text_chunks(text)

            embed_model = HuggingFaceEmbedding(
            model_name="hkunlp/instructor-xl"
            )
            # Create an array of text to embed
            context_array = []
            for i, row in enumerate(text_chunks):
                context_array.append(row.page_content)
            embeddings = [embed_model.get_text_embedding(chunk) for chunk in context_array]
            # embeddings = embed_model.get_text_embedding(context_array)
            # print(embeddings[:5])
# Load button style from JSON file
with open('button_style.json', 'r') as style_file:
    button_style = json.load(style_file)

# Create the main window
root = tk.Tk()
root.title("PDF Loader")
root.geometry("300x100")

# Create a button with styles applied from JSON
file_button = tk.Button(root, 
                        text=button_style['text'], 
                        bg=button_style['bg'], 
                        fg=button_style['fg'], 
                        font=tuple(button_style['font']),
                        borderwidth=button_style['borderwidth'],
                        relief=button_style['relief'],
                        padx=button_style['padx'],
                        pady=button_style['pady'],
                        command=select_and_process_files)
file_button.pack(pady=20)

# Run the application
root.mainloop()
