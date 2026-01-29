# Langchain-Chatbot-with-document-loading
By implement RAG and Langchain, here I create a Chatbot with document loading to proceed some basic mession, such as summery generation or others.

## Features in this project

- PDF / CSV / json / Markdown / TxT document ingestion
- Parent–Child chunking strategy
- Watsonx Embeddings + LLM leveraging
- Chroma Vector Store
- Gradio Web UI

 Note: This project requires access to IBM watsonx.ai.
 If you do not have credentials, 
 please refer to the code structure and architecture sections for implementation details.


### Structures


#### How to operate

- First, you might need to create a virtual environment to operate it.

pip install virtualenv \
virtualenv my_env # create a virtual environment named my_env \
source my_env/bin/activate # activate my_env

- Second, you'll need to install necessary packages.

python3.11 -m pip install \
gradio==4.44.0 \
ibm-watsonx-ai==1.1.2  \
langchain==0.2.11 \
langchain-community==0.2.10 \
langchain-ibm==0.1.11 \
chromadb==0.4.24 \
pypdf==4.3.1 \
pydantic==2.9.1 \
huggingface_hub==0.23.0 \
gradio \
huggingface_hub
