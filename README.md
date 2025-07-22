<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Sender with Gemini AI - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #333;
        }
        pre {
            background: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            font-family: 'Courier New', Courier, monospace;
        }
    </style>
</head>
<body>
    <h1>Email Sender with Gemini AI</h1>
    <p>Sends professional emails using Gemini AI to generate content and Gmail's SMTP server.</p>

    <h2>Features</h2>
    <ul>
        <li>Generates email subject, body, and recipient using Gemini AI.</li>
        <li>Sends emails via Gmail SMTP_SSL.</li>
        <li>Uses <code>.env</code> for secure credentials.</li>
        <li>Validates email fields.</li>
    </ul>

    <h2>Prerequisites</h2>
    <ul>
        <li>Python 3.8+</li>
        <li>Packages: <code>python-dotenv</code>, <code>langchain-google-genai</code></li>
        <li>Gmail App Password</li>
        <li>Google API key</li>
    </ul>

    <h2>Installation</h2>
    <ol>
        <li>Clone repo.</li>
        <li>Install dependencies:
            <pre><code>pip install python-dotenv langchain-google-genai</code></pre>
        </li>
        <li>Create <code>.env</code>:
            <pre><code>api_key=your_google_api_key
app_pass=your_gmail_app_password
from_email=your_gmail_address</code></pre>
        </li>
    </ol>

    <h2>Usage</h2>
    <ol>
        <li>Run:
            <pre><code>python email_sender.py</code></pre>
        </li>
        <li>Input prompt (e.g., "Write a professional email to john.doe@example.com about a project update").</li>
        <li>Script generates and sends email if valid.</li>
    </ol>

    <h2>Example</h2>
    <p><strong>Input</strong>:</p>
    <pre><code>Write a professional email to john.doe@example.com about a project update</code></pre>
    <p><strong>Output</strong>:</p>
    <pre><code>To: john.doe@example.com
Subject: Project Update
Body:
Dear John,
Project milestones are on track. Initial phase complete, development stage next. Expect deliverables by Friday. Contact me with questions.
Best,
[Your Name]
Email sent successfully!</code></pre>

    <h2>Notes</h2>
    <ul>
        <li>Requires Gmail 2FA and App Password.</li>
        <li>Stable internet needed for API/SMTP.</li>
        <li>Body ~70 words for brevity.</li>
    </ul>
</body>
</html>
