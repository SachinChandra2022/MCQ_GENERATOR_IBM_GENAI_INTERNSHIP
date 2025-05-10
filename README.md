# 🧠 MCQ Generator using Generative AI

This project is part of the IBM GenAI Internship and showcases a **Generative AI-powered system** that generates **Multiple-Choice Questions (MCQs)** from a given topic or paragraph. It leverages powerful transformer models to assist in smart education and content generation.


## 🚀 Features

- 📝 Input a paragraph or topic and generate MCQs automatically.
- 🤖 Uses advanced Generative AI models for context-aware question formation.
- 🧠 Supports multiple output options for educational use cases.
- 🖥️ Easy-to-use **Streamlit-based UI**.
- 🔒 API keys securely hidden using `.env`.


## 🛠️ Tech Stack

- **Python**
- **Hugging Face Transformers**
- **OpenAI / Gemini (via API)**
- **Streamlit** for UI
- **dotenv** for environment variable management


## 📦 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/SachinChandra2022/MCQ_GENERATOR_IBM_GENAI_INTERNSHIP.git
   cd MCQ_GENERATOR_IBM_GENAI_INTERNSHIP
   ```
2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate     # For Windows
   ```
3. **Install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate     # For Windows
   ```
4.	**Add your API key**
   •	Create a .env file in the root directory:
5.	**Run the application**
   ```bash
   streamlit run app.py
   ```
## 🧪 Example Input & Output

Input:

“Photosynthesis is the process by which green plants convert sunlight into energy.”

Output:

Q: What is photosynthesis?
A) A process where animals eat food
B) The process of converting light to energy in plants ✅
C) A chemical used in agriculture
D) A type of cell in humans


## 🔒 Security Note

🔑 Your API key is stored securely in a .env file. Ensure that .env is listed in .gitignore to avoid accidental leaks.


## 🤝 Contributors
	•	Sachin Chandra


## 🌐 References
	•	Hugging Face Transformers
	•	OpenAI API Docs
	•	Streamlit Docs
