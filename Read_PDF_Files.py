import requests
import PyPDF2  # or pypdf
import streamlit  as st
import os 


#URL="https://iocl.com/uploads/IOC_Results_Q3_24_25_S.pdf"

myURL_To_Read="https://iocl.com/uploads/IOC_Results_Q3_24_25_S.pdf"



# pdf_url = "YOUR_PDF_URL_HERE"  # Replace with the actual URL of the PDF
pdf_url = myURL_To_Read

try:
    # Download the PDF
    response = requests.get(pdf_url, stream=True)
    response.raise_for_status()  # Raise an exception for bad status codes

    # Open the PDF in binary read mode
    pdf_file = open("temp.pdf", "wb")  # Create a temporary file
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            pdf_file.write(chunk)
    pdf_file.close()

    # Open the PDF with PyPDF2
    with open("temp.pdf", "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)  # or pypdf.PdfReader

        # Iterate through pages and extract text
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text() + "\n"  # Extract text and add a newline
            st.write("Displaying the contents of the PDF file\n")
            st.write(text+"\n")
            st.markdown(text)
            

    #print(text)
    st.write("File Contents Completed...\n")
    print("File reading is completed...Output is on Streamlite Browser..")
    #st.write_stream(text+"\n")
    #st.write(text+"\n")
  


except requests.exceptions.RequestException as e:
    print(f"Error downloading PDF: {e}")
except Exception as e:
    print(f"Error processing PDF: {e}")