# PDF Chatbot with Gemini API Integration

## Overview
This project demonstrates the integration of a PDF chatbot using the **Google Gemini API** to provide conversational responses based on the contents of a PDF file. The chatbot allows users to ask questions related to the content of a specific PDF, and it retrieves relevant answers using AI-powered natural language processing.

## Features
- **PDF Parsing**: The backend extracts and processes text from a provided PDF file (`training.pdf`).
- **Gemini API Integration**: The project uses the **Google Gemini API** for question-answering based on the PDF content.
- **FastAPI Backend**: The application is built using **FastAPI** to provide a RESTful API for interacting with the chatbot.
- **Cross-Origin Resource Sharing (CORS)**: The app supports CORS, allowing the frontend (React) to communicate with the backend seamlessly.

## Key Components:
1. **Todo List Functionality**:
   - Basic in-memory functionality for adding, retrieving, and deleting todo items.
2. **Gemini Chatbot**:
   - The chatbot fetches and processes text from a PDF and allows users to query it using conversational AI via the **Gemini API**.

## How It Works:
1. **PDF Upload & Processing**:
   - The content of the PDF (`training.pdf`) is extracted and stored in the backend.
2. **User Query**:
   - The user sends a query through a POST request to the `/chat` endpoint.
3. **Gemini API Response**:
   - The chatbot uses the **Gemini API** to match the user's query with the content in the PDF and returns a relevant response.

## Setup Instructions:
1. **Clone this repository**:
    ```bash
    git clone https://github.com/your-username/pdf-chatbot.git
    ```
2. **Install dependencies**:
    - Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
3. **Run the FastAPI server**:
    - Start the FastAPI backend:
    ```bash
    uvicorn main:app --reload
    ```
4. **Frontend**:
    - The frontend should be configured separately with React (or any other framework).
    - Ensure the frontend communicates with the backend API by making requests to the `/chat` endpoint.

## Technologies Used:
- **Python**: Backend development with FastAPI.
- **FastAPI**: For building the backend API.
- **Gemini API**: For generating responses from the PDF content.
- **PyPDF2**: For PDF parsing and text extraction.
- **CORS**: To enable communication between React frontend and FastAPI backend.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Future Improvements:
- **RAG Integration**: Integrating a **Vector Database** (e.g., FAISS, Pinecone) for enhanced content retrieval.
- **Additional Features**: Support for more complex PDF content processing and more advanced query capabilities.

