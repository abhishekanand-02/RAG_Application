# RAG Application with Google Gemini

A Retrieval-Augmented Generation (RAG) application built with Streamlit and powered by Google's Gemini AI model. This application allows users to ask questions about documents and get intelligent answers based on the document content.

## 🤖 What is RAG?

**Retrieval-Augmented Generation (RAG)** is an AI technique that combines the power of information retrieval with text generation. Here's how it works:

1. **Document Processing**: The system takes your documents (PDFs, text files, etc.) and breaks them into smaller chunks
2. **Vector Embeddings**: Each chunk is converted into a numerical representation (vector) that captures its semantic meaning
3. **Vector Database**: These vectors are stored in a searchable database (Chroma in this case)
4. **Query Processing**: When you ask a question, the system:
   - Converts your question into a vector
   - Finds the most relevant document chunks using similarity search
   - Passes both your question and the relevant context to the AI model
5. **Intelligent Response**: The AI generates an answer based on both your question and the retrieved document content

## 🚀 What This Project Implements

This RAG application provides:

- **PDF Document Processing**: Automatically loads and processes PDF documents
- **Intelligent Question Answering**: Ask questions about your documents and get contextual answers
- **Google Gemini Integration**: Uses Google's latest Gemini 2.0 Flash model for responses
- **Vector Search**: Employs Chroma vector database for efficient document retrieval
- **Streamlit Web Interface**: Clean, user-friendly web interface for interaction
- **Error Handling**: Robust error handling for API issues and edge cases

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini 2.0 Flash
- **Embeddings**: Google Generative AI Embeddings
- **Vector Database**: Chroma
- **Document Processing**: LangChain
- **Language**: Python 3.13

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.8 or higher
- Google AI API key (get it from [Google AI Studio](https://makersuite.google.com/app/apikey))
- Git (for cloning the repository)

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd RAG_Application
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv rag_venv

# Activate virtual environment
# On Windows:
rag_venv\Scripts\activate
# On macOS/Linux:
source rag_venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the project root and add your Google AI API key:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

### 5. Prepare Your Document

Place your PDF document in the project root directory. The application is currently configured to process `GOT-OCR-2.0-paper.pdf`. To use a different document:

1. Replace the PDF file, or
2. Update the filename in `app.py` line 35:
   ```python
   loader = PyPDFLoader("your-document.pdf")
   ```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## 📖 How to Use

1. **Start the Application**: Run `streamlit run app.py`
2. **Wait for Initialization**: The app will load and process your PDF document (this may take a moment)
3. **Ask Questions**: Type your questions in the chat input at the bottom
4. **Get Answers**: The AI will search through your document and provide relevant answers

### Example Questions

- "What is the main topic of this document?"
- "Summarize the key findings"
- "What methodology was used?"
- "What are the conclusions?"

## 🔧 Configuration Options

You can customize the application by modifying these parameters in `app.py`:

- **Chunk Size**: Change `chunk_size=1000` (line 38) to adjust document chunk size
- **Retrieval Count**: Modify `search_kwargs={"k": 10}` (line 46) to change how many chunks to retrieve
- **Model Temperature**: Adjust `temperature=0` (line 50) for more/less creative responses
- **Model**: Switch to different Gemini models by changing `model="gemini-2.0-flash"`

## 🐛 Troubleshooting

### Common Issues

1. **"No current event loop" Error**: This is fixed in the current version with proper asyncio handling
2. **API Key Issues**: Make sure your `GOOGLE_API_KEY` is correctly set in the `.env` file
3. **PDF Not Found**: Ensure your PDF file is in the correct location and filename matches
4. **Memory Issues**: For large documents, consider reducing chunk size or using a more powerful machine


## 📁 Project Structure

```
RAG_Application/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .env                  # Environment variables (create this)
├── GOT-OCR-2.0-paper.pdf # Sample PDF document
└── rag_venv/             # Virtual environment (created during setup)
```

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding support for more document formats
- Improving the UI/UX
- Adding more AI models
- Enhancing error handling
- Adding document upload functionality

---

**Happy Question Answering! 🎉**
