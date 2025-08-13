# JavaToPython Transpiler Web app
This is a tool that allows users to transpile one file or a whole project in Java to its Python counterpart

# Getting Started
1) Get a Gemini API key: https://aistudio.google.com/apikey
2) Copy .env.example to .env and paste your key:
   GOOGLE_API_KEY=your_key_here
3) Windows (PowerShell):
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   python web_app.py
4) Alternatively, set per-session:
   $env:GOOGLE_API_KEY = 'your_key'
   python web_app.py
