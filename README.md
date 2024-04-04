### Group 6

# FastAPI Application

This is a FastAPI application that is meant as a prototype to support a project where we suggest AI tooling for Zoom. This tool will suggest agenda items and icebreaker questions for someone planning a meeting.

## Installation

### 1. Clone the repository:

```bash
git clone url//from-repo
cd INTP-AI-Proj2

```

### 2. Install all dependencies using either of the following this installs all the python requirements as well as the Bootstrap for the UI:

pip install -r requirements.txt && cd app/templates && npm i 

or

pip3 install -r requirements.txt && cd app/templates && npm i

### 3. Run the application - using mac

uvicorn app.main:app --reload

### 3. Run the application - using windows

python.exe -m uvicorn.main app.main:app --reload

### 4. Add the API Key

Add your API key to the .env file. Use format like: OPENAI_API_KEY="abcd-1234". If you do not have a .env file, create one in the root directory. 

### 5. Use application in browser

visit http://localhost:8000
