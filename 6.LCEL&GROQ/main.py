import os
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq API key
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize the model
model = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)

# Initialize the output parser
parser = StrOutputParser()

# Define the prompt template
system_template = "Translate the following into {language}. Please provide only the translation."
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "{text}")
])

# Create the chain
chain = prompt_template | model | parser

# Streamlit App UI
st.title("Language Translation Chatbot")


# Language input field
language = st.text_input("Language:")

# Text input area for the text to translate
text_input = st.text_area("Enter the text you want to translate:")

# Submit button
if st.button("Translate"):
    if not language.strip() or not text_input.strip():
        st.warning("Please provide both the target language and the text to translate.")
    else:
        # Invoke the translation chain
        result = chain.invoke({"language": language.strip(), "text": text_input.strip()})
        # Display the result
        st.success(f"Translation:\n\n{result}")

































# # or 
# # Language selection dropdown
# language = st.selectbox("Select the target language:", ["Russian", "Spanish", "French", "German", "Chinese", "Japanese"])

# # Text input box
# text_input = st.text_area("Enter the text you want to translate:")

# # Submit button
# if st.button("Translate"):
#     if not language or not text_input:
#         st.warning("Please provide both the text and select a language.")
#     else:
#         # Invoke the translation chain
#         result = chain.invoke({"language": language, "text": text_input})
#         # Display the result
#         st.success(f"Translation:\n\n{result}")




















































# import os 
# import streamlit as st 
# from fastapi import FastAPI
# import uvicorn 
# from langchain_core.prompts import ChatPromptTemplate 
# from langchain_core.output_parsers import StrOutputParser 
# from langchain_groq import ChatGroq 
# from langserve import add_routes 

# from dotenv import load_dotenv
# load_dotenv() 

# groq_api_key = os.getenv("GROQ_API_KEY") 

# model = ChatGroq(model="Gemma2-9b-It" ,groq_api_key=groq_api_key ) 

# parser=StrOutputParser()

# system_template = "Translate the following into {language} plz provide only translation " 

# prompt_template = ChatPromptTemplate.from_messages([ 
#     ("system",system_template)  ,
#     ("user","{text}") 
#     ])


# #Create the Chian 

# chain = prompt_template | model | parser 


# Create the Chain :

# app = FastAPI(title="Langchain Server" , 
#               version="1.0" ,
#               description="A Simple API server using Langchain runnable interfaces") 



# add_routes(app ,
#            chain , 
#            path="/chain")


# if __name__=="__main__" :
#     uvicorn.run(app, host="127.0.0.1", port=8000)