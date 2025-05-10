import streamlit as st
import re
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
genai.configure(api_key)

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def generate_mcq(topic: str, num_questions: int = 1) -> list:
    prompt = f"""
    You are a helpful assistant. Generate exactly {num_questions} multiple-choice questions based on the following content: "{topic}".

    Each question must include:
    - A clear question
    - Exactly four options labeled a), b), c), d)
    - The correct answer clearly mentioned at the end as: Answer: [a/b/c/d]

    Format:
    Question: ...
    a) ...
    b) ...
    c) ...
    d) ...
    Answer: ...
    """
    response = model.generate_content(prompt)
    return response.text
def parse_mcq_output(text):
    mcqs = []
    blocks = re.split(r"\bQuestion:\s*", text)[1:]  # split by 'Question:'
    
    for block in blocks:
        try:
            q_lines = block.strip().split('\n')
            question = q_lines[0].strip()
            
            options = {}
            for line in q_lines[1:]:
                if re.match(r"[a-d]\)", line.strip(), re.IGNORECASE):
                    key = line[0].lower()
                    options[key] = line[3:].strip()
                elif "Answer:" in line:
                    parts = line.split(":")
                    answer_key = parts[1].strip().lower() if len(parts) > 1 else "unknown"
            
            mcqs.append({
                "question": question,
                "options": options,
                "answer": answer_key,
                "correct_option": options.get(answer_key, "Unknown")
            })
        except Exception as e:
            print("Error parsing:", block, "\n", e)
    
    return mcqs
def app():
    st.title("MCQ Generator from Paragraph")
    st.write("Enter a paragraph, and I'll generate MCQs based on it.")

    # Input for paragraph
    paragraph = st.text_area("Input Paragraph", height=200)

    # Input for number of questions
    num_questions = st.number_input("Number of Questions", min_value=1, max_value=10, value=3, step=1)

    if st.button("Generate MCQs"):
        if paragraph:
            with st.spinner("Generating MCQs..."):
                mcq_raw = generate_mcq(paragraph, num_questions)
                mcq_data = parse_mcq_output(mcq_raw)

            # Display the MCQs
            if mcq_data:
                for i, question in enumerate(mcq_data, 1):
                    st.markdown(f"**Q{i}. {question['question']}**")
                    for key, option in question['options'].items():
                        st.write(f"- {key}) {option}")
                    st.markdown(f"**Answer:** {question['answer']}: {question['correct_option']}**")
            else:
                st.error("No MCQs generated. Please check the input.")
        else:
            st.error("Please enter a paragraph first!")

if __name__ == "__main__":
    app()