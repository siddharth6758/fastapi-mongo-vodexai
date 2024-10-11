FastAPI Mongo VodexAI
Getting Started
This repository contains a FastAPI application that integrates with MongoDB.

Prerequisites
Python 3.7 or higher
Virtualenv (for creating isolated environments)
Installation Steps
Clone the Repository

Open your terminal and run the following command:

bash
Copy code
git clone https://github.com/siddharth6758/fastapi-mongo-vodexai.git
Create a Virtual Environment

Navigate to the cloned directory and create a virtual environment:

bash
Copy code
cd fastapi-mongo-vodexai
virtualenv venv
Activate the virtual environment:

On macOS/Linux:

bash
Copy code
source venv/bin/activate
On Windows:

bash
Copy code
venv\Scripts\activate
Install Dependencies

Install the required packages using the requirements.txt file:

bash
Copy code
pip install -r requirements.txt
Run the Application

Start the FastAPI application with the following command:

bash
Copy code
uvicorn main:app --reload
Your application should now be running at http://127.0.0.1:8000.

Usage
You can access the API documentation at http://127.0.0.1:8000/docs.

Contributing
Feel free to open issues or submit pull requests!
