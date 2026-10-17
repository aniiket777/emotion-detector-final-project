# Final Project

An AI-powered emotion detection web application developed with Python and Flask. The application analyzes natural language text for five primary emotions—**anger**, **disgust**, **fear**, **joy**, and **sadness**—and identifies the **dominant emotion**.

This project implements the specifications of the IBM Developer Skills Network AI Application Development curriculum.

---

## Architecture & Structure

```text
ibm-starter/
├── EmotionDetection/
│   ├── __init__.py               # Package init exporting emotion_detector
│   └── emotion_detection.py      # Watson NLP EmotionPredict client & score parser
├── static/
│   └── mywebscript.js            # Asynchronous frontend client for emotion analysis
├── templates/
│   └── index.html                # Bootstrap web interface
├── server.py                     # Flask deployment server (routes: / and /emotionDetector)
├── test_emotion_detection.py     # Unit test suite (unittest with mocked responses)
├── .gitignore                    # Excludes virtual environments, caches, and bytecode
├── LICENSE                       # Apache 2.0 license
└── README.md                     # Project documentation
```

---

## Features

- **Emotion Analysis:** Evaluates input text and extracts confidence scores for `anger`, `disgust`, `fear`, `joy`, and `sadness`.
- **Dominant Emotion Detection:** Dynamically calculates and returns the emotion with the highest confidence score.
- **Input Validation:** Rejects empty or whitespace-only inputs with an HTTP `400` status and the exact message: `Invalid text! Please try again!`.
- **Robust Error Handling:** Catches network timeouts, unreachable upstream services, and malformed responses, returning an HTTP `502` status without crashing or inventing emotion scores.
- **Interactive Web Interface:** Single-page responsive interface built with Bootstrap 4 and asynchronous JavaScript (AJAX).
- **Code Quality:** Fully PEP 8 compliant with complete docstrings, achieving a **10.00 / 10** score on Pylint.
- **Comprehensive Unit Tests:** 8 test cases validating dominant emotions, blank inputs, HTTP 400 errors, and network exceptions using `unittest.mock`.

---

## Note on Watson NLP Endpoint & Environment

The Watson NLP `EmotionPredict` endpoint (`https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict`) is an internal service hosted inside the IBM Skills Network cloud environment. 

When executed outside of the IBM cloud lab environment (such as on a local machine or standard internet connection), requests to this hostname will encounter connection timeouts (`ConnectTimeoutError`). The application's error-handling layer safely catches these timeouts, returning an HTTP `502` error indicating that the emotion detection service is unavailable, without fabricating synthetic scores. When run inside the IBM Skills Network lab environment, live Watson emotion analysis executes normally.

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd ibm-starter
```

### 2. Create and Activate Virtual Environment

**On Windows (PowerShell):**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**On Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
python -m pip install --upgrade pip
python -m pip install flask requests pylint
```

---

## Running the Application

Start the Flask development server on `127.0.0.1:5000`:

```bash
python server.py
```

Open your browser and navigate to:
```text
http://127.0.0.1:5000/
```

---

## Running Tests & Code Quality Checks

### Run Unit Tests
Execute the unit test suite:
```bash
python -m unittest -v test_emotion_detection.py
```

### Run Pylint Code Analysis
Verify code quality and PEP 8 compliance:
```bash
pylint server.py EmotionDetection test_emotion_detection.py
```
Expected result: **10.00 / 10**.
