import streamlit as st
import random

def calculate_percentage_match(job_description, resume_file):
    # This function would use NLP techniques to calculate the percentage match between the job description and the resume.
    # For the purpose of this example, we'll just return a random percentage match.
    return random.randint(0, 100)

def main():
    st.title("Smart ATS")
    st.subheader("Improve Your Resume ATS")

    job_description = st.text_area("Job Description:")
    resume_file = st.file_uploader("Upload Resume (PDF only):", type="pdf")

    if st.button("Percentage Match"):
        # Process the job description and resume file to calculate the percentage match
        percentage_match = calculate_percentage_match(job_description, resume_file)

        # Display the percentage match to the user
        st.write(f"Percentage Match: {percentage_match}%")

        if percentage_match >= 80:
            st.success("Your resume is a great match for this job description!")
        elif percentage_match >= 60:
            st.info("Your resume is a good match for this job description.")
        elif percentage_match >= 40:
            st.warning("Your resume is a fair match for this job description.")
        else:
            st.error("Your resume is not a good match for this job description.")

if __name__ == "__main__":
    main()
