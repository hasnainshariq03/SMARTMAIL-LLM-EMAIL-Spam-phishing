# SmartMail — LLM Email Spam & Phishing Detector

**Developer:** Hasnain Shariq  
**Architecture:** OpenAI API only (no locally trained ML model)  
**Application:** Flask + HTML + CSS + JavaScript

SmartMail is a web application that sends user-provided email text to an OpenAI model for contextual classification as `SPAM`, `PHISHING`, or `LEGITIMATE`. It returns a structured explanation, risk level, indicators and a recommended next step.

> This is an educational decision-support demo, not a production email security gateway. The model does not verify sender identity, visit URLs, scan attachments, or guarantee safety.

## Problem being solved

People receive unsolicited messages and deceptive emails that may try to obtain credentials, payment information or personal data. SmartMail demonstrates how an LLM API can analyze the language and context of an email and explain potential warning signs.

## Features

- Responsive HTML/CSS interface.
- Flask web application and JSON API endpoint.
- OpenAI Responses API integration.
- Structured JSON output constrained by a JSON Schema.
- Three classifications: spam, phishing and legitimate.
- Risk level, explanation, indicators and recommended action.
- Input validation, request-size limits and environment-based API key.
- Basic automated tests.

## Technology stack

| Layer | Technology | Purpose |
|---|---|---|
| Frontend | HTML5, CSS3, JavaScript | User interface |
| Backend | Python, Flask | Routes and validation |
| AI | OpenAI API | Contextual email analysis |
| API SDK | OpenAI Python SDK | API communication |
| Output validation | Structured Outputs / JSON Schema | Consistent response structure |
| Configuration | python-dotenv | Local environment variables |
| Server | Gunicorn | Production WSGI server |
| Tests | pytest | Input validation tests |
| Deployment | Render | Hosting |
| Source control | Git, GitHub | Version control |

## Architecture

1. User pastes an email subject and body.
2. Flask validates the text and enforces a maximum character count.
3. Backend sends the text as untrusted content to the OpenAI API.
4. System instructions tell the model not to follow instructions embedded in the email.
5. The model returns structured JSON with classification and explanation.
6. Flask renders the result in the browser or returns JSON from `/api/analyze`.

No local model training or TF-IDF pipeline is used in this architecture. The model is accessed through an API, so internet access and a valid API key are required.

## Repository structure

```text
SmartMail_LLM_Email_Spam_Phishing/
├── app.py
├── security.py
├── requirements.txt
├── .env.example
├── .gitignore
├── Procfile
├── runtime.txt
├── README.md
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── tests/
    └── test_security.py
```

## Setup locally

### 1. Clone

```bash
git clone https://github.com/hasnainshariq03/SmartMail-LLM-Email-Security.git
cd SmartMail-LLM-Email-Security
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:

```bat
.venv\Scripts\activate.bat
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure API key

Copy `.env.example` to `.env` and add your OpenAI API key:

```env
OPENAI_API_KEY=your_real_api_key
OPENAI_MODEL=gpt-4.1-mini
FLASK_SECRET_KEY=use-a-long-random-secret
MAX_EMAIL_CHARS=12000
```

Get API access and manage billing at https://platform.openai.com/. ChatGPT subscriptions and API billing are separate. Never commit `.env` or expose the API key in frontend JavaScript, screenshots or GitHub.

### 5. Run

```bash
python app.py
```

Open http://127.0.0.1:5000.

## API endpoint

`POST /api/analyze`

Request:

```json
{
  "email_text": "Subject: Account verification\nPlease verify your account immediately..."
}
```

Successful response shape:

```json
{
  "classification": "PHISHING",
  "risk_level": "HIGH",
  "confidence": 0.91,
  "summary": "The message requests account verification.",
  "reason": "The wording may be attempting to obtain account access.",
  "indicators": ["Urgent account request", "Credential-related language"],
  "recommended_action": "Do not use links in the message. Visit the official website independently."
}
```

Example request using curl:

```bash
curl -X POST http://127.0.0.1:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d "{\"email_text\":\"Congratulations, claim your prize now\"}"
```

The example response above is illustrative. Actual model output depends on the email and model behavior.

## Run tests

```bash
pytest -q
```

Tests cover empty, non-string and oversized inputs plus the redaction helper. They do not make live API calls. For integration tests, mock the OpenAI client rather than spending API credits.

## Deploy on Render

1. Create a GitHub repository named `SmartMail-LLM-Email-Security`.
2. Push the project to GitHub.
3. In Render, create a new Web Service and connect the repository.
4. Runtime: Python.
5. Build command: `pip install -r requirements.txt`.
6. Start command: `gunicorn app:app`.
7. Add environment variables in Render dashboard:
   - `OPENAI_API_KEY`
   - `OPENAI_MODEL` (for example `gpt-4.1-mini`, if available to your API project)
   - `FLASK_SECRET_KEY` (a long random secret)
   - `MAX_EMAIL_CHARS=12000`
8. Deploy and test `/health` and the web form.

Do not place secrets in the repository or deployment build logs.

## Security and privacy

- Treat email content as untrusted input. The system prompt explicitly says not to obey instructions inside the email.
- Keep the API key on the server in environment variables. Never put it in HTML or browser JavaScript.
- Do not log raw email content.
- Limit input length and request body size.
- Add authentication, rate limiting, CSRF protection and abuse monitoring before public production use.
- Review OpenAI API data controls and your organization's privacy requirements before sending real email content to an external API.
- Do not submit confidential, regulated or personal information to a demo.
- Avoid automatically deleting, blocking or quarantining messages based only on the LLM's response.
- A model-generated confidence number is subjective and not calibrated.
- This demo does not check link reputation, sender authentication (SPF/DKIM/DMARC), attachment contents or external threat intelligence.

## Resume description

**SmartMail — LLM-Powered Email Spam & Phishing Detector**

Technologies: Python, Flask, HTML5, CSS3, JavaScript, OpenAI API, Structured Outputs, JSON Schema, pytest.

- Developed an LLM-powered email security web application using the OpenAI API to classify email text as spam, phishing or legitimate.
- Designed prompt instructions and structured JSON output to return risk levels, explanations, suspicious indicators and recommended actions.
- Integrated the API with a Flask backend and responsive HTML/CSS frontend.
- Implemented input validation, request-size limits, environment-based API key management and automated tests.

## Future improvements

- Sender-domain and header analysis.
- Safe URL reputation integration using a trusted threat-intelligence service.
- Authentication, rate limiting and analysis history with privacy controls.
- User feedback and analyst review workflow.
- Email-provider integration with explicit user authorization.
- Evaluation benchmark with a labeled dataset and human-reviewed metrics.

## Author

**Hasnain Shariq**  
GitHub: https://github.com/hasnainshariq03
