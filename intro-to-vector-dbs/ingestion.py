import os 
from dotenv import load_dotenv
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_pinecone import PineconeVectorStore
from langchain_openai.embeddings import OpenAIEmbeddings

load_dotenv("/Users/ramsuryayenda/Documents/Project Space/ltphd/Libraries/Langchain_tutorial/Udemy_lanchain/intro-to-vector-dbs/.env")
if __name__ == "__main__":
    print("ingestion")
    loader = TextLoader("/Users/ramsuryayenda/Documents/Project Space/ltphd/Libraries/Langchain_tutorial/Udemy_lanchain/intro-to-vector-dbs/mediumblog1.txt")
    document = loader.load()
    
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(document)
    print("loaded text splitter")
    
    embeddings = OpenAIEmbeddings()
    
    PineconeVectorStore.from_documents(documents=texts,embedding=embeddings, index_name = os.environ.get('INDEX_NAME'))
    
    print("Finish")
    