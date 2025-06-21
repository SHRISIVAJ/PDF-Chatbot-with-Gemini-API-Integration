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

## Setup Instructions

### Backend Setup:
1. **Clone the repository**:
    ```bash
    https://github.com/SHRISIVAJ/PDF-Chatbot-with-Gemini-API-Integration
    ```

2. **Navigate to the backend folder**:
    ```bash
    cd backend
    ```

3. **Install the required dependencies**:
    Make sure you have Python 3.8+ installed. Then, install the required packages by running:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the FastAPI server**:
    Start the FastAPI backend with:
    ```bash
    uvicorn main:app --reload
    ```

   The backend will be running at `http://127.0.0.1:8000`.

### Frontend Setup (React):

1. **Navigate to the frontend folder**:
    ```bash
    cd frontend
    ```

2. **Install the frontend dependencies**:
    Make sure you have **Node.js** installed. Then, install the required npm packages by running:
    ```bash
    npm install
    ```

3. **Run the React development server**:
    Start the frontend development server:
    ```bash
    npm run dev
    ```

   The frontend will be available at `http://localhost:5173`.

## How It Works:
1. **PDF Upload & Processing**:
   - The content of the PDF (`training.pdf`) is extracted and stored in the backend.
   
2. **User Query**:
   - The user sends a query through a POST request to the `/chat` endpoint.
   
3. **Gemini API Response**:
   - The chatbot uses the **Gemini API** to match the user's query with the content in the PDF and returns a relevant response.

## Technologies Used:
- **Python**: Backend development with FastAPI.
- **FastAPI**: For building the backend API.
- **Gemini API**: For generating responses from the PDF content.
- **PyPDF2**: For PDF parsing and text extraction.
- **CORS**: To enable communication between React frontend and FastAPI backend.

