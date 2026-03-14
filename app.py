import streamlit as st
from distractor_engine import generate_distractors

st.title("🧠 AI MCQ Distractor Generator")

st.write("Enter a question and the correct answer to generate logical distractors.")

question = st.text_area("Question")

correct_answer = st.text_input("Correct Answer")

if st.button("Generate Distractors"):

    if question and correct_answer:

        distractors = generate_distractors(question, correct_answer)

        st.subheader("Generated Options")

        st.write(f"A) {correct_answer}")
        st.write(f"B) {distractors[0]}")
        st.write(f"C) {distractors[1]}")
        st.write(f"D) {distractors[2]}")

    else:
        st.warning("Please enter both question and answer.")
