# -*- coding: utf-8 -*-
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_pdf(path):
    loader = PyPDFLoader(path)
    return loader.load_and_split()

if __name__ == "__main__":
    docs = load_pdf("test.pdf")
    print("总页数/块数：", len(docs))