***📧 AI Email Generator***<br><br>
This project is a Python-based tool that automatically generates and sends professional emails using natural language instructions. It leverages Google's Gemini 2.5 model via LangChain to create the subject, body, and extract the recipient's email from user input. The generated email is then sent using Gmail's SMTP service.

To get started, make sure you have Python installed. First, install the required dependencies by running pip install -r requirements.txt. Next, create a .env file in the root directory and add your credentials: your Gemini API key, Gmail app password, and the sender’s Gmail address. It's important to enable 2-Factor Authentication on your Gmail account and generate an App Password, as this script uses secure login via SMTP.

Once the setup is complete, run the script using python main.py. When prompted, simply enter your request in natural language. For example: “Send a follow-up email to hr@example.com regarding internship confirmation.” The model will then generate a subject and email body based on your input and automatically send the email.

Internally, the script constructs specific prompts to separately request the subject, body, and recipient email from the Gemini model. It ensures a clear separation of roles and results in a professional, concise message. This is especially useful for automating HR, job application, or formal communication tasks with minimal effort.

The core technologies used in this project include Python, LangChain, Google Generative AI (Gemini 2.5), Gmail SMTP (smtplib), and python-dotenv for managing environment variables securely.

