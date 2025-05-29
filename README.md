# Chatbot_Using_Langchain
Streamlit Meets LangChain: Building an Interactive AI Chatbot
## Overview
This project leverages LangChain, Google Gemini, and Streamlit to build a dynamic AI chatbot capable of engaging in real-time conversations. Using LangChain's prompt templating, Google Gemini's conversational AI model, and Streamlit's intuitive UI, this chatbot provides seamless interaction for users.
## Features
Conversational AI powered by Google Gemini

LangChain integration for structured and customizable prompts

Streamlit-based UI for an interactive user experience

Environmental variable management using dotenv

Error handling & retry logic via tenacity

Optimized API authentication for secure access

Real-time response generation for user queries

## Tech Stack
Python (Primary Language)

Streamlit (Frontend UI)

LangChain (Prompt engineering & processing)

Google Gemini (LLM model for chat responses)

dotenv (Environment variable management)

tenacity (Error handling & retries)

## Installation
Clone the repository:

bash
git clone https://github.com/your-username/your-repo.git  
cd your-repo  
Create a virtual environment:

bash
python -m venv venv  
source venv/bin/activate  # On Mac/Linux  
venv\Scripts\activate  # On Windows  
Install dependencies:

bash
pip install -r requirements.txt 

Set environment variables: Create a .env file and add the API keys:

plaintext
GOOGLE_API_KEY=your-google-api-key  
LANGCHAIN_API_KEY=your-langchain-api-key  
Run the chatbot:

bash
streamlit run app.py  

## Usage
Open the Streamlit app in your browser

Enter a question in the text input field

Get instant responses from the AI chatbot powered by Google Gemini

## Future Enhancements
Integrating memory capabilities for contextual conversations

Expanding multi-modal AI support (text, images, etc.)

Adding customizable prompt settings for fine-tuned responses

Deploying the chatbot on cloud platforms for wider accessibility
