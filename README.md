# This project builds an intelligent document Q&A chatbot for PDFs, combining Retrieval-Augmented Generation (RAG) with the DeepSeek R1 language model. It enables users to upload legal or technical documents, ask questions, and get reasoning-based answers sourced directly from the provided files.

# Frontend Setup

1. Developed a Streamlit-based UI for seamless chat and PDF upload functionality.

2.Users can upload a PDF and interact with the chatbot through an intuitive interface.

# Document Parsing & Chunking

Used PDFPlumber and LangChain document loaders to extract and preprocess text from user PDFs.Split text into smaller manageable chunks for efficient storage and retrieval.

# Vector Store & Embeddings

Generated semantic embeddings for text chunks using DeepSeek R1 via Ollama server.Stored the embeddings in a FAISS vector database for fast similarity-based retrieval

# Retrieval-Augmented Reasoning

Implemented a RAG pipeline with LangChain to search relevant document chunks based on user queries.Augmented LLM prompts with retrieved context, enabling highly accurate, document-grounded answers.

# Real-Time Q&A

Provided instant, explainable answers leveraging DeepSeek R1’s reasoning capabilities, directly referencing user-uploaded documents.

# Tech Stack: Python, Streamlit, DeepSeek R1, Ollama, LangChain, FAISS, PDFPlumber.

# Prerequisites

1. Install Ollama
  
2. Pull and Run DeepSeek R1 Model : (ollama run deepseek-r1:1.5b)

3. Set Up Python Environment

4. Run the Project

