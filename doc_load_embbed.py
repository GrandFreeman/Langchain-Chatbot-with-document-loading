from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import EmbedTextParamsMetaNames
from ibm_watsonx_ai import Credentials

from langchain_ibm import WatsonxEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

import os
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_community.document_loaders import JSONLoader
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders.csv_loader import UnstructuredCSVLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders import UnstructuredFileLoader



## Document loader
def document_loader(file):
    ext = os.path.splitext(file.name)[1].lower()
    if ext == ".pdf":
        loader = PyPDFLoader(file.name)
    elif ext == ".csv":
        loader = CSVLoader(file.name)
    elif ext ==".txt":
        loader = TextLoader(file.name)
    elif ext ==".json":
        loader = JSONLoader(file.name)
    elif ext == ".md":
        loader = UnstructuredMarkdownLoader(file.name)
    else:
        raise ValueError(f"Unsupported file type: {ext}")
    
    loaded_document = loader.load()
    return loaded_document


## Embedding model
def watsonx_embedding():
    embed_params = {
    EmbedTextParamsMetaNames.TRUNCATE_INPUT_TOKENS: 3,
    #EmbedTextParamsMetaNames.RETURN_OPTIONS: {"input_text": True},
    }#,
    
    project_id = "skills-network"
    watsonx_embedding = WatsonxEmbeddings(
        model_id="ibm/slate-125m-english-rtrvr-v2",  ##
        url="https://us-south.ml.cloud.ibm.com",
        project_id=project_id,
        params=embed_params,
    )
    return watsonx_embedding
