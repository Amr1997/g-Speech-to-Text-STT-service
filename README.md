# Django Project Setup

This guide will help you set up and run the Django project for audio file handling, STT integration, and quota management.

## Prerequisites

Make sure you have the following installed on your machine:

- Python 3.8+ 
- Django (Version mentioned in `requirements.txt`)
- Virtualenv (for virtual environment management)

## Setup Instructions

### 1. Activate Virtual Environment
First, create and activate a virtual environment for the project:

For Windows:

venv\Scripts\activate
For macOS/Linux:


Copy code
source venv/bin/activate
2. Install Required Packages
Once the virtual environment is activated, install the necessary dependencies using the requirements.txt file:


Copy code
pip install -r requirements.txt
3. Apply Migrations
Before running the server, make sure to apply database migrations to set up your database schema:


Copy code
python manage.py makemigrations
python manage.py migrate
4. Run the Server
Now, you can run the Django development server:


Copy code
python manage.py runserver
The server should now be running at http://127.0.0.1:8000/.

Project Features
1. Authentication
The application uses JSON Web Tokens (JWT) for user authentication.
Tokens should be passed with requests to access protected resources.
2. Audio Handling
The application provides endpoints for uploading and recording audio files.
Users can upload audio files for processing through the API.
3. Speech-to-Text (STT) Service Integration
The system integrates with an external STT service to transcribe audio files into text.
An API endpoint is provided to interact with the STT service from the backend (front-end will not directly access the STT service).
4. Quota Management
A quota system tracks and limits each user's audio processing time.
The system ensures that users cannot exceed their allocated quota.
5. Admin Panel
The Django admin panel is extended to allow administrators to manage user quotas.
Admin users can view and adjust the quotas for individual users.
Additional Notes
Make sure to configure the your  credentials in the .env file.
