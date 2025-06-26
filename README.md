# Vectorstore & Embeddings Project

This project demonstrates how to process a PDF document, split its content into manageable text chunks, generate embeddings using a HuggingFace model, and store these embeddings in a FAISS vectorstore for efficient similarity search. The implementation uses the LangChain library for document loading, text splitting, and embedding generation.

## Features
- **PDF Loading:** Loads a PDF file (`documento.pdf`) and extracts its content.
- **Text Splitting:** Splits the document into overlapping chunks for better embedding and retrieval performance.
- **Embeddings:** Uses the HuggingFace model `all-MiniLM-L6-v2` to generate vector representations of text chunks.
- **Vectorstore:** Stores the embeddings in a FAISS vectorstore for fast similarity search and retrieval.
- **Persistence:** Saves the vectorstore locally for later use.

## Requirements
- Python 3.8+
- [LangChain](https://python.langchain.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [HuggingFace Transformers](https://huggingface.co/transformers/)

Install dependencies with:
```bash
pip install langchain faiss-cpu sentence-transformers
```

## Usage
1. Place your PDF file in the project directory and name it `documento.pdf` (or change the filename in `main.py`).
2. Run the script:
   ```bash
   python main.py
   ```
3. The script will:
   - Load and split the PDF.
   - Generate embeddings for each chunk.
   - Store the embeddings in a FAISS vectorstore saved as `mi_vectorstore/`.

## File Structure
- `main.py`: Main script for processing the PDF and creating the vectorstore.
- `documento.pdf`: The PDF document to be processed.
- `mi_vectorstore/`: Directory containing the FAISS index and metadata.

## Customization
- **Chunk Size & Overlap:** Adjust `chunk_size` and `chunk_overlap` in `main.py` for different splitting strategies.
- **Model Selection:** Change the `model_name` in `HuggingFaceEmbeddings` to use a different embedding model.

## Applications
- Semantic search over PDF documents
- Information retrieval
- Document similarity and clustering

## License
This project is for educational purposes. Please check the licenses of the libraries and models used for production use.
