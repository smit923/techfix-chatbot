# TechFix Chatbot: Automated Support & Lead Capture Pipeline

A lightweight, enterprise-ready conversational agent built to automate customer support and lead generation for technical repair services. This production-ready application leverages the `gemini-2.5-flash` engine via the Google GenAI SDK and manages application architecture dynamically using Streamlit.

🚀 **[Live Interactive Demo](PASTE_YOUR_STREAMLIT_APP_URL_HERE)**

## High-Performance Architecture
* **State Management**: Implements an isolated `st.session_state` pipeline to maintain conversational integrity across turns without memory leaks.
* **Multi-Page Framework**: Features modular page architecture including an isolated `2_Lead_Center.py` script to handle collected lead data securely.
* **Automated Lead Capture**: Features automated, client-side data capture that intercepts high-intent queries to securely gather names and phone numbers.

## Core Technical Stack
* **Language**: Python 3.11+
* **Framework**: Streamlit
* **AI Model**: Google Gemini API (`gemini-2.5-flash`)
* **Environment**: GitHub Actions / Streamlit Community Cloud

## Quickstart & Local Deployment

1. Clone the repository:
```bash
git clone https://github.com
cd techfix-chatbot
```

2. Configure environment dependencies:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Initialize local secrets inside `.streamlit/secrets.toml`:
```toml
GEMINI_API_KEY = "your_secured_gemini_api_key"
```

4. Launch the application server:
```bash
streamlit run app.py
```
