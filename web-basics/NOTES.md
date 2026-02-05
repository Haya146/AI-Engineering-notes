# 🌐 Web Basics for AI Projects

This tutorial explains the fundamental web concepts required to understand 
how a full-stack AI application works.

---

## 🧠 What is Client / Server?

### Client
The client is the part of the application that the user interacts with directly.

Examples:
- Streamlit App
- Web Browser

Responsibilities:
- Collect user input
- Send requests to the backend
- Display responses

---

### Server
The server is responsible for processing requests and returning responses.

Examples:
- FastAPI Backend

Responsibilities:
- Handle business logic
- Interact with databases
- Run AI models
- Return responses

---

## 🔁 Client–Server Communication



Client (Streamlit) ---> Server (FastAPI)     
Client (Streamlit) <--- Server (FastAPI)     


---

## 🌍 What is HTTP?

HTTP is the communication protocol that allows the client and server to exchange data.

---

## 📤 HTTP Methods

### GET
Used to retrieve data without modifying it.

Example:


GET /diagnosis/by_patient


---

### POST
Used to send data to the server.

Examples:


POST /upload_report
POST /ask_diagnosis


---

## 📨 Request vs Response

### Request
Contains:
- HTTP method
- URL
- Headers
- Body (JSON data)

---

### Response
Contains:
- Status code
- Data
- Message

---

## 📊 HTTP Status Codes

| Code | Meaning |
|-----|--------|
| 200 | Success |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 500 | Server Error |

---

## 🧾 What is JSON?

JSON is a lightweight data-interchange format used between frontend and backend.

Example:
```json
{
  "username": "haya",
  "role": "patient"
}
```

🏥 Real Example from the Medical Diagnosis App

 - Patient enters a question

 - Streamlit sends a POST request

 - FastAPI processes the request using RAG

 - Diagnosis is returned

 - Result is displayed to the user

✅ Why This Matters

-> Understanding these concepts is essential for:

 - Backend development

 - API communication

 - AI-powered applications

 - Debugging production issues
