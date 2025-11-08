# 🚨 Phishing URL Detector

A simple Python-based phishing URL detection tool with persistent history tracking.

## 📋 Features

- **URL Analysis**: Detects potential phishing URLs based on domain reputation and suspicious keywords
- **Persistent History**: Saves all tested URLs to a local file for future reference
- **Color-coded Results**: Visual feedback with green (legitimate) and red (phishing) indicators
- **Session History**: View all URLs tested in the current session
- **Simple Interface**: Easy-to-use command-line interface

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/LuthandoCandlovu/phishing-detector.git
   cd phishing-detector
Set up virtual environment (recommended):

bash
python -m venv phishenv
.\phishenv\Scripts\activate  # Windows
Install dependencies:

bash
pip install colorama
🚀 Usage
Run the detector:

bash
python phish_detector.py
Commands:
Enter a URL: Test any URL for phishing potential

history: View all URLs tested in this session

exit: Quit the application

Example:
text
Enter a URL: https://google.com-login-verify.com
[✘] RESULT: PHISHING (Confidence: 0.87)

Enter a URL: https://github.com
[✔] RESULT: LEGITIMATE (Confidence: 0.95)
🔍 How It Works
The detector uses a simple rule-based approach:

Legitimate Domains
google.com, github.com, microsoft.com, facebook.com, linkedin.com

Phishing Keywords
login, verify, update, secure, banking, account, appleid

Detection Logic:
High confidence legitimate: Contains trusted domains

High confidence phishing: Contains suspicious keywords

Default legitimate: All other URLs with moderate confidence

📁 Project Structure
text
phishing-detector/
├── phish_detector.py    # Main application
├── url_history.txt      # Persistent URL history (auto-generated)
├── README.md           # This file
└── phishenv/           # Virtual environment (not in repo)
🗂️ Files
phish_detector.py: Main Python script with detection logic

url_history.txt: Auto-generated file storing URL test history

.gitignore: Excludes virtual environment and history files

⚠️ Disclaimer
This is a basic educational tool for demonstration purposes. It uses simple pattern matching and should not be relied upon for critical security decisions. Always use comprehensive security solutions for real-world protection.

🐛 Reporting Issues
Found a bug or have a feature request? Please open an issue on GitHub.

👨‍💻 Author
Luthando Candlovu

GitHub: @LuthandoCandlovu

