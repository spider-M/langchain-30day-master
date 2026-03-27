# -*- coding: utf-8 -*-
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def main():
    loader = TextLoader("test.txt", encoding="utf-8")
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    print("总块数：", len(chunks))
    for i, c in enumerate(chunks):
        print(f"\n块{i+1}：", c.page_content)

if __name__ == "__main__":
    main()