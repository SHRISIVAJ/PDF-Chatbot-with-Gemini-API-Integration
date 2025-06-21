import requests
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

try:
    import PyPDF2
except ImportError:
    print("Error: PyPDF2 library is not installed. Please install it using 'pip install PyPDF2'.")
    exit(1)

app = FastAPI()

# Enable CORS to allow the React frontend to communicate with the backend
origins = [
    "http://localhost:5173",  # React default port with Vite
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Todo List Functionality ---

# Model for a Todo item
class Todo(BaseModel):
    id: int
    task: str
    completed: bool = False

# In-memory storage for todos
todos: List[Todo] = []
todo_id_counter = 1

@app.get("/todos", response_model=List[Todo])
async def get_todos():
    return todos

@app.post("/todos", response_model=Todo)
async def add_todo(task: str):
    global todo_id_counter
    new_todo = Todo(id=todo_id_counter, task=task)
    todos.append(new_todo)
    todo_id_counter += 1
    return new_todo

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    return {"message": "Todo deleted successfully"}

# --- Gemini Chatbot Functionality ---

# Google Gemini API configuration
API_KEY = "AIzaSyAE6A113LwksKNmh4WsgFVNVa29UzQZY4g"
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

# Load PDF content at startup
try:
    with open("roma_ai_training.pdf", "rb") as file:
        reader = PyPDF2.PdfReader(file)
        pdf_content = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                pdf_content += text + "\n"
except FileNotFoundError:
    print("Error: 'roma_ai_training.pdf' not found in the backend directory.")
    exit(1)
except Exception as e:
    print(f"Error reading PDF: {e}")
    exit(1)

# Model for chatbot request
class ChatRequest(BaseModel):
    message: str

def get_gemini_response(user_input: str) -> str:
    """Send user input to Gemini API with PDF context and return the response."""
    headers = {
        "Content-Type": "application/json"
    }
    
    url = f"{API_URL}?key={API_KEY}"
    
    # Prompt to match intents and rephrase answers naturally
    prompt = (
        "You are a helpful assistant that answers questions based on the provided PDF content. "
        "The PDF contains multiple intents, each with training phrases (TP) and answers (AS). "
        "Your task is to match the user's question to the most relevant intent by comparing it to the training phrases. "
        "If a match is found, rephrase the corresponding answer (AS) in a natural, conversational tone while keeping the core information intact. "
        "Do not add extra details or deviate from the original meaning. "
        "If no match is found, return an empty response (no text). "
        "Be strict about matching intents and do not respond to unrelated questions.\n\n"
        f"PDF Content:\n{pdf_content}\n\n"
        f"User Question: {user_input}"
    )
    
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.2  # Low temperature for consistent, focused responses
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        response_data = response.json()
        
        # Extract response text if available
        if "candidates" in response_data and response_data["candidates"]:
            candidate = response_data["candidates"][0]
            if "content" in candidate and "parts" in candidate["content"]:
                return candidate["content"]["parts"][0]["text"].strip()
        return ""  # Return empty string if no valid response
    
    except requests.exceptions.RequestException as e:
        print(f"Error: API request failed - {e}")
        return ""
    except (json.JSONDecodeError, KeyError):
        print("Error: Invalid API response format.")
        return ""

@app.post("/chat")
async def chat(request: ChatRequest):
    response = get_gemini_response(request.message)
    if not response:
        raise HTTPException(status_code=404, detail="No relevant answer found")
    return {"response": response}