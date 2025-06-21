import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

function App() {
  const [todos, setTodos] = useState([]);
  const [newTask, setNewTask] = useState('');
  const [chatMessages, setChatMessages] = useState([]);
  const [chatInput, setChatInput] = useState('');

  useEffect(() => {
    fetchTodos();
  }, []);

  const fetchTodos = async () => {
    try {
      const response = await axios.get(`${API_URL}/todos`);
      setTodos(response.data);
    } catch (error) {
      console.error('Error fetching todos:', error);
    }
  };

  const addTodo = async (e) => {
    e.preventDefault();
    if (!newTask.trim()) return;
    try {
      const response = await axios.post(`${API_URL}/todos`, { task: newTask });
      setTodos([...todos, response.data]);
      setNewTask('');
    } catch (error) {
      console.error('Error adding todo:', error);
    }
  };

  const deleteTodo = async (id) => {
    try {
      await axios.delete(`${API_URL}/todos/${id}`);
      setTodos(todos.filter(todo => todo.id !== id));
    } catch (error) {
      console.error('Error deleting todo:', error);
    }
  };

  const sendChatMessage = async (e) => {
    e.preventDefault();
    if (!chatInput.trim()) return;

    setChatMessages([...chatMessages, { sender: 'user', text: chatInput }]);

    try {
      const response = await axios.post(`${API_URL}/chat`, { message: chatInput });
      const botResponse = response.data.response;
      setChatMessages([
        ...chatMessages,
        { sender: 'user', text: chatInput },
        { sender: 'bot', text: botResponse },
      ]);
    } catch (error) {
      console.error('Error getting chatbot response:', error);
      setChatMessages([
        ...chatMessages,
        { sender: 'user', text: chatInput },
        { sender: 'bot', text: 'Sorry, I couldn’t find an answer.' },
      ]);
    }

    setChatInput('');
  };

  return (
    <div className="app">
      <h1>Todo & Chatbot App</h1>

      <div className="todo-section">
        <h2>Todo List</h2>
        <form onSubmit={addTodo} className="todo-form">
          <input
            type="text"
            value={newTask}
            onChange={(e) => setNewTask(e.target.value)}
            placeholder="Add a new task"
            className="todo-input"
          />
          <button type="submit" className="todo-button">Add Task</button>
        </form>
        <ul className="todo-list">
          {todos.map(todo => (
            <li key={todo.id} className="todo-item">
              <span>{todo.task}</span>
              <button onClick={() => deleteTodo(todo.id)} className="delete-button">Delete</button>
            </li>
          ))}
        </ul>
      </div>

      <div className="chat-section">
        <h2>Chatbot</h2>
        <div className="chat-messages">
          {chatMessages.map((msg, index) => (
            <div key={index} className={`chat-message ${msg.sender}`}>
              <span>{msg.sender === 'user' ? 'You: ' : 'Bot: '}</span>
              {msg.text}
            </div>
          ))}
        </div>
        <form onSubmit={sendChatMessage} className="chat-form">
          <input
            type="text"
            value={chatInput}
            onChange={(e) => setChatInput(e.target.value)}
            placeholder="Ask a question..."
            className="chat-input"
          />
          <button type="submit" className="chat-button">Send</button>
        </form>
      </div>
    </div>
  );
}

export default App;
