# Personalized Medicine Platform

This project is a simple prototype of a Personalized Medicine Platform that allows:
- Uploading a genomic file (`.vcf`)
- Analyzing variants and predicting disease risks
- Simulating drug responses and recommending treatments
- Displaying biomarkers and accepting clinical information
- Integrating with a chatbot (Rasa) and Flask web backend

---

## 💡 Features Implemented

- Accept `.vcf` file uploads via chatbot or web UI
- Count nucleotides (A, T, G, C)
- Detect genetic variants
- Predict disease risks and drug responses
- Recommend treatments and show biomarker insights
- Accept clinical data (e.g., age, diabetes, smoker)
- JSON and HTML output modes
- Downloadable results via web interface

---

## 🚀 How to Run This Project

### 1. Clone the Repository
```bash
cd Desktop
mkdir personalized_medicine_platform
cd personalized_medicine_platform
```

Put the project files inside this folder.

### 2. Create & Activate Virtual Environment (Windows)
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask Web App
```bash
cd app
python app.py
```
Visit `http://localhost:5006` in your browser.

### 5. Run the Rasa Bot in Separate Terminal
```bash
cd rasa_bot
rasa run actions
```
And then in another terminal:
```bash
rasa shell
```

---

## 🧬 Sample Usage via Chatbot

Try saying:
```
hi
i want to analyze my genome
```
Chatbot will send a `.vcf` file to Flask backend and return complete analysis.

---

## 📁 Directory Structure
```
personalized_medicine_platform/
├── app/                # Flask backend + HTML
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   └── sample_genome.vcf
│
├── rasa_bot/           # Chatbot logic
│   ├── actions/
│   │   └── actions.py
│   └── domain.yml
│   └── other rasa files...
│
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## 🛠 Technologies Used
- Python 3.8
- Flask
- Rasa 2.8.17
- HTML (Jinja2 Template)

---

## 📝 License
For academic or personal use only. Not for clinical deployment.

