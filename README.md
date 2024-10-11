# FastAPI Mongo VodexAI

This project is a FastAPI application that connects to a MongoDB database.

## Getting Started

Follow the steps below to set up and run the project locally.

### 1. Clone the Repository

Open your terminal and run the following command to clone the repository:

```bash
git clone https://github.com/siddharth6758/fastapi-mongo-vodexai.git
```

### 2. Create a Virtual Environment

Navigate to the project directory:

```bash
cd fastapi-mongo-vodexai
```

Then, create a virtual environment. You can use `venv` or any other virtual environment tool. Here's how to do it with `venv`:

```bash
virtualenv venv
```

Activate the virtual environment:

- On macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

- On Windows:

  ```bash
  .\venv\Scripts\activate
  ```

### 3. Install Requirements

Install the required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

In your terminal, run the following command to start the FastAPI application:

```bash
web: uvicorn main:app --reload
```

You should now be able to access the application at `http://127.0.0.1:8000`.

## Additional Information

- For API documentation, visit `http://127.0.0.1:8000/docs` after running the application.
- Ensure that you have MongoDB installed and running for the application to connect successfully.
