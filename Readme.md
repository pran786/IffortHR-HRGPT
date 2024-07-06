# 🤖 AI-Powered HR Assistant

![HR Assistant Logo](https://example.com/hr-assistant-logo.png)

## 📚 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Overview

The AI-Powered HR Assistant is a cutting-edge Django-based API that leverages the power of OpenAI's language models to provide instant, accurate responses to HR-related queries. By scraping and analyzing your company's website, this assistant ensures that all information provided is tailored to your organization's specific policies and practices.

## ✨ Features

- 🌐 Web scraping of company HR policies
- 🧠 AI-powered natural language understanding
- 🎯 Context-aware responses
- 🚀 Fast and scalable Django API
- 🔒 Secure handling of sensitive information

## 🛠 Technology Stack

- **Backend**: Django, Django REST Framework
- **AI/ML**: OpenAI API (GPT-3.5 Turbo, Text Embedding 3 small)
- **Web Scraping**: BeautifulSoup4
- **Data Processing**: NumPy, Scikit-learn
- **Environment Management**: python-dotenv

## 📦 Installation

1. Clone the repository:
2. Set up a virtual environment:
3. Install dependencies:
4. Set up environment variables:
Create a `.env` file in the project root and add:
5. Run migrations:
## 🚀 Usage

1. Start the Django development server:

2. The API will be available at `http://localhost:8000/ask/`

## 🔗 API Endpoints

### POST /api/ask/

Ask a question to the HR Assistant.

**Request Body**:
```json
{
 "query": "who is the founder of the company"
}

**Response**:

```json
{
 "Response": "The co-founders of Iffort are Sunny Jindal and Daksh Sharma."
}

