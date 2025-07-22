import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

load_dotenv()
api_key = os.getenv("api_key")
app_pass = os.getenv("app_pass")
from_email = os.getenv("from_email")


def send_email(subject, body, to_email, from_email, app_password):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(from_email, app_password)
        smtp.send_message(msg)
        print("Email sent successfully!")


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",
                             google_api_key=api_key,
                             temperature=0.3)

# Prompt templates for individual fields
subject_template = PromptTemplate.from_template(
    "Generate only the subject of an email based on the following user instruction:\n\n{user_input}\n\nOnly return the subject line. the body content should be of about 70 words. make it look like professional."
)

body_template = PromptTemplate.from_template(
    "Generate only the body content of an email based on the following user instruction:\n\n{user_input}\n\nOnly return the email body. Don't include subject or recipient."
)

to_email_template = PromptTemplate.from_template(
    "Extract only the recipient's email address from the following instruction:\n\n{user_input}\n\nOnly return the email address."
)

# Get input from user
user_input = input("You: ")

# Ask Gemini for each part separately
subject_prompt = subject_template.format(user_input=user_input)
body_prompt = body_template.format(user_input=user_input)
to_email_prompt = to_email_template.format(user_input=user_input)

subject_response = llm.invoke(subject_prompt)
body_response = llm.invoke(body_prompt)
to_email_response = llm.invoke(to_email_prompt)

# Strip values
subject = subject_response.content.strip()
body = body_response.content.strip()
to_email = to_email_response.content.strip()

print("\n🔍 Generated Email Details:")
print("To: ", to_email)
print("Subject: ", subject)
print("Body:\n", body)

# Validate before sending
if to_email and subject and body:
    send_email(subject=subject,
               body=body,
               to_email=to_email,
               from_email=from_email,
               app_password=app_pass)
else:
    print("One or more email fields are missing or invalid.")
