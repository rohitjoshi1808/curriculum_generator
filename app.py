
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key= os.getenv("OPENAI_API_KEY")

def create_curriculum(standard, subject):
# Define a short poem as a prompt
    curriculum = """
You are an academic headmaster. Prepare an efficient curriculum for the subject {subject}, for Standard {standard} students.

Curriculum Guidelines:
- Term Duration: 6 months
- Ensure the curriculum is focused, realistic, and outcome-driven.
- Include monthly topic plans.
- Highlight key learning objectives.
- Suggest relevant activities or assessments.
- Ensure time management and pacing is age-appropriate.

Structure the output in clear bullet points or sections, and keep it practical for classroom execution.

"""
    
    prompt = curriculum.replace("{standard}", standard)
    prompt = prompt.replace("{subject}", subject)
    print(prompt)

    # Call OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.0,
        max_tokens=1000
    )
    
    # Extract and print the result
    continuation = response['choices'][0]['message']['content']
    return continuation
    
# curriculum = create_curriculum(standard="6th standard", subject="English")
# print(curriculum)