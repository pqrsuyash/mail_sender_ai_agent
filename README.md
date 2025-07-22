Email Sender with Gemini AI

Sends professional emails using Gemini AI to generate content and Gmail's SMTP server.

Features





Generates email subject, body, and recipient using Gemini AI.



Sends emails via Gmail SMTP_SSL.



Uses .env for secure credentials.



Validates email fields.

Prerequisites





Python 3.8+



Packages: python-dotenv, langchain-google-genai



Gmail App Password



Google API key

Installation





Clone repo.



Install dependencies:

pip install python-dotenv langchain-google-genai



Create .env:

api_key=your_google_api_key
app_pass=your_gmail_app_password
from_email=your_gmail_address

Usage





Run:

python email_sender.py



Input prompt (e.g., "Write a professional email to john.doe@example.com about a project update").



Script generates and sends email if valid.

Example

Input:

Write a professional email to john.doe@example.com about a project update

Output:

To: john.doe@example.com
Subject: Project Update
Body:
Dear John,
Project milestones are on track. Initial phase complete, development stage next. Expect deliverables by Friday. Contact me with questions.
Best,
[Your Name]
Email sent successfully!

Notes





Requires Gmail 2FA and App Password.



Stable internet needed for API/SMTP.



Body ~70 words for brevity.
