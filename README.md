# Ngamba Island Chimpanzee Sanctuary Chatbot

An AI-powered chatbot designed for **Ngamba Island Chimpanzee Sanctuary**, built with **Django REST Framework (Backend)** and **React + TypeScript (Frontend)**. The chatbot leverages **Google Generative AI (Gemini 2.5)** to provide information about chimpanzees, tours, donations, and the island.

---

## Tech Stack

- **Backend:** Django 5.2.3, Django REST Framework, django-cors-headers, python-dotenv
- **Frontend:** React 19, TypeScript, Vite
- **AI Model:** Google Generative AI (`gemini-2.5-flash` via `google-generativeai` Python SDK)

---

## Project Structure

NICS_chatbot/
│
├── chatbackend/ # Django Backend
│ ├── chatbot/ # Django App
│ │ ├── views.py
│ │ ├── serializers.py
│ │ ├── urls.py
│ │ └── init.py
│ ├── chatbackend/ # Django Project
│ │ ├── settings.py
│ │ ├── urls.py
│ │ └── wsgi.py
│ ├── db.sqlite3
│ ├── .env # Environment variables
│ └── manage.py
│
├── chatbot-frontend/ # React Frontend
│ ├── src/
│ │ ├── App.tsx
│ │ └── index.tsx
│ ├── package.json
│ └── vite.config.ts
│
└── README.md

yaml
Copy
Edit


---

## Setup Instructions

### 1. Backend (Django)

#### Install dependencies:

```bash
cd chatbackend
pipenv install
pipenv shell
pipenv install django-cors-headers python-dotenv google-generativeai djangorestframework

GEN_AI_API=your_google_generative_ai_api_key_here

pipenv run python manage.py migrate
pipenv run python manage.py runserver

cd chatbot-frontend
npm install

npm run dev

```

![image](images\chatbot.PNG)

http://localhost:5173/

### Features
1. Interactive chatbot for Ngamba Island visitors and donors.

2. Uses Google Generative AI (Gemini 2.5) for natural language understanding.

3. Fully integrated React + Django REST API architecture.

## Author
Ayebazibwe Ishmael